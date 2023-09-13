import os
import pprint

# NOTE:
#   Windows: 'link' is always recognized as a 'file'
#   Unix: 'islink()' is also true for regular files, so need to check for
#         'islink()' before 'isfile()'


def main(path):
    # NOTE: dict: <key=filename> <value=filetype>
    d0 = {
        entry: 'dir' if os.path.isdir(entry) else
        'link' if os.path.islink(entry) else
        'file' if os.path.isfile(entry) else
        'other'
    for entry in os.listdir(path)}

    print('>>> dict-comprehension dictionary (1) <<<')
    pprint.pprint(d0)

    d1 = {
        entry: 'dir' if os.path.isdir(f'{os.path.join(path, entry)}') else
        'link' if os.path.islink(f'{os.path.join(path, entry)}') else
        'file' if os.path.isfile(f'{os.path.join(path, entry)}') else
        'other'
    for entry in os.listdir(path)}

    print('>>> dict-comprehension dictionary (2) <<<')
    pprint.pprint(d1)


    # NOTE: dict: <key=filetype> <value=list-of-filenames> 
    d2 = {} 
    for _entry in os.listdir(path):
        entry = f'{os.path.join(path, _entry)}'
        if os.path.isdir(entry):
            if 'dir' in d2.keys(): d2['dir'].append(_entry)
            else: d2['dir'] = [_entry]
        else:
            if os.path.islink(entry):
                if 'link' in d2.keys(): d2['link'].append(_entry)
                else: d2['link'] = [_entry]
            else:
                if os.path.isfile(entry):
                    if 'file' in d2.keys(): d2['file'].append(_entry)
                    else: d2['file'] = [_entry]
                else:
                    if 'other' in d2.keys(): d2['other'].append(_entry)
                    else: d2['other'] = [_entry]

    print('>>> for-loop_if-else dictionary (1) <<<')
    pprint.pprint(d2)

    # NOTE: as dict 'd' dict: <key=filename> <value=filetype>
    d3 = {}
    for _entry in os.listdir(path):
        entry = f'{os.path.join(path,_entry)}'
        if os.path.isdir(entry): d3[_entry] = 'dir'
        else:
            if os.path.islink(entry): d3[_entry] = 'link'
            else:
                if os.path.isfile(entry): d3[_entry] = 'file'
                else:
                    d3[entry] = 'other'
                    print(f'file-name: {entry} ==> "other"')
                    #print(os.path.dirname(os.path.abspath(entry)))
                    

    print('>>> for-loop_if-else dictionary (2) <<<')
    pprint.pprint(d3)
    #print(os.name)



if __name__ == '__main__':
    main(path='./test_dir')