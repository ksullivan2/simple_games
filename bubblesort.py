def bubblesort(my_list):
    did_something = False
    for index in range(len(my_list)-1):
        if my_list[index] < my_list[index+1]:
            my_list[index], my_list[index+1] = my_list[index+1] , my_list[index]
            did_something = True
            print(my_list)
    if did_something == True:
        bubblesort(my_list)
    


my_list = [3,1,7,5,2]
bubblesort(my_list)

