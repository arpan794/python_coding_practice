# even odd numbers

# num = input("Input the Integer no.: ")

# if num.isdigit():    # check only +ve intregers
#     num = int(num)

#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# else:
#     print("Invalid Input")

# --------------------------------------------
    
num = input("Enter an integer: ") # check both +ve and -ve integers

if num.lstrip("+-").isdigit():
    num = int(num)

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Invalid Input")


# ----------------------------------------------

# try:
#     num = int(input("Input the Integer no.: "))

#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# except ValueError:
#     print("Please enter a valid integer.")



"""
### `lstrip()` in Short

`lstrip()` removes characters from the **left side (beginning)** of a string.

### Example

```python
num = "-123"

print(num.lstrip("-"))
```

Output:

```text
123
```

---

### Your Example

```python
num.lstrip("+-")
```

means:

> Remove `+` or `-` characters from the beginning of the string.

Examples:

```python
"-123".lstrip("+-")   # "123"
"+123".lstrip("+-")   # "123"
"123".lstrip("+-")    # "123"
```

Then:

```python
num.lstrip("+-").isdigit()
```

can correctly recognize:

```text
-123
+123
123
```

as valid integers.

### Quick Memory Trick

* `lstrip()` → remove from **left**
* `rstrip()` → remove from **right**
* `strip()` → remove from **both sides**

"""

"""
**Yes, but not in this case.**

```python
num.strip("+-")
```

removes `+` and `-` from **both ends** of the string.

Example:

```python
"-123".strip("+-")   # "123"
"+123".strip("+-")   # "123"
```

But it also does:

```python
"123-".strip("+-")   # "123"
```

which is **not a valid integer**.

For validating signed integers, use:

```python
num.lstrip("+-").isdigit()
```

because `+` or `-` are only allowed at the beginning.

"""