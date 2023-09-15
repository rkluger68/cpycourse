# A practical Overview of Python Built-in Types

This chapter describes important properties of Python's built-in types.

Python provides a bunch of popular data types. **Simple types** (also called
primitive data types) as well as **compound types**, which are collections or
containers of data of equal or different type.

Each of the Python data types provide a data type-specific set of *methods* and
*operators* that determine the data type's behaviour. This ensemble of __data__
and __behaviour__ defines the properties of all Python objects.  For the
complete list please refer to [Python Built-in
Types](https://docs.python.org/3/library/stdtypes.html).

Python built-in data types are Python classes themselves. Instances of nearly
all Python builtin data-types can be created in two different ways:

 - using a type-specific literal notation: literals in the case of **simple
   data types** or "literals in brackets" `(`,  `)`, `[`, `]`, `{`, `}` in
   the case of **compound data-types** 
 - using the data type's class constructor

The type of a literal or a variable (referencing or naming an object) can be
identified using the built-in `type()`-function:

``` python
>>> type("I'm curious about her")
<class 'str'>
>>> number = 42
>>> type(number)
<class 'int'>
>>> 
```

## Numeric datatypes

### Integers - `int`

Example usage:

``` python
>>> 1
1
>>> int()
0
>>> type(1)  # type of int
<class 'int'>
>>> 1 + 2  # built-in '+'-operator for int
3
>>> type(1 + 2)  # result type
<class 'int'>
>>>
```

### Floating Point Values - `float`

Example usage:
``` python
>>> 1.2
1.2
>>> float()
0.0
>>> type(1.2)  # type of float-literal
<class 'float'>
>>> 1.2 + 3.7  # built-in '+'-operator
4.9
>>> type(1.2 + 3.7)  # result type
<class 'float'>
>>>
```

!!! info

    `float` is a binary floating point number representation. This has
    consequences regarding exact number representation (not possible for most
    base 10 decimal fractions, e.g. 1.1 or 2.2 are not representable *exactly*
    as floats) and brings rounding issues, see the great [explanation in the
    official Python
    documentation](https://docs.python.org/3/tutorial/floatingpoint.html?highlight=float).

    E.g.

    ``` python
    >>> 1.1  # The float string representation "hides" the inexactness(!) 
    1.1
    >>> '{:.51f}'.format(1.1)
    '1.100000000000000088817841970012523233890533447265625'
    ```

    The standard library
    [decimal](https://docs.python.org/3/library/decimal.html) module can be
    used if this is of concern i.e. whenever the problem domain requires exact
    base 10 decimal arithmetic and rounding, e.g. in finance.
    
    It features correct decimal rounding and user-configurable precision:

    ``` python
    >>> import decimal
    >>> decimal.Decimal('1.1')
    Decimal('1.1')
    ```

--8<--
training/lessons/input-number-rounding/input-number-rounding.md
--8<--

## Sequences

Sequences are indexed, ordered "list data sets" of objects:

 - strings are *immutable* sequences of characters
 - tuples are *immutable* sequences of arbitrary objects
 - lists are *mutable* sequences of arbitrary objects

### Common Sequence Operations

``` python
# Length of sequence s denoted as N
s[i]                  # item at sequence s index i
s[i:j]                # slice of s from i to j: s[i], ..., s[N-1] (a shallow copy)
s[i:j:k]              # slice of s from i to j with step k: s[i], s[i+k], ...
len(s)                # length of s: N
min(s)                # smallest item in s
max(s)                # biggest item in s
s.index(x[, i[, j]])  # index of item x (between i and j, if given)
s.count(x)            # number of occurences of x in s
x in s                # True if an item in s equals x
x not in s            # False if an item in s equals x
s1 + s2               # concatenation of s1 and s2
s * n                 # n-times concatenation of s
n * s                 # - " -
```

### Immutable Sequences

#### Strings - `str`

Strings are *character* sequences (of unicode characters):

``` python
>>> s = 'text data is ubiquituous'
>>> s1, s2 = 'foo', 'bar'
>>> type(s)
<class 'str'>
>>> s[0]
't'
>>> s[0:10]
'text data '
>>> s[0:10:2]
'tx aa'
>>> len(s)
24
>>> min(s)
' '
>>> max(s)
'x'
>>> s.index('a')
6
>>> s.index('data', 0, 10)  # use of substrings is supported
5
>>> s.count('is')
1
>>> 'data' in s
True
>>> 'data' not in s
False
>>> s1 + s2
'foobar'
>>> s * 2
'text data is ubiquituoustext data is ubiquituous'
>>> 2 * s
'text data is ubiquituoustext data is ubiquituous'
>>>
```

##### String Methods

`str` objects have plenty of additional functionality:

```
----------------------------------------------------------------------
# string s 
s.capitalize() -> str
# capitalized (1st character uppercase, rest lowercase) copy of s

----------------------------------------------------------------------
s.casefold() -> str
# "casefolded" copy of s (lowercase with replacement of "caseless" characters,
# e.g. "ß" --> "ss"

----------------------------------------------------------------------
s.center(width[, fillchar]) -> str
# s centered in width-length string, padded with fillchar (default blank)

----------------------------------------------------------------------
s.encode(encoding='utf-8', errors='strict') -> bytes
# return s encoded to bytes object with encoding.

----------------------------------------------------------------------
s.endswith(suffix[, start[, end]]) -> bool
# True if s ends with suffix, False otherwise. 

----------------------------------------------------------------------
s.expandtabs(tabsize=8) -> str
# tab-to-space-expanded copy of s

----------------------------------------------------------------------
s.find(sub[, start[, end]]) -> int
# lowest index i is s where substring sub is found, -1 if not found.

----------------------------------------------------------------------
s.format(*args, **kwargs) -> str
# return copy of s with the {}-format placeholders substituted by arguments

----------------------------------------------------------------------
s.format_map(mapping) -> str
# return copy of s with the {}-format placeholders substituted from mapping

----------------------------------------------------------------------
s.isalnum() -> bool
# True if all characters are alphanumeric and s is non-empty

----------------------------------------------------------------------
s.isalpha() -> bool
# True if all characters are alphabetic and s is non-empty

----------------------------------------------------------------------
s.isdecimal() -> bool
# True if all characters are decimal (can form numbers in base 10) and s is non-empty

----------------------------------------------------------------------
s.isdigit() -> bool
# True if all characters are digits (includes sub-/superscripts) and s is non-empty

----------------------------------------------------------------------
s.isidentifier() -> bool
# True if s qualifies as a valid identifier

----------------------------------------------------------------------
s.islower() -> bool
# True if all characters are lowercase and s is non-empty

----------------------------------------------------------------------
s.isnumeric() -> bool
# True if all characters are numeric (have Unicode numeric property) and s is non-empty

----------------------------------------------------------------------
s.isprintable() -> bool
# True if all characters in S are printable

----------------------------------------------------------------------
s.isspace() -> bool
# True is s is all-whitespace and s is non-empty

----------------------------------------------------------------------
s.istitle() -> bool
# True is s is titlecased (each word in s starts uppercase and continues
lowercase) and s is non-empty

----------------------------------------------------------------------
s.isupper() -> bool
# True if s is all uppercase

----------------------------------------------------------------------
s.join(iterable) -> str
# concatenate the strings in iterable with s as separator

----------------------------------------------------------------------
s.ljust(width[, fillchar]) -> str
# return string of length starting with s ("left-justified"), padded with
# fillchar; doesn't truncate s if len(s) > width

----------------------------------------------------------------------
s.lower() -> str
# return all-lowercase copy of s

----------------------------------------------------------------------
s.lstrip([chars]) -> str
# return copy of s with leading whitespace removed, or with each character in
# chars removed from the beginning of s if chars is not None

----------------------------------------------------------------------
s.maketrans(x, y=None, z=None) -> dict
# return translation table dictionary for str.translate(); a single argument
# must be a ordinal/character-to-ordinal/string/None mapping dictionary; two
# arguments must be strings of the same length (chars + replacement chars)

----------------------------------------------------------------------
s.partition(sep) -> (head, sep, tail)
# return tuple (characters-before-sep, sep, characters-after sep) if separator
# sep is found, otherwise (s, '', '')

----------------------------------------------------------------------
s.replace(old, new[, count]) -> str
# copy of s with all occurences (up to count) of substring old replaced by new

----------------------------------------------------------------------
s.rfind(sub[, start[, end]]) -> int
# return highest index where sub is found in s (between start and end), i.e.
# "search from the right"; -1 if sub isn't found

----------------------------------------------------------------------
s.rindex(sub[, start[, end]]) -> int
# return highest index where sub is found in s (between start and end), i.e.
# "search from the right"; raise ValueError if sub is not found

----------------------------------------------------------------------
s.rjust(width[, fillchar]) -> str
# return string of length ending with s ("right-justified"), padded with
# fillchar; doesn't truncate s if len(s) > width

----------------------------------------------------------------------
s.rpartition(sep) -> (head, sep, tail)
# return tuple (characters-before-sep, sep, characters-after sep) if separator
# sep is found while searching from the end of s, otherwise (s, '', '')

----------------------------------------------------------------------
s.rsplit(sep=None, maxsplit=-1) -> list of strings
# split s at separator s (up to maxsplit, searching from the end of s), return
# the resulting list of words; split at any whitespace if sep is None (the
# default)

----------------------------------------------------------------------
s.rstrip([chars]) -> str
# return copy of s with trailing whitespace removed, or with each character in
# chars removed from end of s if chars is not None

----------------------------------------------------------------------
s.split(sep=None, maxsplit=-1) -> list of strings
# split s at separator s (up to maxsplit, searching from the start of s),
# return the resulting list of words; split at any whitespace if sep is None 
# (the default)

----------------------------------------------------------------------
s.splitlines([keepends]) -> list of strings
# return list of lines in s split at line boundaries

----------------------------------------------------------------------
s.startswith(prefix[, start[, end]]) -> bool
# True is s startswith prefix (can be a tuple of prefixes)

----------------------------------------------------------------------
s.strip([chars]) -> str
# return copy of s with leading + trailing whitespace removed, or with each
# character in start and end of s, if chars is not None

----------------------------------------------------------------------
s.swapcase() -> str
# return an case-inverted copy of s

----------------------------------------------------------------------
s.title() -> str
# return a titlecased copy of s

----------------------------------------------------------------------
s.translate(table) -> str
# return copy of s with all characters replaced according to
# ordinal-to-ordinal/string/None mapping replacement table 

----------------------------------------------------------------------
s.upper() -> str
# return an all-uppercase copy of s

----------------------------------------------------------------------
s.zfill(width) -> str
# return s right-justified and padded with zeros; never truncates
```

#### Tuples - `tuple`

A Python list is an immutable sequence of arbitrary objects:

``` python
>>> s = ('tuples', 'contain', 'objects', 42, 7.47, {'on': True, 'off': False},
>>> (-3, 0, 4), object())
>>> s1 = (1, 2, 3)
>>> s2 = (4.0, 5.0, 6.0)
>>> type(s)
<class 'tuple'>
>>> s[0]
'tuples'
>>> s[0:7]
('tuples', 'contain', 'objects', 42, 7.47, {'on': True, 'off': False}, (-3, 0,
4))
>>> s[0:7:2]
('tuples', 'objects', 7.47, (-3, 0, 4))
>>> len(s)
8
>>> min(s1)
1
>>> max(s2)
6.0
>>> s.index(42)
3
>>> s.index(42, 0, 3)  # will raise: 42 is not in this index range
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: tuple.index(x): x not in tuple
>>> s.count(42)
1
>>> 'objects' in s
True
>>> 'types' not in s
True
>>> s1 + s2
(1, 2, 3, 4.0, 5.0, 6.0)
>>> s1 * 2
(1, 2, 3, 1, 2, 3)
>>> 2 * s1
(1, 2, 3, 1, 2, 3)
>>>
```

### Mutable Sequences

#### Lists - `list`

A Python list is a mutable sequence of arbitrary objects.

Common sequence operations on lists:

``` python
>>> s = ['lists', 'contain', 'objects', 42, 7.47, {'on': True, 'off': False}, (-3,
0, 4), object()]
>>> s1 = [1, 2, 3]
>>> s2 = [4.0, 5.0, 6.0]
>>> s[0]
'lists'
>>> s[0:7]
['lists', 'contain', 'objects', 42, 7.47, {'on': True, 'off': False}, (-3, 0,
4)]
>>> s[0:7:2]
['lists', 'objects', 7.47, (-3, 0, 4)]
>>> len(s)
8
>>> min(s1)
1
>>> max(s2)
6.0
>>> s.index(42)
3
>>> s.index(42, 0, 3)  # will raise: 42 is not in this index range
Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
ValueError: 42 is not in list
>>> s.count(42)
1
>>> 'objects' in s
True
>>> 'types' not in s
True
>>> s1 + s2
[1, 2, 3, 4.0, 5.0, 6.0]
>>> s1 * 2
[1, 2, 3, 1, 2, 3]
>>> 2 * s1
[1, 2, 3, 1, 2, 3]
>>>
```

#### Additional Operations

``` python
# Length of sequence s denoted as N
s[i] = x              # set sequence s index i to x (replacing previous item)
s[i:j] = iterable     # replace slice of s from i to j with iterable contents
s[i:j:k] = iterable   # replace slice of s from i to j with step k with iterable contents
s += iterable         # extend sequence s with iterable contents
del s[i]              # remove item at i from s
del s[i:j]            # remove items from i to j
del s[i:j:k]          # remove items from i to j, step width k
del s[:]              # remove all items from s
s.clear()             # remove all items from s
s.copy()              # create a shallow copy of s
s.extend(iterable)    # extend sequence s with iterable contents
s.insert(i, x)        # insert x at index i (i.e. before item previously at i)
s.pop(i)              # remove item at i (default: -1, i.e. last item)
s.remove(x)           # remove the first item in s that equals x
s.reverse()           # reverse sequence items in-place
s.sort()              # sort list items in-place; opt. key function + reverse flag
```


Additional modifying list operations:

``` python
>>> s = ['lists', 'contain', 'objects', 42, 7.47, {'on': True, 'off': False},
>>> (-3, 0, 4), object()]
>>> s1 = [1, 2, 3]
>>> s2 = [4.0, 5.0, 6.0]
>>> s[0] = 'programs'
>>> print(s)
['programs', 'contain', 'objects', 42, 7.47, {'on': True, 'off': False}, (-3,
0, 4), <object object at 0x7f6b7657e0c0>]
>>> s.insert(2, 'lots of')
>>> print(s)
['programs', 'contain', 'lots of', 'objects', 42, 7.47, {'on': True, 'off':
False}, (-3, 0, 4), <object object at 0x7f6b7657e0c0>]
>>> s[4:5] = [1999, 2000, 2001]
>>> print(s)
['programs', 'contain', 'lots of', 'objects', 1999, 2000, 2001, 7.47, {'on':
True, 'off': False}, (-3, 0, 4), <object object at 0x7f6b7657e0c0>]
>>> s[5:-1] = ('a', 'b', 'c')
>>> print(s)
['programs', 'contain', 'lots of', 'objects', 1999, 'a', 'b', 'c', <object
object at 0x7f6b7657e0c0>]
>>> del s[0]
>>> print(s)
['contain', 'lots of', 'objects', 1999, 'a', 'b', 'c', <object object at
0x7f6b7657e0c0>]
>>> del s[2:3]
>>> print(s)
['contain', 'lots of', 1999, 'a', 'b', 'c', <object object at 0x7f6b7657e0c0>]
>>> del s[0:-1:2]
>>> print(s)
['lots of', 'a', 'c', <object object at 0x7f6b7657e0c0>]
>>> del s[:]       # same as s.clear()
>>> print(s)
[]
>>> print(s.copy())
[]
>>> s.extend(s1)
>>> print(s)
[1, 2, 3]
>>> s += s2
>>> print(s)
[1, 2, 3, 4.0, 5.0, 6.0]
>>> s.pop(0)
1
>>> print(s)
[2, 3, 4.0, 5.0, 6.0]
>>> s.remove(3)
>>> print(s)
[2, 4.0, 5.0, 6.0]
>>> s.reverse()
>>> print(s)
[6.0, 5.0, 4.0, 2]
>>>
```

**Hint:**
The Python standard library also provides an `array`-type where the objects are restricted to be of the same type, see
[Python Arrays](https://docs.python.org/3/library/array.html).


### Dictionaries - `dict`

Dictionaries are *mapping objects*: a collection of objects indexed by key
values.[^hashtable] Keys must be *hashable* objects which rules out
certain mutable objects (e.g. a `dict` or a `set` cannot act as a dictionary
key). 

[^hashtable]: Sometimes such objects are called "hash table" or "associative array".

Since Python 3.7[^dict-order] dictionary order is guaranteed to be insertion order, with
updating a key not affecting order.

Dictionaries support the following operations:

[^dict-order]:
    (C)Python 3.6 actually, but then an implementation detail rather than a
    language property.

``` python
# m is a dictionary (a "mapping")
len(m) -> int                         # number of items in m
m[k] -> object                        # value for key k in m; KeyError if no k
m[k] = v                              # set value v for key k in mapping
del m[k]                              # remove item with key k; KeyError if no k
k in m -> bool                        # True if k is key in m
m.clear() -> None                     # empty m i.e. remove all items
m.copy() -> dict                      # shallow copy of m
m.fromkeys(iterable, value=None)      # create dict with keys from iterable,
                                      # values set to value.
m.get(k, d=None) -> m[k]              # m[k] if k in m, else d. 
m.items() -> dict_items(m)            # iterable set-like object as a view on
                                      # m's items
m.keys() -> dict_keys(m)              # iterable set-like object as a view on
                                      # m's keys
m.pop(k, [, d]) -> m[k]               # remove key and return the corresponding
                                      # value; raise KeyError if k is not found
                                      # unless default d
m.popitem() -> (k, v)                 # remove and return (key, value) pair
                                      #(LIFO); KeyError if m is empty
m.setdefault(k [, d]) -> m.get(k, d)  # Return m[k] if k in d else set D[k] = d
                                      # and return d
m.update(b[, ]**kwargs)               # update m from dict/iterable (key,
                                      # value)-sequence b and kwargs 
m.values() -> dict_values(m)          # iterable object as a view on m's values

```

`dict` example

``` python
>>> {'name': 'Paul', 'age': 26, 'profession': 'author'}
{'name': 'Paul', 'age': 26, 'profession': 'author'}
>>> type({'name': 'Paul', 'age': 26, 'profession': 'author'})
<class 'dict'>
>>> 
```

***dictionary-lookup***

Accessing individual elements of a dictionary `m` is done using the dictionary key-indexing-operator `m.[key]`

``` python
>>> {'name': 'Paul', 'age': 26, 'profession': 'author'}['name']
'Paul'
>>> 
```

### Sets - `set`

The Python `set` is a datatype according to the mathematical set theory it therefore is a collection of unique unnamed objects, probably of different types, and a set-operations like `union`, `intersection` and others.

As opposed to the other Python builtin data types, `set`- type generation can only be done explicitly

`set`- types generation

``` python
>>> set([1,2, 'foo']) # explicit: 'set'- class constructor (1) using '[' ']' brackets
{1,2,'foo'}
>>> set((1,2,'foo'))  # explicit: 'set'- class constructor (2) using '(' ')' brackets
{1,2,'foo'}
```

`set`-example

``` python
>>> set([1, 2,'foo'])   # simple set with uniqe elements
{1, 2, 'foo'}
>>> type(set([1, 2,'foo'])) # type of set
<class 'set'>
>>> set([1, 2,'foo', 'foo'])  # simple set with a non-uniqe element (getting dropped)
{1, 2, 'foo'}
>>> type(set([1, 2,'foo', 'foo']))
<class 'set'>
>>> set([1, 2,'foo']) & set([1,2]) # intersection of 2 sets using '&'-operator
{1, 2}
>>> type(set([1, 2,'foo']) & set([1,2]))
<class 'set'>
>>> 
```
  

### None - `None`

The Python `None` type is referred to as the `Null`-Object. It has a builtin contstant named `None`

``` python
>>> None
>>> type(None)
<class 'NoneType'>
>>>
```

### Boolean `bool`

The Python `bool` type has a two builtin constants named `False` an `True`

``` python
>>> True
True
>>> type(True)
>>> <class 'bool'>
>>> 
```


