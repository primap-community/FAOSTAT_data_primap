function prepare_FAO2022TOT_data(source_name, last_hist_year)
% Prepares FAO data into country time series. Countries which were
% split up during the course of history are downscaled to their current
% members using the shares that were present in the first year in which all
% members had emission values in the CDIAC source. countries which are now
% merged over time get their previous members added up to the country with
% the current political boundaries.
% The resulting table is: CO2_CATM0EL_TOTAL_NET_HISTORY_CDIAC2010PROC
%
% author : CC
% version : 20120315
% version : 20120403 JG - substitute negative data by zero, fixed
% version : 20131024 JG - CDIAC2013 based on the CDIAC2011 file
% combine_subregions
% version : 20150416 JG - delete time series consisting only of zeros
% version : 20150511 JG - fixed wrong region downscaling
% version : 20150715 JG - summing to primap country definitions
% version : 20170120 JG - 2016 data
% version : 20170825 JG - IPCC 2006 categories
% version : 20190708 JG - convert to Gg from GgCO2eq for all single gas tables
% version : 20201009 JG - 2020A data which needs extrpolation as not all sectors have been updated
% version : 20201207 JG - 2020B data

%% issues FAO
% gap in Micronesia data (sometimes filled with zero data)
% gap in Maldives data (sometimes filled with zero data)
% Saint kitts and Newis. very low data in last years (CH4, IPC3A, IPC3C)
% Afghanistan: very low data in last year (CH4, IPC3C)
% many countries: very low data before 1990 and sometimes also in last year (CH4, IPC3C)
% this is probably due to mixing LU and AGRI data, where LU data only covers 1990-2015
% while AGRI data covers 1960 - 2016 (same for N2O)
% saint Lucia: data only until 1980 (CH4, IPC3C)

%%%% drained organic soils current omitted

global CONSTANTS;

errorID = 'CreateDatabase:DataPreparation:FAO:PrepareFAO2022Data:';
narginchk(0, 2)

if nargin == 2
    source = source_name;
elseif nargin == 1
    if ischar(source_name)
        source = source_name;
        last_hist_year = 0;
    else
        source = 'FAO2022P2';
    end
else
    source = 'FAO2022P2';
    last_hist_year = 0;
end

sourceSuffix = 'I';
%tempSuffix = 'P';
procSource = [source sourceSuffix];
%tempSource = [source tempSuffix];
scenario = 'HISTORY';
scenarioProjection = 'PROJECTION';
%GWPspec = CONSTANTS.gwpSARSpecification; % make source dependent if necessary

nYearKey = 5; % number of years to consider for downscaling key

%% TODO check if extrapolation of subsectors needed

%% remove existing proc source
allProcTablenames = get_table_sheetcodes_for({CONSTANTS.nameOfSheetSource}, {{procSource}});%, tempSource}});
remove_tables_from_database(allProcTablenames);

%% copy to temp source
copy_source_scenario_tables_from_to(source, scenario, procSource, scenario);

%% adjust countries
% first aggregate what are now parts of countries into current countries,
% by adding parts + country.
allTablenames = get_table_sheetcodes_for({CONSTANTS.nameOfSheetSource}, ...
    {{procSource}});
warning off Tools:AssertValidcategoryforSourceScenario:ValidCategory

theseTables = struct;
% for each emissions table, make these group manipulations
for iTable = 1:length(allTablenames)
    % adjust countries
    newTable = adjust_countries(allTablenames{iTable}, nYearKey, false);
    if isempty(fieldnames(newTable))
        primap_log([errorID 'EmptyTable'], CONSTANTS.ERRuserErrorWarning, ...
            ['Table ' allTablenames{iTable} ' empty after country adjustment and removal of NaN and zero data']);
    else
        theseTables.(newTable.(CONSTANTS.nameOfSheetCode)) = newTable;
    end

end

%%% add tables to database
remove_tables_from_database(allTablenames);
success = overwrite_or_add_tables_in_database(theseTables, true, false);
if ~all(success)
    primap_log([errorID 'NotAllSplitTablesAdded'], CONSTANTS.ERRprogramError, ...
        'Some downscaled AGRI tables not added to DB. Check preceeding messages for reason');
