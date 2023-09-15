# Everything will flow: Python control-flow constructs

Control flow (-statements) controls the order of execution of statements within
a program. Python offers a common set of 'control-flow' statements.

## choices - the `if` statement

The `if` statement provides condtional-execution of code-blocks, see also Python docs [`if` statement](https://docs.python.org/3/tutorial/controlflow.html#if-statements).

***`if` statement example***

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

## `for` statement

The `for` statement is a count-based loop-control, i.e. the number of
repetitions is based upon the elements of an "iterable".


An iterable can be e.g. a

 - `list`,
 - `tuple`,
 -  `str`, 
 - `range` (e.g. `range(0,3)` or  `range(2)` or `range(1,3)`
 - ...

### range() for loop examples

***Note:***
The `range()` built-in function creates object of type `range`, which produces
a sequence of integers, see
[Range](https://docs.python.org/3/library/stdtypes.html#ranges) or
`help(range)`:

```python
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object

... <abbreviated>
 
```

#### range() with start and stop

``` python
>>> for elem in range(2, 6):
...     print(elem)
...
2
3
4
5
>>>
```

#### range() with stop

``` python
>>> for elem in range(3):
...     print(elem)
... 
0
1
2
>>>
```

#### range() with start, stop and step

``` python
>>> for elem in range(0,9,3):
...     print (elem)
... 
0
3
6
>>>
```

### Looping over objects

Example: `for` loop using a `list` object:

```python
>>> for elem in [0, 1, 2]:
...     print(elem)
... 
0
1
2
>>>
```

You *are* able to modify a looped-over mutable object:

```python
>>> for elem in my_list:
...     print(elem)
...     del my_list[0]
... 
1
3
>>>
```

But: ***Don't do that!*** You'll create hard to understand code and unexpected
behaviour.

## `while` statement

The `while` statement is a condition-based loop-control, i.e the number of
repetitions is controlled by a boolean-expression evaluating to `True`.

In a `while` loop a 'condition variable' is evaluated *before* running the loop
body (and usually changed *within* the body). 

### simple `while` statement

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

## `break` statement

With the `break` statement loops can be terminated prematurely.

Usage: Stop iteration at occurence of a condition.

***Using `break` statement in a `for` loop***

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

***Using `break` statement in a `while` loop***

```python
>>> s = "text"
>>> idx = 0
>>> while idx < len(s):
...     if s[idx] == 'x':
...         break
...     print(s[idx])
...     idx += 1
... 
t
e
>>>
```

## `continue` statement

With a `continue` statement loops can skip the rest of the current iteration.

Usage: 'skip-on-condition'

***Using `continue` statement in a `for` loop***

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

***Using `continue` statement in a `while` loop***

```python
>> idx = 0
>>> while idx < len(s):
...     if s[idx] == 'x':
...         idx += 1
...         continue
...     print(s[idx])
...     idx += 1
... 
t
e
t
>>>
```

## `else` clause of loops

In Python loops can have an optional `else` clause.

See the Python docs for the purpose of a[loop `else` clause](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)) and when it is executed. Quote: 

"Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement"

So the `else` clause can be seen as 'finalizer' block of statements which are
processed ath the end of a loop during normal operations.

The exact workings of the `else` clause is a bit hard to remember.[^1] Still,
sometimes it comes in handy.

[^1]: For one of the authors, at least. :wink:

***Using `else` clause in a `for` loop***

``` python
>>> s = "text"
>>> for elem in s:
...     print(elem)
... else:
...     print("End of normal processing")
... 
t
e
x
t
End of normal processing
>>> 
```

whereas:

``` python
>>> s = "text"
>>> for elem in s:
...     print(elem)
...     if elem == "x":
...         break
... else:
...     print("End of normal processing")
...
t
e
x
>>>
```


***Using `else` clause in a `while` loop***

``` python
>>> s = "text"
>>> idx = 0
>>> while idx < len(s):
...     print(s[idx])
...     idx += 1
... else:
...     print("End of normal processing")
... 
t
e
x
t
End of normal processing
>>>
```

whereas:

``` python
>>> s = "text"
>>> idx = 0
>>> while idx < len(s):
...     print(s[idx])
...     if s[idx] == "x":
...         break
...     idx += 1
... else:
...     print("End of normal processing")
...
t
e
>>>
```

## `pass` statement

The `pass`- statement is a `noop` statement, meaning no-operation, as it does
nothing.

Use it where you need a statement syntactically but there is no needed/sensible
program action, see the [Python Docs on `pass` statement](https://docs.python.org/3/tutorial/controlflow.html#pass-statements).

*** Example - `pass` statement in a class definition***

```python
>>> class A: pass
... 
>>> type(A)
<class 'type'>
>>>
```

## `match` statement

The match statement is a relatively young addition at the time of writing, and
we won't cover it in any depth here.

Dubbed 'structural pattern matching' it's new in Python version 3.10 and allows
you to match a value ('subject') against one ore more patterns.

When the match subject matches a pattern (a 'match success' or 'pattern
success') then the matched values may be bound to names.

In it's simplest form it looks s.th. like this:

```python
>>> def match_traffic_light_status(status):
...     match status:
...         case 'green':
...             print('Go!')
...         case 'red':
...             print('Stop!')
...         case _:
...             print(f'traffic light {status}?!')
... 
>>> match_traffic_light_status('red')
Stop!
>>> match_traffic_light_status('blue')
traffic light blue?!
>>>
```

In this basic form it bears some similarity to switch-case constructs found in
e.g. the C language, but it is way more powerful.

See the [Python
tutorial](https://docs.python.org/3/tutorial/controlflow.html#match-statements)
and [Reference](https://docs.python.org/3/reference/compound_stmts.html#match)
for in-depth knowledge on `match`.
