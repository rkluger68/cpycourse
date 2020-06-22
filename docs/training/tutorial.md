# A Curious Python Course: Tutorial

A little introduction to the language mainly by example, to show (some of)
Python's main features.

This tutorial refers to Python version 3.

## Python Documentation ##

If you need information way beyond what we can show you here, the (great!)
official Python documentation can be found here:
https://docs.python.org/3/index.html

## Starting the Python interpreter

For an **interactive session** simply type `python` or `python3` in a console/shell of your computer (`$`-shell prompt on \*nix-based systems):

``` bash
$ python
Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
[GCC 4.8.5] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The first lines show the interpreter version, some information about the build
environment of the interpreter (compiler version and platform) and the
copyright information.

The Python *prompt* `>>>` is signaling that the interpreter awaits user input.

The version and copyright information on startup can be suppressed using the
quiet-option `-q`.

``` bash    
$ python -q
>>>
```

**Note:**
From now on, whenever you see `>>> ...`-lines this means an example in an 
interactive Python session.

Type in your 1.st Python statement. After pressing the `<Enter>`-key the
interpreter will execute the statement, and in this case will show the result.

``` python
>>> print("Hello, world!")
Hello, world!
>>>
```

After finishing the execution of the statement, the interpreter comes back to the prompt, awaiting the next input.

If you enter a simple expression at the prompt (e.g. an integer or string 
[literal](main-course/grasping-python.md/literals) and press Enter a *string
representation* of the result is printed:

``` python
>>> "Hello, world!"
'Hello, world!'
>>> 42
42
>>> 
```


The interactive session can be stopped by pressing `<Ctrl>-D` (Linux) or `<Ctrl>-Z` (Windows).

A **summary of the Python interpreter's commandline options** can be listed with its help option `-h`. This will display the **usage**, the available commandline options and **environment variables** controlling the interpreter. Here's
the output of a Python 3 interpreter on Linux:

``` 
$python3 -h
usage: python3 [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-b     : issue warnings about str(bytes_instance), str(bytearray_instance)
         and comparing bytes/bytearray with str. (-bb: issue errors)
-B     : don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser; also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the user's environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : remove assert and __debug__-dependent statements; add .opt-1 before
         .pyc extension; also PYTHONOPTIMIZE=x
-OO    : do -O changes and also discard docstrings; add .opt-2 before
         .pyc extension
-q     : don't print version and copyright messages on interactive startup
-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : don't imply 'import site' on initialization
-u     : force the binary I/O layers of stdout and stderr to be unbuffered;
         stdin is always buffered; text I/O layer will be line-buffered;
         also PYTHONUNBUFFERED=x
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
         when given twice, print more information about the build
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-X opt : set implementation-specific option
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]

Other environment variables:
PYTHONSTARTUP: file executed on interactive startup (no default)
PYTHONPATH   : ':'-separated list of directories prefixed to the
               default module search path.  The result is sys.path.
PYTHONHOME   : alternate <prefix> directory (or <prefix>:<exec_prefix>).
               The default module search path uses <prefix>/lib/pythonX.X.
PYTHONCASEOK : ignore case in 'import' statements (Windows).
PYTHONIOENCODING: Encoding[:errors] used for stdin/stdout/stderr.
PYTHONFAULTHANDLER: dump the Python traceback on fatal errors.
PYTHONHASHSEED: if this variable is set to 'random', a random value is used
   to seed the hashes of str, bytes and datetime objects.  It can also be
   set to an integer in the range [0,4294967295] to get hash values with a
   predictable seed.
PYTHONMALLOC: set the Python memory allocators and/or install debug hooks
   on Python memory allocators. Use PYTHONMALLOC=debug to install debug
   hooks.
