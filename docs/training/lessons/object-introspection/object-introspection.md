!!! question "Lesson: Object Introspection"

    === "Task"

        Write a program that lets the user enter a text.
        
        Try to convert the user's input text to data in this order:

          1. Try to convert the text to `int`.
          2. If that fails, try to convert to `float`.
          3. If that fails, simply use the text data.

        By introspection, find out about the converted object's callable
        methods, apart from those whose name starts with a leading underscore
        ('_').

        Generate and print a menu for the user to select which method should be
        applied to the (converted) object. Invoke the selected method and print
        the method's return value and the object.

        Optional: Some methods might require an argument and thus can not
        simply be called without. Find out if the method needs arguments in the
        introspection step and sort those out for the selection menu
        generation.

        Optional 2: Experiment with additional type converters for the input 
        data, e.g. also accept `list` and `tuple`. Can you simple use
        the `list` or `tuple` constructors for type conversion here?
        Try to execute the `sort` method of a list object.

    === "Hints"

        Use the `input()` built-in function to read user input interactively.

        Remember you can `try` an operation and catch a resulting exception if
        it fails.

        Optional: `inspect.signature` can provide you with information about
        a callable's parameters.

        Optional 2: An easy way to parse text input to lists or tuples is by
        using `json.loads`.

        The program output could look something like this:

        ```
        python3 object_introspection.py
        Your input please: 42
        value = 42 [<class 'int'>]
        ==========================================
        Please select the method you want to call:
        1 - as_integer_ratio
        2 - bit_count
        3 - bit_length
        4 - conjugate
        5 - from_bytes
        6 - to_bytes
        ==========================================
        Please enter your choice: 1
        You selected 'as_integer_ratio'
        Result:
          (42).as_integer_ratio() --> (42, 1) [<class 'tuple'>]
          value = 42
        ```

    === "Solution"

        ??? example "*Really* take a peek now?"

            ``` python title="object_introspection.py"
            --8<-- "training/lessons/object-introspection/object_introspection.py"
            ```

            [:material-file-download:](object_introspection.py)
