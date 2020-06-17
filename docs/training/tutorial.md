# CPC: Tutorial

This tutorial refers to Python Version 3.

## Python Documentation ##

The Python official documentation can be found here <https://docs.python.org/3/index.html>

## Starting the Python interpreter

For an ***interactive session*** simply type `python` or `python3` in a console/shell of your computer (`$` - shell-prompt)

    $ python
    Python 3.6.5 (default, Jun 28 2018, 16:00:48) 
    [GCC 4.8.5] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

The first lines shows the interpreter-version, some information about the build-environment of the interpreter (compiler version and platform) and the copyright information.

The Python prompt `>>>` is signaling that the interpreter awaits user input.

The version and copyright information on startup can be suppressed using the quiet-option `-q`

    $ python -q
    >>>

***Note*** 
From now on this tutorial uses the `python -q` for interactive sessions, avoid inflating the output and focussing on the relevant code and output.

Type in your 1.st Python statement. After pressing the \<enter\>-key the interpreter will execute the statement, and in this
case will show the result.

    >>> print ("Hello World")
    Hello World
    >>>

After finishing the execution of the statement, the interpreter comes back to the prompt, awaiting the next input.

The interactive session can be stopped pressing \<Ctrl\>-D (Linux) or \<Ctrl\>-Z (Windows).

A ***summary*** of the Python interpreter's ***commandline options*** can be listed with it's help-option `-h`. This will display the ***usage***, the available commandline options and ***environment variables*** controlling the interpreter:

    $ python -h
    usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
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
    -u     : force the stdout and stderr streams to be unbuffered;
             this option has no effect on stdin; also PYTHONUNBUFFERED=x
    -v     : verbose (trace import statements); also PYTHONVERBOSE=x
             can be supplied multiple times to increase verbosity
    -V     : print the Python version number and exit (also --version)
             when given twice, print more information about the build
    -W arg : warning control; arg is action:message:category:module:lineno
             also PYTHONWARNINGS=arg
    -x     : skip first line of source, allowing use of non-Unix forms of #!cmd
    -X opt : set implementation-specific option. The following options are available:

         -X faulthandler: enable faulthandler
         -X showrefcount: output the total reference count and number of used
             memory blocks when the program finishes or after each statement in the
             interactive interpreter. This only works on debug builds
         -X tracemalloc: start tracing Python memory allocations using the
             tracemalloc module. By default, only the most recent frame is stored in a
             traceback of a trace. Use -X tracemalloc=NFRAME to start tracing with a
             traceback limit of NFRAME frames
         -X showalloccount: output the total count of allocated objects for each
             type when the program finishes. This only works when Python was built with
             COUNT_ALLOCS defined
         -X importtime: show how long each import takes. It shows module name,
             cumulative time (including nested imports) and self time (excluding
             nested imports). Note that its output may be broken in multi-threaded
             application. Typical usage is python3 -X importtime -c 'import asyncio'
         -X dev: enable CPythonâ?Ts â?odevelopment modeâ??, introducing additional runtime
             checks which are too expensive to be enabled by default. Effect of the
             developer mode:
                * Add default warning filter, as -W default
                * Install debug hooks on memory allocators: see the PyMem_SetupDebugHooks() C function
                * Enable the faulthandler module to dump the Python traceback on a crash
                * Enable asyncio debug mode
                * Set the dev_mode attribute of sys.flags to True
                * io.IOBase destructor logs close() exceptions
         -X utf8: enable UTF-8 mode for operating system interfaces, overriding the default
             locale-aware mode. -X utf8=0 explicitly disables UTF-8 mode (even when it would
             otherwise activate automatically)
         -X pycache_prefix=PATH: enable writing .pyc files to a parallel tree rooted at the
             given directory instead of to the code tree

    --check-hash-based-pycs always|default|never:
        control how Python invalidates hash-based .pyc files
    file   : program read from script file
    -      : program read from stdin (default; interactive mode if a tty)
    arg ...: arguments passed to program in sys.argv[1:]

    Other environment variables:
    PYTHONSTARTUP: file executed on interactive startup (no default)
    PYTHONPATH   : ';'-separated list of directories prefixed to the
               default module search path.  The result is sys.path.
    PYTHONHOME   : alternate <prefix> directory (or <prefix>;<exec_prefix>).
               The default module search path uses <prefix>\python{major}{minor}.
    PYTHONCASEOK : ignore case in 'import' statements (Windows).
    PYTHONUTF8: if set to 1, enable the UTF-8 mode.
    PYTHONIOENCODING: Encoding[:errors] used for stdin/stdout/stderr.
    PYTHONFAULTHANDLER: dump the Python traceback on fatal errors.
    PYTHONHASHSEED: if this variable is set to 'random', a random value is used
       to seed the hashes of str and bytes objects.  It can also be set to an
       integer in the range [0,4294967295] to get hash values with a
       predictable seed.
    PYTHONMALLOC: set the Python memory allocators and/or install debug hooks
       on Python memory allocators. Use PYTHONMALLOC=debug to install debug
       hooks.
    PYTHONCOERCECLOCALE: if this variable is set to 0, it disables the locale
       coercion behavior. Use PYTHONCOERCECLOCALE=warn to request display of
       locale coercion and locale compatibility warnings on stderr.
    PYTHONBREAKPOINT: if this variable is set to 0, it disables the default
       debugger. It can be set to the callable of your debugger of choice.
    PYTHONDEVMODE: enable the development mode.
    PYTHONPYCACHEPREFIX: root directory for bytecode cache (pyc) files.