```

## Running a Python program

A program is built up of a **sequence of python statements** (i.e. the "programcode" or "code"). This code can be 

 - entered at the Python prompt, in interactive mode,
 - provided as a command line argument or
 - stored in module files with the `.py`-extension.

For simple, short ad-hoc one-liners it can be very handy to use command line
string arguments:

``` bash
$ python -c "print('Hello'); print('World')"
Hello
World
$
```    

As shown you can use the semicolon to separate multiple statements.

But typically the code is placed into Python source files named `<module name>.py`, in our case [helloworld.py](../src/helloworld.py):

``` python
--8<--
src/helloworld.py
--8<--
```
The code can then be executed running the following command:

``` bash
$ python helloworld.py
Hello, world!
$
```

### A Sample Python Program

This is a simple Python program that calculates the present value of
a series of cashflows
``` python
--8<--
src/present_value.py
--8<--
```

Running this program yields the following output:
```
$ python3 src/present_value.py 
Present value for [-100, -2, 3, 6, 8, 110] and interest rate 0.03:
    pv = 8.371752776288233
```

### Python Program Building Blocks

A program is built as a sequence of instructions. The basic building blocks of 
a Python program are:

1. [Expressions](main-course/grasping-python.md#expressions)
1. [Operands and Operators](main-course/grasping-python.md#operands-and-operators)
1. [Statements](main-course/grasping-python.md#statements)
1. [Comments](main-course/grasping-python.md#comments)

So

  - a program is a sequence of comments and statements  
  - a statement is either an 'executable instruction' (**do-something**) or an 'evaluable expression' (**compute-something**)  
  - an expression is built up from operands and operators  

### Program Execution

Running a program can be described as a top-down line-by-line processing:
evaluation of expressions and execution of statements.

## Variables and Assignments

Variables are one of the the key elements of programming languages. Allthough
the implementation may differ, the key concept is the same:
Providing named access to an area in memory holding data, which can be changed during program execution.

In Python a variable is a name referencing an object in memory. You can create
a variable with an assignment-statement:

``` python
>>> a = 5
```

Python variables can be rebound by further assignments.  At different points
in time, the variable may refer to different objects, with different values
and types of value. This makes Python a dynamically typed language.

``` python
>>> a = 5 # create variable 'a' which is bound to integer object 5
>>> a     # named access to object
5
>>> type(a) # the value variable 'a' is of type 'int'
<class 'int'>
>>> a = 'foo' # rebind the variable to a different object
>>> a
'foo'
>>> type(a) # the value variable 'a' now is of type 'str'
<class 'str'>
>>>
```

## It's all about data: Python Data Types and Python Objects

[Python provides a bunch of popular data types.](main-course/builtin-types.md)

All data is represented as an object and has a type:
``` python
>>> 'foo'
'foo'
>>> type('foo')  # type built-in function returns an object's type
<class 'str'>
>>> isinstance('foo', str)  # isinstance tests if an object is of a certain type
True
>>>
```

### Strings - `str`

Strings are essential for handling text data:

``` python
>>> 'Python knows text'
'Python knows text'
>>> "Python knows text"  # double-quoted is also allowed
'Python knows text'
>>> # triple quoted text can span lines
>>> """Python
... knows
... text"""
'Python\nknows\ntext'
>>> 
```
    

Strings conveniently support many useful operations:
``` python
>>> ''.join(('foo', 'bar'))  # string concatenating using builtin method 'join()'
'foobar'
>>> 'foo' + 'bar'             # string concatenating using '+' operator
'foobar'
>>> 'foobar'.upper()
'FOOBAR'
>>> 'foo bar'.title()
'Foo Bar'
```

``` python
Strings are sequence of characters indexed by integer values. You can use the
indexes to access the individual characters:

