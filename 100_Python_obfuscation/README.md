# Obfuscation
## First-level obfuscation

First-level obfuscation solution, but it is built-in: Python has a compiler to byte-code:

```
python -OO -m py_compile <your program.py>
```

### Example

```
python3 -OO -m 'hello'
```

Result is the `.pyo`-file.
In __pycache__ - folder

### Call Byte code

```
cd test
python3 -O hello.cpython-38.opt-2.pyc
``` 
