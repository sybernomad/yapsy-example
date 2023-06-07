from yapsy.IPlugin import IPlugin


class UpperCasePlugin(IPlugin):
    def process(self, text):
        return text.upper()
