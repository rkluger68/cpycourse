import os
import pprint

# Notes:
# - isfile() and isdir() follow symbolic links, so they will return their link
#   target file type. Thus, the islink() condition must come first to actually
#   detect a link file type.
# - Windows: no symlinks, a checked-out link from the test_dir is represented
#   as a file and thus recognized as 'file'


def dict_comp_filetypes_cwd():
    """Return a {<path entry>: <file type} dictionary of the current working
    directory.

    Uses a dict comprehension.
    """
    dct = {
        entry:
            'link' if os.path.islink(entry) else
            'dir' if os.path.isdir(entry) else
            'file' if os.path.isfile(entry) else
            'other'
        for entry in os.listdir()
        }
    return dct


def dict_comp_filetypes(path='.'):
    """Return a {<path entry>: <file type} dictionary of the given path.

    Uses a dict comprehension.
    """
    # To avoid joining path + entry to the full path both for the dict key and
    # in the value's if-else expression, we (ab)use the walrus operator.
    # This *must* sit in the if condition part of the dict comprehension.
    # 
    # Feels a tiny bit hacky, without walrus it looks like this:
    # 
    # dct = {
    #   os.path.join(path, entry):
    #       'link' if os.path.islink(os.path.join(path, entry)) else
    #       'dir' if os.path.isdir(os.path.join(path, entry)) else
    #       'file' if os.path.isfile(os.path.join(path, entry)) else
    #       'other'
    #   for entry in os.listdir(path)
    #   }
    dct = {
        file_path:
            'link' if os.path.islink(file_path) else
            'dir' if os.path.isdir(file_path) else
            'file' if os.path.isfile(file_path) else
            'other'
        for entry in os.listdir(path)
        if (file_path := os.path.join(path, entry))
        }
    return dct


def for_loop_filetypes(path='.'):
    """Return a {<path entry>: <file type} dictionary of the given path.
    
    Uses a traditional for loop.
    """
    dct = {}
    for entry in os.listdir(path):
        file_path = os.path.join(path, entry)

        if os.path.isdir(file_path):
            file_type = 'dir'
        elif os.path.islink(file_path):
            file_type = 'link'
        elif os.path.isfile(file_path):
            file_type = 'file'
        else:
            file_typ = 'other'
        dct[file_path] = file_type

    return dct


def main(path):
    func = dict_comp_filetypes_cwd
    print(f'\n*** dict comprehension using {func.__name__}')
    dct = func()
    pprint.pprint(dct)

    func = dict_comp_filetypes
    print(f'\n*** dict comprehension using {func.__name__}(path={path})')
    dct = func(path)
    pprint.pprint(dct)

    func = for_loop_filetypes
    print(f'\n*** dict comprehension using {func.__name__}(path={path})')
    dct = func(path)
    pprint.pprint(dct)


if __name__ == '__main__':
    main(path='./test_dir')
