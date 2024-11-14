"""Exceptions"""


class DateTagNotFoundError(Exception):
    """
    Raised when date for latest update cannot be found on FAO domain website
    """

    def __init__(
        self,
        url: str,
    ) -> None:
        """
        Initialise the error

        Parameters
        ----------
        url
            Link to download domain page
        """
        msg = f"Tag for date lat updated was not found on page with url {url}."
        super().__init__(msg)
