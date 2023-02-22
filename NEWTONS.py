def a_cal (a, n):
    temp = a;
    for i in range(1, n):
        temp = temp * (a - i);
    return temp;
def fac(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;

n = 4; 
y = [[0 for i in range(n)]
        for j in range(n)];
        
        # CHANGE F(X) VALUES HERE
y[0][0] = 23.5492;
y[1][0] = 25.3913;
y[2][0] = 26.8224;
y[3][0] = 27.4589;

x = [ 7.2, 7.4, 7.5, 7.6 ]; # CHANGE X VALUES HERE
  
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
for i in range(n):
    print(x[i], end = "\t");
    for j in range(n - i):
        print(y[i][j], end = "\t");
    print("");