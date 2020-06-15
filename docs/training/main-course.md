# A Curious Python Course

## Everything is an object ##

In Python everything is an object. An object is an entity encompassing the "data" and its acceptable operations. The Python data model <https://docs.python.org/dev/reference/datamodel.html> further describes:

"Every object has an ***identity***, a ***type*** and a ***value***. An object’s identity never changes once it has been created; you may think of it as the object’s address in memory. The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity."

Python objects can also be generated from user-defined objects ("classes"). Moreover Python doesn't restrict "data" to be simply data types, instead data can also be code, see the <https://docs.python.org/dev/reference/datamodel.html>


***More characteristics on objects***

1. the identity of an object never changes after creation (see above)
2. the type of an object never changes after creation
3. the type of the object defines the allowed values and the acceptable operations
4. the value of **immutable** object cannot change
5. the value of **mutable** objects can change
6. the mutability/immutability of object-values is defined by its type:
    - immutable types: `str`, `int`, `float`, `complex`, `tuple`, `frozenset`
    - mutable types: `list`, `dict`, `set`, user-defined objects (classes)


### Object Identity ###

    >>> # (1) create some objects
    >>> a = 1 # from builtin base-type 'int'
    >>> b = 1
    >>> c = 2
    >>> # (2) check object types
    >>> type(a)
    <class 'int'>
    >>> type(b)
    <class 'int'>
    >>> type(c)
    <class 'int'>
    >>> (3) check memory adress of objects using id()
    >>> id(a) 
    140480615689600
    >>> id(b)         # 'b' points to the same object than 'a'?
    140480615689600
    >>> id(c)
    140480615689632

Memory adress of variable 'a' and variable 'b' are identical, ie. they point to the same object in memory

    >>> (4) check object identity
    >>> a is b
    True
    >>> a is c
    False
    >>> 


### Object Lifetime and Object Reference ###

Every object which is created must be destroyed when it is no longer needed, otherwise we ran out-of-memory. In Python every objects carries the "still-in-use" information in a "reference count". This reference counter records the number of variables referencing this object. Remember, a variable is a name pointing to a memory location. An assignment(-expression) establishes a reference between the variable name and the memory location (i.e. the object) - during this step the reference count of the object is inreased. Conversely the object's reference count is decreased, when the variable is deleted (explicit using `del` or implicit by running out-of-scope) or re-assigned to another object.
If the reference count of an objects is `0` the object is automatically destroyed by the garbage collector of the Python interpreter.

This can be demonstared as follows using the `getrefcount()`-function of the Python standard library module `sys`

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


***Note***
Checking the reference count will always increase the count itself during the check, because the `sys.getrefcount()`-function-call will also establish a reference to the object 'a' is pointing to. 


### Immutable/mutable Objects ###

Test
