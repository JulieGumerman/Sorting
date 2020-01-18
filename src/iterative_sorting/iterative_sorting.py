# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements

            
    for i in range(1, len(arr)):
        #store smaller variable and current variable
        temporary = arr[i]
        small_guy = i
        #loop through to sort... if j is larger than 0 and you are not to the end of the list yet...
        while small_guy > 0 and temporary < arr[small_guy-1]:
            arr[small_guy] = arr[small_guy-1]
            small_guy -=1
        arr[small_guy] = temporary


        # TO-DO: swap
        #arr = new_arr




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr