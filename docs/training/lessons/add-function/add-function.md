!!! question "Lesson: Add Function"
   
    === "Task"
        
        Create a Python program that repeatedly
        
        - reads 2 float values from the user
        - adds the 2 input values and
        - prints the resulting sum value

        until the user interrupts the program with `Ctrl-c`.

        To add the 2 int numbers create a custom `add(x, y)` function that you
        call to perform the addition.

        Optional: After printing the sum value, ask the user if she wants to
        continue. If not, print "Goodbye!" and end the program.

    === "Hints"
        
        Remember that the `input()` function returns text - to use number
        operations you will need to convert the resulting user input to a
        `float`: `float(input_text)`.

        Your program output could look like this:

        ```
        python add-function/add_function.py 

        Please enter number x: 3
        Please enter number y: 4
        The sum of x and y is 7.0.
        Do you want to continue (y/n)? [y] n
        Goodbye!
        ```

    === "Solution"

        ??? example "*Really* take a peek now?"

            ``` python title="add_function.py"
            --8<-- "training/lessons/add-function/add_function.py"
            ```

            [:material-file-download:](add_function.py)
