name = 'Simeon'
amount = 2323232.232324

print("My name is {name}. I'm happy {when}. I've {amount} $ in my pocket".format(name = name, when = 'now', amount=amount))
print("     {} : {:.2f}".format(name, amount))

parts = "I am %s and I'm happy".split()
print("-".join(parts))


t = "12345678901234567890"
d = "90"

print(t[t.index(d):])
print(t[t.index(d) + len(d):])
