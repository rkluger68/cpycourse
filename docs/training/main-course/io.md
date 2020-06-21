# Get it in (and out): (File) Input and Output

Programs can consume data from different input- and produce data into different output-'channels'.
Generally speaking channels are a concept providing a common interface to concrete data-sources and data-sinks.
Bute heere we use the term 'channel' in a more fluffy sense, meaning we refer to concrete types of data-sources and data-sinks.

The channel-interfaces typically provides

- `open()`
- `close()`
- `read()` (or:`get()`, (`receive()`)
- `write()` (or:`put()`, (`send()`)

operations, sometimes named differently, as shown.

Typical channels are:

- standard-input/standard-output
- file-input/file-output
- input-streams/output-streams (streams can be seen as in-memory files) 
- sockets

Here we focus on ***files*** as concrete data-sources/-sinks.

## Open a file

Python provides a builtin function [`open()`](https://docs.python.org/3/library/functions.html#open) to open a file. It it doesn't exists it is created. The `open()`-call returns a 'file-object' (Remember: In Python everything is an object), sometimes called a 'file-descriptor', which provides typical file-operation methods.

***file-open***

``` python
>>> fd = open('foo.txt')       # same as open('foo.txt', 'r')
>>> type(fd)
<class '_io.TextIOWrapper'>
>>>
```

typical file-operations.

``` python
>>> dir(fd)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
>>> 
```
***Note 1:***
You can find help about all file-objects attribute and methods by using the `help()`-buitlin function

1. Get help for the `read()`-method
```python
>>> help(fd.read)
Help on built-in function read:

read(size=-1, /) method of _io.TextIOWrapper instance
    Read at most n characters from stream.
    
    Read from underlying buffer until we have n characters or we hit EOF.
    If n is negative or omitted, read until EOF
```
2. The full information for the file-object is displayed using `help(fd)`

***Note 2:***
The file-`open()`-call as shown, opens an **existing** file named 'foo.txt' (expected to be in the current working directory `cwd` , i.e the directory you started the python interpreter) in 'read-mode'. If your file is in a different directory than the `cwd`, you have to provide a fully qualified file-name either with a relative-path to the`cwd`or an absolute-path starting from the file-system-root. Here a Unix-based example using `/` as path-separator (use `\` on Windows-Systems):

- Assume your `cwd` is `/var/tmp/python_course/stundent_1`
- assume your file-location is `/var/tmp/python_course/stundent_1/data`
- then your qualified filename could be:
  - relative: `./data/.foo.txt`
  - absolute: `/var/tmp/python_course/stundent_1/data/foo.txt'

If the file doesn't exists, an error is raised:

``` python
>>> fd = open('bar.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'bar.txt'
>>>
```


## Create a file

There is no explictit function to create a file. A file is implicitly created using the `write()`-method providing the mode-parameter `w` if it doesn't exists.

``` python
>>> fd2 = open('bar.txt', 'w')
>>> 
```


## Read from a file

Assume the file 'foo.txt' contains the following 2-lines

```bash
cat foo.txt
abc
def
```

There are three ways getting the content of a file

- read number of characters
- complete file
- line-by-line

### Read some characters

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

``` python
>>> help(fd.readline)
Help on built-in function readline:

readline(size=-1, /) method of _io.TextIOWrapper instance
    Read until newline or EOF.
    
    Returns an empty string if EOF is hit immediately.
``` 
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

File-writing need an file-object opened in `write`-mode.
Assume you have an empty `bar.txt`file

Use the `write()`-method of the file-object

```python
>>> help(fd.write)
Help on built-in function write:

write(text, /) method of _io.TextIOWrapper instance
    Write string to stream.
    Returns the number of characters written (which is always equal to
    the length of the string).
```
Now open a file for writing

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

```bash
at bar.txt 
abc
def
```

## Close a file

To close a file use `close()`-method of the file-object

``` python
>>> fd.close()
>>>
```

***Note***
Never forget to close a file after finishing the file-processing.




