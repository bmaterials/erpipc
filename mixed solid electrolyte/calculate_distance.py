

###计算两点距离
def calculate_distance(a, b):
    if len(a) == len(b) == 3:
        dis = pow((((float(a[0]) - float(b[0]))/2) ** 2 +
                   ((float(a[1]) - float(b[1]))/2) ** 2 +
                   ((float(a[2]) - float(b[2]))/2) ** 2), 0.5)
    elif len(a) == len(b) == 2:
        dis = pow((((float(a[0]) - float(b[0]))/2) ** 2 + ((float(a[1]) - float(b[1]))/2) ** 2), 0.5)
    else:
        print("size  wrong")
    return dis