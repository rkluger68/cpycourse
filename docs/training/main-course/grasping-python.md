# Important for grasping Python

## Syntax

### Indentation

### Comments

### Docstrings

### Valid Identifiers & Reserved words

### Literals

### Source code encoding

## Names and Objects

Python variables are names for objects. An object can have many names:

``` python
>>> x = 1
>>> y = x
>>> x
1
>>> y
1
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
```

But it is still the same object:

``` python
>>> x is y  # is checks for object identity
True
>>> l1 is l2
True
>>> id(x), id(y)  # id() returns an object's unique id
(140700697906560, 140700697906560)
>>> id(l1), id(l2)
(140700698907784, 140700698907784)
```

Compare that to the meaning of variables in other languages, e.g. C.

In C (or C++) a variable is basically the in-program name for a "memory cell"
(a memory location that can hold a value of the type declared for that variable
). Thus, assignment in C/C++ means writing a value of the proper type into that
"memory cell".

Whereas a variable in Python is rather one "label" (of potentially many) for an
object in a sense more analogous to a C++ reference or a C pointer: a name for
an object.

Consequently, assignment in Python means "pinning" a new name to an object; it 
*never* copies data.[^c-assignment]

[^c-assignment]: Whereas in C/C++ assignment usually copies data.

Deleting a name doesn't affect object existence:
``` python
>>> del x
>>> y
1
```
(as long as there is still a name *referencing* that object)

Further reading: A great in-depth explanation can be found
[here](https://nedbatchelder.com/text/names1.html).


