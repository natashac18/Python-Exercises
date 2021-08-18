def fizz_buzz(max):
    li1 = list(range(0,(max+1)))
    li2 = [] 

    for item in li1:

        div4 = item%4
        div6 = item%6

        if div4==0 and div6==0:
            pass
        elif div4==0 or div6==0:
            li2.append(item)

    print(li2)
            

fizz_buzz(10)