end


%% split into historical data and projection in case projections are available and last_hist_year is given
if last_hist_year > 0
    % get all tablenames
    newTables = struct;
    allTablenames = get_table_sheetcodes_for({CONSTANTS.nameOfSheetSource}, {{procSource}});
    for iTable = 1 : length(allTablenames)
        % get table from DB
        currentTable = get_table_from_database(allTablenames{iTable});
        % check if table contains projection values
        if any(currentTable.(CONSTANTS.nameOfYearVector) > last_hist_year)
            % create projection table
            currentTableProj = currentTable;
            currentTableProj.(CONSTANTS.nameOfDataField) = currentTableProj.(CONSTANTS.nameOfDataField)(:, ...
                currentTableProj.(CONSTANTS.nameOfYearVector) > last_hist_year);
            currentTableProj.(CONSTANTS.nameOfYearVector) = ...
                currentTableProj.(CONSTANTS.nameOfYearVector)(currentTableProj.(CONSTANTS.nameOfYearVector) > last_hist_year);
            currentTableProj.(CONSTANTS.nameOfSheetScenario) = scenarioProjection;
            currentTableProj.(CONSTANTS.nameOfSheetCode) = concatenate_structure_field_values(currentTableProj, ...
                CONSTANTS.tableNameConstructionFromSheets);
            currentTableProj = delete_only_nan_containing_countries(currentTableProj);
            if ~isempty(fieldnames(currentTableProj))
                newTables.(currentTableProj.(CONSTANTS.nameOfSheetCode)) = currentTableProj;
            end

            % create historical table
            currentTableHist = currentTable;
            currentTableHist.(CONSTANTS.nameOfDataField) = currentTableHist.(CONSTANTS.nameOfDataField)(:, ...
                currentTableHist.(CONSTANTS.nameOfYearVector) <= last_hist_year);
            currentTableHist.(CONSTANTS.nameOfYearVector) = ...
                currentTableHist.(CONSTANTS.nameOfYearVector)(currentTableHist.(CONSTANTS.nameOfYearVector) <= last_hist_year);
            currentTableHist = delete_only_nan_containing_countries(currentTableHist);
            newTables.(currentTableHist.(CONSTANTS.nameOfSheetCode)) = currentTableHist;
        end
    end
    success = overwrite_or_add_tables_in_database(newTables, true, false);
    if ~all(success)
        primap_log([errorID 'NotAllSplitTablesAdded'], CONSTANTS.ERRprogramError, ...
            'Some split tables not added to DB. Check preceeding messages for reason');
    end
end


%% construct higher level IPC categories
% general parameters

defaultParams=struct;
%defaultParams.future.type='linear';
defaultParams.future.type='none';
defaultParams.future.fityears=15;
%defaultParams.past.type='linear';
defaultParams.past.type='none';
defaultParams.past.fityears=20;
defaultParams.past.fallback='none';

FAOEntities = {'CO2', 'CH4', 'N2O'};

categories = struct;

%%% IPC3A = IPC3A1 + IPC3A2
categories.IPC3A = struct;
categories.IPC3A.targetCategory = 'IPC3A';
categories.IPC3A.subcategories = {'IPC3A1', 'IPC3A2'};
categories.IPC3A.entities = FAOEntities;
categories.IPC3A.params = defaultParams;



%%% IPCM3C1AG =  IPC3C1B + IPC3C1C
categories.IPCM3C1AG = struct;
categories.IPCM3C1AG.targetCategory = 'IPCM3C1AG';
categories.IPCM3C1AG.subcategories = {'IPC3C1C', 'IPC3C1B'};
categories.IPCM3C1AG.entities = FAOEntities;
categories.IPCM3C1AG.params = defaultParams;

%%% IPC3C1 = IPCM3C1AG + IPCM3C1LU
%%%%%%%%%% LULUCF currently missing
categories.IPC3C1 = struct;
categories.IPC3C1.targetCategory = 'IPC3C1';
categories.IPC3C1.subcategories = {'IPCM3C1AG', 'IPCM3C1LU'};
categories.IPC3C1.entities = FAOEntities;
categories.IPC3C1.params = defaultParams;

