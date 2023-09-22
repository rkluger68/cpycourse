# Be classy: Python Classes and Instances

Classes are the Python building block creating user-defined types in an
object-oriented manner. Classes encapsulate data ('attributes') and appropriate
'methods' (a fancy name for functions operating on objects of a class). As
such, a class defines the properties and behaviour of an object whose type is
that class. An object of a class is called a 'class instance'.

Classes are 1st class objects themselves. They define state (as class attributes, e.g. the `__name__` attribute) and instances' behaviour (a set of methods).

Python classes don't really support 'access' modifiers (public, protected,
private) like some other programming languages do - all attributes are
basically public. Apart from some basic mechanism to protect certain private
attributes from being accessed accidentally, that is - which you can circumvent
easily if you're determined to.

In Python land the philosophy is one of "consenting adults": Whoever
violates the contracts by accessing things he better shouldn't will have to
suffer the potential consequences (of functional misbehaviour).

Let's start with a simple class.

## Simple Class

Classes typically have (optional) class & instance attributes and (optional)
methods.

1. Instance attributes:
 - each class instance has its own copy of its instance attributes
 - instance attributes are accessed with the `.`-dot operator: `<class
   instance>.<instance attribute>`
2. Class attributes:
 - Attributes defined on the class, not the instance. These are shared by all
   instances of a class.
3. Methods:
 - must be called through a class instance
 - methods are accessed using the `.`-dot operator: `<class
   instance>.<instance-method>(<parameters>)`
 - every instance method needs an explicit *1.st* parameter named `self`

The simplest class could look like this:

``` python
>>> class SomeClass:
...     pass
...
>>>
```

We *call* the class to construct an instance:

``` python
>>> SomeClass()
<__main__.SomeClass object at 0x7fd540925a60>
>>>
```

Calling a class invokes the class constructor(s) - which is actually
divided into the two special methods `__new__` and `__init__` in Python.
`__new__` is responsible for creating a new empty object instance of the target
class while `__init__` is supposed to initialize the instance with proper
initial state.

