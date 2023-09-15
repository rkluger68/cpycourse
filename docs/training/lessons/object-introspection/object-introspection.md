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

    === "Hints"

        Use the `input()` built-in function to read user input interactively.

        Remember you can `try` an operation and catch a resulting exception if
        it fails.

        The program output could look something like this:

        ```
        python3 object_introspection.py
        Your input please: 42
        value = 42 [type: int]
        ==========================================
        Please select the method you want to call:
          1 - as_integer_ratio
          2 - bit_length
          3 - conjugate
          4 - from_bytes
          5 - to_bytes
        ==========================================
        Please enter your choice: 
        You selected 'as_integer_ratio'
        Result:
            42.as_integer_ratio() --> (42, 1)
            value: 42
        ```

    === "Solution"

        ??? example "*Really* take a peek now?"

            ``` python title=""
            --8<-- "training/lessons/"
            ```

            [:material-file-download:](.py)
