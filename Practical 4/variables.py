a = 508
b = 533
c = 555

d = b - a
e = c - b

print("d =", d)
print("e =", e)
if e > d:
    print("population growth is accelerating.")
elif e < d:
    print("population growth is decelerating.")
elif e == d:
    print("population growth is constant.")
    
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