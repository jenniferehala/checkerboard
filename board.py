def make_checkerboard(x,y):
    result = []
    for i in range(0,x):
        temp = []
        for j in range(0,y):
            temp.append((i+j) % 2)
        result.append(temp)
    
    return result

chkbd_function= make_checkerboard(12,12)

for row in chkbd_function:
    print(row)

