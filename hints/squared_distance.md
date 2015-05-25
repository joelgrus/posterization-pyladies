the simplest thing to do is to use a `for` loop. 

you can use `range(len(p))` to get the indexes.

if you want to be slightly slicker, you can use `zip`.

`zip(p, q)` is the list of pairs `(p[0], q[0])`, `(p[1], q[1])` and so on.

if you want to be very slick, you can do it in one line with `sum` and a list comprehension.