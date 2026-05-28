def number_pattern(n):

    if not isinstance(n,int):
        return "Argument must be an integer value."

    if n < 1 :
        return "Argument must be an integer greater than 0."

    tem_list=[]

    for i in range(1,n+1):
        tem_list.append(str(i))

    return " ".join(tem_list)

print(number_pattern(7))


     