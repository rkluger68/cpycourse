# Be classy: Python Classes and Instances

Classes are the Python building block creating user-defined types in an object-oriented manner. Classes encapsulate data ('attributes') and appropriate functions ('methods'), which define the bahaviour of class-instances (i.e. objects of that class). Python supports composition ("has-a"-relation) and (multiple-) inheritance ("is-a"-relation) between classes/instances. In combination with method-overriding and a special kind of polymorphism (***Duck-Typing***), Python offers the complete bunch of object-oriented features.

## Simple class

Simple classe typically have instance-attributes and instance-methods.

1. instance attributes: 
    - each class instance has its own 'local' copy of its instance-atttributes  
    - instance-attribute are accessd using the '.'-dot operator: '<class-instance>.<instance-attribute>'
2. instance-methods: 
    - must be called with a class-instance
    - instance-method are accessed using the '.'-dot operator: '<class-instance>.<instance-attribute>(<params>)

***class definition***  

    >>> class A:
    ...     def __init__(self, name):  # class constructor
    ...          self.name = name      # instance-attribute
    ...     def getName(self):         # instance method
    ...         return self.name
    ... 
    >>>
  
***class instantiation - attribute and method access***

    >>> a1 = ('A')
    >>> a1.name          # attribute-access using class-instance and '.'-dot operator
    'A'
    >>> a1.getName()     # method-access  using class-instance and '.'-dot operator
    'A'
    >>>    


## Inheritance

Derived classes inherit all attributes/methodes defined in the base-class.

***class definition***  

    >>> class B(A):                            # class 'B' inherhits from class 'A'
    ...     def __init__(self, name, number):  # class constructor
    ...         A.__init__(self, name)         # call base-class constructor
    ...         self.number = number           # instance variable
    ...     def getNumber(self):               # instance methode
    ...         return self.number
    ... 
    >>> 


***class instantiation***

    >>> b = B('B', 100)
    >>> b.name                                # attribute-access
    'B'
    >>> b.getName()                           # method-access
    'B'
    >>> b.number                              # attribute-access
    100
    >>> b.getNumber()                         # attribute-access     
    100
    >>>


## class attributes

As opposed to 'instance'-attributes 'class'-attributes are common to all class instances.

***class definition***

    >>> class A:
    ...     count = 0
    ...     def __init__(self, name):
    ...         self.name = name
    ...         A.count += 1
    ... 
    >>> 
    
***class instantiation***

    >>> a1 = A('A1')    # 1.st instance increments class-attribute
    >>> a1.count
    1
    >>> a2 = A('A2')    # 2.nd instance increments class-attribute
    >>> a2.count
    2
    >>> a1.count        # Note: both instances share the same attribute
    2
    >>>




  
