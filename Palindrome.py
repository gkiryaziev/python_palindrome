def ispalindrome(num):
    return num == num[::-1]

fin = 0

for n in range(0, 1000):
    for i in range(0, 1000):
        res = n * i
        if ispalindrome(str(res)):
            if res > fin:
                fin = res
                print("{0} * {1} = {2}".format(n, i, fin))
input()
