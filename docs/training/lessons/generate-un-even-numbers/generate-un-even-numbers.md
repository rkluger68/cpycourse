!!! question "Lesson: Generate even and odd numbers"

    === "Task"
    
        Write a generator that yields even natural numbers [1, 2, 3, ...]
        infinitely, i.e.  until interrupted with `Ctrl-c`.

        Optional: Write a generator that yields even or uneven numbers,
        depending on a parameter that switches even/uneven behaviour.

        Optional: Write a generator that yields even or uneven numbers
        (switchable) up to an upper limit.

    === "Hints"

        Remember the 
        
        - loop control flow constructs (for-loop, while-loop) that can be used
          to do repeating things,
        - conditionals (if-elif-else) to decide which "code paths" or
          "branches" should be executed and
        - (maybe) the modulo operator or the `divmod()` built-in function for a
          possibility to check if a number is even or not.

        There are many ways to solve this task... 

    === "Solution"

        ??? example "*Really* take a peek now?"

            ``` python title="generate_numbers.py"
            --8<-- "training/lessons/generate-un-even-numbers/generate_numbers.py"
            ```

            [:material-file-download:](generate_numbers.py)
