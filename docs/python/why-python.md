# Why should I learn (+ use) Python?

## It's easy to use

Use the power of the [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) and try away:

``` python
>>> print('Python is easy to learn')
Python is easy to learn
```

Get built-in help:

``` python
>>> help()

Welcome to Python 3.6's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.6/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 
```

**Scale** from simple, one-off scripts or even command line one-liners to
**world-class applications**:

``` python
python -c 'import math; print(math.sqrt(2))'
1.4142135623730951
```

Amongst many others, Dropbox, Google, Instagram, Spotify and YouTube [have been
known to run parts of their stack with Python](https://codeinstitute.net/blog/7-popular-software-programs-written-in-python/),
sometimes *primarily* using Python.

Python also played an important role in [getting the 1st ever black hole
image](https://www.blog.pythonlibrary.org/2019/04/11/python-used-to-take-photo-of-black-hole/)
in 2019 and [NASA's 2021 Mars
mission](https://discuss.python.org/t/python-is-running-on-mars/8312/1).


## It has many applications

Python is

 - useful in many domains, from simple scripts to building web applications to
   image processing, number crunching and data science (and many many more)
 - an excellent "glue language":
     - easy integration of C/C++ code (or Rust, Go, Fortran, ...)
 - a great rapid prototyping language:
     - succinct
     - no lengthy compilation
     - a lot of "batteries included" (i.e. extensive standard library)
 - extensible, i.e. in the need for speed you can write performance critical
   code as e.g. a C extension (but more often than not Python is just fast 
   enough, anyway)
  
 
## It has excellent documentation & a great community

Simply take at look at https://docs.python.org/ and
https://www.python.org/community/.


## It is widely used & usage is growing rapidly

- Currently the fastest growing / dominant language? Python
    - ranks no. 1 on the [TIOBE Index](https://www.tiobe.com/tiobe-index/)
      (08/2023)
    - ranks no. 1 on the [PYPL PopularitY of Programming Language](http://pypl.github.io/PYPL.html) index (09/2023)
    - ranks no. 2 (behind JavaScript) on the [Redmonk Programming Language Rankings](https://redmonk.com/sogrady/2023/05/16/language-rankings-1-23/) (01/2023)
    - ranks no. 2 (behind JavaScript) in the [GitHub octoverse report top languages](https://octoverse.github.com/2022/top-programming-languages) (2022)
- huge uptake since around 2012-2014 in the scientific community and data
  science:
    - machine learning
    - AI
    - statistical computing
- known to e.g. replace R and Matlab applications due to being
    - user friendly and easy to learn,
    - more flexible, extensible & general-purpose (i.e. apart from the data
      science-specific necessities the huge Python ecosystem of standard
      library and 3rd party libraries is at your hands)
    - used by a large and growing community
- may soon be the primary language of choice in the data science field (if it
  isn't already)


## It is (arguably) the most readable programming language (for many)
(Take this with more than a grain of salt - beauty is all in the eye of the
beholder :wink:)

Readability is key:

 - source code is read *way* more often than written (as in: reading other
   people's code for learning or review, reading your own code for 
   refactoring/debugging/understanding what you did last month, ...)
 - Python is "executable pseudocode" (to some):
        ``` python
        # pseudocode
        x := 1
        IF x > 0 THEN
            print "positive" 
        ELSE
            print "negative or 0" 
        END IF


        # python
        x = 1
        if x > 0:
            print("positive")
        else:
            print("negative or 0")
        ```
 - Python uses significant whitespace (indentation) for grouping code blocks
   (rather than {} braces), which makes it very readable for most 
   people[^python-whitespace]

[^python-whitespace]: Though there's die-hard non-believers that will always hate this :wink:


### Some "Hello, world!" examples

To each their own...

=== "Python"
    ``` python
    print("Hello, world!")
    ```

=== "C"
    ``` c
    #include <stdio.h>
    int main(void)
    {
        printf("Hello, world!\n");
        return 0;
    }
    ```

=== "C++"
    ``` c++
    #include <iostream>
    int main(void)
    {
        std::cout << "Hello, world!" << std::endl;
        return 0;
    }
    ```

=== "Java"
    ``` java
    class Hello {
        public static void main(String[] args) {
            System.out.print("Hello, world!");
        }
    }
    ```

=== "Go"
    ``` go
    package main
    import "fmt"
    func main() {
        fmt.Println("Hello, world!")
    }
    ```
=== "Rust"
    ``` rust
    fn main() {
      println!("Hello, world");
    }
    ```
