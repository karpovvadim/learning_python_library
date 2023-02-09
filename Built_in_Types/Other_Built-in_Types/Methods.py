class C:
    def method(self):
        pass


c = C()
try:
    c.method.whoami = 'my name is method'  # can't set on the method
except AttributeError:
    print("AttributeError: 'method' object has no attribute 'whoami'")

c.method.__func__.whoami = 'my name is method'

print(c.method.whoami)
