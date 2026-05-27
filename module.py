import random as r

print(r.random())
print(r.randint(1, 10))
print(r.randrange(1, 10))
print(r.randrange(2, 10, 2))

colors = ["Red", "Green", "Blue"]
print(r.choice(colors))
print(r.choices(colors, k=2))
print(r.sample(colors, k=2))

t = [1, 2, 3, 4, 5, 6]

r.shuffle(t)
print(t)

print(r.uniform(1.1, 2.2))