%%% IPCM3C4AG = 'IPC3C4B', 'IPC3C4C', 'IPC3C4D',
% omit currently as drained organic soils is missing but present in M3C45AG
% categories.IPCM3C4AG = struct;
% categories.IPCM3C4AG.targetCategory = 'IPCM3C4AG';
% categories.IPCM3C4AG.subcategories = {'IPC3C4A', 'IPC3C4B', 'IPC3C4C', 'IPC3C4D', };
% categories.IPCM3C4AG.entities = FAOEntities;
% categories.IPCM3C4AG.params = defaultParams;

%%% IPC3C4 = IPCM3C4AG
%%%%%%%%%% LULUCF currently missing
categories.IPC3C4 = struct;
categories.IPC3C4.targetCategory = 'IPC3C4';
categories.IPC3C4.subcategories = {'IPCM3C4AG'};
categories.IPC3C4.entities = FAOEntities;
categories.IPC3C4.params = defaultParams;

%%% IPC3C = IPC3C1 + IPC3C4 + IPC3C5 + IPC3C6 + IPC3C7
%%%%%%%%%% LULUCF currently missing
categories.IPC3C = struct;
categories.IPC3C.targetCategory = 'IPC3C';
categories.IPC3C.subcategories = {'IPC3C1', 'IPCM3C45AG', 'IPC3C7'}; % 'IPC3C5', 'IPC3C6',
categories.IPC3C.entities = FAOEntities;
categories.IPC3C.params = defaultParams;

%%% IPCM3CAG = IPCM3C1AG + IPCM3C4AG + IPC3C5 + IPC3C6 + IPC3C7
categories.IPCM3CAG = struct;
categories.IPCM3CAG.targetCategory = 'IPCM3CAG';
categories.IPCM3CAG.subcategories = {'IPCM3C1AG', 'IPCM3C45AG', 'IPC3C7'}; %'IPC3C5', 'IPC3C6',
categories.IPCM3CAG.entities = FAOEntities;
categories.IPCM3CAG.params = defaultParams;

% %%% IPCM3CLU = IPCM3C1LU
% categories.IPCM3CLU = struct;
% categories.IPCM3CLU.targetCategory = 'IPCM3CLU';
% categories.IPCM3CLU.subcategories = {'IPCM3C1LU'};
% categories.IPCM3CLU.entities = FAOEntities;
% categories.IPCM3CLU.params = defaultParams;
%
% %%% IPC3 = IPC3A + IPC3B + IPC3C
% if any(strcmp(source, {'FAO2021A'}))
%     categories.IPC3 = struct;
%     categories.IPC3.targetCategory = 'IPC3';
%     categories.IPC3.subcategories = {'IPC3A', 'IPCMLULUCF', 'IPCM3CAG'};
%     categories.IPC3.entities = FAOEntities;
%     categories.IPC3.params = defaultParams;
% else
%     categories.IPC3 = struct;
%     categories.IPC3.targetCategory = 'IPC3';
%     categories.IPC3.subcategories = {'IPC3A', 'IPC3B', 'IPC3C'};
%     categories.IPC3.entities = FAOEntities;
%     categories.IPC3.params = defaultParams;
%
%     %%% IPCMLULUCF = IPC3B + IPC3CLU
%     categories.IPCMLULUCF = struct;
%     categories.IPCMLULUCF.targetCategory = 'IPCMLULUCF';
%     categories.IPCMLULUCF.subcategories = {'IPC3B', 'IPCM3CLU'};
%     categories.IPCMLULUCF.entities = FAOEntities;
%     categories.IPCMLULUCF.params = defaultParams;
% end


%%% IPCMAG = IPC3A + IPCM3CA
categories.IPCMAG = struct;
categories.IPCMAG.targetCategory = 'IPCMAG';
categories.IPCMAG.subcategories = {'IPC3A', 'IPCM3CAG'};
categories.IPCMAG.entities = FAOEntities;
categories.IPCMAG.params = defaultParams;

