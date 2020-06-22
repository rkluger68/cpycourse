# Exceptional behaviour: Creating and handling exceptions

Exceptions are the answer of handling errors during program-execution. A SyntaxError is an Exception which ca't be handled.
Every other error can be programatically be expected and processed

Errors mainly occur in circumstances where

1. program resources are
   - occupied/unavailable
2. data is not as expected
   - wrong-type
   - wrong format
   - wrong value e.g.out-of-range)

This section gives a brief overview of exception-handling

But lets start with creating a simple exception

## Creating an Exception

***FileNotFoundError***

This an example from the 1.st category 'resource not available'

``` python
>>> open('foo.txt')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'foo.txt'
>>>

```

***TypeError Exception example***

This an example from the 2.nd category 'data not as is expected'

```python
>>> a = 'foo' + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
>>> 
```


## Handling Exceptions

Similar to C++ `try-catch`- and Java's `try-catch` statements, Python provides a `try-except-finally`-statement.
The complete description can be founf in the Python docs [Handling Exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

***A simple example***
An example showing the general usage

``` python
>>> try:
...     # statements in the try-block
...     pass
... except FileNotFoundError as e:             # catch two different exceptions in one 'except'-block
...     # handle 'FileNotFoundError'
... except TypeError as e:
...     # handle 'TypeError'
...     pass
... except (ImportError, NameError) as e:      # catch two different exceptions in one 'except'-block
...     # Handle 'ImportError' and 'KeyError'
...     pass
>>>
```
In this example excpetions of type 'FileNotFoundError', 'ImportError','NameError' will be catched. Every other
exception will be provided to the surrounding code-block and has to be catzched and processed there.

***A more complex example***

The next example uses the optional `else`- and `finally`-clauses of a 'tyr-except`-statement

``` python
>>> try:
...     # statements in the try-block
...     pass
... except FileNotFoundError as e:
...     # handle 'FileNotFoundError'
...     pass
... except TypeError as e:
...     # handle 'TypeError'
...     pass
... except (ImportError, NameError)
...     # Handle ImportError and KeyError
... else: # optional
...     # do some additional works, in the case the 'try'-block succeeds
...     pass
... finally: # optional
...     # cleanup/free some ressource, this code block is executed no matter if te try succeeds or an error occurs
...     pass
>>>
```

*Note:*
- the `else`-block:
  - if present must folow the `except`-clauses
  - will only be executed if the `try`-blocks succeeds, i.e. it is executed after a successfull `try`-block
- the `finally`-clause:
  - will be executed no matter if the `try`-block succeeds or an error is raised
   - detailed descriptions plaese read [Defining Clean-Up Actions](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)


## Raising Exceptions

Raising an exception is simple done using the `raise`-statement (C++:`throw`-keyword, Java: `throw`-statement)

*** `raise`-example***

``` python
>>> raise TypeError('Argument has wrong type')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Argument has wrong type
>>> 
```

## User-defined Exceptions

Python programms provide a bunch of builtrin-exceptions (see [Exception Hierarchy]
(https://docs.python.org/3/library/exceptions.html#exception-hierarchy).
But sometimes it's necessary to prived more spceialized exceptions. 

***User-defined Exception***

```python
>>> class MyException(Exception):
...     def __init__(self, value):
...         self.value = value
... 
>>> type(MyException)
<class 'type'>
>>> 
```

***Usage***

```python
>>> try:
...     raise MyException('MyException-ERROR')
... except MyException as e:
...     print(str(e))
... 
MyException-ERROR
>>>
```




