# Be classy: Python Classes and Instances

Classes are the Python building block creating user-defined types in an object-oriented manner. Classes encapsulate data ('attributes') and appropriate functions ('methods'), which define the bahaviour of class-instances (i.e. objects of that class). Python supports composition ("has-a"-relation) and (multiple-) inheritance ("is-a"-relation) between classes/instances. In combination with method-overriding and a special kind of polymorphism (***Duck-Typing***), Python offers most of bunch of object-oriented features (Most of because Python doesn't really class privacy as explained below).

## Simple class

Simple classe typically have instance-attributes and instance-methods.

1. instance attributes: 
    - each class instance has its own 'local' copy of its instance-atttributes  
    - instance-attributes are accessd using the `.`-dot operator:  Pseudo-syntax `<class-instance>.<instance-attribute>`
2. instance-methods: 
    - must be called with a class-instance
    - instance-methoda are accessed using the `.`-dot operator: Pseudo-syntax `<class-instance>.<instance-attribute>(<params>)`

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

### Class Privacy - private Attributes

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


### Class Poperties

With class properties (decorator `@roperties `) methods can be accessed like ordinary attributes. As such they form dynmically computed attributes.







  