%%% IPCMAGELV = IPCM3CA
categories.IPCMAGELV = struct;
categories.IPCMAGELV.targetCategory = 'IPCMAGELV';
categories.IPCMAGELV.subcategories = {'IPCM3CAG'};
categories.IPCMAGELV.entities = FAOEntities;
categories.IPCMAGELV.params = defaultParams;

entities = struct;
entities.KYOTOGHG = struct;
entities.KYOTOGHG.targetEntity = 'KYOTOGHG';
entities.KYOTOGHG.subEntities = {'CO2', 'CH4', 'N2O'};
entities.KYOTOGHG.categories = {'IPC3', 'IPC3A', 'IPC3C', 'IPCMAG', 'IPCMAGELV', 'IPCMLULUCF'}; %'IPC3B',
entities.KYOTOGHG.params = defaultParams;
entities.KYOTOGHG.GWP = CONSTANTS.gwpSARSpecification;

entities.KYOTOGHGAR4 = struct;
entities.KYOTOGHGAR4.targetEntity = 'KYOTOGHGAR4';
entities.KYOTOGHGAR4.subEntities = {'CO2', 'CH4', 'N2O'};
entities.KYOTOGHGAR4.categories = {'IPC3', 'IPC3A', 'IPC3C', 'IPCMAG', 'IPCMAGELV', 'IPCMLULUCF'}; %'IPC3B',
entities.KYOTOGHGAR4.params = defaultParams;
entities.KYOTOGHGAR4.GWP = CONSTANTS.gwpAR4Specification;

entities.KYOTOGHGAR5 = struct;
entities.KYOTOGHGAR5.targetEntity = 'KYOTOGHGAR5';
entities.KYOTOGHGAR5.subEntities = {'CO2', 'CH4', 'N2O'};
entities.KYOTOGHGAR5.categories = {'IPC3', 'IPC3A', 'IPC3C', 'IPCMAG', 'IPCMAGELV', 'IPCMLULUCF'}; %'IPC3B',
entities.KYOTOGHGAR5.params = defaultParams;
entities.KYOTOGHGAR5.GWP = CONSTANTS.gwpAR5Specification;

entities.KYOTOGHGAR6 = struct;
entities.KYOTOGHGAR6.targetEntity = 'KYOTOGHGAR6';
entities.KYOTOGHGAR6.subEntities = {'CO2', 'CH4', 'N2O'};
entities.KYOTOGHGAR6.categories = {'IPC3', 'IPC3A', 'IPC3C', 'IPCMAG', 'IPCMAGELV', 'IPCMLULUCF'}; %'IPC3B',
entities.KYOTOGHGAR6.params = defaultParams;
entities.KYOTOGHGAR6.GWP = CONSTANTS.gwpAR6Specification;

aggregate_and_extrapolate_source(procSource, scenario, categories, entities);
aggregate_and_extrapolate_source(procSource, scenarioProjection, categories, entities);

remove_desired_regions_from_source_scenario({'EARTH', 'POLYNESIA'}, procSource, scenario);
remove_desired_regions_from_source_scenario({'EARTH', 'POLYNESIA'}, procSource, scenarioProjection);

% TODO
% remove years with partial data from aggregate timeseries
% FAO2020B
% IPC3C1, IPCM3CAG, IPC3C, IPC3, IPCMAG, IPCMAGELV, IPC3B, IPCMLULUCF (remove 2019, 2020)

% sum countries to CRF / UNFCCC reporting level
sum_countries_primap(procSource, false);



%% remove the FAO terminology tables
% tempTables = get_table_sheetcodes_for({CONSTANTS.nameOfSheetSource}, {{tempSource}});
% %success = remove_tables_from_database(tempTables);
% if ~all(success)
%     disp('some tales could not be removed from the DB');
% end
% keep them as sometimes country downscaled tables in FAO eminology are needed

warning off Tools:AssertValidcategoryforSourceScenario:ValidCategory