>>> 'foo bar'[0]  # 1st character
'f'
>>> 'foo bar'[-1]  # last character
'r'
>>> 'foo bar'[2:5]  # slice of characters
'o b'
>>> 
```


### Numeric Data Types

Numeric data types represent numeric values. Python has the built-in numeric
data types `int` and `float` that support the usual arithmetic operations.

`int` is used for integers or "whole" numbers:

``` python
>>> 1
1
>>> type(1)
<class 'int'>
```

Some basic integer operations:

``` python
>>> 1 + 2
3
>>> (1 + 2) * 3
9
>>> 2**5
32
>>> 
```

Fractional numbers are represented by `float`:

``` python
>>> 1.2
1.2
>>> type(1.2)
<class 'float'>
```

Example `float` operations:

``` python
>>> 1.1 + 1.2
2.3
>>> (1.1 + 1.2) * 3.0
6.8999999999999995
>>> 1.1**2
1.2100000000000002
>>> 
```

As you'll have noticed `float` is
[not an exact data type](https://docs.python.org/3/tutorial/floatingpoint.html)
.

If you need more accuracy than `float`  arithmetic supports the Python
standard library also features a
[Decimal data type](https://docs.python.org/3/library/decimal.html).

### Lists - `list`

A Python list is an array of unnamed objects of (potentially) different types.

``` python
>>> [1, 'foo', 3.14]
[1, 'foo', 3.14]
>>> type([1,'foo', 3.14])
<class 'list'>
```

Similar to `str` list supports many useful sequence operations:

``` python
>>> [1,'foo', 3.14] # list of 3 elements
[1, 'foo', 3.14]
>>> [1,'foo', 3.14] + ['bar']
[1, 'foo', 3.14, 'bar']
>>> type([1,'foo', 3.14] + ['bar'])
<class 'list'>
>>> len([1, 'foo', 3.14]) # get length of a list
3
>>> l = [1,'foo', 3.14]
>>> l[0]
1
>>> l[-1]
3.14
>>> l[0:1]
[1]
>>> l[0:2]
[1, 'foo']
>>> l[1:]
['foo', 3.14]
>>> l.insert(2, 'bar')
>>> l
[1, 'foo', 'bar', 3.14]
>>> l.pop()
3.14
>>> l.index('foo')
1
>>> del l[0]
>>> l
['foo', 'bar']
>>> l[0] = 'bea'
>>> l
['bea', 'bar']
>>> 
```

### Tuples - `tuple`

Tuples pretty similar to lists. They can store unnamed objects of different
type but opposed to Python lists, they are unchangeable, i.e elements can't be
inserted, substituted or removed:

``` python
>>> (1, 'foo', 3.14)
(1, 'foo', 3.14)
>>> type((1, 'foo', 3.14))
<class 'tuple'>
```

Example tuple operations:

``` python
>>> len((1, 'foo', 3.14)) # length of a tuple
3
>>> l = (1, 'foo', 3.14)
>>> l[0]
1
>>> l[-1]
3.14
>>> l[0:2]
(1, 'foo')
>>> l + (42, )  # create a new extended tuple by concatenation
(1, 'foo', 3.14, 42)
>>> del l[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion
>>> l[0] = 'more'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment
>>> 
```

### Dictionaries - `dict`

Dictionaries are a nearly ubiquituous data type in Python. Dictionaries are a
"mapping" data type storing key-value data:

``` python
>>> {'name': 'Paul', 'age': 26, 'profession': 'author'}
{'name': 'Paul', 'age': 26, 'profession': 'author'}
>>> type({'name': 'Paul', 'age': 26, 'profession': 'author'})
<class 'dict'>
>>>
```

Example `dict` operations:

``` python
>>> d = {'name': 'Paul', 'age': 26, 'profession': 'author'}
>>> d['name']
'Paul'
>>> d['age'] = 27
>>> list(d.items())
[('name', 'Paul'), ('age', 27), ('profession', 'author')]
>>> list(d.keys())
['name', 'age', 'profession']
>>> list(d.values())
['Paul', 27, 'author']
>>> del d['age']
>>> d
{'name': 'Paul', 'profession': 'author'}
>>> d.popitem()
('profession', 'author')
>>> d
{'name': 'Paul'}
>>> 

```

### Sets - `set`

The Python `set` is a datatype similar to a mathematical set. It's a collection
of unique objects, (potentially) of different types, and supports set
operations like `union`, `intersection` and others.

``` python
>>> {1, 2, 'foo'}
{1, 2, 'foo'}
>>> set([1, 2, 'foo'])  # create set from a list
{1, 2, 'foo'}
>>> set((1, 2,'foo'))  # create set from a tuple
{1, 2, 'foo'}
>>> type({1, 2, 'foo'})
<class 'set'>
>>> 
```

`set`-example

``` python
>>> set([1, 2, 'foo', 'foo'])  # set from a list with a duplicate element
{1, 2, 'foo'}
>>> set([1, 2,'foo']) & set([1, 2]) # intersection of 2 sets using '&'-operator
{1, 2}
>>>
>>> {1, 2, 3}.difference({1, 2})
{3}
>>> {1, 2, 3}.union({1, 2, 4})
{1, 2, 3, 4}
>>> {1, 2, 3}.intersection({1, 2, 4})
{1, 2}
>>> 
```

### None - `None`

The Python `None` type is referred to as the `Null`-Object. It has a builtin contstant named `None`

``` python
>>> None
>>> type(None)
<class 'NoneType'>
>>>
```

### Boolean `bool`

The Python `bool` type has a two builtin constants named `False` an `True`

``` python
>>> True
True
>>> type(True)
>>> <class 'bool'>
>>> 
```

## Input and Output

Programs serve a purpose, they follow the IPO-model: Input - Processing - Output

Programs consume information (input), do some work (based on that input) and produces information (output). 
On the input-side information can be 'raw data' or 'commands' (which tell the program what to do with the data).
On the output-side information can be 'computed data' or simple 'status information' describing the state of (individual) processing steps.

Programs can consume and produce information from and to different channels. One kind of these channels is referred to as 'standard-input'/'standard-output' enabling a user interactively to provide input to and retrieve output from a program.
In Python there are builtin-functions (`input()`, `print()`) performing that tasks.


**Input-Example**

``` python
>>> # just echo the input
>>> input('Please enter your name: ')
Please enter your name: Donald
'Donald'
>>>
```  
  or:

``` python
>>> # store the input
>>> name = input('Please enter your name: ')
Please enter your name: Donald
>>> 
```

**Output-Example**

``` python
>>> # print the stored input
>>> print('Hallo %s' % name)
Hallo Donald
>>> 
```
    
**Combined Input/Output Example**

``` python
>>> print('Hallo %s' % input('Please enter your name: '))
Please enter your name: Donald
Hallo Donald
>>>
```

## Control Flow

[Wikipedia](https://en.wikipedia.org/wiki/Control_flow) describes control flow as follows:

"In computer science, control flow (or flow of control) is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated. The emphasis on explicit control flow distinguishes an imperative programming language from a declarative programming language."

Python provides two kinds of 'explicit controls' affecting the order of execution:

1. Choices
2. Loops

### Choices

Choices are conditional-controls, affectiong the order of execution according to a boolean-condition.

#### if-statements

Python provides different variations of `if`-statements:

Simple `if` - example:

``` python
>>> a = 1
>>> if a == 1:
...     print('a is 1')
... 
a is 1
>>> 
```

`if-elif` - example:

``` python
>>> a = 2
>>> if a == 1:
...     print('a is 1')
... elif a == 2:
...     print('a is 2')
... 
a is 2
>>>
```

`if-elif-else` - example:

``` python
>>> a = 3
>>> if a == 1:
...     print('a is 1')
... elif a == 2:
...     print('a is 2')
... else:
...     print('a is neither 1 nor 2')
... 
a is neither 1 nor 2
>>>
```

### Loops

Loops are repetitive controls, affecting the number of iterations a code
block is executed.

### for-statement

The Python `for-statement` can be viewed as a representative of what Wikipedia calls a [count-controlled-loop](https://en.wikipedia.org/wiki/Control_flow#Count-controlled_loops). The number of repetitions in a `for`-loop is defined by the number elements of a (probably dynamically generated) sequence.

`for`-loop example:

``` python
>>> for elem in [1, 2, 3]:  # number of elements in the list defines the number of repetitions
...     print(elem)
... 
1
2
3
>>>
``` 

`for`-loops operate on *iterables*.

### while-statement

The Python `while-statement` can be viewed as a representative of what Wikipedia calls a [condition-controlled-loop](https://en.wikipedia.org/wiki/Control_flow#Condition-controlled_loops). In a `while`-loop a condition-variable is set before and changed within the `while`-loop. 

`while`-loop example

``` python
>>> a = 1
>>> while a < 4:
...     print(a)
...     a += 1   # change the condition-variable
... 
1
2
3
>>>
```


## Functions

Functions are **named code blocks** providing a dedicated task (procedure) or calculation (function). Functions *can* have input parameters and return values, i.e. result values returnd to the caller.

**function definition**
A function is defined using the `def`-statement

``` python
>>> # function definition
>>> def echo(text):   # (1) function header
...    # (2) function body
...    print(text)    # 1.st statement
...    return         # 2.nd statement
...
>>>
```

A function definition consist of a (1) function-header and a (2) function body.
The function header beginning with the `def` keyword followed by the function-name and a probably empty list of comma-separated input-parameters in parenthesis, followed by colons character `:`.
The function body consists of an indented code-block of statements. In an interactive session the interpreters secondary prompt `...` shows the indentation level.

**function call**
A function is called simply using it's function name followed by a list of comma-separated call-parameters in parenthesis:

``` python
>>> # function call
>>> echo("Hello World")
Hello World
>>>
```

Functions can be called repeatedly and therefore are a major building block of reusable-code in imperative programinmg languages.


## Classes and Instances

Python allows user-defined data-types called **classes**. Classes are type-definitions which include data - so called **attributes** - and **methods** - functions that define the type-specific behaviour. **Instances** are objects created from classes.

The following example demonstrates a simple `class`-definition, class-instantiations and common operations on class-instances like attribute-access and method-call using the `.`-dot operator

**class definition**

``` python
>>> class MyDog:
...     def __init__(self, name):    # class constructor
...         self.name = name         # instance-attribute
...     def bark(self):              # instance-method returning nothing
...         print("wuff")
...
>>>
```
    
**class instances**

``` python
>>> mydog = MyDog("Django")         # create class instance
>>> mydog.name                      # access instance-attribute using '.'-dot operator
'Django'
>>> mydog.bark()                    # call instance-method using '.'-dot operator
wuff
>>>
```

## Exceptions

Python uses exceptions to communicate invalid (or impossible) operations aka
runtime errors:

``` python
>>> 1 + "1"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Such exceptions can be caught and handled:

``` python
>>> try:
...     myfile = open('myfile.txt', 'r')
... except FileNotFoundError as exc:
...     print('caught', exc)
...     # ... (do some sensible handling of this situation here)
... 
caught [Errno 2] No such file or directory: 'myfile.txt'
>>> 
```

## Modules & Packages

You can modularize your code using modules (files) and packages (directories
of module files):

``` python
--8<--
src/mymodule.py
--8<--
```

Now you can **reuse** this functionality:

``` python
>>> import mymodule
>>> mymodule.myfunc("I just called")
I just called
42
>>> 
```

## Generators

A callable that doesn't return a single value but generates - possibly
unlimited - values is called a generator. Generators *yield* values instead
of returning values:

``` python
>>> def gen(limit=-1):
...     if limit < 0:
...         val = 0
...         while True:
...             yield val
...             val += 1
...     else:
...         for val in range(limit):
...             yield val
... 
>>> [i for i in gen(5)]
[0, 1, 2, 3, 4]
```