Find more information on the 2-step process of class instantiation in the
Python docs on the
[`__new__(...)`-method](https://docs.python.org/3/reference/datamodel.html?highlight=__init#object.__new__)
and
[`__init__(...)`-method](https://docs.python.org/3/reference/datamodel.html?highlight=__init#object.__init__).


For regular user-defined classes you'll usually only deal with `__init__`.

We can access attributes of an instance or a class:

```python
>>> some_instance = SomeClass()
>>> some_instance.__class__
<class '__main__.SomeClass'>
>>> SomeClass.__name__
'SomeClass'
>>>
```


Let's add a custom constructor (initializer, to be precise) and a method:

``` python
>>> class SomeClass:
...     def __init__(self, name):                     # constructor
...         self.name = name                          # instance attribute
...     def greet(self):
...         print(f'Hello, my name is {self.name}.')  # method
...
>>>
```

We can now construct an instance providing the necessary parameter and access
the object's attributes and methods:

``` python
>>> some_instance = SomeClass('Judi')
>>> some_instance.name     # attribute access
'Judi'
>>> some_instance.greet()  # method call
Hello, my name is Judi.
```

A class can optionally define a finalizer method called `__del__()`, to
explicitly perform finalization tasks like closing ressources opened by the
class instance.

`__del__` is called by the interpreter's reference counting or garbage
collection mechanism, when the reference count (see [Object Lifetime and Object
Reference](objects.md)) of the class instance reaches 0:

``` python
>>> class ExpensiveResource:
...     def disconnect(self):
...         print(f'{self} disconnected')
...
>>> class ResourceUser:
...     def __init__(self, resource):
...         self.resource = resource
...     def __del__(self):
...         try:
...             self.resource.disconnect()
...             self.resource = None
...         except:
...             pass
...
>>> resource_user = ResourceUser(ExpensiveResource())
>>> del resource_user  # decrease refcount
<__main__.ExpensiveResource object at 0x7fd540973be0> disconnected
>>>
```

**Notes**:

 - `del x` does *not* directly invoke `x.__del__()`. It only decreases its
   reference count by one!
 - It's not guaranteed that `__del__` is called for a still-existing object
   when Python exits.

Due to `__del__`'s characteristics it *can* make sense to provide for an
explicit method for shutting down a class instance and its ressources (like
e.g. `close()` or `stop()`).

For more details see
[__del__()](https://docs.python.org/3/reference/datamodel.html?highlight=__del#object.__del__).


## Notes on the `self`-Parameter

During a method call

    <class instance>.<method>(<param-1>, ... <param-n>)

the python interpreter effectively invokes (pseudocode)

    <class>.<unbound method>(<class instance>, <param-1>, ..., <param-n>)

Basically, it looks up the method name on the class (where it's simply a
function or "unbound method"), "binds" the instance to that function and then
calls the resulting bound method with the rest of the parameters.

This machinery is the reason why an explicit `self` parameter is needed for
every method definition: the `self` parameter retrieves the class instance. See
also [Instance methods](https://docs.python.org/3/reference/datamodel.html)
section of the Python docs.

The explicit `self`-parameter is similar to the implicit
`this`-pointer/reference of C++ and Java:

1. Python: explicit `self` 1.st parameter in every instance method
2. C++ `this`-pointer: Implicit parameter to all member functions. A keyword
   holding a pointer to the current object
3. Java `this`-reference: Implicit parameter of all member functions. A keyword
   holding a reference to the current object.

**Note:**
The name `self` is just a convention. Use it to keep the code understandable.


## Class Privacy - Private Attributes

Python doesen't provide 'access-modifiers' like e.g. C++ (`public`, `private`,
`protected`) to control access to attributes or methods. I.e.  attributes and
methods are 'public'.

Python relies upon sane usage of a class and 2 forms of data "hiding" (but no
real protection by access control):

1. 'private-by-convention': Attributes prefixed with a single underscore `_`
   should be regarded as a private attributes, not part of the 'public API' of
   clas
2. 'private-by-lexical-substitition': Attributes prefixed with double
   underscores `__` like e.g. `__foo` will be implicitly renamed to
   `_classname__foo` by the interpreter. This textual substitution is called
   'name mangling'.

In action:

``` python
>>> class Person:
...     def __init__(self, name, age, gender):
...         self.name = name           # public
...         self._age = age            # private-by-convention
...         self.__gender = name       # private-by-lexical-substitution
...     def __log_access(self, accessed):  # private-by-lexical-substitution
...         print(f'*** Access to sensitive data {accessed}')
...     def get_age(self):
...         return self._age
...     def get_gender(self):
...         self.__log_access('__gender')
...         return self.__gender
...
>>> person = Person('Kara', age=27, gender='w')
>>> person.name  # Access the public attribute.
'Kara'
>>> person._age  # Just as well access `_age` - private just by convention.
27
>>> person.__gender  # `__gender` is protected to some degree by name mangling.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute '__gender'
>>> person.get_gender()  # Luckily for us there's a public accessor method.
*** Access to sensitive data __gender
'Kara'
>>>
>>> person.__log_access('huhu')  # leading double underscore, also inaccessible
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Person' object has no attribute '__log_access'
>>>
```

The name mangling mechanism also applies to access from subclasses to a base
class double-underscore attribute:

``` python
>>> class Base:
...     def __init__(self):
...         self.__x = 1
...
>>> class Derived(Base):
...     def access_x(self):  # This won't work...
...         return self.__x
...
>>> derived = Derived()
<__main__.Derived object at 0x7fd541621790>
>>> derived.access_x()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in access_x
AttributeError: 'Derived' object has no attribute '_Derived__x'
>>> 
```

For more details please refer to [Private Variables](https://docs.python.org/3/tutorial/classes.html#private-variables)

## Relationships between Classes

Python supports 'inheritance' ("is-a"-relation) and 'composition' ("has-a"-relations) of classes/instances.

(Multiple) inheritance and the mechanism of 'method overriding' provide for
the usual notion of 'poymorphism' found in many object-oriented languages.

In addition, Python allows for the so-called **Duck-Typing**, kind of a
polymorphism not relying on being of a certain type but implementing certain
features (implementing a 'protocol').

### Inheritance ("is-a"-relation)

**Note on class privacy:**
As mentioned above, Python doesn't provide any strict mechanism for class
privacy, neither 'data protection' nor 'data hiding'. This also applies to
class inheritance. Inheritance is public by default, as a consequence all of
the base -class attributes and methods are inherited by a derived class.


**class definition**

``` python
>>> class B(A):                            # class 'B' inherhits from class 'A'
...     def __init__(self, name, number):  # class constructor
...         A.__init__(self, name)         # call base-class initialisation-method
...         self.number = number           # instance variable
...     def getNumber(self):               # instance methode
...         return self.number
...
>>>
```

***class instantiation***

``` python
>>> b = B('Inheritance', 100)
>>> b.name                                # attribute-access
'Inheritance'
>>> b.get_name()                           # method-access
'Inheritance'
>>> b.number                              # attribute-access
100
>>> b.getNumber()                         # attribute-access
100
>>>
```

## Multiple Inheritance

Python also supports multiple inheritance

***class definition***

``` python
>>> class A:
...     def __init__(self, name):
...         self.name = name
...     def get_name(self):
...         return self.name
...
>>>
>>> class Z:
...     def __init__(self, another_name):
...         self.another_name = another_name
...     def getAnotherName(self):
...         return self.another_name
...
>>>
>>> class B(A,Z):   # multiple inheritance
...     def __init__(self, name, another_name, number):
...         A.__init__(self, name)           # call base-class initialisation-method of class 'A'
...         Z.__init__(self, another_name)   # call base-class initialisation-method of class 'Z'
...         self.number = number
...     def getNumber(self):
...         return self.number
...
>>>
```

***class instantiation***

```python
>>> b = B('BaseClass_A', 'BaseClass_Z', 100)
>>> b.getNumber()
100
>>> b.get_name()
'BaseClass_A'
>>> b.getAnotherName()
'BaseClass_Z'
>>> dir(b)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'another_name', 'getAnotherName', 'get_name', 'getNumber', 'name', 'number']
>>>
```

***Note:***
The `dir(<object>`)- builtin function lists all names in the namespace of the given object. As can be seen above all defined names of all base-class are in the namespace of the derived class.

## Composition ("has-a"-relation)

Python also support composition, i.e. a class 'Car' has an instance attribute pointing to an instance attribute of class 'Engine'

### 'Owned-By' Composition

***class definitions***

```python
>>> class Engine:
...     def __init__(self, name):
...         self.name = name
...     def get_name(self):
...         return self.name
...
>>> class Car:
...     def __init__(self, name, engine_name):
...         # 'class Engine' instance is owned (it's created)
...         self.engine = Engine(engine_name)
...         self.name = name
...     def get_name(self):
...         return self.name
...
>>>
```

***class instantiation***

``` python
>>> car = Car('Porsche', 'V6-Engine')
>>> car.get_name()
'Porsche'
>>> car.engine.get_name()
'V6-Engine'
>>>
```

### 'Used-By' Composition

***class definitions***

``` python
>>> class Engine:
...     def __init__(self, name):
...         self.name = name
...     def get_name(self):
...         return self.name
...
>>> class Car:
...     def __init__(self, name, engine):
...         # 'class Engine' instance is used (it's injected)
...         self.engine = engine
...         self.name = name
...     def get_name(self):
...         return self.name
...
>>>
```

***class instantiation***

```python
>>> engine = Engine('V6-Engine')
>>> car = Car('Porsche', engine)
>>> engine.get_name()
'V6-Engine'
>>> car.get_name()
'Porsche'
>>> car.engine.get_name()
'V6-Engine'
>>>
```

## A note on 'Inheritance vs Composition'

Key principle of both concepts is code reusabilty:

- Inheritance: Base class methods are inherited by derived classes and can be extended or overwritten
- Composition: Combines existing classes to build more complex classes

Interest reading in [The Composition Over Inheritance Principle](https://python-patterns.guide/gang-of-four/composition-over-inheritance/) first described in the [Gang of Four Book](https://python-patterns.guide/gang-of-four/)

## Class Attributes

As opposed to 'instance'-attributes 'class'-attributes are common to all class instances.

***class definition***

``` python
>>> class A:
...     count = 0
...     def __init__(self, name):
...         self.name = name
...         A.count += 1
...
>>>
```

***class instantiation***

``` python
>>> a1 = A('A1')    # 1.st instance increments class-attribute
>>> a1.count
1
>>> a2 = A('A2')    # 2.nd instance increments class-attribute
>>> a2.count
2
>>> a1.count        # Note: both instances share the same attribute
2
>>>
>>> id(a1.count)
140201179340160
>>> id(a2.count)
140201179340160
>>>
```


## Class Properties

Ordinary Python instance attributes are by default 'readable', 'writable' and 'deletable'. Python class properties ('property-attributes') are attributes with 'access-control', i.e. they can be designed to be 'readable', 'writeable' and 'deletable'. Python properties therefore are managed attributes. This is done with special `getter`-, `setter`- and `deleter`- methods which enables the properties to be accessed as ordinary atttributes (instead of a method-call).

***Usecase:***
Properties are a way of data encapusulation. Hiding ordinary attributes behind a 'property-interface/facade' introduces a level of indirection to the origin attribute. The origin attribute may change behind the scenes in keeping the user interface with the property-facade. The property can be seen as the user-interface, while the origin attribute is an implementation detail which is a subject to change.

Python support two different ways of implementing properties:

1. 'lower-level' using `property()` builtin function
2. 'higher-level' using  `@propery`-decorator

The Python docs provide a good [property-example](https://docs.python.org/3/library/functions.html#property), with read-, write- and delete-access. For convenience this is simply copied here.

***example using `property()`-builtin function***

``` python
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
```

usage

``` python
>>> p1 = C()
>>> p1.x = 1       # (1) set property value
>>> p1.x           # (2) get property value
1
>>> del p1.x       # (3) delete property
>>> p1.x = 11      # (4) re-create property
>>> p1.x
11
```

***example using the `@propery`-builtin decorator***
``` python
class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
```

usage

``` python
>>> p1 = C()
>>> p1.x = 9       # (1) set property value
>>> p1.x           # (2) get property value
9
>>> del p1.x       # (3) delete property
>>> p1.x = 99      # (4) re-create property
>>> p1.x
99
>>>
```

***'readonly property example ***

The above example stripped-down to be read-only:

``` python
>>> class C:
...     def __init__(self, x):
...         self._x = x
...     @property
...     def x(self):
...         return self._x
...
>>>
```

usage

```python
>>> a = C('foo')
>>> a.x                                   # (1) read access
'foo'
>>> a.x = 'bar'                           # (2) write access
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>> del a.x                              # (3) delete access
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't delete attribute
>>>
```

***Note:***
Property 'x' is read-only, write- and delete-access fail.


## Duck Typing

Statically typed languages like C++ use virtual function for runtime polymorphism. Derived classes therefore override base-class functions retaining their signature. When base-class objects, which hold a derived class reference, call their base-class function, the runtime will virtual dispatch the derived-class function.
This allows programing on a abstract base-class level. But this is restricted to class-objects having an inheritance relationship.

Pythons polymorphism is based on 'duck typing', where the polymorphism is not based on common types, instead it is based on common behaviour (methods) and attributes of the objects itself. See Wikipedia article on [Duck typing](https://en.wikipedia.org/wiki/Duck_typing): "If it walks like a duck and it quacks like a duck, then it must be a duck"

This enable more architecural freedom on the program/class-design, because class-hierarchies can be breaked down and allow more loosely coupled program-design, as David M. Beazley writes in his Book "Python Essential Reference (Fourth Edition)".


## Special Methods

### class methods

As opposed to instance-methods, class-methods operate on the class-object.

***Usecase:***
Python doesn't support method overloading like C++ or Java. Therefore multiple methods with the same name within a single class is not supported. As a consequence only a single class constructor (`__init__()`-method) can be defined. With 'class-method's it's possible to overcome this.

Python 'classc-methods' are defined using the `@sclassmethod`-decorator preceeding to the method-definition

*`@classmethod`-example*

``` python
>>> class ByteStringStore:
...     encoding = 'utf-8'
...     def __init__(self, bytestring):
...         self.bytestring = bytestring
...     @classmethod
...     def from_unicode(cls, unicodestring):
...         return cls(unicodestring.encode(cls.encoding)
...
... )
...
>>> a = ByteStringStore(b'abc')
>>> b= ByteStringStore.from_unicode('äöü')
>>> type(a)
<class '__main__.ByteStringStore'>
>>> type(b)
<class '__main__.ByteStringStore'>
>>>

```

### Static Methods

Python static-methods neither work on class instance-objects nor on class-objects (that's the task of 'instance-method' and 'class-methods'). Python 'static-methods' can best be compared to module-functions, defined in the namespace of a class, instead of a modules-namespace.

***Usecase:*** Python 'static-methods' can be used for (utility-)functions that logical link to a class, but do not work on the class or their instaances itself

Python 'static-methods' are defined using the `@staticmethod`-decorator preceeding to the method-definition

*`@staticmethod`-example*

```python
>>> class A:
...     @staticmethod
...     def mystaticmethod():
...         print('this is a staticmethod')
...
>>> A.mystaticmethod()
this is a staticmethod
>>>
```

Python `@staticmethods` are the correspondents to C++ and Java staticmethods, see the Python docs for [`classmethod`](https://docs.python.org/3/library/functions.html#classmethod)

## Callable Classes

Callable classes are classes where the class instances can simply be called as a function. Giving the class a callable-interface, their instances are callable. A class is made callable by defining a the special instance-method named `__call__()`).

 ***Usecase:***
 If different classes provide different instance-method names for the same functionality (e.g. `A.get_name()` and `B.getMyName()`), the usage for the programmers is cumbersome. If they want to get the name from the objects on the one hand they have to call `a.get_name()`and on the other hand `b.getMyName()`. Making the classes callable, gives them a uniform interface, the name for both class instance can be fetched in the same manner, simply using the object-name following parenthesis: `a()` and `b()`.

 ***Definition of a callable class***

``` python
>>> class CallableClass:
...     name = None
...     def __init__(self, name):
...         CallableClass.name = name
...     def get_name(self):
...         print('>>> calling normal instance-method: %s() <<<' % self.get_name.__name__)
...         return CallableClass.name
...     def __call__(self):
...         print('>>> calling special instance-method: %s() <<<' % self.__call__.__name__)
...         return CallableClass.name
...
>>>
```



***Usage of a callable instance***

``` python
>>> foo = CallableClass('foo')                        # (1) Create an instance of the callable class
>>> print('name = %s' % foo.get_name())                # (2) use the 'standard'-class-interface instance-method 'get_name()'
>>> calling normal instance-method: get_name() <<<
name = foo
>>> print('name = %s' % foo())                        # (3) use the 'callable'-class-interface instance-method '__call__()'
>>> calling special instance-method: __call__() <<<
name = foo
>>>
```


Let's give it a try

--8<--
training/lessons/customer-class/customer.md
--8<--


## Class Decorators

Decorators are explained in detail [here](decorators.md). Here we just give a brief overview concerning decorating in the context of classes.

***Usecase***
Generally speaking a decorator is a 'wrappers' around functions or classes with the purpose of adding some functionality.
Wrappers are callable object, see [callable-class](#callable-classes).

So there are two parties in the decorating process:

1. the decorator
2. the object to be decorated

### Using a class as a decorator

In the following example we define a ***class*** as a decorator and define a ***function*** which is decorated with this 'class-decorator'.

***Class Decorator definition and function decoration***

``` python
>>> class MyDecorator:
...     def __init__(self, func):
...         self.func = func
...     def __call__(self, *args):
...         # put the additional functionalty here around the function
...         print('==> START calling %s()' % self.func.__name__)  # some output before the wrapped function is called
...         self.func(*args)                                      # call the wrapped-function
...         print('<== END calling %s()' % self.func.__name__)    # some output after the wrapped function is called
...
>>> @MyDecorator
... def myfunc(x):
...     print('>>> INSIDE decorated function: %s<<<' % x)
...
>>>
```

***function call***

``` python
>>> myfunc('decorator-example')
==> START calling myfunc()
>>> INSIDE decorated function: decorator-example<<<
<== END calling myfunc()
>>>
```

***Note:***
Here the class-decorator was used to provide some additional output, when the 'decorated' function is called.

### Decorating a class

In the following example we define a ***function*** as a decorator and define a ***class*** which is decorated with this 'function-decorator'.

***Note:***
Here the decorator works on class-definition level, providing some additional funtionality around the class-definition. For sure a rather infrequent usecase which can be classified in some sense as meta-programming.

``` python
>>> def mydecoratorfunc(cls):
...     print('>>> A new class was born: %s' % cls)
...     return cls
...
>>> @mydecoratorfunc
... class A: pass
...
>>> A new class was born: <class '__main__.A'>
>>>
```

## Class Testing

Python provides 2 builtin-function to identify/test the membership on class instance-types.

1. `types()`: Identifies the concrete class of the class instance
2. `isinstance()`: Testing the belonging to a certain type (along the class-hierarchy!)

```python
>>> class A(): pass
...
>>> class B(A): pass
...
>>> class C(): pass
...
>>> a = A()
>>> b = B()
>>> c = C()
>>> type(a)
<class '__main__.A'>
>>> type(b)
<class '__main__.B'>
>>> type(c)
<class '__main__.C'>
>>> isinstance(a, A)
True
>>> isinstance(b, A)          # check along the inheritance-hierarchy
True
>>> isinstance(c, B)
False

```

## MetaClasses

It should be mentioned that Python also supports techniques for meta-programming, for example to create metaclasses. But this is subject to advanced courses.

## Further readings on classes

 Please refer to the Python docs about [Classes](https://docs.python.org/3/tutorial/classes.html).





