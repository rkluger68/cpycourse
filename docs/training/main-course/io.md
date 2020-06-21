# Get it in (and out): (File) Input and Output

Programs can consume data from different input- and produce data into different output-'channels'.
Channels are a concept providing a common interface to concrete data-sources and data-sink.

The interface typically provides

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
typical file-operations

``` python
>>> dir(fd)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
>>> 
```

***Note:***
The file-`open()`-call as shown, opens an **existing** file named 'foo.txt' (expected to be in the current working directory `cwd` , i.e the directory you started the python interpreter) in 'read-mode'. If your file is in a different directory than the `cwd`, you have to provide a fully qualified file-name either with a relative-path to the`cwd`or an absolute-path starting from the file-system-root. Here a Unix-based example using `/` as path-separator (use `\` on Windows-Systems):

- Assume your `cwd` is `/var/tmp/python_course/stundent_1`
- assume your file-location is `/var/tmp/python_course/stundent_1/data`
- then your qualified filename could be:
  - relative: `./data/.foo.txt`
  - absolute: `/var/tmp/python_course/stundent_1/data/foo.txt'


## Read from a file

## Write to a file


