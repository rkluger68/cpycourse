!!! question "Lesson: Iterate file"

    === "Task"

        Create a Python script that

        - takes a file name/path as a command line argument
        - opens a file using the built-in `open()` function
        - uses a generator to iterate over the file's lines and
        - yields these lines split by the ','-separator character and
        - prints them to stdout (i.e. the console)

        Optional: Add a command line option that allows for setting the separator to another character.

        Optional 2: Add command line options to set an output file path and write the processed lines to this output file, joining the split lines with another "target separator" (also set with a command line option).

    === "Hints"

        Use the `argparse` stdlib library to parse the command line (see https://docs.python.org/3/howto/argparse.html).

   
    === "Solution"

        ??? pied-piper "Example `iterate_file.py"

            ``` python title="iterate_file.py"
            --8<-- "training/lessons/file-iteration/iterate_file.py"
            ```

            [:material-file-download:](iterate_file.py)
