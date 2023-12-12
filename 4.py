def outer_func(x):
    def innet_func():
        return x
    x-=2
    return innet_func()

ans=outer_func(5)
print(ans)

#3