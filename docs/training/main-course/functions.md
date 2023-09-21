# Functions

Providing repeating tasks or calculations in functions is an effective way of
code reuse ("write oncy, use many times"). This is a brief introduction of
Python functions, not covering all possible variations of function definitions.
More on this can be found in the official [Python docs on
functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions).

Functions - as basically everything in Python - are themselves first class
Python objects. Once defined, they can of course get executed (by "calling"
them). But like any other object they can just as well be assigned to a
variable, passed as arguments to another callable or used as a return value.


## Function Definition

In Python user defined functions are defined using the `def` statement. A
function definition is made up of a function header (defining the function name
and the call signature) and a function body (the implementation of the
task/calculation as a sequence of statements with an optional return
statement).


**Note:**
The terms "parameter" and "argument" are often used interchangeably, but this
is a little bit diffuse. The terms "formal parameters" for their use in
function definitions and "actual parameter" or "argument" for the use in
function calls may be a bit more precise. Here we'll use "parameter" for the
parameter variable names in function definitions and "argument" for the actual
values provided by the function caller.

## Function without Parameters

Function definition:

``` python
>>> def get_greeting():                    # function header
...     """Return a friendly greeting."""   # optional doc string
...     # function body
...     greet_text = "Hello!"
...     return greet_text
...
>>>
```

Such a function is *called* simply by using the function name followed by
parentheses:

Function call:

``` python
>>> my_greeting = get_greeting()
>>> print(my_greeting)
Hello!
>>>
```

## Function with Parameters

Function definition:

``` python
>>> def increment(a, stride):                    # function header
...     """Return a incremented with stride."""   # optional doc string
...     # function body
...     c = a + stride
...     return c
...
>>>
```

For calling the function we now add the arguments in the parentheses when calling the function:

Function call:

``` python
>>> result = increment(1, 2)
>>> print(result)
3
>>>
```

**Note:**
The number of call arguments equals the number of defined parameters.  The
order of the arguments must match the order of function parameters: During the
function call the 1.st call argument is mapped to the 1st function parameter,
the 2.nd call argument is mapped to the 2nd function parameter, etc. I.e. a
positional mapping from call arguments to parameters takes place - the
arguments are *positional arguments* here.

Let's give it a try!

--8<--
training/lessons/check-palindromes/check-palindromes.md
--8<--

## Function with Optional Parameters

Optional parameters are parameters with default values in the function
definition. Such optional parameters may be omitted during the function call.

Function definition with default paramater value:

``` python
>>> def increment(a, stride=1):  # function-header with default-argument
...     """Return a incremented with stride."""   # optional doc string
...     # function-body
...     c = a + stride
...     return c
...
>>>
```

Function call omitting the optional parameter:
  
``` python  
>>> result = increment(1)
>>> print(result)
2
>>> 
```
  
Function call overwriting the default value of the optional parameter:
 
``` python
>>> result = increment(1, 5)
>>> print(result)
6
>>> 
```
  
**Notes:**

- any parameters without default values must be provided by the caller when
  calling a function
- optional parameters must be defined at the end of the parameter list,
  otherwise a SyntaxError is raised

E.g.

``` python
>>> def add(a, b=1, c):
...     return a + b + c
... 
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```
  
  
## Function with Variable Parameter List (Variadic Parameter)

A function can be defined having a variable args parameter. This is specified
in preceding the last positional parameter with an asterisk-character `*` in
the function definition.

Function definition:

```python
>>> # 2 normal parameter & variable args parameter
>>> def print_info(header, footer, *args):
...     print(header)
...     for elem in args: print(elem)  # args is a tuple
...     print(footer)
... 
>>>
```


Varargs function call:

```python
>>> # last 2 arguments are mapped as a tuple into the *-parameter
>>> print_info('-->', '<--', 'Hello', 'World')
-->
Hello
World
<--
>>>
```
    
