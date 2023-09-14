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

        This site's repo contains a test directory with some typical (unix)
        file types (symbolic link, directory, file) in the
        `/docs/training/lessons/rewrite-dict-comprehension/test_dir` folder.

        Some notes:

        - isfile() and isdir() follow symbolic links, so they will return their
          link target file type. Thus, the islink() condition must come first
          to actually detect a link file type.
        - Windows: no symlinks, a checked-out link from the test_dir is
          represented as a file and thus recognized as 'file'

    === "Solution"

        ??? example

            ``` python title="rewrite_dict_comprehension.py"
            --8<-- "training/lessons/rewrite-dict-comprehension/rewrite_dict_comprehension.py"
            ```

            [:material-file-download:](rewrite_dict_comprehension.py)
