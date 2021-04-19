# Module 2 Quiz

**What gets printed?**

```python
xs = [1,2,3]
xs.append(7)
print(sum(xs))
```

1. [ ] It's impossible to know.
1. [ X ] 13
1. [ ] Something else.

**In the Python statement x = a + 5 - b:**

- a and b are ________
- a + 5 - b is ________

1. [ X ] operands, an expression
1. [ ] terms, a group
1. [ ] operands, an equation
1. [ ] operators, a statement

**What is the value of the expression 100 / 25?

1. [ ] 4
1. [ X ] 4.0

**You should use the == operator to determine whether objects of type float are equal.**

1. [ ] True
1. [ X ] False

```python
1.1 + 2.2 == 3.3
```

**what is the value of y after these lines of code are executed?**

```python
x = 10.0
y = (x < 100.0) and isinstance(x, float)
```

1. [ ] None
1. [ X ] True
1. [ ] Correct
1. [ ] 1
1. [ ] 0
1. [ ] False

**Which of the following are truthy:**

1. [X ] 0.000001
1. [ ] 0
1. [ ] []
1. [ ] True
1. [ ] 'None'
1. [ ] False

**What is the value of the expression a and b?:**

```python
a = 100
b = 200
```

1. [ ] 0
1. [ X ] 200
1. [ ] 100
1. [ ] False
1. [ ] True

**Will the highlighted line of code raise an exception?**

```python
x = -100
from math import sqrt
x > 0 and sqrt(x)
```
1. [ ] Yes
1. [ X ] No

**Which of the following operators has the lowest precedence?**

1. [ X ] and
1. [ ] not
1. [ ] %
1. [ ] +
1. [ ] **

**What is the value of the expression 1 + 2 ** 3 * 4?**

1. [ X  ] 33
1. [ ] 36
1. [ ] 108
1. [ ] 4097

**The following statements return the same value:**

```python
x = 100

x *= 5
x = x * 5
```

1. [ X ] True ** considering that both statements are not used in the same program one after the other else the first x returns 500, the second one returns 2500. The statements are equivalent one or the other can be used
1. [ ] False

**The Python Enhancement Proposal (PEP) that enumerates stylistic guidelines for Python code is:**

1. [ ] PEP 8000
1. [ X ] PEP 8
1. [ ] PEP 257
1. [ ] PEP 20


**The following code will run successfully without error:**

```python
x, y = 1, 2
    z = 3

print(x, y, z)
```
1. [ ] True
1. [ X ] False

**Variables must be declared before they are assigned a value.**

1. [ ] True
1. [ X ] False

**Variables may be assigned a value of one type, and after be assigned a value of a different type.**

1. [ X ] True
1. [ ] False

**How many objects and how many references are created by this program?**

x = 100
y = x

1. [ ] One object, one reference
1. [ ] Two objects, one reference
1. [ X ] Two objects, two references
1. [  ] One object, two references

**PEP8 recommend which of the following styles for multi-word variable names:**

1. [ ] customerFirstName (Camel Case)
1. [ ] CustomerFirstName (Pascal Case)
1. [ X ] customer_first_name (Snake Case)
1. [ ] customer-first-name (Kebab Case)