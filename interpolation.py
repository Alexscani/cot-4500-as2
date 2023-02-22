x = [3.6, 3.8, 3.9]
y = [1.675, 1.436, 1.318]

m = len(x)
n = m - 1 #this is the degree of the poly

xp = float(input("X = "))
yp = 0
for i in range (n+1):
    p = 1
    for j in range(n+1):
        if j != i:
            p*= (xp - x[j])/(x[i]-x[j])
    yp +=y[i]*p
print('for x = %.2f,y = %f'% (xp,yp))