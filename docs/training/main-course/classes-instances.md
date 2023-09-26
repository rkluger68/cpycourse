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

## A Simple Class

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


## Class Attributes

As opposed to instance attributes class attributes are common to all class
instances:

``` python
>>> class A:
...     count = 0
...     def __init__(self, name):
...         self.name = name
...         A.count += 1
...
>>> a1 = A('A1')    # 1st instance increments class attribute
>>> a1.count
1
>>> a2 = A('A2')    # 2nd instance increments class attribute
>>> a2.count
2
>>> a1.count        # Both instances share the same attribute
2
>>>
>>> id(a1.count)
140201179340160
>>> id(a2.count)
140201179340160
>>>
```


## Class Privacy - Private Attributes

Python doesen't provide 'access modifiers' like e.g. C++ (`public`, `private`,
`protected`) to control access to attributes or methods. I.e.  attributes and
methods are 'public'.

Python relies upon sane usage of a class and 2 forms of data "hiding" (but no
real protection by access control):

1. 'private-by-convention': Attributes prefixed with a single underscore `_`
   should be regarded as private attributes, not part of the 'public API' of
   the class.
2. 'private-by-lexical-substitition': Attributes starting with double
   underscores `__`[^leading-dunder] like e.g. `__foo` will be implicitly renamed to
   `_classname__foo` by the interpreter. This textual substitution is called
   'name mangling'.

[^leading-dunder]:
    But not also *ending* with double underscores - leading plus trailing
    double underscores ('dunder') denote 'special methods' that implement
    object protocols, e.g. for operator overloading.

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

For more details please refer to [Private Variables](https://docs.python.org/3/tutorial/classes.html#private-variables).


## Class Properties

Ordinary Python instance attributes are readable, writable and deletable by
default. Using *properties* attribute access can be *managed* to allow for
control with regard to read, write and delete access.

Python properties represent managed attributes. This is achieved through
Python's [descriptor
protocol](https://docs.python.org/3/howto/descriptor.html), by providing 
`getter`, `setter` and `deleter` methods which enable intercepting regular
attribute access with accessor functions.

**Usecase:** Properties are a way of data encapsulation. Hiding ordinary
attributes behind a property interface/facade introduces a level of
indirection to the original attribute: the original attribute may change behind
the scenes while keeping the class' public interface/API stable for its users.

This can be a powerful mechanism to evolve a class interface without affecting
existing client code. When public access to an attribute has already been
established but later improvements need internal implementation changes, these
can be wrapped using `property`.

The most convenient way to define properties is by using a decorator:

``` python
class C:
    def __init__(self):
        self._x = None

    # Provide read access to self._x.
    # The decorated method is used as read accessor function.
    @property
    def x(self):
        """The 'x' property."""
        return self._x

    # Provide write access to self._x.
    # The decorated method is used as write accessor function.
    @x.setter
    def x(self, value):
        self._x = value

    # Allow for deleting self._x.
    # The decorated method is used as delete accessor function.
    @x.deleter
    def x(self):
        del self._x
```

Note: The setter and deleter methods shall have the same name as the getter
method.

In use:

``` python
>>> obj = C()
>>> obj.x = 9       # set property value
>>> obj.x           # get property value
9
>>> del obj.x       # delete property
>>> obj.x = 99      # re-create property
>>> obj.x
99
>>>
```

Alternatively, the `property` built-in can also be used like this to create
managed attributes:

``` python
class C:
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "The 'x' property.")
```

This is equivalent to the decorarator variant.

A read-only property simply doesn't define setter and deleter methods:

``` python
>>> class C:
...     def __init__(self, x):
...         self._x = x
...     @property
...     def x(self):
...         return self._x
...
>>>
>>> obj = C('foo')
>>> obj.x                                  # read access
'foo'
>>> obj.x = 'bar'                          # attempt write access
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>> del obj.x                              # attempt delete access
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't delete attribute
>>>
```

Similarly, read/write access without delete can be achieved by leaving out the
deleter method.

## Relationships between Classes

Python supports 'inheritance' ("is-a" relation) and 'composition' ("has-a" relation) of classes/instances.

(Multiple) inheritance and the mechanism of 'method overriding' provide for
the usual notion of 'polymorphism' found in many object-oriented languages.

In addition, Python allows for the so-called **Duck-Typing**, a kind of
polymorphism that does not build upon an object being of a certain single type
but implementing certain features (implementing a 'protocol').

### Inheritance ("is-a" relation)

When a class is defined as the 'subclass' of another class it *inherits* all
its *properties* and *behaviour* - in other words, its attributes and methods:

``` python
>>> class SomeClass:
...     def __init__(self, name):
...         self.name = name
...     def greet(self):
...         print(f'Hello, my name is {self.name}.')
...
>>> class SomeSubClass(SomeClass):  # SomeSubClass inherits from SomeClass
...     pass
...
```

We can then reuse the inherited functionality (properties and behaviour) with
the subclass:

``` python
>>> sub_instance = SomeSubClass('Fredrik')
>>> sub_instance.name     # access inherited instance attribute
'Fredrik'
>>> sub_instance.greet()  # invoke inherited method
Hello, my name is Fredrik.
>>>
```

The class which a subclass (aka derived class) inherits from is called a
'superclass' or 'base class'.[^baseclass-superclass]

[^baseclass-superclass]:
    Sometimes, for multiple levels of inheritance only the "root" of the
    inheritance tree is called base class, i.e. only a superclass which is
    not a subclass. Strictly speaking, this would always be `object` in Python
    but it's also loosely used for only the user defined "base class".

A subclass can *specialize* the behaviour of a superclass by means of
overriding methods:

``` python
>>> class SomeFriendlySubClass(SomeClass):
...     def greet(self):  # override superclass greet() method
...         print(f"Hello, I'm especially friendly and my name is {self.name}.")
...
>>> sub_instance = SomeFriendlySubClass('Pat')
>>> sub_instance.greet()
Hello, I'm especially friendly and my name is Pat.
>>>
```

A subclass can also add behaviour:

``` python
>>> class SomeSocialFriendlyClass(SomeFriendlySubClass):
...     def meet(self, other):  # additional method
...         print(f"Hello {other}, nice to meet you!")
... 
>>> social_obj = SomeSocialFriendlyClass('Taylor')
>>> social_obj.meet('Ed')
Hello Ed, nice to meet you!
>>> 
```

Note how `SomeSocialFriendlyClass` inherits from `SomeFriendlySubClass` which
in turn inherits from `SomeClass`. This results in a *hierarchy*  of
superclasses and subclasses.

Inheritance allows for several things:

 - Sharing code: A subclass can use the attributes and methods of its
   superclasses (i.e. re-using or sharing their implementation).
 - Setting up 'interface contracts' through types and subtypes (superclasses
   and subclasses): If a subclass provides all the relevant properties and
   behaviour (attributes and methods) of a superclass than it can be used
   wherever the superclass is expected.
 - Specialising behaviour: A subclass can modify behaviour by overriding
   methods of a superclass.

#### A Small Inheritance Example

A very basic example illustrating some of Python's inheritance specifics:

``` python
--8<--
src/inherit.py
--8<--
```

Note that a subclass that implements `__init__` must explicitly call the
superclass constructor. While you can do this manually by calling
`SuperClass.__init__(self, ...)` in `SubClass.__init__` it's usually better to
use `super().__init__(...)` for this, see [python super()
docs](https://docs.python.org/3/library/functions.html#super) and the [guide to
using
super()](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/).


When run this will output:

``` console
$ python3 inherit.py

Advanced Python Wizardry product_id=Product-1
Advanced Python Wizardry (Peter Y. Thonista):
All of Python's secrets

The Very Best of product_id=Product-2
The Pythonics: The Very Best of
Best or 1991-2023
 1. Python Shuffle
 2. Snake Boogie
 3. Green is the New Black
 4. Hisses & Kisses

Currently available products in inventory: 2
```

**A note on class privacy:**
As mentioned above, Python doesn't provide any strict mechanism for class
privacy, neither 'data protection' nor 'data hiding'. This also applies to
class inheritance. Inheritance is public by default, as a consequence all of
a base class' attributes and methods are inherited by a derived class.

The name mangling mechanism for attribute names with leading double underscores
also applies to access from subclasses to a base class attribute:

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

#### Multiple Inheritance

In Python a class can inherit from more than one superclass. This is called
*multiple inheritance*.

Suppose we'd like to implement a very basic data processing pipeline that
pushes data messages through interconnected nodes, akin to a "directed graph".

Some nodes act as data-producing nodes only, some as data-consuming nodes
only. But there's also nodes that both consume data ("receive messages") and
produce data ("send messages"). This could be modeled with multiple
inheritance:

``` python
--8<--
src/multiple_inheritance.py
--8<--
```

This outputs:

``` console
$ python3.8 multiple_inheritance.py
PrinterSink "Sink": msg=0 trail=('Source', 'A', 'B', 'Sink')
PrinterSink "Sink": msg=0 trail=('Source', 'A', 'C', 'Sink')
PrinterSink "Sink": msg=1 trail=('Source', 'A', 'B', 'Sink')
PrinterSink "Sink": msg=1 trail=('Source', 'A', 'C', 'Sink')
PrinterSink "Sink": msg=2 trail=('Source', 'A', 'B', 'Sink')
PrinterSink "Sink": msg=2 trail=('Source', 'A', 'C', 'Sink')
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__', 'add_out_nodes', 'name',
'out_nodes', 'send'] ``` console
```

Note: The `dir(<object>)` built-in function lists all names in the namespace of
the given object. With inheritance, this encompasses the names defined in the
object's superclasses.

Multiple inheritance can get pretty tricky. Must of the time it's sensible to
avoid it and stick to single inheritance - or use other concepts to model the
domain, like composition or duck typing.


### Composition ("has-a" relation)

Python also supports composition, i.e. a class has or uses an instance of
another class to provide certain behaviour.


#### 'Owned-By' Composition

E.g. `Car` creates and has an instance attribute which is an `Engine`-like
object:

```python
>>> class Engine:                             
...     @property                             
...     def name(self):                       
...         ... 
... 
>>> class CombustionEngine:           
...     def __init__(self, cylinders, layout):
...         self.cylinders = cylinders        
...         self.layout = layout              
...     @property                             
...     def name(self):                       
...         return f'{self.cylinders}-cylinders-{self.layout}'
... 
>>> class Car:                     
...     def __init__(self, brand, model):
...         self.brand = brand     
...         self.model = model     
...         self.engine = CombustionEngine(cylinders=6, layout='boxer')
...     @property                  
...     def name(self):            
...         return f'{self.brand} {self.model}'
...     # Since using the Engine class is an internal detail here (and could       
...     # change) we should provide for a method to get the engine name.
...     @property      
...     def engine_name(self):     
...         return self.engine.name
... 
>>> car = Car('Racemaker', '9110')
>>> car.name
'Racemaker 9110'
>>> car.engine_name
'6-cylinders-boxer'
>>> 
```

#### 'Used-By' Composition

It's usually better to not couple the classes so tightly and instead *inject*
an object to the using class:

``` python
>>> class Engine:                             
...     @property                             
...     def name(self):
...         ...
...
>>> class CombustionEngine(Engine):
...     def __init__(self, cylinders, layout):
...         self.cylinders = cylinders
...         self.layout = layout   
...     @property                  
...     def name(self):            
...         return f'{self.cylinders}-cylinders-{self.layout}'
... 
>>> class Car:                     
...     def __init__(self, brand, model, engine):
...         self.brand = brand     
...         self.model = model     
...         self.engine = engine   
...     @property                                                              ...     def name(self):
...         return f'{self.brand} {self.model}'
... 
>>> engine = CombustionEngine(cylinders=6, layout='boxer')
>>> car = Car('Racemaker', '9110', engine=engine)
>>> car.name
'Racemaker 9110'
>>> # Directly accessing Engine attributes is unproblematic now, since it's
>>> # not an internal implementation detail of Car.
>>> engine.name
'6-cylinders-boxer'
>>> car.engine.name
'6-cylinders-boxer'
>>> 
```

This gains flexibility e.g. for testing since it's now easy to inject a mock or
fake object instead of "the real thing". Moreover, we could now easily fit a
modern age `ElectricMotor` into our dinosaur sports car. 

Instead of injecting a class instance there's room for variation:  a middle
ground may be to inject a class object instead, leaving instantiation to the
using class.


### A note on 'Inheritance vs Composition'

The overaching goal of both concepts is code reusability:

- Inheritance: base class methods and attributes are inherited by derived
  classes and can be extended or overwritten
- Composition: combine existing classes (not in an inheritance relationship) as
  building blocks to build more complex functionality

They aren't mutually exclusive. It can well make sense to combine the two
approaches to model your domain.

The material presented here doesn't aim to properly discuss the advantages and
disadvantages of using inheritance vs composition or even object orientation at
all. There is plenty of good reading material on this subject out there. As
always:

 - Use the model that fits best for the problem at hand.
 - Prefer simplicity - if possible.
 - Be skeptical about advice that tells you something should *never* be used
   or done.

Interesting reading: [The Composition Over Inheritance Principle](https://python-patterns.guide/gang-of-four/composition-over-inheritance/) first described in the [Gang of Four Book](https://python-patterns.guide/gang-of-four/).

### Duck Typing

Statically typed languages like C++ use virtual function dispatch for runtime
polymorphism. Derived classes override base class member functions (methods)
retaining their signature.

When variables of the base class type holding a reference to a derived class
instance call a member function, the runtime will 'virtually dispatch' to the
derived class' overridden member function. 

While this does allow for runtime polymorphism it is restricted to a (sub-)
type relationship through inheritance: only subclasses of the superclass/base
class are appropriate where the superclass is expected.

In contrast, Pythons provides 'duck typing' where the polymorphism is not based
on common types but on common behaviour (methods and attributes of an object).
See the [Wikipedia article on Duck
typing](https://en.wikipedia.org/wiki/Duck_typing): "If it walks like a duck
and it quacks like a duck, then it must be a duck."

This enables more freedom for the program and class design, because rigid class
hierarchies may be avoided and a more loosely coupled architecture becomes
possible.

Here's a contrived example:

``` python
>>> class Animal:
...     def speak(self):
...         print('Animals speak')
... 
>>> class Cat(Animal):
...     def speak(self):
...         print('Meow')
... 
>>> class Dog(Animal):
...     def speak(self):
...         print('Wuff')
... 
>>> def make_animals_talk(animal):
...     animal.speak()
... 
>>> make_animals_talk(Cat())
Meow
>>> make_animals_talk(Dog())
Wuff
>>> class RoboDuck:       # Robot duck with A.I., not a live animal
...     def speak(self):  # RoboDuck implements the 'speak protocol'
...         print('Beep beep beep')
... 
>>> # This will work: RoboDuck is not a subclass of Animal, but it implements
>>> # the 'speak protocol'
>>> make_animals_talk(RoboDuck())
Beep beep beep
>>>
```

Duck typing works well with composition, too.

## Class & Static Methods

### Class Methods

As opposed to instance methods, class methods operate on the class object.

**Usecase:**
Python doesn't support method overloading like C++ or Java. Therefore multiple
methods with the same name (and different signatures) are not possible
within a single class. As a consequence, only a single class constructor can be
defined. Class methods can be a good way to provide alternative constructor
methods.

Class methods are defined by applying the `@classmethod` decorator to a method:

``` python
>>> class ByteStringStore:
...     def __init__(self, bytestring, encoding='utf-8'):
...         self.bytestring = bytestring
...         self.encoding = encoding
...     @classmethod
...     def from_unicode(cls, unicodestring, encoding='utf-8'):
...         return cls(unicodestring.encode(encoding))
...
>>> a = ByteStringStore(b'abc')
>>> b = ByteStringStore.from_unicode('äöü')
>>> type(a)
<class '__main__.ByteStringStore'>
>>> type(b)
<class '__main__.ByteStringStore'>
>>>

```

The decorated method must take the class object as its 1st argument
(usually called `cls` by convention).

### Static Methods

Like e.g. C++ static member functions Python's static methods neither work on
class instances nor on classes. Rather, the class acts as an additional
namespace for these methods, much like a module acts as a namespace for 
functions.

Static methods could be used for (utility) functions that belong to a class
conceptually but do not work on the class or their instances themselves.

Static methods are defined by prepending the `@staticmethod` decorator
to a method definition:


```python
>>> class Namespace:
...     @staticmethod
...     def mystaticmethod():
...         print('this is a staticmethod')
...
>>> Namespace.mystaticmethod()
this is a staticmethod
>>>
```

Python static methods correspond to C++ and Java static methods, see the Python
docs for
[`staticmethod`](https://docs.python.org/3/library/functions.html#staticmethod).

## Callable Class Instances

Callable class instances are instances that can be *called* like a function.

Since a class instance regularly holds state (in its instance attributes),
making it callable is a way to implement a "stateful
function".[^stateful-inner-functions]

[^stateful-inner-functions]:
    There are others, like e.g. inner functions accessing names (or "cells")
    from outer scopes.

The equivalent in C++ is called a function object.

Class instances can made callable by defining the special method `__call__()`
on the class:

``` python
>>> class Counter:
...     def __init__(self, start=0):
...         self.count = start
...     def __call__(self):
...         self.count += 1
...         return self.count
... 
>>> count = Counter()
>>> count()
1
>>> count()
2
>>> count()
3
>>> 
```

## Lesson: Customer Class

--8<--
training/lessons/customer-class/customer.md
--8<--


## Class Decoration

We'll just give a brief overview on decorator in the context of classes.
Decorators are explained in detail [here](decorators.md).

In principal a decorator 'wraps' functions or classes with the
purpose of adding some functionality. A decorator is callable (it must be able
to retrieve the function/class to wrap) and returns the wrapped argument -
usually a (modified) function or class.

### Using a Class as a Decorator

We can define a callable class instance (see above) and use its class as a
decorator for a function:

``` python
>>> class MyDecorator:
...     def __init__(self, func):
...         self.func = func
...     def __call__(self, *args):
...         # Additional functionality around the function:
...         # Some output before the wrapped function is called...
...         print('==> START calling %s()' % self.func.__name__)
...         self.func(*args)   # call the wrapped function
...         # ...some output after the wrapped function has returned.
...         print('<== END calling %s()' % self.func.__name__)
...
>>> @MyDecorator
... def myfunc(x):
...     print('>>> INSIDE decorated function: %s<<<' % x)
...
>>> myfunc('decorator-example')
==> START calling myfunc()
>>> INSIDE decorated function: decorator-example<<<
<== END calling myfunc()
>>>
```

### Decorating a class

A decorator can also be used to wrap a class instead of a function, providing
some additional functionality to the class definition.

We can e.g. add custom methods to a class:

``` python
>>> def make_friendly(cls):
...     def greet(self):
...         print("Hello, I'm a friendly class.")
...     setattr(cls, "greet", greet)
...     return cls
... 
>>> @make_friendly
... class MyClass:
...     pass
... 
>>> MyClass().greet()
Hello, I'm a friendly class.
>>> 
```

In a more realistic scenario we might use a decorator that traces/logs entering
and exiting all the methods of a class, maybe switchable through environment
variables or configuration.

Since decorators can modify classes they can be used for things that are
otherwise achievable with meta-programming, i.e. using [custom
metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses).


## Class Instance Testing

Python provides 2 built-in functions to identify/test the types of class
instances:

1. `type()`: Returns the type of on object, e.g. the class of a class instance
2. `isinstance(...)`: Tests if an object is an instance of a certain type (
   along the class inheritance hierarchy)

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
>>> isinstance(b, A)          # check along the inheritance hierarchy
True
>>> isinstance(c, B)
False

```

## Metaclasses

As mentioned before, Python also supports techniques for meta-programming, for
example to create metaclasses. But this is subject to advanced courses, see
[custom
metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses)
for more.

## Further Readings on Classes

Please refer to the Python docs about
[Classes](https://docs.python.org/3/tutorial/classes.html).





