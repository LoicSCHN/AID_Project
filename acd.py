import matplotlib.pyplot as plt

def generator(arr, x):
    print(arr)
    z = []
    for i in range (0,x):
        z.append(0)
        i += 1
    i = 0
    for i in range (0,x):
        k = arr[i]
        z[k] += 1
        i += 1
    return (z)


def grapher(k, l, n): 
    y = k
    z = l
    i = 0
    x = []
    while (i< n):
        x.append(i)
        i += 1
    print(x)
    print(y)
    print(z)
    plt.plot(x, y, label = "students")
    plt.plot(x, z, label = "universities")
    plt.ylabel ("amount")
    plt.xlabel("satisfaction level")
    plt.legend()
    plt.show()
    
   
        




arr = [10,9,9,10,5,6,7,8,9,10,9] 
arr2 = [5,8,8,8,8,9,10,3,1,2,5]
#k = generator(arr, 11)
#l = generator(arr2, 11)
grapher(generator(arr,11), generator(arr2, 11), 11)
# mittel satisfaction berechnen??? 