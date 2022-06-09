def mul(a):
    def helper(b):
        return a * b
    return helper
print (mul(4)(5))


# mul возвращает <function multi at XXXXXXXXXXX> и в это функцию мы передаем следующее значение 


tpl = lambda a, b: (a, b)

a = tpl(1, 2) # -- > a -- > (1, 2)

b = tpl(3, a) # -- > b -- > (3, (1, 2))

c = tpl(a, b) # -- > c -- > ((1, 2), (3, (1, 2))
