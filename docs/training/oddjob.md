# Oddjob - Oddities, Stumbling Blocks & "Warts"

## Mutable Function Arguments
This is something that bytes practically all Python developers at least once in
their ventures.

A not too ingeniouse example for this (as you obviously wouldn't really need
that function in the first place) that illustrates the behaviour:

``` python
>>> def append(elem, sequence=[]):
...     """Append elem to sequence and return the sequence.
...     """
...     sequence.append(elem)
...     return sequence
>>> append(1)
[1]
>>> append(2)
[1, 2]
>>> append(3)
[1, 2, 3]
>>> 
```

Note how the mutable default `sequence=[]` list argument is created at
*function definition time*, not each time the function gets called.

This can be counter-intuitive at the beginning but isn't really difficult to
grasp. It can be annoying (linters actually often warn you if you do s.th.
like it in a function definition) but it can also be (ab)used as a feature
in cornercases, for keeping a certain state.


To steer clear of unexpected results, mutable default arguments are usually
best avoided. This can be done e.g. like so:

``` python
>>> def append(elem, sequence=None):
...     """Append elem to sequence and return the sequence.
...     """
...     sequence = [] if sequence is None else sequence
...     sequence.append(elem)
...     return sequence
>>> 
```


