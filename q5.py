# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class _STRING_PROCESSOR:
    def __init__(self):
        self._STRING = ""

    def _GET_STRING(self):
        self._STRING = str(input("Give me a random string "))

    def _PRINT_STRING(self):
        print(self._STRING.upper())

_STR_VAR = _STRING_PROCESSOR()

_STR_VAR._GET_STRING()
_STR_VAR._PRINT_STRING()