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

## User-defined Exceptions