Varargs function call with more args:

``` python
# last 3 arguments are mapped as a tuple into the *-parameter
>>> print_info('-->', '<--', 'Tic', 'Tac', 'Toe')
-->
Tic
Tac
Toe
<--
>>>
```

## Keyword Arguments

In the above sections the functions are called with **positional arguments**.
In addition functions can also be called using named arguments (keyword
arguments).

To demonstrate this, we use the `increment`-function definition from above.

Function definition:
  
``` python
>>> def increment(a, stride=1):  # function-header
...     """Return a incremented with stride."""   # optional doc string
...     # function-body
...     c = a + stride
...     return c
...
>>>
```

Function call using keyword parameter:

``` python
>>> increment(a=1)
2
>>>
```

Function call using multiple keyword parameters:

``` python
>>> increment(stride=3, a=1)  # Note the order!
4
>>>
```

**Note:**
When (only) using keyword arguments the positions of the call arguments don't
matter.


## Functions with Variable Args and Variable Keyword Args

Python allows function definitions with arbitray additional keyword parameters.
This is specified in preceeding the last parameter with double-asterisk
characters `**`. Additional keyword arguments are mapped into the keyword parameter as a dictionary during the function call.

Function definition with variable keyword parameters:
  
``` python  
>>> def print_info(header, footer, *args, **kwargs):
...     print(header)
...     for elem in args:
...         print(elem)
...     for elem in kwargs.keys():
...         print('%s: %s' % (elem, kwargs[elem]))
...     print(footer)
... 
>>> 
``` 

Function call:

``` python
>>> print_info('-->', '<--', 'Madrid', 'Berlin', 'Paris', capitals_of='European Countries', belonging_to='EU')
-->
Madrid
Berlin
Paris
capitals_of: European Countries
belonging_to: EU
<--
>>>
```

## Function Return Value

Functions always return a single value. If a function body doesn't contain any
explicit return statement the function implicitly returns `None`. I.e. the
return statement is optional, still the function returns a value (the `None`
object).

``` python
>>> def say_hello():
...     print("Hello!")  # Look Ma, no explicit return statement!
... 
>>> function_result = say_hello()
Hello!
>>> print(function_result)  # We still get a None return value
None
>>> 
```

Functions can contain `return` at multiple places in the function body. Every
return statement leads to immediately leaving the function, the return value
being the function's result.

While Python functions always return a *single* object you can easily return
multiple values by packing them into a collection (`tuple`, `list`, ...).

``` python
>>> def divide(number, divisor):
...     """Divmod implementation, returns a (quotient, remainder) tuple. """
...     quotient = number // divisor
...     remainder = number % divisor
...     return (quotient, remainder)
... 
>>> result = divide(9, 4)
>>> print(result)
(2, 1)
```

You can "destructure" a tuple to its elements very conveniently:

``` python
>>> # divide(...) returns a 2-element tuple, which we destructure 
>>> res_quotient, res_remainder = divide(9, 4)
>>> print(res_quotient) 
2
>>> print(res_remainder) 
1
>>>
```

## Inner functions

Functions can be defined at every place, at module-level, inside classes (methods), but also inside functions.

***function definition***

``` python
>>> def outer_func(inner_func):
...     """ function which defines inner functions"""
...     def x():
...         print(x.__name__)
...     def y():
...         print(y.__name__)
...     # return an inner function, simply by its name
...     if inner_func == 1:
...         return x
...     else:
...         return y
... 
>>>
```

***function call***

``` python
>>> a_func = outer_func(1)    # assign a function
>>> a_func()                  # call the function
x
>>> b_func = outer_func(2)    # assign a function
>>> b_func()                  # call the function
y
>>>
```

**Note:**
As can be seen, functions are like ordinary Python objects that can be returned and assigned.

## Functions Annotations

