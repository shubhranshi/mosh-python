# finding duplicate characters in a string (3 different approaches)

def find_dup(string1):
    l = []
    for x in string1:
        if string1.count(x) > 1 and x not in l:
            l.append(x)
    print(' '.join(l))

    m = [x for x in string1 if string1.count(x) > 1]
    m = set(m)
    print(' '.join(m))

    n = filter(lambda x: string1.count(x) > 1, string1)
    n = set(n)
    print(' '.join(n))


string1 = 'geeks for geeks'

find_dup(string1)