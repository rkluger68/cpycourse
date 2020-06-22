# Python?

The programming language - not the animal, not (quite) the
[Monty](https://docs.python.org/3/faq/general.html#why-is-it-called-python).
But these days it uses a cute little
["two snakes" logo](https://www.python.org/community/logos/), anyway.


## What is Python?
From the Python homepage (www.python.org):

["Python is an interpreted, interactive, object-oriented programming language."](https://docs.python.org/3/faq/general.html#what-is-python)

## A bit more in-depth information

### [Hello world](../src/helloworld.py) in Python
``` python
>>> print('Hello, World!')
Hello, World!
```

### Python is interpreted

An interpreter is a computer program that directly/immediately executes
programming language instructions. I.e. there's no such thing as an explicit
separate compilation (to
[machine code](https://en.wikipedia.org/wiki/Machine_code) step before program
instructions can be run.[^interpreter]

[^interpreter]:
    As often, the lines are blurred though. Interpreters often implicitly
    "compile" to some form of intermediate "bytecode" or use ["just-in-time
    compilation"](https://en.wikipedia.org/wiki/Just-in-time_compilation)
    to compile (parts of) the code, e.g. for performance reasons. 



### Python is interactive
Python has a so-called "**R**ead-**E**val-**P**rint-**L**oop"
([REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop)).
That means that you can start the Python interpreter, type Python commands at
its prompt and immediately see the results:

```python
Python 3.8.2 (default, Feb 26 2020, 02:56:10)
>>> 1 + 1
2
```

### Python is object-oriented
   
According to https://de.wikipedia.org/wiki/Objektorientierte_Programmierung: 

> Alan Kay, inventor of Smalltalk and the term „object oriented“, defined object-oriented in the context of Smalltalk as: 
> > "
> >  1. Everything is an object, 
> >  2. Objects communicate by sending and receiving messages (in terms of objects), 
> >  3. Objects have their own memory (in terms of objects), 
> >  4. Every object is an instance of a class (which must be an object), 
> >  5. The class holds the shared behavior for its instances (in the form of objects in a program list), 
> >  6. To eval a program list, control is passed to the first object and the remainder is treated as its message
> > "

### Python is also dynamic

The term "dynamic" isn't actually defined all too clearly. With regard to Python one could describe it with these capabilities:

 - you can evaluate source code (e.g. from text strings) at runtime
 - you can create new types or extend existing types (and use them) at runtime
 - you can inspect (or "introspect") objects at runtime, i.e. get information 
   about their type, data, operations and metadata
 - Python is dynamically typed, not statically typed
     - but strongly typed:

         ``` python
         >>> "3" + 5
         Traceback (most recent call last):
           File "<stdin>", line 1, in <module>
           TypeError: can only concatenate str (not "int") to str
         ```

The dynamic nature of Python makes it very flexible.[^python-dynamic]

[^python-dynamic]:
    But comes at a price: reasoning about Python code before runtime i.e. 
    execution is hard which makes it difficult to apply optimizations like
    just-in-time compilation or transpile to less dynamic languages.


### Python is multi-paradigm

Python supports multiple programming paradigms:

#### Imperative (+ procedural) programming in Python

Programs are lists of instructions for the computer for processing the
program's input (and alter program state) to achieve a program's goal;
reusable units are defined as procedures.

#### Object oriented programming
The program is modelled as objects that bundle data and possible operations
(methods) on that data (that alter object and program state).

#### Functional programming
Functions that take input and produce output are combined to solve a program's
goal. Ideally, such functions do not maintain internal state or manipulate
outer state; in pure(ly) functional languages (which Python is not!) the
language enforces this no-side-effects approach.


## Who invented it?
See [a brief history of Python](python-history.md).

## Do I need it?
See [why should I use Python](why-python.md).

## Where to get it

Python is Free/Libre Open Source Software (F(L)OSS) and can be obtained here: www.python.org

There is "Python the lanuage" and "Python the implementation:

Aside from the predominant reference implementation dubbed "CPython" several other implementations of Python the language exist, with varying degrees of version compatibility and adoption:
 * [PyPy](https://www.pypy.org/)
 * [Jython](https://www.jython.org/)
 * [IronPython](https://ironpython.net/)
 * ...and probably others

Furthermore, several Python distributions bundle Python, Python packages,
external dependencies and additional tooling. A very prominent one is 
[Anaconda](https://www.anaconda.com/), with major adoption in the data science
world.


