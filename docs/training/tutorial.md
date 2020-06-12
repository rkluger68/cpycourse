# CPC: Tutorial

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

Other programming languages use different delimiter-symbols expressing the end of single-statement and grouped statements.
E.g in Java or C the semicolon `;` is used as single-statement-delimiter, the curly braces `{` `}` are used for code-blocks.

## Variables, assignments and expressions

Variables are one of the the key-elements of programing languages. Allthough the implementation may differ, the key-concept is equal:
Providing a named access to an area in memory holding data, which can be changed during program execution.

In Python a variable is a name referencing such a memory area. The variable is bound to the memory location upon an assignment(-statement).
Python-Variables are not tightly coupled to a memory location, the can be rebound to different memory locations by further assignments. At different point in time, the variable may refer to different locations in memory, storing different values and types of value. This makes Python a dynamic-typed language

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

### Strings

### Numeric datatypes

### Lists

### Tuples

### Dictionaries

### Sets

### None

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
