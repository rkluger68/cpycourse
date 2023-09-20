# classy_animals.py

class MyDog:
    """A dog class.
    """
    def __init__(self, name):
        self.name = name

    def bark(self, text=""):
        """Make my dog bark.

        Args:
            text (str): A barkable output text
        """
        output = f"{self.name} says wuff"
        if text:
            output += ' ' + text
        print(output)

    def speak(self, text=""):
        """Make my dog speak in dog lingo.

        Args:
            text (str): A dog speak output text
        """
        return self.bark(text=text)


class MyCat:
    """A cat class.
    """
    def __init__(self, name):
        self.name = name

    def meow(self, text=""):
        """Make my cat meow.

        Args:
            text (str): A meowable output text
        """
        output = f"{self.name} says miau"
        if text:
            output += " " + text
        print(output)

    def speak(self, text=""):
        """Make my cat speak in cat lingo.

        Args:
            text (str): A cat speak output text
        """
        return self.meow(text=text)


animals = [MyDog("Django"), MyCat("Amanda")]

for animal in animals:
    animal.speak("a lot")
