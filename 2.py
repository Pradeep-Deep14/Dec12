def foo(x=[]):
    x.append(1)
    return x

print(foo())
print(foo())

#[1]
#[1, 1]