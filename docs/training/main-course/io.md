# Get it in (and out): (File) Input and Output

Programs can consume data from different input- and produce data into different output-'channels'.
Generally speaking channels are a concept providing a common interface to concrete data-sources and data-sinks.
Bute here we use the term 'channel' in a more fluffy sense, meaning we refer to concrete types of data-sources and data-sinks.

Channel-interfaces typically provide

- `open()`
- `close()`
- `read()` (or:`get()`, (`receive()`)
- `write()` (or:`put()`, (`send()`)

operations, sometimes named differently, as shown.

Typical channels are:

- standard-input/standard-output
- streams: file-input/file-output (Text I/O, Binary I/O, Raw I/O)
- sockets: a 'network channel'

Here we focus on ***'Text I/O'-files*** ('text-stream') as concrete data-sources/-sinks.

## Open a file

Python provides the [`open()`](https://docs.python.org/3/library/functions.html#open) builtin function to open a file. If it doesn't exists an Exception is raised. The `open()`-call returns a 'file-object' (Remember: In Python everything is an object), sometimes called a 'file-descriptor', which provides typical file-operation methods.

***Access-Modes***

Files can be opened in different access-modes. The mode is provided as a parameter to the `open()`-call. Available modes are (copied from the `help(open)`-builtin call):

```python
========= ===============================================================
Character Meaning
--------- ---------------------------------------------------------------
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
========= ===============================================================
```


***file `open()`-call***

Python's interactive `help(open)`-builtin gives a full description of the `open()`-builtin, here abbreviated:

```python
>>> help(open)
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=T
rue, opener=None)
    Open file and return a stream.  Raise IOError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory) of the file to
    be opened or an integer file descriptor of the file to be
    wrapped. (If a file descriptor is given, it is closed when the
    returned I/O object is closed, unless closefd is set to False.)
    
... <abbreviated>

```

***Note:***

Navigation in `help()`-mode
 -`q` (quit) 
 - `<enter>`: Line down
 - `<space>`: Page down
 - On Windows the Python interpreter automatically 'quits' help-mode after reaching the end, on Linux you have toe enter `q`


1. file `open()` in 'read-mode' - if it doesn't exists:

``` python
>>> fd = open('bar.txt')      # same as open('bar.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'bar.txt'
>>>
```

2. file `open()` in 'read-mode' - if the file-exists

``` python
>>> fd = open('foo.txt')       # same as open('foo.txt', 'r')
>>> type(fd)
<class '_io.TextIOWrapper'>
>>>
```

The `open()`-builtin call will return a 'file-object' of type  `_io.TextIOWrapper`. It will open an **existing** file named 'foo.txt' (expected to be in the current working directory `cwd` , i.e the directory you started the python interpreter) in 'read-mode'. If your file is in a different directory than the `cwd`, you have to provide a fully qualified file-name either with a relative-path to the`cwd`or an absolute-path starting from the file-system-root. Here a Unix-based example using `/` as path-separator (use `\` on Windows-Systems):

- Assume your `cwd` is `/var/tmp/python_course/stundent_1`
- assume your file-location is `/var/tmp/python_course/stundent_1/data`
- then your qualified filename could be:
  - relative: `./data/.foo.txt`
  - absolute: `/var/tmp/python_course/stundent_1/data/foo.txt'


3. Check available 'file-operations' (methods) and attributes of 'file-objects'

A full set f available attributes and methods on (text-based)-file objects can be found in the Python docs of [`_io.TextIOWrapper`](https://docs.python.org/3/library/io.html?highlight=streams#id1).


***using `dir()`-builtin***

You can list the available attributes and methods of typical file-operations using the `dir(<file-object>)`-builtin function as shown here:

``` python
>>> dir(fd)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
>>> 
```

***using `help()`-builtin***

Again you can display the full description using the `help(fd)`-builtin on the returned file-object `fd` or any subsequent method or attribute e.g. `help(fd.read)`.


## Create a file

There is no explictit function to create a file. A file is implicitly created (if it doesn't exists) using the `write()`-method providing the mode-parameter `w`.

``` python
>>> fd2 = open('bar.txt', 'w')
>>> 
```

***Note:***
Be aware of that `w`-mode will overwrite (truncate) a files content, if you need to keep it, use `a`-append mode.

## Read from a file

Assume the file 'foo.txt' contains the following 2-lines

``` bash
cat foo.txt
abc
def
```

There are three ways getting the content of a file

- read number of characters
- complete file
- line-by-line

### Read some characters

***file `read()`-call***
Here we ask for 2-characters in a `read()`-call

```python
>>> fd = open('foo.txt')
>>> fd.read(2)
'ab'
>>> fd.read(2)
'c\n'
>>> fd.read(2)
'de'
>>> fd.read(2)
'f\n'
>>> 
```
this can be looped

```python
>>> fd = open('foo.txt')
>>> s = None
>>> while s != '':
...     s = fd.read(2)
...     print(repr(s))
... 
'ab'
'c\n'
'de'
'f\n'
''
>>>
```

***Note:***
`read()` returns the empty string `''` when it reached the EOF (End Of File)


### Read the complete file

***file `read()`-call***

If the `read()` is called without a parameter, it returns the complete content of the file .

``` python
>>> fd = open('foo.txt')
>>> s = fd.read()
>>> print(s)
abc
def

>>>
```

### Read line-by-line

A file can be read line-by-line using the `readline()`-method of the file-objects, see `help(fd.readline)`:

***file `readline()`-call***

Read line-by-line

``` python
>>> fd = open('foo.txt')
>>> s = None
>>> while s != '':
...     s = fd.readline()
...     print(repr(s))
... 
'abc\n'
'def\n'
''
>>>
```

## Write to a file

File-writing needs a file-object opened in 'write'- or 'append'--mode.
Assume you have an empty `bar.txt`file


*** file `write()`-call***

``` python
>>> fd = open('bar.txt', 'w')   # open the file in write-mode
>>> fd.write('abc\n')
4
>>> fd.write('def\n')
4
>>> fd.flush()
>>>
```

*** Note:***
The written output is buffered until it reaches a dedicated size before it is finally written to the file.
Flushing the buffer enforces writing the content to the buffer into the file.

You can check the written file

``` bash
cat bar.txt 
abc
def
```

## Close a file

To close a file use `close()`-method of the file-object

***file `close()`-call***

``` python
>>> fd.close()
>>>
```

***Note:***
Never forget to close a file after finishing the file-processing.




