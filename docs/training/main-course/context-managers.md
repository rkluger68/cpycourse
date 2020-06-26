# Context is Key: Context Managers

Python objects that follow the so-called "context manager protocol" can be 
used with Python's `with` statement. The `with` statement starts a code block
that is processed "within a context", e.g. a resource that has been acquired:

``` python
>>> with open("myfile.txt", "w") as myfile:
...     myfile.write("Hello!")
... 
6
>>> with open("myfile.txt", "r") as myfile:
...     myfile.readlines()
... 
['Hello!']
>>> 
>> myfile
<_io.TextIOWrapper name='myfile.txt' mode='r' encoding='UTF-8'>
>>> myfile.closed
True
>>> 
```

After the `with` statement code block ends the context is "terminated", e.g. an
acquired resource gets closed or destroyed.

This is a useful mechanism for (but not limited to) closing resources that
shouldn't be left open. Prominent examples for such resources are

 - files
 - network connections
 - database connections

It's possible to use multiple context managers for a code block:

``` python
>>> with open('in.txt', 'r') as infile, open('out.txt', 'w') as outfile:
>>>     for line in infile:
>>>         # better do s.th. sensible with line first...
>>>         outfile.write(line)
>>>
```

Context managers can be implemented by providing an object with the context
manager protocol methods:

``` python
class MyContextManager:
    def __enter__(self):
        # context initialization goes here (e.g. resource acquisition)
        # ...

    def __exit__(self, exc_type, exc_value, traceback):
        # context finalization goes here (e.g. resource closing/cleanup)
        # ...

```

A context manager object gets *entered* through the `with` statement execution
and *exits* when the `with` code block ends.

Useful tools for easily creating context managers can be found in the
[stdlib `contextlib`](https://docs.python.org/3/library/contextlib.html).
