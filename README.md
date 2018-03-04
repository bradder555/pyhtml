# pyhtml
Simple functional python HTML templating DSL

## performance
Running benchmarks 100 times each...
pyhtml template            45.13 ms

Django template           269.48 ms

Django template autoescaped           271.02 ms

Jinja2 template            11.14 ms

Jinja2 template autoescaped            31.68 ms

Mako template             8.00 ms

Mako template autoescaped            23.65 ms

Python string template            50.64 ms

Python list concatenation             5.94 ms

*6x faster than django!!*

The codebase is very rough at the moment, but I have a simple working proof of concept.

The entire page is a function that consists of a series of nested functions or lists of functions.

Calling the function will render the page, (or just calling render(tree_of_functions))

It's trivial to write blocks or sections, which can then be incorporated into the main render. (i.e. sub_block_demo)

Since everything is a function, it's easy to write (iter(dict) --> table), so good scope for code reuse.

I think there's a lot of room for improvement, i wonder if i may have gone overboard with the lambdas, or if there's some 
more terse ways of representing what i want.

Very keen to hear any feedback anyone might have.

For usage, see main.py...

Should be trivial to incorporate into various python frameworks.


## colaborators welcome

