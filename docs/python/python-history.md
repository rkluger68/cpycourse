# A (very) brief selective history of Python

Python was [first published in February 1991](https://raw.githubusercontent.com/python/cpython/master/Misc/HISTORY) by Dutch programmer [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum).

From the get-go Python

 - had a focus on clean syntax,
 - emphasized readability and
 - was designed to be extensible.

Early versions already show many of the core Python capabilities available in
modern Python. In fact, looking at code [running on really ancient Python
doesn't actually feel very different](
http://www.dalkescientific.com/writings/diary/archive/2009/03/27/python_0_9_1p1.html) :smiley:.

With its permissive F(L)OSS license and Guido turning out to be a highly
competent Python community lead - lovingly and jokingly dubbed the
["Benevolent dictator for life" (BDFL)](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life), a role from which he stepped down in 2018 - Python found
evolutionary language development, steady growth and application in very many
domains.

Since around 2012-2014 Python gained massive adoption in the scientific and 
data analytics world, boosting its popularity to [unprecedented heights](why-python.md#it-is-widely-used-usage-is-growing-rapidly).

For some historical perspective, here's the first public releases of other popular programming languages:

 - [C](https://en.wikipedia.org/wiki/C_(programming_language)): 1972
 - [C++](https://en.wikipedia.org/wiki/The_C%2B%2B_Programming_Language): 1985
 - [JavaScript](https://en.wikipedia.org/wiki/JavaScript): 1995
 - [Java](https://web.archive.org/web/20070310235103/http://www.sun.com/smi/Press/sunflash/1996-01/sunflash.960123.10561.xml): 1996
 - [Go](https://en.wikipedia.org/wiki/Go_(programming_language)): 2009
 - [Rust](https://en.wikipedia.org/wiki/Rust_(programming_language)): 2010


## Some subjectively selected Python milestones

### Python 0.9.0 (1991)
1st public release ever, already with classes, exception handling, functions,
basic types, modules.

### Python 1.0.0 (1994)
Python reaches 1.0! Selected highlights: double quotes allowed for strings as well as single quotes, `lambda` anonymous functions, `map()`, `filter()`, `reduce()` functions for functional programming support, range objects.

### Zope (1998)
Open source web application and content manager framework. Pioneers web object
publishing and object database.

### Python 1.5.2 (1999)
Fondly remembered by some author(s) as their 1st ever personally used Python version. Extremely stable run in production for many years. :smiley:

### Python 1.6 (2000)
Unicode support: new unicode datatype.

### Python 2.0 (2000)
["Python Enhancements Proposal" (PEP)](https://www.python.org/dev/peps/pep-0001/)
process established, list comprehensions. 

### Python 2.2 (2001)
Unification of types (written in C) and classes (written in Python), "new style
classes", generators.

### NumPy 1.0 (2006)
Python library for multi-dimensional array and matrix calculations. Previously
Numeric, part/basis of [SciPy](https://en.wikipedia.org/wiki/SciPy).

### Python 2.7 (2010)
The last Python 2 minor release line.

### Python 3.0 (2008)
Aka "Python 3000" or "Py3k": Backward compatibility-breaking new major version:
`print` is now a function, all text strings are unicode objects, function
annotations (and many many more changes).

### Anaconda 0.8.0 (2012)
Data science Python distribution, package & environment manager.

### Python 3.3 (2012)
Python 3.3 restores the u'unicode string' syntax which makes the Python 2 to
Python 3 transition way easier than before.

### Python 3.5 (2015)
Greatly improved async programming, now with syntactic support. Also, [type
hints](https://docs.python.org/3/whatsnew/3.5.html#pep-484-type-hints) and
[matrix multiplication
operator](https://docs.python.org/3/whatsnew/3.5.html#pep-465-a-dedicated-infix-operator-for-matrix-multiplication).

### Guido steps down as Python BDFL (2018)
After having the final Python design responsibility and say-so since 1991 Guido
van Rossum decides to step down from his BDFL role.

The Python core developer community decides to establish a steering council of
annually elected core developers to take over the [language
governance](https://peps.python.org/pep-0013/) powers and duties.

### Python 2.7.18 (2020)
The last release of Python 2.

### Faster CPython (2021)
Python inventor and BDFL emeritus Guido van Rossum gets tired of retirement and
joins Microsoft to push the ["Faster CPython"
project](https://github.com/faster-cpython/ideas/blob/main/FasterCPythonDark.pdf),
together with other expert contributors.

### Python 3.11.5 (2023)
The latest and greatest Python (at the time of writing).

Python 3.11 can be [up to 10-60% faster than Python 3.10, with an average
1.22x speedup in the standard benchmark
suite()](https://www.python.org/downloads/release/python-3115/).
