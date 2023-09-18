!!! question "Lesson: Classy Animals"
   
    === "Task"
       
        Create a new empty Python source file and copy the "MyDog" example
        class to it. Add a new method `speak` that calls the existing method
        `bark`.

        Here's the `MyDog` class, again:

        ``` python
        class MyDog:
            def __init__(self, name):
                self.name = name

            def bark(self):
                print(f"{self.name} says wuff")
        ```

        Then, create a new class `MyCat` in the same file that - like `MyDog` -
        also expects a `name` argument in its `__init__` method, with those 2
        additional methods:

        - a method `meow` that prints the string "<MyCat name> says miau" where
          <MyCat name> is the name attribute of the instance object
        - a method `speak` that calls the `meow` method.

        Create an `animals` list containing a `MyDog` and a `MyCat` instance.

        Loop over the animals list. For each animal, invoke the `speak()`
        method.

        Optional: Enhance the `MyDog` and `MyCat` classes' methods to accept an
        optional `text` argument. Modify the `MyDog.bark` and the `MyCat.meow`
        methods to additionally print the animal's class name and the `text`
        argument, e.g. like

        ``` python
        >>> my_cat = MyCat("Amanda")
        >>> my_cat.speak(text="a lot")
        "MyCat Amanda says miau a lot".
        >>>
        ```

    === "Hints"

        When defining a method in a class remember that each method *must* have
        a `self` parameter as the 1st positional parameter.

        You can get an instance's class by retrieving its `__class__`
        attribute. The name of a class object can be found in the class'
        `__name__` attribute, e.g.

        ``` python
        >>> # Get the name of the MyDog class object.
        >>> MyDog.__name__
        'MyDog'
        >>> 
        >>> # Get the name of a MyDog instance's class object.
        >>> MyDog("Lucie").__class__.__name__  # Get the name of a MyDog
        'MyDog'
        ```

        Inside of a method, a class or instance attribute can be accessed
        through the self parameter (which references the instance object).

    === "Solution"

        ??? example "*Really* take a peek now?"

            ``` python title="classy_animals.py"
            --8<-- "training/lessons/classy-animals/classy_animals.py"
            ```

            [:material-file-download:](classy_animals.py)
