# CPC: Tutorial

## Python Documentation ##

The Python official documentation can be found here (https://docs.python.org/3/index.html)

## Starting the Python interpreter

For an interactive session simply type `python` in a console/shell of your computer

    $ python
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

The Python prompt `>>>` is signaling that the interpreter awaits user input.

Type in your 1.st Python statement. After pressing the \<enter\>-key the interpreter will execute the statement, and in this
case will show the result.

    >>> print ("Hello World")
    Hello World
    >>>

As can be seen, after finishing the execution of the statement, the interpreter comes back to the prompt, awaiting the next input.

The intercative session can be stopped pressing \<Ctrl\>-D (Linux) or \<Ctrl\>-Z (Windows).


## Running a Python program

A programm is built-up of a **sequence of python-statements** (i.e. the "programm code" or in short "code"). This code can be provideed explicit as a command-string on commandline as shown here, where the individual statements are separated by semicolons ';' :

    $ python3 -c "print('Hello'); print('World')"
    Hello
    World
    $

This is sufficient for simple, short ad-hoc checks.

But typically the code is placed into Python source files named \<module-name\>.py (in our case helloworld.py),
  and the code can be executed running the following command:

    $ python3 helloworld.py
    Hello
    World
    $
 
## Python program building blocks

As mentioned above a program is build as a sequence of statetements. This is very rough and needs to be breakdown to more basic building blocks of the programming language. A brief, incomplete overview

1. Comments
2. Expressions
3. Statements
4. Variables


### Comments

Comments are used for inplace documenting the code. In Python the '#'-delimiter starts a comment.
A comment ends at the end of a line.

    # This is a single line comment


### Expressions

An expression is sequence of operands and operators evaluating to a single value. Operands itself can be expressions.
Examples:

    "foo"        # string literal
    3.14         # float literal
    True         # boolean literal
    a + b        # simple expression usimng add-operator
    x == y       # simple expression using equal-comparison operator
    id(x)        # simple expression using 'id'-builtin function getting the memory address the variable 'x' refers to
    a is b       # simple expression using 'is'-operator

The evaluation (calculation) of an expression itself is triggered by an appropriate statement.
Expressions are printable and assignable.


### Statements

***Single statement***:
A single statement is an executable instruction ending with a newline or semicolon. A statement changes the state of the program.

Example 1 - expression statement

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 5+3
    8
    >>> 

Example 2 - assignement statement

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> a = 5+3 # assignement-statement
    >>> a       # expression-statement
    8
    >>> 
    

***Grouping statements***:
Consecutive statements can be grouped together forming a code-blocks using ___indentation___. The level of idention marks the code-block
a statement belongs.

Grouping statement - i.e. building code blocks - is the basis for structuring the program. Organized in "higher-level" building blocks like functions, classes, modules and packages, they provide reusable code fragments.

Other programming languages use different delimiter-symbols expressing the end of single-statement and grouped statements.
E.g in Java or C the semicolon `;` is used as single-statement-delimiter, the curly braces `{` `}` are used for code-blocks.



## Variables, assignments and expressions

Variables are one of the the key-elements of programing languages. Allthough the implementation may differ, the key-concept is equal:
Providing a named access to an area in memory holding data, which can be changed during program execution.

In Python a variable is a name referencing such a memory area. The variable is bound to the memory location upon an assignment(-statement).
Python-Variables are not tightly coupled to a memory location, the can be rebound to different memory locations by further assignments. At different point in time, the variable may refer to different locations in memory, storing different values and types of value. This makes Python a dynamic-typed language.

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    >>> a = 5 # create variable 'a' which is bound to a memory location, which stores an integer value 5
    >>> a     # named access to value in memory, the variable refers to
    5
    >>> id(a) # show the memory adress the variable 'a' points to
    139915719974400
    >>> type(a)
    <class 'int'>
    >>> a = 'foo' # rebound the variable to a different location in memory
    >>> a
    'foo'
    >>> id(a) #  show the memory adress the variable 'a' points to
    139915720973312
    >>> 
    >>> type(a)
    <class 'str'>
    >>> 


## It's all about data: Python data structures

Python provides a bunch of popular data types. ***simple types*** (also called primitive datatypes) can best be imagined as data containers, which held values of a dedicated type. In addition Python provides some ***compound types***, which are collection of data containers of equal or different type, serving a dedicated purpose.

Each of the Python data types provide a data type specific set of builtin-methods and operators which can be applied on that kind of type.
For the complete list please refer to (https://docs.python.org/3/library/stdtypes.html).

***Note 1***
The type of a data-literal (or a variable referencing a data type holding that data-literal value) can be identified using the builtin `type()`-function. 

***Note 2***
Python data types itself are Python classes

***Note 3***
A type-test of a Python variable is done using buitlins `isinstance()`method

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> isinstance('foo', str)
    True
    >>>

### Everything in Python is an object ###
===> Should this be placed in the main course material ???

### Strings - `str`

Strings are data containers storing character-sequences (string-literals). For nesting purposes, Python ***string-literals*** can be typed in different ways:

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.   
    >>> 'foo' # single quoted string
    'foo'
    >>> type('foo')
    <class 'str'>
    >>> "foo" # double quoted string
    'foo'
    >>> type("foo")
    <class 'str'>
    >>> '''foo''' # triple quoted string
    'foo'
    >>> type('''foo''')
    <class 'str'>
    >>> 'foo"bar"' # nested string
    'foo"bar"'
    >>> type('foo"bar"')
    <class 'str'>
    >>> 


Example `str` builtin method and operator

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> ''.join( ('foo', 'bar'))  # string concatenating using builtin method 'join()'
    'foobar'
    >>> 'foo' + 'bar'             # string concatenating using '+' operator
    'foobar'
    >>>
 

### Numeric datatypes - `int`, `float`

Example `int`-literals
    
    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 1 # int-literal
    1
    >>> type(1) # type of int-literal
    <class 'int'>
    >>> 1+2 # builtin'+'-operator for int-literal
    3
    >>> type(1+2) # result type
    <class 'int'>
    >>>

Example `float`-literals

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 1.2 # a float-literal
    1.2
    >>> type(1.2) # type of float-literal
    <class 'float'>
    >>> 1.2 + 3.7 # builtin '+'-operand
    4.9
    >>> type(1.2 + 3.7) # result type
    <class 'float'>
    >>>


### Lists - `list`

A Python list is an array of elements of probably different types. 

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> [1,'foo', 3.14] # list of 3 elements
    [1, 'foo', 3.14]
    >>> type([1,'foo', 3.14])
    <class 'list'>
    >>> [1,'foo', 3.14] + ['bar']
    [1, 'foo', 3.14, 'bar']
    >>> type([1,'foo', 3.14] + ['bar'])
    <class 'list'>
    >>>

***list-indexing and length of a list***

Accessing list-elements of a list `l`is done using the Python list-indexing operator `l[i]`. The start list-index is `0`

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> [1,'foo', 3.14][0] # acces 1.st element of a list (index:0)
    1
    >>> len([1,'foo', 3.14]) # get ength of a list
    3
    >>>


***NOTE***
The Python standard library also provides a `array`-type where the elements are restricted to be of th same type, see
(https://docs.python.org/3/library/array.html)

### Tuples - `tuple`

Tuples are very similar to lists. They can store elements of differen type, nearly have the same operations - but opposed to Python lists, they are unchangeable, i.e elements can't be added or removed:

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> (1, 'foo', 3.14)
    (1, 'foo', 3.14)
    >>> type((1, 'foo', 3.14))
    <class 'tuple'>
    >>> 


***tuple-indexing and length of a list***

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> (1, 'foo', 3.14)[0] # tuple-indexing
    1
    >>> len((1, 'foo', 3.14)) # lenth of a tuple
    3
    >>>

***NOTE***

You can't change tuples, but you alwas can generate a new tuple out of an existing tuple an a new tuple-element

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> (1, 'foo', 3.14) + ('bar',) # creating a new tuple out of 2 existing tuples
    (1, 'foo', 3.14, 'bar')
    >>>


### Dictionaries - `dict`
Python provides a mapping data type storing key-value pairs called dictionaries (`dict`).

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> {'name': 'Paul', 'age': 26, 'profession': 'Autho'}
    {'name': 'Paul', 'age': 26, 'profession': 'Author'}
    >>> type({'name': 'Paul', 'age': 26, 'profession': 'Author'})
    <class 'dict'>
    >>> 

***dictionary-lookup***

Accessing individual elements of a dictionary `m` is done using the dictionary key-indexing-operator `m.[key]`

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> {'name': 'Paul', 'age': 26, 'profession': 'Hacker'}['name']
    'Paul'
    >>> 


### Sets - `set`

The Python `set` is a datatype according to the mathematical set theory it therefore is a collection of unique elements, probably of different types and a set-operations like `union`, `intersection` and others

    
    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> set([1, 2,'foo'])   # simple set with uniqe elements
    {1, 2, 'foo'}
    >>> type(set([1, 2,'foo'])) # type of set
    <class 'set'>
    >>> set([1, 2,'foo', 'foo'])  # simple set with a non-uniqe element (getting dropped)
    {1, 2, 'foo'}
    >>> type(set([1, 2,'foo', 'foo']))
    <class 'set'>
    >>> set([1, 2,'foo']) & set([1,2]) # intersection of 2 sets
    {1, 2}
    >>> type(set([1, 2,'foo']) & set([1,2]))
    <class 'set'>
    >>> 

  

### None - `None`

The Python `None` type is referred to as the `Null`-Object. It has a builtin contstant named `None`

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> None
    >>> type(None)
    <class 'NoneType'>
    >>>


### Boolean `bool`

The Python `bool` type has a two builtin constants named `False` an `True`

    python3
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> type(True)
    <class 'bool'>
    >>> 

## Input and Output

## Flow Control

### Conditionals

### Iteration and Loops


## Functions


## Classes and Instances


## Generators


## Exceptions


## Modules & Packages


## Important for grasping Python

### Syntax

### Immutable and Mutable Tpes

### Names and Objects

### Everything is an Object
