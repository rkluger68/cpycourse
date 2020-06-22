# Python decorators

Python decorators are used to add functionality to functions, methods or
classes. Some of the use cases are e.g.:
 
 - add logging/tracing around function calls
 - add locking for threaded code
 - register functions or classes 
 - add caching to callables

## Decorating functions

A very basic decorator to trace function entry and exit could look like this:
``` python
>>> def trace(func):
...     # create a wrapper function...
...     def _wrapper(*args, **kwargs):
...         # ...that prints entry to and exit from the wrapped function,
...         # with function name, arguments and result...
...         print('--> {func}(args={args}, kwargs={kwargs})'.format(
...             func=func.__name__, args=args, kwargs=kwargs))
...         result = func(*args, **kwargs)
...         print('<-- {func} -> {result}'.format(
...             func=func.__name__, result=result))
...     # ...and return the wrapper for use instead of the original function
...     return _wrapper
... 
```

We can now apply this decorator to a function:
``` python
>>> @trace
... def inc(x):
...     """Return x increased by 1."""
...     return x + 1
... 
>>>
```

Calling our decorated "traced" function:

``` python
>>> inc(6)
--> inc(args=(6,), kwargs={})
<-- inc -> 7
>>>
```

Note how we have instrumented the original function with tracing output, while
not modifying any of the original function code.

Since a (function) decorator is just a callable that takes a function as an
argument and returns an enhanced, wrapped version of that function, the 
`@`-decorator syntax is merely syntactial "sugar" for:
``` python
>>> def inc(x):
...     """Return x increased by 1."""
...     return x + 1
... 
>>> inc = trace(inc)
>>> inc(6)
--> inc(args=(6,), kwargs={})
<-- inc -> 7
>>> 
```

Let's take a look at how our decorated function behaves, now using
@decorator-syntax again:

``` python
>>> def trace(func):
...     # create a wrapper function...
...     def _wrapper(*args, **kwargs):
...         # ...that prints entry to and exit from the wrapped function,
...         # with function name, arguments and result...
...         print('--> {func}(args={args}, kwargs={kwargs})'.format(
...             func=func.__name__, args=args, kwargs=kwargs))
...         result = func(*args, **kwargs)
...         print('<-- {func} -> {result}'.format(
...             func=func.__name__, result=result))
...     # ...and return the wrapper for use instead of the original function
...     return _wrapper
... 
>>> @trace
... def inc(x):
...     """Return x increased by 1.
...     """
...     return 1
... 
>>> print(inc.__doc__)
None
>>> inspect.signature(inc)
<Signature (*args, **kwargs)>
>>>  

```

Hm, this doesn't look too good a citizen:
 - the original function documentation has been lost
 - there's no information about the original function argument signature

This is due to the fact that we see docstring and function signature of the
wrapper, not the wrapped function. Luckily, there's a convenient way for us to 
retain this information using the `functools` library:

``` python
>>> def trace(func):
...     # create a wrapper function...
...     @functools.wraps(func)
...     def _wrapper(*args, **kwargs):
...         # ...that prints entry to and exit from the wrapped function,
...         # with function name, arguments and result...
...         print('--> {func}(args={args}, kwargs={kwargs})'.format(
...             func=func.__name__, args=args, kwargs=kwargs))
...         result = func(*args, **kwargs)
...         print('<-- {func} -> {result}'.format(
...             func=func.__name__, result=result))
...     # ...and return the wrapper for use instead of the original function
...     return _wrapper
... 
>>> @trace
... def inc(x):
...     """Return x increased by 1.
...     """
...     return x + 1
... 
>>> print(inc.__doc__)
Return x increased by 1.

>>> inspect.signature(inc)
<Signature (x)>
>>>  
```

## Decorating methods

We can just as well decorate methods:

