# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    # for i in range(0, len(arr) - 1):
        # cur_index = i
        # smallest_index = cur_index
        # # TO-DO: find next smallest element
        # # (hint, can do in 3 loc) 
        # new_arr = []
        # if arr[i] > arr[i + 1]:
        #     new_arr.append(arr[i])
            
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -=1
        arr[j] = temp


        # TO-DO: swap
        #arr = new_arr




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr