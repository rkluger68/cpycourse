# Be classy: Python Classes and Instances

Classes are the Python building block creating user-defined types in an object-oriented manner. Classes encapsulate data ('attributes') and appropriate functions ('methods'), which define the bahaviour of class-instances (i.e. objects of that class). Python supports composition ("has-a"-relation) and (multiple-) inheritance ("is-a"-relation) between classes/instances. In combination with method-overriding and a special kind of polymorphism (***Duck-Typing***), Python offers most of bunch of object-oriented features (Most, because Python doesn't really supports class privacy as explained below).

## Simple class

Simple classe typically have instance-attributes and instance-methods.

1. instance attributes: 
    - each class instance has its own 'local' copy of its instance-atttributes  
    - instance-attributes are accessd using the `.`-dot operator:  Pseudo-syntax `<class-instance>.<instance-attribute>`
2. instance-methods: 
    - must be called with a class-instance
    - instance-methods are accessed using the `.`-dot operator: Pseudo-syntax `<class-instance>.<instance-attribute>(<params>)`
    - the class constructor is named `__init__()`. The `__init__()`-method is not mandatory to create class-instances (that's the task of the [`__new__()`-method](https://docs.python.org/3/reference/datamodel.html?highlight=__init#object.__new__), which is implicitly there. But practically the `__init__()`-method is always necessary to initialize the instance-attributes
    - a class can define a destructor-mehod called `__del__()`, to explicitly do some finalizer tasks e.g. close ressources opened by the class-instance. The destructor is never called explicitly by user-code, instead its is called by the interpreters garbage collector, when the reference count (see [Object Lifetime and Object Reference](objects.md)) of the class instance reaches 0. For more details see [__del__()](https://docs.python.org/3/reference/datamodel.html?highlight=__del#object.__del__).
    - every instance-method need an explicit *1.st*-parameter named `self`

***class definition***  

``` python
>>> class A:
...     def __init__(self, name):  # class constructor
...          self.name = name      # instance-attribute
...     def getName(self):         # instance method
...         return self.name
... 
>>>
```
  
***class instantiation - attribute and method access***

``` python
>>> a1 = ('A')
>>> a1.name          # attribute-access using class-instance and '.'-dot operator
'A'
>>> a1.getName()     # method-access  using class-instance and '.'-dot operator
'A'
>>>    
```

## Note on `self`-parameter 

During a instance-method call the python interpreter implicity converts (pseudocode)

    <class-instance-object>.<instance-method>(<param-1>, ... <param-n>)

into

    <class-object><instance-method>(<class-instance-object>, <param-1>, ... <param-n>)

The `self`-argument is the class-instance-object iself. See also the section [Instance methods](https://docs.python.org/3/reference/datamodel.html?highlight=__del#the-standard-type-hierarchy).

The `self`-parameter is therfore similar to the `this`-pointer of C++ and Java:

1. Python `self`: Explicit 1.st parameter in every instance-method
2. C++ `this`-pointer: keyword holding a pointer to the current object implicit parameter to all member functions
3. Java `this`-keyword: reference to the current object

*Note*
The name `self` is a convention , and could be changed, but it shouldn't because

## Class Privacy - private Attributes

Python doesen't provide any kind of 'access-specifiers' like e.g. C++ (public, private, protected) to control access to
attributes or methods. I.e. attributes and methods are 'public' accessible.

Python provides 2 weak forms of data-hiding (but no real protection by access-control)

1. 'private-by-convention': Attributes prefixed with a single underscore `_` should be regarded as a private attribute
2. 'private-by-lexical-substitition': Attributes prefixed with double underscores `__` like e.g. `__foo` will be implicitly renamed to `_classname__foo` by the interpreter. This textual substitution is called 'name-mangling'.

As can be seen the following example this 'protections' can be bypassed:

``` python
>>> class A:
...     def __init__(self, name):
...         self.name = name
...         self._name = name        # attribute 'private-by-convention'
...         self.__name = name       # attribute 'private-by-lexical-substitution'
...     def getName(self):
...         return self.name
...     def _getName(self):
...         return self._name
...     def __getName(self):
...         return self.__name
...
>>>
```

***usage***

```python
>>> a = A("ClassPrivacy")
>>> dir(a)
['_A__getName', '_A__name', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_getName', '_name', 'getName', 'name']
>>> a.name             # (1) public attribute
'ClassPrivacy'
>>> a._name            # (2) private-by-convention ==> still accessible
'ClassPrivacy'
>>> a.__name           # (3) private-by-lecical-convention ==> not accessible because it is not found
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__name'
>>> a.getName()        # (4) public method                       
'ClassPrivacy'
>>> a._getName()       # (5) private-by-convention ==> still accessible/callable
'ClassPrivacy'
>>> a.__getName()      # (6) private-by-lecical-convention ==> not accessible because it is not found
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute '__getName'
>>> a._A__name         # (7) bypass protection because you know the rule
'ClassPrivacy'
>>> a._A__getName()    # (8) bypass protection because you know the rule
'ClassPrivacy'
>>>
```

For more details please refer to [Private Variables](https://docs.python.org/3/tutorial/classes.html#private-variables)

## Inheritance ("is-a"-relation)

*Note: class privacy*  
As mentioned above Python doesn't provide any real mechanism for class privacy, neither 'data-protection' nor 'data-hiding'. This alos applies to class-inheritance. Because all attributes/methods are public, derived classes inherit all attributes/methodes defined in the base-class.

***class definition***  

``` python
>>> class B(A):                            # class 'B' inherhits from class 'A'
...     def __init__(self, name, number):  # class constructor
...         A.__init__(self, name)         # call base-class constructor
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
>>> b.getName()                           # method-access
'Inheritance'
>>> b.number                              # attribute-access
100
>>> b.getNumber()                         # attribute-access     
100
>>>
```

## Multiple Inheritance

Python also support multiple inheritance

***class definition*** 

``` python
>>> class A:
...     def __init__(self, name):
...         self.name = name
...     def getName(self):
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
...         A.__init__(self, name)           # call base-class constructor class 'A'
...         Z.__init__(self, another_name)   # call base-class constructor class 'Z'
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
>>> b.getName()
'BaseClass_A'
>>> b.getAnotherName()
'BaseClass_Z'
>>> dir(b)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'another_name', 'getAnotherName', 'getName', 'getNumber', 'name', 'number']
>>>
```

*Note*
The `dir(<object>`)- builin function list all names in the namespace of the given object

## Composition ("has-a"-relation)

***class definitions***  

``` python
>>> class A:
...     def __init__(self, name):
...         self.name = name
...     def getName(self):
...         return self.name
... 
>>> class B:
...     def __init__(self, name, number):
...         self.a = A(name)
...         self.number = number
...     def getNumber(self):
...         return self.number
...     def getName(self):
...         return self.a.getName()
... 
>>>
```

***class instantiation***

``` python
>>> b = B('Composition', 100)
>>> b.getName()
'Composition'
>>> b.getNumber()
100
>>> 
```

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
```


## Class Poperties [WIP]


With class properties (decorator `@roperties`) methods can be accessed like ordinary attributes. As such they form dynmically computed attributes.

Python support two different ways of implementing properties:

1. 'lower-level' using `property()` builtin  function
2. 'higher-level' using  `@propery()`-decorator

The Python docs provide a good [property-example](https://docs.python.org/3/library/functions.html#property), which is copied here simply for convenience.

*** example using builtin `property()` function ***

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
>>> p1.x = 1
>>> p1.x
1
>>> del p1.x
>>> p1.x = 11
>>> p1.x
11
```

*** example using builtin `@propery()` decorator ***
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
>>> p1 = D()
>>> p1.x = 9
>>> p1.x
9
>>> del p1.x
>>> p1.x = 99
>>> p1.x
99
>>>
```

## Duck Typing [WIP]

Statically typed languages like C++ use virtual function for runtime polymorphism. Derived classes therefore override base-class functions retaining their signature. When base-class objects which held a derived class reference call their base-class function the runtime will virtual dispatch the derived-class function.
This allows programing on a abstract base-class level. But this is only possible with class-objects inheritance
Pythons polymorphism is based on 'duck typing'. 

This enable more architecural freedom on the program/class-design, because class-hierarchies can be breaked down and allow lmore loosely couped

Virtual functions


## Special Methods

### class methods

As opposed to instance-methods, class-methods operate on the class-object.

*use-case*: Python doesn't support method overloading like C++ or Java. Therefore multiple methods with the same name within a single class is not supported. As a consequence only a single class constructor (`__init__()`-method). With Python `@classmethod` it

*`@classicmethod`-example*

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

Python static-methods neither work on class-instance-objects nor on class-objects (that's the task of instance-method and class-methods). Python staticmethods can best be compared to module-functions, defined in the namespace of a class, instead of a modules-namespace.

*Usecase*: Python staticmethods can be used for (utility-)function that logical link to a class

Python staticmethods are defined using the `@staticmethod`-decorator preceeding to the method-definition

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

## Class Testing

Python provides 2 builtin-function to identify/test of the membership on class-instance-types

1. `types()`: Identifies the class of the class-instance
2. `isinstance()`: Testing the

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








  
