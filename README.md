# Coroutine implemented using Generator in Python

This code is just a playful attempt at implementing coroutine with generator in Python.

According to [wikipedia](https://en.wikipedia.org/wiki/Coroutine),

>Generators, also known as semicoroutines,are a subset of coroutines. Specifically, while both can yield multiple times, suspending their execution and allowing re-entry at multiple entry points, they differ in coroutines' ability to control where execution continues immediately after they yield, while generators cannot, instead transferring control back to the generator's caller. That is, since generators are primarily used to simplify the writing of iterators, the yield statement in a generator does not specify a coroutine to jump to, but rather passes a value back to a parent routine.

>However, it is still possible to implement coroutines on top of a generator facility, with the aid of a top-level dispatcher routine (a trampoline, essentially) that passes control explicitly to child generators identified by tokens passed back from the generators

This code intended to explore just that.