[Function Annotations](https://docs.python.org/3/tutorial/controlflow.html#function-annotations) allow programmers to associate meta-information to a function-header. One kind of interesting mata-information are so called 'type-hints', which can provide 'type-information' about the function-paramertes and return-value.

Function annotations are stored in the `__annotations__` attribute of a function object.

***Function Annotation example***

``` python
>>> def concatenate(string_1: str, string_2: str) -> str:
...     return string_1 + string_2
... 
>>> concate('foo', 'bar')
'foobar'
>>> concate.__annotations__
{'string_1': <class 'str'>, 'string_2': <class 'str'>, 'return': <class 'str'>}
>>> 
```

For a more detailed inforamtions please refer to [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/) and [PEP 484 -- Type Hints ](https://www.python.org/dev/peps/pep-0484/)

***Note 1:***
Function annotations are optional, they are just informations. They are neither evaluated nor their compliance is enforced by the interpreter itself. It's provided in the language, helping other libraries do some type-checking.

***Note 2:***
'Type Hints'-support is implemented in the Python standard library [`typing`](https://docs.python.org/3/library/typing.html).

***Note 3:***
PEP - Python Enhancement Proposal - is the official process of suggesting enhancements to the Python language, please read [PEP 001 -- PEP Purpose and Guidelines](https://www.python.org/dev/peps/pep-0001/).


## Python Function Call Semantics

Traditional function call semantics are:

1. call-by-value: 

 - the value of the argument variable is copied to the call parameter of the function
 - changing the value inside the function doesn't effect the caller

2. call-by-reference: 

 - a reference of the caller's variable is passed to the call parameter of the
   function
 - as a consequence, changes to the variable inside the function will affect
   the callers variable (side effect from callee back to the caller) 
 - alongside the function return value, this provides additional communication
   channels between caller and callee (since the changes made inside the
   function can be seen on the outside)

**Python does not have such a distinction.** Every variable is a name
for an object / constitutes a reference to an object. In that sense everything
is passed around by reference, which is also the case for function calls.

Instead, the Python function call semantics are solely influenced by the
mutability or immutability of the caller's function call arguments:

1. Argument variables referring to an immutable object will not produce side
   effects on the caller side, since the function (the callee) can not change
   the immutable object.
2. Argument variables referring to a mutable object may have side effects on
   the caller side. If the mutable object is changed inside the function
   (callee), these changes will be visible to whatever reference/name for it on
   the outside.

**Function call with immutable argument:**

``` python
>>> a = 1
>>> id(1)             # object id of the 1 integer object 
139752035048832
>>> def increment(number):
...     # number refers to the same object as the callers variable (1)
...     print(id(number))
...     number += 1       # assignment (number = number + 1) creates new object
...     print(id(number)) # id of the new object
...     return a
... 
>>> b = increment(a)
139752035048832
139752035048864
>>> a
1    
>>> id(a)            # a still refers to the unchanged same object 1
139752035048832
>>>
```

**Note:**
Immutable objects of the caller are not affected by changes made by the callee
(the called function).
 
**Function call with mutable call argument:**

``` python
>>> caller_dict = {'a': 1, 'b': 2}
>>> id(caller_dict)     #  id of the object referred to by name caller_dict
139752035393824
>>> def change_mutable_arg(dct):
...     print(id(dct))  # dct refers to the same object as the callers variable (1)
...     for elem in dct.keys(): dct[elem] += 1  # changes the mutable object
...     print(id(dct))  # dct still refers to (changed)  origin object
...     return dct
... 
>>> result_dict = change_mutable_arg(caller_dict)
139752035393824
139752035393824
>>> caller_dict      # reflects the changes, side effect of the function call 
{'a': 2, 'b': 3}
>>> id(result_dict)  # same object, same id
139752035393824
>>> result_dict
{'a': 2, 'b': 3}
>>> 
```

**Note:**
Function calls with mutable object arguments may have side effects to the
caller - if the called function modifies a mutable object. 