end %prepareFAO2015data


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function newTable = adjust_countries(tablename, nYearKey, negativeToZero)
    global CONSTANTS;

    errorID = 'CreateDatabase:DataPreparation:FAO:PrepareFAO2016Data:AdjustCountries';
    thisTable = get_table_from_database(tablename);
    %thisTable.(CONSTANTS.nameOfSheetSource) = tempSource;
    %thisTable.(CONSTANTS.nameOfSheetCode) = concatenate_structure_field_values(thisTable,'default');
    thisTable.(CONSTANTS.nameOfSheetDescr) = [thisTable.(CONSTANTS.nameOfSheetDescr) ...
        ', regions summed and downscaled to country time series'];
    source = thisTable.(CONSTANTS.nameOfSheetSource);

    if negativeToZero
        % change negative values to zero for FAO1
        isneg = thisTable.data < 0;
        thisTable.data(isneg) = 0;
    end

    % remove countries which contain only NaN data
    thisTable = delete_only_nan_containing_countries(thisTable);
    % remove countries which contain only zero data
    thisTable = delete_only_zero_containing_countries(thisTable);

    if ~isempty(fieldnames(thisTable))
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %% REGIONS DOWNSCALED TO COUNTRIES, REGIONS DELETED
        % FIRST, REGIONS THAT SPLIT INTO COUNTRIES THAT EXIST IN FAO
        % split most recent first. Some regions split into other regions that
        % must be split first.

        % USSR = RUSSIA + ARMENIA + AZERBAIJAN + BELARUS + BULGARIA + ESTONIA  (<= 1991)
        %        + GEORGIA + KAZAKHSTAN + KYRGYZSTAN + LATVIA + LITHUANIA +
        %        MOLDOVA + TAJIKISTAN + TURKMENISTAN + UKRAINE + UZBEKISTAN
        regions2Delete = {'FSU'}; % doesn't work for FAO1K
        theseCountries = get_members_of(regions2Delete{1});
        yearKey = 1992;
        thisTable = downscale_existing(thisTable,regions2Delete,theseCountries,yearKey, nYearKey, true);

        % SERBIA/MONTENEGRO = SERBIA + MONTENEGRO (<= 2005)
        regions2Delete = {'SRBMNE'};
        theseCountries = get_members_of(regions2Delete{1});
        yearKey = 2006;
        thisTable = downscale_existing(thisTable,regions2Delete,theseCountries,yearKey, nYearKey, true);

        % YUGOSLAVIA = BOSNIA/HERZEGOVINA + CROATIA + MACEDONIA + SLOVENIA + SERBIA + MONTENEGRO (<= 1991)
        regions2Delete = {'YUG'};
        theseCountries = get_members_of(regions2Delete{1});
        yearKey = 1992;
        thisTable = downscale_existing(thisTable,regions2Delete,theseCountries,yearKey, nYearKey, true);

        % CZECHOSLOVAKIA = CZECH REPUBLIC + SLOVAKIA (<= 1991)
        regions2Delete = {'CZESVK'};
        theseCountries = get_members_of(regions2Delete{1}); %{'CZE','SVK'};
        yearKey = 1992;
        thisTable = downscale_existing(thisTable,regions2Delete,theseCountries,yearKey, nYearKey, true);

        % Pacific Islands Trust Territory = Federated States of Micronesia + Palau
        % + Northern Mariana Islands + Marshall Islands (<= 1994)
        regions2Delete = {'TTPI'};
        theseCountries = get_members_of(regions2Delete{1}); %{'FSM'  'MHL'    'MNP'    'PLW'};
        yearKey = 1995;
        thisTable = downscale_existing(thisTable,regions2Delete,theseCountries,yearKey, nYearKey, true);

        % BELLUX = Belgium + Luxembourg (<= 1999)
        regions2Delete = {'BELLUX'};
        theseCountries = get_members_of(regions2Delete{1});
        yearKey = 2000;
        thisTable = downscale_existing(thisTable,regions2Delete,theseCountries,yearKey, nYearKey, true);

        % ETHERI = Ethiopia + Eritrea (<= 1992)
        regions2Delete = {'ETHERI'};
        theseCountries = get_members_of(regions2Delete{1});
        yearKey = 1993;
        thisTable = downscale_existing(thisTable,regions2Delete,theseCountries,yearKey, nYearKey, true);

        % Sudan and South Sudan (South Sudan has individual data for 2012 onwards)
        if any(strcmp(source, {'FAO2016P', 'FAO2018P', 'FAO2019AP', 'FAO2019BP', 'FAO2020AP', 'FAO2020BP', ...
                'FAO2020CP', 'FAO2021AP'}))
            regions2Delete = {'SDN'};
            theseCountries = {'SDN', 'SSD'};
            yearKey = 2012;
            thisTable = downscale_existing(thisTable,regions2Delete,theseCountries,yearKey, nYearKey, true);
        end

        % Sudan and South Sudan (South Sudan has individual data for 2012 onwards)
        if any(strcmp(source, {'FAO2023AI', 'FAO2024AI'}))
            regions2Delete = {'SDNSSD'};
            theseCountries = {'SDN', 'SSD'};
            yearKey = 2012;
            thisTable = downscale_existing(thisTable,regions2Delete,theseCountries,yearKey, nYearKey, true);
        end

        % interpolate gap in FSM data
        dataFSM = get_cydata_from_independent_table(thisTable, {'FSM'}, 'all');
        if ~all(isnan(dataFSM.(CONSTANTS.nameOfDataField)))
            gaps = get_gaps(dataFSM.(CONSTANTS.nameOfDataField));
            if ~isempty(gaps)
                dataFSM.(CONSTANTS.nameOfDataField) = interpolate_in_single_dv(gaps, dataFSM.(CONSTANTS.nameOfDataField));
                thisTable = add_cydata_to_independent_table(thisTable, dataFSM);
            end
        end

        % remove countries which contain only NaN data
        thisTable = delete_only_nan_containing_countries(thisTable);
        % remove countries which contain only zero data
        newTable = delete_only_zero_containing_countries(thisTable);
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    else
        newTable = struct;
    end
