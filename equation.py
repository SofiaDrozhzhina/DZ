def equation(a, b):
    x1_str, y1_str = a.split(';')
    x2_str, y2_str = b.split(';')
    x1 = float(x1_str)
    y1 = float(y1_str)
    x2 = float(x2_str)
    y2 = float(y2_str)
    if x1 == x2:
        print(x1)
        return
    if y1 == y2:
        print(y1)
        return
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    print(k, b)

