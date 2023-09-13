!!! question "Lesson: Rewrite dict comprehension"

    === "Task" 
    
        Rewrite the dict comprehension

        ``` python
        dct = {
            entry:
                'link' if os.path.islink(entry) else
                'dir' if os.path.isdir(entry) else
                'file' if os.path.isfile(entry) else
                'other'
            for entry in os.listdir()
            }
        ```

        using a "traditional" for loop and if-else statements.

    === "Hints"

        Use `help(os.listdir)` for more information about this standard library
        function.

    === "Solution"

        ??? example

            ``` python title="rewrite_dict_comprehension.py"
            --8<-- "training/lessons/rewrite-dict-comprehension/rewrite_dict_comprehension.py"
            ```

            [:material-file-download:](rewrite_dict_comprehension.py)