end


function thisTable = downscale_existing(thisTable,regions2Delete,theseCountries, yearKey, nYearKey, remove)
    % split regional data proportionally, based on ratios in first year
    % after yearKey where there is at least one nonzero value

    global CONSTANTS
    errorID = 'CreateDatabase:DataPreparation:FAO:PrepareFAO2016Data:DownscaleExisting';
    if ~exist('remove', 'var')
        remove = true;
    end

    cyRegion = get_cydata_from_independent_table(thisTable,regions2Delete,'all');
    if isempty(cyRegion.(CONSTANTS.nameOfCountryVector))
        return;
    end
    cyKey = get_cydata_from_independent_table(thisTable,theseCountries,'all');
    cyDownscaled = cyRegion;
    cyDownscaled.(CONSTANTS.nameOfCountryVector) = cyKey.(CONSTANTS.nameOfCountryVector);
    %split only if region is not all NaN or zeros
    if ~all(isnan(cyRegion.(CONSTANTS.nameOfDataField)) | cyRegion.(CONSTANTS.nameOfDataField) == 0)
        % remove all years before yearKey
        iYearKey = find(cyKey.(CONSTANTS.nameOfYearVector) == yearKey);
        cyKey.(CONSTANTS.nameOfYearVector) = cyKey.(CONSTANTS.nameOfYearVector)(iYearKey:end);
        cyKey.(CONSTANTS.nameOfDataField) = cyKey.(CONSTANTS.nameOfDataField)(:,iYearKey:end);
        % check which year the first nonzero value arises
        iYearStart = find(~isnan(nansum_primap(cyKey.(CONSTANTS.nameOfDataField),1)) & ...
            (nansum_primap(cyKey.(CONSTANTS.nameOfDataField),1) ~= 0));
        if isempty(iYearStart)
            % cannot divide regional data
            primap_log([errorID 'ProgramError'], CONSTANTS.ERRuserErrorWarning, ...
                ['Downscaling not possible for region ' regions2Delete{1} ...
                ', year(s) for downscaling key have only zeros or NaN. Table: ' ...
                thisTable.(CONSTANTS.nameOfSheetCode)]);
            if remove
                thisTable = remove_countries_from_independent_table(thisTable,regions2Delete);
            end
            return
        end
        % for the data to be downscaled remove all data beginning with the startYear
        yearStart = cyKey.(CONSTANTS.nameOfYearVector)(iYearStart(1));
        iYearStartRegion = find(cyDownscaled.(CONSTANTS.nameOfYearVector) == yearStart);
        cyDownscaled.(CONSTANTS.nameOfDataField) = cyDownscaled.(CONSTANTS.nameOfDataField)(:, 1 : iYearStartRegion - 1);
        cyDownscaled.(CONSTANTS.nameOfYearVector) = cyDownscaled.(CONSTANTS.nameOfYearVector)(1 : iYearStartRegion - 1);
        % for the key remove all years before yearStart
        cyKey.(CONSTANTS.nameOfYearVector) = cyKey.(CONSTANTS.nameOfYearVector)(iYearStart(1):end);
        cyKey.(CONSTANTS.nameOfDataField) = cyKey.(CONSTANTS.nameOfDataField)(:,iYearStart(1):end);
        % key is constructed from nYearKey years or available years,
        % whatever is less
        if length(cyKey.(CONSTANTS.nameOfYearVector)) > nYearKey
            cyKey.(CONSTANTS.nameOfYearVector) = cyKey.(CONSTANTS.nameOfYearVector)(1:nYearKey);
            cyKey.(CONSTANTS.nameOfDataField) = cyKey.(CONSTANTS.nameOfDataField)(:,1:nYearKey);
        end
        key = nansum_primap(cyKey.(CONSTANTS.nameOfDataField),2);
        arrRatio = repmat(key/nansum_primap(key), ...
            1,length(cyDownscaled.(CONSTANTS.nameOfYearVector)));
        cyDownscaled.(CONSTANTS.nameOfDataField) = arrRatio .* ...
            repmat(cyDownscaled.(CONSTANTS.nameOfDataField),length(cyKey.(CONSTANTS.nameOfCountryVector)),1);
        cyDownscaled = delete_only_nan_containing_countries(cyDownscaled);

        % add downscaled numbers to existing data
        thisCydata = get_cydata_from_independent_table(thisTable,theseCountries,'all');
        %thisCydata = delete_only_nan_containing_countries(thisCydata);
        warning off Tools:AssertContentOfCydata:FailedValidation
        thisNewCydata = add_cydata_to_cydata(thisCydata, cyDownscaled);
        %thisNewCydata = summation_of_cydata(thisCydata, cyDownscaled,false,true);
        warning on Tools:AssertContentOfCydata:FailedValidation
        if remove
            thisTable = remove_countries_from_independent_table(thisTable,regions2Delete);
        end
        thisTable = add_cydata_to_independent_table(thisTable,thisNewCydata);
    else
        if remove
            thisTable = remove_countries_from_independent_table(thisTable,regions2Delete);
        end
    end
