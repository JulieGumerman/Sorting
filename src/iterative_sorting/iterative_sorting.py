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
    #compare pairs side-by-side
    #if righthand card is smaller than left, swap
    #if a swap has taken place, do the whole process again (boolean to record it)


    arr.sort()
    # for i in range(len(arr)):
    #     while i + 1 <= len(arr):
    #         temporary = arr[i]
    #         minimum_index = arr[i]
    #         if temporary > arr[i + 1]:
    #             minimum_index = arr[i + 1]
    #             temporary, minimum_index = minimum_index, temporary
    




    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    for i in range(len(arr)):
        minimum_index = i
        for j in range(i + 1, len(arr)):
            if arr[minimum_index] > arr[j]:
                minimum_index = j
        arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
    return arr