``` python
>>> class Increaser:
...     def __init__(self, increment=1):
...         self.increment = increment
...     @trace
...     def inc(self, x):
...         """Return x increased by increment init argument.
...         """
...         return x + self.increment
... 
>>> inc = Increaser(3)
>>> inc.inc(10)
--> inc(args=(<__main__.Increaser object at 0x7fc62185c320>, 10), kwargs={})
<-- inc -> 13
>>> 
>>> print(inc.inc.__doc__)
Return x increased by increment init argument.

>>> inspect.signature(inc.inc)
<Signature (x)>
>>> 
```

In fact, Python implements its notion of *class methods* and *static methods*
via the built-in [`@classmethod`](classes-instances.md#class-methods) and
[`@staticmethod`](classes-instances.md#static-methods) decorators.


## Decorating classes

Decorating classes is just as easy:

``` python
>>> class Registry:
...     _registered_classes = []
...     
...     @classmethod
...     def register(cls, register_cls):
...         cls._registered_classes.append(register_cls)
...     
...     @classmethod
...     def registered_classes(cls):
...         return cls._registered_classes
... 
>>> register = Registry.register
>>> registry = Registry()
>>> 
>>> @register
... class MyClass1:
...     pass
... 
>>> @register
... class MyClass2:
...     pass
... 
>>> registry.registered_classes()
[<class '__main__.MyClass1'>, <class '__main__.MyClass2'>]
>>> 
```

## Advanced Decorators
Decorators can also take arguments.

Let's modify the tracing functionality to allow for selective entry and/or exit
tracing:

``` python
>>> def traced(entry=True, exit=True):
...     # create tracing wrappers depending on the entry & exit args
...     if entry and exit:
...         def trace(func):
...             @functools.wraps(func)
...             def _wrapper(*args, **kwargs):
...                 print('--> {func}(args={args}, kwargs={kwargs})'.format(
...                     func=func.__name__, args=args, kwargs=kwargs))
...                 result = func(*args, **kwargs)
...                 print('<-- {func} -> {result}'.format(
...                    func=func.__name__, result=result))
...             return _wrapper
...     
...     elif entry:
...         def trace(func):
...             @functools.wraps(func)
...             def _wrapper(*args, **kwargs):
...                 print('--> {func}(args={args}, kwargs={kwargs})'.format(
...                     func=func.__name__, args=args, kwargs=kwargs))
...                 result = func(*args, **kwargs)
...             return _wrapper
...     
...     elif exit:
...         def trace(func):
...             @functools.wraps(func)
...             def _wrapper(*args, **kwargs):
...                 result = func(*args, **kwargs)
...                 print('<-- {func} -> {result}'.format(
...                    func=func.__name__, result=result))
...             return _wrapper
...     else:
...         trace = None
...     
...     # create the decorator that will add the selected tracing setup 
...     def decorate(cls):
...         if trace is not None:
...             for (name, method) in inspect.getmembers(cls):
...                 if not name.startswith('__'):
...                     wrapped = trace(method)
...                     setattr(cls, name, wrapped)
...         return cls
...     
...     return decorate
... 
>>> 
```


We'll try this out on a delicious fruit salad:

``` python
>>> class FruitSalad:
...         
...     def __init__(self):
...         self.fruits = {}
...     
...     def add(self, fruit, weight):
...         if fruit not in self.fruits:
...             self.fruits[fruit] = weight
...         else:
...             self.fruits[fruit] += weight
... 
>>> 
>>> fruit_salad = FruitSalad()
>>> fruit_salad.add('apple', '500')
>>> fruit_salad.add('orange', '800')
>>> 
```

Make a traced fruit salad:

``` python
>>> 
>>> @traced()
... class FruitSalad:
...         
...     def __init__(self):
...         self.fruits = {}
...     
...     def add(self, fruit, weight):
...         if fruit not in self.fruits:
...             self.fruits[fruit] = weight
...         else:
...             self.fruits[fruit] += weight
... 
>>> fruit_salad = FruitSalad()
>>> fruit_salad.add('apple', '500')
--> add(args=(<__main__.FruitSalad object at 0x7fc61868cda0>, 'apple', '500'),
kwargs={})
<-- add -> None
>>> fruit_salad.add('orange', '800')
--> add(args=(<__main__.FruitSalad object at 0x7fc61868cda0>, 'orange', '800'),
kwargs={})
<-- add -> None
>>> 
```

This might look a little bit confusing initially. The important point is to
realize that the callable `traced` we use in the `@traced()` decoration line is
now rather a "decorator factory" than a decorator: it *creates* a decorator 
(the `decorate` function), and returns this to be applied on the decorated
class.

We can now switch off tracing method entry and only trace funtion exit:

``` python
>>> 
>>> @traced(entry=False)
... class FruitSalad:
...         
...     def __init__(self):
...         self.fruits = {}
...     
...     def add(self, fruit, weight):
...         if fruit not in self.fruits:
...             self.fruits[fruit] = weight
...         else:
...             self.fruits[fruit] += weight
... 
>>> fruit_salad = FruitSalad()
>>> fruit_salad.add('apple', '500')
<-- add -> None
>>> fruit_salad.add('orange', '800')
<-- add -> None
>>> 
```

**Note**: Maybe that's just cosmetics but it's a little annoying that we need
to use `@traced()` syntax even if we simple use the default arguments.

Let's make use of Python's [keyword-only] syntax to work around this:

``` python
>>> def traced(cls=None, *, entry=True, exit=True):
...     if entry and exit:
...         def trace(func):
...             @functools.wraps(func)
...             def _wrapper(*args, **kwargs):
...                 print('--> {func}(args={args}, kwargs={kwargs})'.format(
...                     func=func.__name__, args=args, kwargs=kwargs))
...                 result = func(*args, **kwargs)
...                 print('<-- {func} -> {result}'.format(
...                    func=func.__name__, result=result))
...             return _wrapper
...     
...     elif entry:
...         def trace(func):
...             @functools.wraps(func)
...             def _wrapper(*args, **kwargs):
...                 print('--> {func}(args={args}, kwargs={kwargs})'.format(
...                     func=func.__name__, args=args, kwargs=kwargs))
...                 result = func(*args, **kwargs)
...             return _wrapper
...     
...     elif exit:
...         def trace(func):
...             @functools.wraps(func)
...             def _wrapper(*args, **kwargs):
...                 result = func(*args, **kwargs)
...                 print('<-- {func} -> {result}'.format(
...                    func=func.__name__, result=result))
...             return _wrapper
...     else:
...         trace = None
...     
...     def decorate(cls):
...         if trace is not None:
...             for (name, method) in inspect.getmembers(cls):
...                 if not name.startswith('__'):
...                     wrapped = trace(method)
...                     setattr(cls, name, wrapped)
...         return cls
...     
...     
...     if cls is None:
...         # called with arguments
...         return decorate
...     else:
...         # invoked without arguments
...         return decorate(cls)
...
>>>
```

We are now able to omit () from the decoration line:

``` python
>>> @traced
... class FruitSalad:
...         
...     def __init__(self):
...         self.fruits = {}
...     
...     def add(self, fruit, weight):
...         if fruit not in self.fruits:
...             self.fruits[fruit] = weight
...         else:
...             self.fruits[fruit] += weight
... 
>>> fruit_salad = FruitSalad()
>>> fruit_salad.add('apple', '500')
--> add(args=(<__main__.FruitSalad object at 0x7fc61868cda0>, 'apple', '500'),
kwargs={})
<-- add -> None
>>> fruit_salad.add('orange', '800')
--> add(args=(<__main__.FruitSalad object at 0x7fc61868cda0>, 'orange', '800'),
kwargs={})
<-- add -> None
>>> 
```

## Further Reading

One of the most exhaustive discussions of decorator intricacies is
[a series of blog posts by Graham Dumpleton](https://github.com/GrahamDumpleton/wrapt/tree/develop/blog), who also wrote the
[wrapt library](https://github.com/GrahamDumpleton/wrapt) for decoration
purposes.
