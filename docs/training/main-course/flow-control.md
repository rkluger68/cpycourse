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

The `for`-statement is a count-based loop-control, i.e. the number of repetitions is based upon the number of elements of a 'sequence'. All sequence-types provide a `len()`-method, returning the number of elements of the object.

A 'sequence' can be (class construction in paranthesis)

1. `list`:  class/type-constructor `list()` e.g. `list([1,2,3])` or `list([(1,2,3))`
2. `tuple`: class/type-constructor `tuple()` e.g. `tuple([1,2,3])` or  `tuple((1,2,3))`
3. `str`:   class/type-constructor `str()` e.g `str("foo")` 
4. `range` (`range()`: e.g. `range(0,3)` or  `range(2)` or `range(1,3)`

***Note:***
The `range()`-builtin function creates object of type `range`, which produces a sequence of integers,
see [Range](https://docs.python.org/3/library/stdtypes.html#ranges) or `help(range)`:
```python
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object

... <abbreviated>
 
```

***for-loop using a `list`-object (1)***

In this example create a sequence as an implicit unnamed counter variable

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

Normally you provide an explicit list-counter-variable to the for-loop-statement

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
Better use immutable 'tuple`-object to avoid side-effects


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

With `break`-statement loops can quit prematurely

Usage: Stop iteration at '1.st-occurence-of'

***Using `break`-statement in a `for`-loop***

```python
>>> s = "text"
>>> for elem in s:
...     if elem == 'x':
...         break
...     print(elem)
... 
t
e
>>>
```

***Using `break`-statement in a `while`-loop***

```python
>>> s = "text"
>>> a = 0
>>> while a < len(s):
...     if s[a] == 'x':
...         break
...     print(s[a])
...     a += 1
... 
t
e
>>>
```

## `continue`-statement

With a `continue`-statement loops skip the current iteration

Usage: 'skip-on-condition'

***Using `continue`-statement in a `for`-loop***

```python
>>> for elem in s:
...     if elem == 'x':
...         continue
...     print(elem)
... 
t
e
t
>>>
```

***Using `continue`-statement in a `while`-loop***

```python
>> a = 0
>>> while a < len(s):
...     if s[a] == 'x':
...         a += 1
...         continue
...     print(s[a])
...     a += 1
... 
t
e
t
>>>
```

## `else`-clause

As from the Python docs about the purpose of `else`-clause and when it is executed (see [`else`-clause](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)):

"Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement"

So the `else`-clause can be seen as 'finalizer'-block of statements which are processed ath the end of a loop during normal operations.

***Using `else`-clause in a `for`-loop***

``` python
>>> s = "text"
>>> for elem in s:
...     print(elem)
... else:
...     print('End of normal processing')
... 
t
e
x
t
End of normal processing
>>> 
```



***Using `else`-clause in a `while`-loop***

``` python
>>> s = "text"
>>> a = 0
>>> while a < len(s):
...     print(s[a])
...     a = a+1
... else:
...     print('End of normal processing')
... 
t
e
x
t
End of normal processing
>>>
```

***Note:***
Don't mix up with the `else`-clause of the `if`-statement which is part of a choice-control

## `pass`-statement

The `pass`- statement is a `noop`´-statement , meaning no-operation, as it does nothing:

Usage: As from the Python Docs[`pass`-statement](https://docs.python.org/3/tutorial/controlflow.html#pass-statements) 
"It can be used when a statement is required syntactically but the program requires no action"

*** Example `pass`-statement*- demonstrating a class-definition**

```python
>>> class A: pass
... 
>>> type(A)
<class 'type'>
>>>
```