## Running a Python program

A programm is built-up of a **sequence of python-statements** (i.e. the "programm code" or in short "code"). This code can be provideed explicit as a command-string on commandline as shown here, where the individual statements are separated by semicolons ';' :

    $ python -c "print('Hello'); print('World')"
    Hello
    World
    $

This is sufficient for simple, short ad-hoc checks.

But typically the code is placed into Python source files named \<module-name\>.py (in our case helloworld.py),
  and the code can be executed running the following command:

    $ python helloworld.py
    Hello
    World
    $
 
## Python program building blocks

As mentioned above a program is build as a sequence of statements. This is very rough and needs to be breakdown to more basic building blocks of the programming language. A brief (incomplete) top-down view of a program is build up:

Program
1. Comments
2. Statements
3. Expressions
4. Operands and Operators

which means:
  - a program is a sequence of comments and statements
  - a statement is either an 'executable instruction' (***do-something***) or an 'evaluable expression' (***compute-something***)
  - an expression is build up from operands and operators

### Program execution

Running a program therefore can be described as a top-down process of execution of statements and evaluation of expressions.

### Comments

Comments are used for inplace documenting the code. In Python the '#'-delimiter starts a comment.
A comment ends at the end of a line. The Python interpreters ignores comments.

    # This is a single line comment

### Statements

***Single statement***:
A single statement is an executable instruction ending with a newline or semicolon. A statement changes the state of the program.

Example 1 - expression statement

    $ python -q
    >>> 5+3 # expression-statement
    8
    >>> 

Example 2 - assignement statement

    $ python -q
    >>> a = 5+3 # assignement-statement
    >>> a       # expression-statement
    8
    >>> 
    
***Grouping statements***:
Consecutive statements can be grouped together forming a code-blocks using ___indentation___. The level of idention marks the code-block
a statement belongs.

Grouping statement - i.e. building code blocks - is the basis for structuring the program. Organized in "higher-level" building blocks like functions, classes, modules and packages, they provide reusable code fragments. 

A meaningful "programm organization" is crucial creating
  - understandable
  - maintainable
  - extendible
  - testable
code.

***Note***
Other programming languages use different delimiter-symbols expressing the end of single-statement and grouped statements.
E.g in Java or C the semicolon `;` is used as single-statement-delimiter, the curly braces `{` `}` are used for code-blocks.

### Expressions

An expression is sequence of ***operands*** and ***operators*** evaluating to a single value. Operands itself can be expressions.
Examples:

    "foo"        # string literal
    3.14         # float literal
    True         # boolean literal
    a            # simple identifier
    a + b        # simple expression using add-operator
    x == y       # simple expression using equal-comparison operator
    id(x)        # simple expression using 'id()'-builtin function getting the memory address the variable 'x' refers to
    a is b       # simple expression using 'is'-operator (check identity as with id()-builtin function)

The evaluation (calculation) of an expression itself is triggered by an appropriate statement - in an interactive interpreter session this means you need to finish your entered expression with a carriage return (newline), this will make an expression statement out of an expression.
Expressions are printable and assignable. Because expressions are assignable, they form the smallest unit of reusable code.

### Operands and Operators

Operands are literals, identifiers (variable names) or functions returning a single value. Operators are (meaningful) links between operands.

## Variables, assignments and expressions

Variables are one of the the key-elements of programing languages. Allthough the implementation may differ, the key-concept is equal:
Providing a named access to an area in memory holding data, which can be changed during program execution.

In Python a variable is a name referencing such a memory area. The variable is bound to the memory location upon an assignment(-statement). A Python ***variable is introduced*** by an assignment-statement, e.g.:

    >>> a = 5