end




% countries in the source which are not UNFCCC
%   'ARUBA'
%    'ANGUILLA'
%    'NETHERLANDS ANTILLES'
%    'AMERICAN SAMOA'
%    'BERMUDA'
%    'CHANNEL ISLANDS'
%    'CAYMAN ISLANDS'
%    'WESTERN SAHARA'
%    'FALKLAND ISLANDS (MALVINAS)'
%    'FAROE ISLANDS'
%    'GIBRALTAR'
%    'GUADELOUPE'
%    'GREENLAND'
%    'FRENCH GUIANA'
%    'GUAM'
%    'HONG KONG'
%    'ISLE OF MAN'
%    'MACAO'
%    'NORTHERN MARIANA ISLANDS'
%    'MONTSERRAT'
%    'MARTINIQUE'
%    'MAYOTTE'
%    'NEW CALEDONIA'
%    'NORFOLK ISLAND'
%    'PITCAIRN, HENDERSON, DUICE AN...'
%    'PUERTO RICO'
%    'PALESTINIAN TERRITORY, Occupied'
%    'FRENCH POLYNESIA'
%    'REUNION'
%    'SAINT HELENA, ASCENSION AND T...'
%    'SVALBARD AND JAN MAYEN ISLANDS'
%    'SAINT PIERRE AND MIQUELON'
%    'TURKS AND CAICOS ISLANDS'
%    'TOKELAU'
%    'TAIWAN'
%    'VIRGIN ISLANDS (BRITISH)'
%    'VIRGIN ISLANDS (U.S.)'
%    'WALLIS AND FUTUNA ISLANDS'
