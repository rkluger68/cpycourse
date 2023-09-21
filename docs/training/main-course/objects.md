# Python Objects: Understanding (the basics of) the Python Object Model

## Everything is an Object

In Python everything is an object:

Functions are objects, classes are objects, instances are objects, types are
objects, modules are objects, you name it: everything's an object.


The type of an object can be identified using the built-in `type()` function:

``` python
>>> type("I'm curious about her")
<class 'str'>
>>> number = 42
>>> type(number)
<class 'int'>
>>> 
```

Even code is an object:

``` python
>>> source = "lambda: 'Hello!'"
>>> code = compile(source, '', 'eval')
>>> type(code)
<class 'code'>
>>> isinstance(code, object)
True
>>> f = eval(code)
>>> f()
'Hello!'
>>>
```


An object is an entity encompassing the "data" and its acceptable operations.
The Python data model documentation
(<https://docs.python.org/dev/reference/datamodel.html>) describes:

"Every object has an ***identity***, a ***type*** and a ***value***. An
object’s identity never changes once it has been created; you may think of it
as the object’s address in memory. The ‘is’ operator compares the identity of
two objects; the id() function returns an integer representing its identity."

Often, Python objects are created and *named* immediately with an assignment.
Assigments introduce a *name* to refer to the object but don't create the
object:[^float-identity]

``` python
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
```

[^float-identity]:
    Note though that `a = 1.2; b = 1.2; a is b` would actually yield `True`!
    This is due to identical float constants on the same line being stored as 
    one float constant, thus labeling the single float object with the names
    `a` and `b`
    (try `compile('a = 1.2; b = 1.2; a is b', '', 'exec').co_consts`).

But note that an object *needn't have* a name:

``` python
>>> l = [1, 2.0, lambda x: x]
```

In this example while the `list` does have a name ("l") none of its items has
one: Neither the 1st integer item nor the 2nd float item nor the 3rd anonymous
function item.

Python objects can be created e.g. by

 - instantiating built-in types
 - instantiating user-defined types (classes)
 - defining classes
 - defining functions
 - defining anonymous functions

You can create an instance of the most basic type `object` like this:

``` python
>>> object()
<object object at 0x7f33e1b9b0d0>
```

### Objects are First-Class
This means that all (named) objects are equal in the sense that they can be
treated equally: a function object can be an argument to another function,
a module object can be a list item, a class can be a dictionary value (or even
a dictionary key), ...

This allows for writing powerful constructs:
``` python
>> data = [42, 5.0, "   some examples are more intelligent than others  "]
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

1. The *identity* of an object never changes after creation (see above).
2. The *type* of an object never changes after creation.
3. The *type* of the object defines the allowed values and the acceptable
operations.
4. An objects is **mutable** if its *value* can be changed, **immutable**
otherwise.

### Object Attribute Access

You can access an object's attributes with the '.'-operator:

``` python
>>> text = "I'm a string!"
>>> # Object attribute access - in this case, access a method attribute.
>>> text.upper
<built-in method upper of str object at 0x7f141886e730>
>>> # Objects have an internal __class__ attribute.
>>> text.__class__
<class 'str'>
>>> # A class object has an internal __name__ attribute.
>>> text.__class__.__name__
'str'
>>> 
```

You can "query" an object if it has a certain attribute using `hasattr(obj,
"attribute name")`, at runtime:

``` python
>>> text = "I'm also string!"
>>> hasattr(text, 'upper')
True
>>> hasattr(text, '__class__')
True
>>> hasattr(text.__class__, '__name__')
True
>>> hasattr(text, 'something_else')
False
```

In the same vein, you can dynamically access object attributes at runtime with
the `getattr` built-in function:

``` python
>>> getattr(text, 'upper')
<built-in method upper of str object at 0x7f1416b0cb20>
>>> getattr(text, '__class__')
<class 'str'>
>>> getattr(text, 'something_else')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'something_else'
>>> getattr(text, 'something_else', "default value")
'default value'
>>> 
```

This is *very* powerful.

## Immutable and Mutable Objects

The mutability/immutability of objects is determined by their types:

 1. immutable types: `str`, `int`, `float`, `complex`, `tuple`, `frozenset`
 2. mutable types: `list`, `dict`, `set`, user-defined objects (classes)

### Examples: immutable types

Immutable type `int`:

``` python
>>> a = 1
>>> id(a)
140026581642624
>>> a = 2       # assign name 'a' to a new object
>>> id(a)
140026581642656
>>> a += 1
>>> a
3
>>> # a is now a name for another new object: immutable object 2 hasn't
>>> # changed in-place
>>> id(a)
140357021310400
```

Immutable type `float`:

``` python
>>> f1 = 1.2 
>>> f2 = 1.2
>>> f3 = f1     # (1) f3 is another name for the object named f1
>>> id(f1)
140026583519544
>>> id(f2)
140026583519592
>>> id(f3)
140026583519544
>>> f1 = 1.3    # (2) the name f1 is now given to another object
>>> f1
1.3
>>> f2
1.2
>>> f3          # (3) f3 is unaffected: it is still a name for the original object (1)
1.2
>>> id(f1)
140026583519352
>>> id(f2)
140026583519592
>>> id(f3)
140026583519544
>>> 
```

### Examples: mutable types

Mutable type `list`:

``` python
>>> l1 = [1, 2, 3]
>>> l2 = l1      # (1) l2 is another name for the object named l1
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
>>> l1 =  [1, 2, 3]
>>> l2 = l1
>>> l1 += [4]  # extend mutable object
>>> l1
[1, 2, 3, 4]
>>> l2
[1, 2, 3, 4]
>>> l1 is l2
True
>>> 
```

Mutable type `dict`:

``` python
>>> d1 = {1: 'one', 2: 'two'}
>>> d2 = d1
>>> d2[1] = 'three'  # create some confusion
>>> d2
{1: 'three', 2: 'two'}
>>> d1
{1: 'three', 2: 'two'}
>>> 
```

## Object Lifetime and Object Reference

Every object that is created must be destroyed when it is no longer needed,
otherwise we run out of memory eventually. In Python objects aren't explicitly
destroyed but may be garbage-collected by the interpreter when they become
unreachable, i.e. they aren't referenced any more (by name or by other objects).

CPython implementation detail: CPython uses *reference counting*. Every object
carries the "in-use" information in a "reference count" which records the
number of references to this object. Remember, a variable is a name referencing
an object. An assignment of a name to an object establishes this reference -
during this step the reference count of the object is increased.

Conversely the object's reference count is decreased when the variable is
deleted (explicit using `del` or implicit by running out of scope) or
re-assigned to another object.

If the reference count of an objects is `0` the object is automatically
destroyed by the garbage collector of the Python interpreter (not necessarily
immediately, so don't rely on it!).

You can watch these mechanisms using the `getrefcount()`-function of the Python
standard library module `sys`:

``` python
>>> import sys
>>> l1 = ['cpython', 'does', 'refcounting']  # create named new list
>>> sys.getrefcount(l1)
2
>>> id(l1)
39141600
>>> l2 = l1             # new name for existing object
>>> id(l2)              # yes, it's the same object indeed
39141600
>>> sys.getrefcount(l1) # ==> refcount increased
3
>>> sys.getrefcount(l2)
3
>>> l3 = l1  # yet another new name for (=reference to) existing object
>>> sys.getrefcount(l1)
4
>>> del l3               # delete name l3
>>> sys.getrefcount(l1)  # ==> refcount of list object decreased
3
>>> l2 = object()        # assign name l2 to another object
>>> sys.getrefcount(l1)  # ==> refcount of list object decreased
2
>>> 
```

**Remark:**
As you may have noted the reference count is higher than you might expect.
This is due to the fact that the `sys.getrefcount()`-function call also 
increases the object's reference count, as it needs to hold a reference to the 
object, too, while it is running.

## Introspection

Python objects are highly introspectable. That means that you can find out
pretty much anything about their properties and capabailities (names, types,
attributes, methods, annotations, ...) at runtime.

A method to list an object's attribute is the `dir()` built-in:

``` python
>>> dir(3)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__',
'__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__',
'__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__',
'__getnewargs__', '__gt__', '__hash__', '__index__', '__init__',
'__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__',
'__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__',
'__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__',
'__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__',
'__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__',
'__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
'__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__',
'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes',
'imag', 'numerator', 'real', 'to_bytes']
>>>
>>> class IntervalDefaults:
...     min_val = -10
...     max_val = 10
... 
>>> dir(IntervalDefaults)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__', 'max_val', 'min_val']
>>> 
```

Or you can peek into an object's `__dict__`, since Python objects' inner
workings are predominantly implemented with the help of dictionaries:

``` python
>>> IntervalDefaults.__dict__  # nowadays, a read-only dict on classes
mappingproxy({'__module__': '__main__', 'min_val': -10, 'max_val': 10,
'__dict__': <attribute '__dict__' of 'IntervalDefaults' objects>,
'__weakref__': <attribute '__weakref__' of 'IntervalDefaults' objects>,
'__doc__': None})
>>>
```

To check if an object is callable there's the `callable` built-in:

``` python
>>> def noop(): pass
... 
>>> callable(noop)
True
>>> 
```

The standard library [inspect](https://docs.python.org/3/library/inspect.html)
module offers extensive introspection support:

``` python
>>> def accelerate(car, target_speed, thrust=100):
...     ...
...
>>> import inspect
>>> inspect.signature(accelerate)
<Signature (car, target_speed, thrust=100)>
>>> inspect.signature(accelerate).parameters
mappingproxy(OrderedDict([('car', <Parameter "car">), ('target_speed',
<Parameter "target_speed">), ('thrust', <Parameter "thrust=100">)]))
>>> inspect.signature(accelerate).parameters['car'].default
<class 'inspect._empty'>
>>> 
```

--8<--
training/lessons/object-introspection/object-introspection.md
--8<--
