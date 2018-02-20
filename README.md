# pyhtml
Simple functional python HTML templating DSL

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

I would like to run some benchmarking tests between this and other templating engines. 
Since it relies entirely on python's parser and AST, i suspect the performance should be very good. -- some future work.

## colaborators welcome

