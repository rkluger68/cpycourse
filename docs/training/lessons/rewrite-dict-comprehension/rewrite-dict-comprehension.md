!!! question "Lesson: Rewrite dict comprehension"
    Rewrite the dict comprehension

    ``` python
    d = {entry: 'dir' if os.path.isdir(entry) else
                'file' if os.path.isfile(entry) else
                'link' if os.path.islink(entry) else
                'other'
         for entry in os.listdir()}
    ```

    using a "traditional" for loop and if-else statements.

