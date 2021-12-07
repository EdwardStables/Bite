# BITE

A Python library for intuitively working with numbers interactively in a way that's useful for computer engineers, programmers, and digital electronics.

This is meant to act like a fancy calculator. Don't try to use it for larger projects. Many of the design decisions made are to make it easy to use interactively, and will come back to bite you if you try to use it in 'proper' software. It is also not very fast.

## `Num` - Creating and Accessing

The main type in BITE is a `Num`. You can give Num an integer, or a string with a base. 

```python
>>> Num(63)
63
>>> Num(0x3f)
63
>>> Num("12", base=3)
18
```

You can access the main representations of a `Num` (binary, octal, decimal, or hex) as a string with the members:
```python
>>> n = Num(63)
>>> n.bin
'0b111111'
>>> n.oct
'0o77'
>>> n.dec
'0d63'
>>> n.hex
'0x3f'
```

And the value of `Num` with `Num.num`, or just by printing the variable itself.
```python
>>> n = Num(12)
>>> n.num
12
>>> n
12
```

You can set the width of `Num` with the `size` argument. This will change the representation of `Num` from `Num.bin`, `Num.oct`,`Num.dec`,`Num.hex` with left-padding 0s to the maximum length. If width is smaller than the value given to `Num` then the value will be truncated to fit in width.

```python
# Padding
>>> n = Num(3, size=4)
>>> n
3
>>> n.dec
'0d03'
>>> n.bin
'0b0011'
>>> n.hex
'0x3'

# Truncation
>>> m = Num(13, size=3)
>>> m
5
>>> m.bin
'b101'
```

You can index into the bits of `Num` with python index notation. **Note:** as of right now, this works with `[big:little]` indexing, and will extract bits from left to right:

```python
>>> n = Num(121)
>>> n.bin
'0b1111001'
>>> n[5:1]
'11100'
```

## Operators on `Num` (currently WIP)

`Num`s will support the operators you'd expect: add, sub, LLS, LRS, and, or, xor, and not. Additionally you will be able to do an arithmetic right shift with the `Num.asr()` function. 

As of writing, Nums support addition and subtraction, as well as logic left and right shifts.


