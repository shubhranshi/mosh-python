def sqr_gen():
    i = 1
    while True:
        yield i*i
        i += 1


for num in sqr_gen():
    if num > 25:
        break
    print(num)



def fib_gen(limit):
    a,b = 0, 1
    while a<limit:
        yield a
        a, b = b, b+a


for i in fib_gen(5):
    print(i)


x = ['f','a','c','b']
print(sorted(x))

x = '033452336789'
print(x[-10:-5])

l = ['07895462130', '919875641230', '9195969878']
nl = [str('+91 ' + item[-10:-5] + ' ' + item[-5:]) for item in l]
print(nl)


def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


people = [['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']]
format_list = [name_format(person) for person in sorted(people, key=lambda person:person[2],)]

print(format_list)