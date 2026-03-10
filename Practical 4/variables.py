a = 508
b = 533
c = 555

d = b - a
e = c - b

print("d =", d)
print("e =", e)

# Population growth is decelerating because e is smaller than d.

X = True
Y = False
W = X or Y

print("W =", W)

# Truth table for W = X or Y
# X      Y      W
# True   True   True
# True   False  True
# False  True   True
# False  False  False