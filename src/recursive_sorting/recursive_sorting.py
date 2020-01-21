#divide and conquer!!!!!



# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    for i in arr:
        if i % 2 == 0:
            temp = arr[i]
            temp_two = arr[i + 1]
            new_arr = []
            new_arr.append(temp)
            new_arr.append(temp_two)
            new_arr.sort()
            arr.append(new_arr)
            arr.remove(temp)
            arr.remove(temp_two)
            
 

    
    #split array into a bunch of tiny arrays with two apiece
    #put those two-number arrays in order
    #merge into four; sort
    #merge; sort one last time

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
