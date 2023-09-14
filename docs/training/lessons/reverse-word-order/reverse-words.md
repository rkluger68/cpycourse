!!! question "Lesson: Reverse Words"

    === "Task"

        Create a function that
      
        - takes a single string argument and
        - returns a string with the words of the original argument in reversed order

        E.g. when given `"Mary says hi"` the function returns `"hi says Mary"`.

        Optionally: Create a Python script `reverse_words.py` that takes a string command line argument and prints the words of this argument in reversed order. E.g. when executed as
      
        `python3 reverse_words.py "Mary says hi"` the program prints
        `"hi says Mary"`.

        Optionally: Add options to the function and the script that allow for returning/printing the result string


    === "Hints"

         1. You can access the command line arguments through `sys.argv`.

         2. Python features an extensive command line parsing library in the stlib: `argparse`.

             - reversed or unreversed and that in
             - all-uppercase, all-lowercase, titlecase or capitalized.

         3. Use `help("")` or `help(str)` to learn useful string methods.

   
   === "Solution"

        ??? pied-piper "Example `reverse_order`-function"

            ``` py
            >>> def reverse_order(words):
            ...     list_of_words= words.split(' ')
            ...     list_of_words.reverse() # NOTE: reverse is inplace
            ...     return ' '.join(list_of_words)
            ... 
            >>> reverse_order("Mary says hi")
            'hi says Mary'
            >>>
            ```

        ??? pied-piper "Example reverse_words.py Script"

            ``` python title="reverse_words.py"
            --8<-- "training/lessons/reverse_word-order/reverse_words.py"
            ```

            ``` bash
            python3.8 reverse_words.py --help
            ```

            ``` bash
            python3.8 reverse_words.py --word "Hi says Mary" --format_style capitalize --reverse
            ```

            [:material-file-download:](reverse_words.py)

