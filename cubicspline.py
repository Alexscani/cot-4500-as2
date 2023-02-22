from scipy import interpolate
def f(x):
    x_Points = [ 2, 5, 8, 10]
    y_Points = [ 3, 5, 7, 9]
    tck = interpolate.splrep(x_Points, y_Points)
    return interpolate.splev(x, tck)

print(f(1.2))