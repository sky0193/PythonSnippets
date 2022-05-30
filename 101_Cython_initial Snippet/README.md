# Cython example of multiple pyx files 

Example from https://gist.github.com/kigawas/cc4f84cb8c51a0fa92448e85da603d7b

## Run: 

```
python3 setup.py build_ext --inplace
```

## Test 

- Move `*.so` to Testing-folder 
- The folder structure will look like

```
├── a.pyx
├── b.pyx
├── README.md
├── setup.py
└── Testing
    ├── a.cpython-38-x86_64-linux-gnu.so
    ├── b.cpython-38-x86_64-linux-gnu.so
    └── Testing.py
```

- Run

```
cd Testing
python3 Testing.py
```
