import matplotlib.pyplot as plt

fun_list1 = []
for i in range(5):
    def fun1(e):
        return e+i
    fun_list1.append(fun1)

    # late binding x = 3
    # x = x * x
    # here we using late binding \
    # we use late binding when we never want e value in next requirment

fun_list2 =[]
for i in range(5):
    def fun2(e, iv=i):
        return e+iv
    # early binding  x = 3
    # print (x) here we use early binding
    # we use here early binding  store value of i in iv to use it again in next use

    fun_list2.append(fun2)

fun_list3 = [lambda e: e + i for i in range(5)]
fun_list4 = [lambda e, iv=i: e+iv for i in range(5)]

print("#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ###")

print(fun_list1,fun_list3)

print("#### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ###")

i = 56


def myrange(start, stop, step=1):
    """Enumerates the values from start in steps of size step that are less then stop."""
    assert step > 0, "Only positve implemented in myrange"
    i = start
    while i < stop:
        yield i
        i += step

print("my range(2, 30, 3):", list(myrange(2, 30, 3)))


def ga(n):
    """Generate square of even non-negative integer less than n"""
    for e in range(n):
        if e % 2 == 0:
            yield e * e


a = ga(20)


def myenumerate(enum):
    for i in range(len(enum)):
        yield i, enum[i]


def myplot(min, max, step, fun1, fun2):
    plt.ion()  # Make it interactive
    plt.xlabel("The x axis.")
    plt.ylabel("The y axis.")
    plt.xscale('Linear')  # Makes a 'log' or 'linear' scale
    xvalues = range(min, max, step)
    plt.plot(xvalues, [fun1(x) for x in xvalues], label=fun2._doc_)  # Use the doc string of the function
    plt.legend(loc="upper right")  # Display the legend.


def slin(x):
    """y = 2x+7"""
    return 2*x+7


def sqfun(x):
    """y = (x-40) ^ 2/10-20"""
    return (x-40) ** 2 / 10-20

#
# def myenumerate(enum):
#     for i in range(len(enum)):
#         yield i,enum[i]
#
# import matplotlib.pyplot as plt
# def myplot(min, max, step,fun1,fun2):
#     plt.ion() ## make it intreactivre
#     plt.xlabel(" Thge  x axis")
#     plt.xlabel("The y axis")
#     plt.xscale("linear") ## makes a 'log' or linear scale
# xvalues = range(min,max,step)
# plt.plot(xvalues,[fun1(x)] for x in xvalues, label =" The first fun")
# plt.plot(xvalues,[fun2(x) for x in xvalues], linestyle = '---' , color = "k", label = fun2.__doc__)
# ## use the doc string of the function
# plt.legend(loc="upper right")
# ## display the legend
#
# def slin(x):
#     """ param x: y = 2x + 7"""
#     return 2*x+7
# def sqfun(x):
#     """ y=(x - 40) ^ 2/ 10 -20"""
#     return (x-40)** 2/10-20