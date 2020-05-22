# Teacher

This module is just a POC on how we could help newcomers better understand
some exceptions.

This is just a POC, a full implementation is done by André Roberge at
https://github.com/aroberge/friendly-traceback.


## Demo

Importing `teacher` in an REPL or at the top of a file enable it, like:

```python
import teacher

a = "Foo"
b = "Bar"

print(a * "bar")
```

Gives:
```bash
$ python test.py
test.py:6: TypeError: can't multiply sequence by non-int of type 'str'
You tried to multiply a by 'bar'
which is not allowed, the sequence a can only be multiplied by an integer.
```
