from yapsy.IPlugin import IPlugin


class TextProcessorPlugin(IPlugin):
    """
    A template for creating text processing plugins.

    This class serves as a base class for specific text processing plugins.
    It extends the IPlugin interface from the Yapsy library.

    Methods
    -------
    process(text: str)
        Processes a string of text. Must be implemented in subclass.
    """

    def process(self, text):
        """
        Process the provided text.

        Parameters
        ----------
        text : str
            The text to process.

        Raises
        ------
        NotImplementedError
            This method needs to be implemented by any class that extends
            TextProcessorPlugin. This error is raised to catch any usage of
            this method from the base class, indicating the method has not
            been properly implemented in the subclass.
        """

        raise NotImplementedError
