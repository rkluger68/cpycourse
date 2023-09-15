!!! question "Lesson: Round Input Numbers"

    === "Task"

        Write a program that lets the user enter a number with decimal places
        (e.g. 12.33) and then outputs this number rounded up and down to 
        whole numbers.

        Optional: Instead of rounding to whole numbers round to a configurable
        number of decimal places. Ask the user for the rounding decimal places
        to use first. Note: Do not round up *and* down in this case.

        Optional: Use `decimal.Decimal` to represent the input numbers if you
        used floats before. Otherwise, use `float` for the numbers now.

    === "Hints"

        Use the `input()` built-in function to read user input interactively.

        Remember how whole numbers can be represented in Python. Use
        `help(round)` to find out about the built-in `round()` function.

        The program output could look something like this:

        ```
        python3 input_number_rounding.py
        Please enter a number: 12.33
        Rounded down: 12
        Rounded up: 13
        
        Please enter a number: 42
        Rounded down: 42 
        Rounded up: 42
        ```

    === "Solution"

        ??? example "*Really* take a peek now?"

            ``` python title="input_number_rounding.py"
            --8<-- "training/lessons/input-number-rounding/input_number_rounding.py"
            ```

            [:material-file-download:](input_number_rounding.py)
