for row2 in range(0,12):
    if row2%2==0:
        for column2 in range (1,8):
            if column2%2==1:
                print("--")
            else:
                print("||||")
    else:
        print("======")