# Python Objects: Understanding (the basics of) the Python Object Model

## Everything is an Object

In Python everything is an object:

Functions are objects, classes are objects, instances are objects, types are
objects, modules are objects, you name it: everything's an object. Even code
is an object.

An object is an entity encompassing the "data" and its acceptable operations.
The Python data model (<https://docs.python.org/dev/reference/datamodel.html>)
further describes:

"Every object has an ***identity***, a ***type*** and a ***value***. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity."

Often, Python objects are created and *named* immediately with an assignment. Assigments introduce a *name* to refer to the object but don't create the
object:[^float-identity]

    :::python
    >>> a = 1.2  # new name a for new float object
    >>> b = 1.2  # new name b for new float object
    >>> c = a    # new name c for existing float object
    >>> type(a)
    <class 'float'>
    >>> type(b)
    <class 'float'>
    >>> type(c)
    <class 'float'>
    >>> id(a)        # (1)
    140026583519544  # (2) different identity than (1) ==> different object
    >>> id(b)
    140026583519592
    >>> id(c)        # (3) same identity as (1) ==> same object
    140026583519544
    >>> a is b
    False
    >>> a is c
    True
    >>>

[^float-identity]:
    Note though that `a = 1.2; b = 1.2; a is b` would actually yield `True`!
    This is due to identical float constants on the same line being stored as 
    one float constant, thus labeling the single float object with the names
    `a` and `b`
    (try `compile('a = 1.2; b = 1.2; a is b', '', 'exec').co_consts`).

But note that an object *needn't have* a name:

    :::python
    >>> l = [1, 2.0, lambda x: x]

In this example while the `list` does have a name ("l") none of its items has
one: Neither the 1st integer item nor the 2nd float item nor the 3rd anonymous
function item.

Python objects can be created e.g. by

 - instantiating built-in types
 - instantiating user-defined types (classes)
 - defining classes
 - defining functions
 - defining anonymous functions
 
### Objects are First-Class
This means that all (named) objects are equal in the sense that they can be
treated equally: a function object can be an argument to another function,
a module object can be a list item, a class can be a dictionary value (or even
a dictionary key), ...

This allows for writing powerful constructs:
``` python
>> data = [42, 5.0, "some examples are more intelligent than others"]
>>> dispatcher = {                                
...     str: lambda x: x.strip(),  # we want strings stripped
...     int: lambda x: str(x**2),  # we want ints squared 
...     float: lambda x: str(-x)   # we want inverted floats
...     }
>>> print('|'.join(
...     dispatcher[type(d)](d) for d in data)
...     )
1764|-5.0|some examples are more intelligent than others
>>> 
```

### More characteristics of objects

1. the *identity* of an object never changes after creation (see above)
2. the *type* of an object never changes after creation
3. the *type* of the object defines the allowed values and the acceptable operations
4. an objects is **mutable** if its *value* can be changed, **immutable** otherwise


## Immutable/mutable Objects

The mutability/immutability of object-values is defined by its type:

 1. immutable types: `str`, `int`, `float`, `complex`, `tuple`, `frozenset`
 2. mutable types: `list`, `dict`, `set`, user-defined objects (classes)

Changing the value of variable pointing to an immutable type causes a copy of the original referenced/underlying Python object. This is sometimes called "copy-on-write".

Changing the value of a variable pointing to a mutable type just changes that value.



Example: immutable type `int`

    :::python
    >>> a = 1
    >>> id(a)    # 
    140026581642624
    >>> a = 2    # (1) Changing the value of 'a' causes the creation of a new
    >>> id(a)
    140026581642656
    >>> 

Example: immutable type `float`

    :::python
    >>> f1 = 1.2 
    >>> f2 = 1.2
    >>> f3 = f1     # (1) f3 is a reference to the same object f1 points to
    >>> id(f1)
    140026583519544
    >>> id(f2)
    140026583519592
    >>> id(f3)
    140026583519544
    >>> f1 = 1.3    # (2) change the value of f1 cause a copy-on-write
    >>> f1
    1.3
    >>> f2
    1.2
    >>> f3          # (3) f3 still points to origin objects of f1 (1), so the change (2) doesn't affect f3
    1.2
    >>> id(f1)
    140026583519352
    >>> id(f2)
    140026583519592
    >>> id(f3)
    140026583519544
    >>> 


Example mutable type `list`

    :::python
    >>> l1 = [1,2,3]
    >>> l2 = l1      # (1) l2 is a reference to the same object l1 points to
    >>> id(l1)
    140026582652168
    >>> id(l2)
    140026582652168
    >>> l1[0] = 9    # (2) change a value of of l1
    >>> l1
    [9, 2, 3]
    >>> l2           # (3) the change (2) also effects the value of l2
    [9, 2, 3]
    >>> id(l1)
    140026582652168
    >>> id(l2)
    140026582652168
    >>> 


## Object Lifetime and Object Reference

Every object which is created must be destroyed when it is no longer needed, otherwise we ran out-of-memory. In Python every objects carries the "still-in-use" information in a "reference count". This reference counter records the number of variables referencing this object. Remember, a variable is a name pointing to a memory location. An assignment(-expression) establishes a reference between the variable name and the memory location (i.e. the object) - during this step the reference count of the object is inreased. Conversely the object's reference count is decreased, when the variable is deleted (explicit using `del` or implicit by running out-of-scope) or re-assigned to another object.
If the reference count of an objects is `0` the object is automatically destroyed by the garbage collector of the Python interpreter.

This can be demonstared as follows using the `getrefcount()`-function of the Python standard library module `sys`

    :::python
    >>> import sys                     # import sys-module
    >>> a = 'foo'                      # (1) define a variable 'a' - a new object is created
    >>> sys.getrefcount(a)             # check reference-count of the object 'a' points to (*)
    2
    >>> id(a)                          # check memory adress
    140574134795264
    >>> b = a                          # (2) establish additional reference to the object
    >>> id(b)                          # check memory adress ==> ok it point to the same object
    140574134795264
    >>> sys.getrefcount(a)             # check reference count
    3
    >>> c = a                          # (3) establish additiona reference
    >>> id(c)                          # check memory adress
    140574134795264
    >>> sys.getrefcount(a)             # check reference count
    4
    >>> del c  # delete variable 'c'   # (4) remove reference by deleting the variable
    >>> sys.getrefcount(a)             # check reference count
    3
    >>> b = 1                          # (5) re-assign variable 'b'
    >>> id(b)                          # check memory adress
    140574133796224
    >>> sys.getrefcount(a)             # check reference count (*)
    2
    >>>


**Note:**
Checking the reference count will always increase the count itself during the check, because the `sys.getrefcount()`-function-call will also establish a reference to the object 'a' is pointing to. 
