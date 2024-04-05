output_a = "{:+d}".format(52)
a = 0
b = [i for i in range(10)]

for i in range(10):
    print("{}".format(b))


print("{:+05d}".format(50))
print("{:+05d}".format(5))
print("{:-05d}".format(-5))

a = 3.76
g = "{:g}".format(a)
print(type(g),g)

plus = '+'
print(plus.isidentifier())