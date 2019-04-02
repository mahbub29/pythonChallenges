# Define a class named American which has a static method called printNationality.


class American:
    @staticmethod
    def printNationality():
        print("American")


person = American()
person.printNationality()
American.printNationality()

