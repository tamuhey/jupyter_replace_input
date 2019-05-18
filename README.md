# jupyter_replace_input

magic command to replace `input` to output the contents in cell line by line

## Installation

```
$ pip3 install git+git://github.com/tamuhey/jupyter-replace-input.git
```

## Usage

1. Load this extension

```python
%load_ext replace_input
```

2. Replace input

```python
%%replace_input
foo
bar
```

3. Use input

```python
print("1: ", input())
print("2: ", input())
```

```
1: foo
2: bar
```

4. The content of the cell is exhausted, raise `StopIteration`

```python
print("3: ", input())
```

```
StopIteration:
```
