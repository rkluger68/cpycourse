# Everything will flow: Python control-flow constructs

Control flow(-statements) controls the order of execution of statements within a program. Python offers a common set of 'control-flow'-statements.

## choices - the `if`-statement

The `if`-statement provides condtional-execution of code-blocks, see also Python docs [`if`-statement](https://docs.python.org/3/tutorial/controlflow.html#if-statements).

***`if`-statement example***

```python
>>> a = 1
>>> if a == 0:
...     print('a is 0')
... elif a == 1:
...     print('a is 1')
... elif a == 2:
...     print('a is 2')
... else:
...     print('a neither 0, nor 1 or 2')
... 
>>> a is 1
```

## loops

## `for`-statement

The `for`-statement is a count-based loop-control, i.e. the number of repitions is based upon the number of elements of a 'sequence'. All sequence-types provide a `len()`-method, returning the number of elements of the object.

A 'sequence' can be (class construction in paranthesis)

1. `list`:  class/type-constructor `list()` e.g. `list([1,2,3])` or `list([(1,2,3))`
2. `tuple`: class/type-constructor `tuple()` e.g. `tuple([1,2,3])` or  `tuple((1,2,3))`
3. `str`:   class/type-constructor `str()` e.g `str("foo")` 
4. `range` (`range()`: e.g. `range(0,3)` or  `range(2)` or `range(1,3)`

***Note:***
The `range()`-builtin function creates object of type `range`, which produces a sequence of integers,
see (Range)[https://docs.python.org/3/library/stdtypes.html#ranges] or `help(range)`:
```python
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object

... <abbreviated>
 
```

***for-loop using a `list`-object (1)***

```python
>>> for elem in list([0,1,2]):
...     print(elem)
... 
0
1
2
>>>
```

***for-loop using a `list`-object (1)***

Normally you provide a list-counter-variable to the for-loop-statement

```python
>>> a
[1, 2, 3]
>>> for elem in a:
...     print(elem)
...     del a[-1]    # (1) changing the counter-variable inside the loop will affect number of repetitions
... 
1
2
>>> a                # (2) list-objects are mutable they will also effects the variable i the outer-block
[1]
>>>
```
***Note:***
Better use immutable 'tuple`-object


***for-loop using a `range`-objects (1)***

Example using 'start' and 'stop'-parameter

``` python
>>> for elem in range(0,3):
...     print(elem)
... 
0
1
2
>>>
```

***for-loop using a `range`-objects (2)***

Example using only 'stop'-parameter

``` python
>>> for elem in range(3):
...     print(elem)
... 
0
1
2
>>>
```

***for-loop using a `range`-objects (3)***

Example using only 'start'-, stop'- and 'step'-parameter


``` python
>>> for elem in range(0,9,3):
...     print (elem)
... 
0
3
6
>>>
```

## `while`-statement

The `while`-statement is a condition-based loop-control, i.e the number of repetitions is controlled by a boolean-expression evaluating to `True`.

In a while-loop a 'condition-variable' is set *before* and changed *within* the while-loop. 


### simple `while`-statement

```python
>>> a = 0
>>> while a < 3:
...     print(a)
...     a += 1   # change the condition variable
... 
0
1
2
>>
```


## `break`-statement

## `continue`-statement

## `else`-clause

## `pass`-statement


