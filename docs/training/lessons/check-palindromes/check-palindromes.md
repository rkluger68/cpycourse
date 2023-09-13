!!! question "Lesson: Check palindromes"

    === "Task"

        Create a function that
        
        - takes a single string argument and
        - returns `True` if string is a palindrome, `False` otherwise.

        1. Use a loop for implementation.
        2. Try an alternative implementation using "extended slicing": Check
           `word == word[::-1]` 
        3. Test the function by calling it with a palindromes and other texts.
        
        Optional: Create a Python script `check_palindromes.py` that asks the
        user to enter a text to be checked if it qualifies as a palindrome.
       
        E.g.
        ```
        python3 check_palindromes.py
        Please enter a word: abba
        entered word: abba     # optional output
        reverse word: abba
        is_palindrome: abba ==> True
        ```
        
        ```
        python3 check_palindromes.py
        Please enter a word: foo
        entered word: foo       # optional output
        reverse word: oof
        is_palindrome: foo ==> False
        ```

        Optional: Instead of interactive user input, accept a command line
        argument to your Python script so that it can be invoked like `python
        check_palindromes.py "racecar"`.

    === "Hints"

        Use the `input()` built-in function to read user input interactively.
        
        The most basic form to read command line arguments is by accessing
        them through `sys.argv`. For anything more serious the
        [argparse](https://docs.python.org/3/library/argparse.html) standard
        library module can be used.

    === "Solution"

        ??? example

            ``` python title="check_palindromes.py"
            --8<-- "training/lessons/check-palindromes/check_palindromes.py"
            ```

            [:material-file-download:](check_palindromes.py)