Python-Variables are not tightly coupled to a memory location, they can be rebound to different memory locations by further assignments. At different point in time, the variable may refer to different locations in memory, storing different values and types of value. This makes Python a dynamic-typed language.

    $ python -q
    >>> a = 5 # create variable 'a' which is bound to a memory location, which stores an integer value 5
    >>> a     # named access to value in memory, the variable refers to
    5
    >>> id(a) # show the memory adress the variable 'a' points to
    139915719974400
    >>> type(a) # the value variable 'a' is of type 'int'
    <class 'int'>
    >>> a = 'foo' # rebound the variable to a different location in memory
    >>> a
    'foo'
    >>> id(a) #  show the memory adress the variable 'a' points to
    139915720973312
    >>> 
    >>> type(a) # the value variable 'a' now is of type 'str'
    <class 'str'>
    >>> 


## It's all about data: Python data structures

Python provides a bunch of popular data types. ***Simple types*** (also called primitive data-types) can best be imagined as data containers, which held values of a dedicated type. In addition Python provides some ***compound types***, which are collection of data containers of equal or different type, serving a dedicated purpose.

Each of the Python data types provide a data type specific set of `builtin-methods` and `operators` which can be applied on that kind of type.
For the complete list please refer to <https://docs.python.org/3/library/stdtypes.html>.

***Note 1***:
The type of a data-literal (or a variable referencing a data type holding that data-literal value) can be identified using the builtin `type()`-function. 

***Note 2***:
Python builtin data types itself are Python classes. Instances of nearly all Python builtin data-types can be gererated in two different ways:

1. implicit using a type-specific notation (literals) in the case of ***simple data-types*** or different kind of brackets `(`,  `)`, `[`, `]`, `{`, `} in the case of ***compound data-types*** 
2. explict using the types class-constructor (provided as Python `builtin`-function)

***Note 3***:
A type-test of a Python variable is done using buitlins `isinstance()` function

    python -q
    >>> isinstance('foo', str)
    True
    >>>

***Note 4***:
To keep things short we use simple expression-statements instead of assignment-statements in the following subsections, i.e

    python -q
    >>> 1 # expression-statement
    1
    
    python -q
    >>> a = 1 # assignment-statement
    >>> a     # expression-statement
    >>> 1


### Everything in Python is an object ###
===> Should this be placed in the main course material ???

### Strings - `str`

Strings are data containers storing character-sequences (string-literals). The character-sequence is embeded in a pair of quote.

`str`-types generation:

    $ python -q
    >>> 'foo'      # implicit: generate instance of 'str'- datatype using string-literal notation
    foo
    >>> str('foo') # explicit: using 'str'-class constructor
    
For nesting purposes, Python ***string-literals*** can be typed in different ways.

    $ python -q
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

    $ python -q
    >>> ''.join( ('foo', 'bar'))  # string concatenating using builtin method 'join()'
    'foobar'
    >>> 'foo' + 'bar'             # string concatenating using '+' operator
    'foobar'
    >>>
 

### Numeric datatypes - `int`, `float`

`int`-types generation:

    $ python -h
    >>> 1      # implicit: 'int'-literal
    1
    >>> int(1) # explicit: 'int'-class constructor
    >>>

Example `int`-literals and `int`-operation
    
    $ python -q
    >>> 1       # 'int'-literal
    1
    >>> type(1) # type of int-literal
    <class 'int'>
    >>> 1+2 # builtin'+'-operator for int-literal
    3
    >>> type(1+2) # result type
    <class 'int'>
    >>>

`float`- types generation:

    $ python -h
    >>> 1.2        # implicit: 'float'-literal
    1.2
    >>> float(1.2) # explicit: 'float'-class constructor
    

Example `float`-literals and `float`-operation

    $ python -q
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

`list`- types generation

    $ python -h
    >>> [1, 'foo', 3.14]       # implicti: list brackets '[' ']'
    [1, 'foo', 3.14]
    >>> list([1, 'foo', 3.14]) # explicit: 'list'-class constructor

`list`- example

    $ python -q
    >>> [[1,'foo', 3.14] # list of 3 elements
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

    $ python -q
    >>> [1,'foo', 3.14][0]   # access 1.st element of a list (index:0)
    1
    >>> len([1,'foo', 3.14]) # get length of a list
    3
    >>>


***NOTE***
The Python standard library also provides a `array`-type where the elements are restricted to be of th same type, see
(https://docs.python.org/3/library/array.html)

### Tuples - `tuple`

Tuples are very similar to lists. They can store elements of differen type, nearly have the same operations - but opposed to Python lists, they are unchangeable, i.e elements can't be added or removed.

`tuple`- types generation

    $ python -h
    >>> (1, 'foo', 3.14)        # implictit: using 'tuple'-brackets '(' ')'
    (1, 'foo', 3.14)
    >>> tuple((1, 'foo', 3.14)) # explicit:  'tuple'-class constructor (1) using 'tuple'-brackets '(' ')'
    (1, 'foo', 3.14)
    >>>
    >>> tuple([1, 'foo', 3.14)] # explicit:  'tuple'-class constructor (2) using 'list'-brackets '[' ']'
    (1, 'foo', 3.14)

`tuple`-example

    $ python -q
    >>> (1, 'foo', 3.14)
    (1, 'foo', 3.14)
    >>> type((1, 'foo', 3.14))
    <class 'tuple'>
    >>> 


***tuple-indexing and length of a tuple***

    $ python -q
    >>> (1, 'foo', 3.14)[0] # tuple-indexing
    1
    >>> len((1, 'foo', 3.14)) # lenth of a tuple
    3
    >>>

***NOTE***

You can't change tuples, but you always can generate a new tuple out of an existing tuple an a new tuple-element

    $ python -q
    >>> (1, 'foo', 3.14) + ('bar',) # creating a new tuple out of 2 existing tuples
    (1, 'foo', 3.14, 'bar')
    >>>


### Dictionaries - `dict`
Python provides a mapping data type storing key-value pairs called dictionaries (`dict`). Typically used storing a collection of named-objects.

`dict`- types generation

    $ python -h
    >>> {'name': 'Paul', 'age': 26, 'profession': 'author'}       # implicit: using curly braces '{' '}'
    {'name': 'Paul', 'age': 26, 'profession': 'author'}
    >>> dict({'name': 'Paul', 'age': 26, 'profession': 'author})  # explicit: 'dict'-class constructor
    {'name': 'Paul', 'age': 26, 'profession': 'author}

`dict` example

    $ python -q
    >>> {'name': 'Paul', 'age': 26, 'profession': 'author'}
    {'name': 'Paul', 'age': 26, 'profession': 'author'}
    >>> type({'name': 'Paul', 'age': 26, 'profession': 'author'})
    <class 'dict'>
    >>> 

***dictionary-lookup***

Accessing individual elements of a dictionary `m` is done using the dictionary key-indexing-operator `m.[key]`

    $ python -q
    >>> {'name': 'Paul', 'age': 26, 'profession': 'author'}['name']
    'Paul'
    >>> 


### Sets - `set`

The Python `set` is a datatype according to the mathematical set theory it therefore is a collection of unique elements, probably of different types, and a set-operations like `union`, `intersection` and others.

As opposed to the other Python builtin data types, `set`- type generation can only be done explicitly

`set`- types generation

    $ python -q
    >>> set([1,2, 'foo']) # explicit: 'set'- class constructor (1) using '[' ']' brackets
    {1,2,'foo'}
    >>> set((1,2,'foo'))  # explicit: 'set'- class constructor (2) using '(' ')' brackets
    {1,2,'foo'}

`set`-example

    $ python -q
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

    $ python -q
    >>> None
    >>> type(None)
    <class 'NoneType'>
    >>>

### Boolean `bool`

The Python `bool` type has a two builtin constants named `False` an `True`

    $ python -q
    >>> type(True)
    <class 'bool'>
    >>> 

## Input and Output

## Flow Control

### Conditionals

### Iteration and Loops


## Functions

Functions are ***named code blocks*** providing a dedicated task (procedure) or calculation (function). Functions can have input parameters and return values, i.e. result values returnd to the caller.

***function definition***
A function is defined using the `def`-statement

    python -q
    >>> # function definition
    >>> def echo(text):   # (1) function header
    ...    # (2) function body
    ...    print(text)    # 1.st statement
    ...    return         # 2.nd statement
    ...
    >>>

A function definition consist of a (1) function-header and a (2) function body.
The function header beginning with the `def` keyword followed by the function-name and a probably empty list of comma-separated input-parameters in parenthesis, followed by colons character `:`.
The function body consists of an indented code-block of statements. In an interactive session the interpreters secondary prompt `...` shows the indentation level.

***function call***
A function is called simply using it's function name followed by a list of comma-separated call-parameters in parenthesis:

    >>> # function call
    >>> echo("Hello World")
    Hello World
    >>>

Functions can be called repeatedly and therefore are a major building block of reusable-code in imperative programinmg languages.


## Classes and Instances


## Generators


## Exceptions


## Modules & Packages


## Important for grasping Python

### Syntax

### Immutable and Mutable Tpes

### Names and Objects

### Everything is an Object
