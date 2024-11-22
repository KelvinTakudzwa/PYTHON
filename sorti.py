array = [1,0,0,2,1,2,1,0,0,3,5,1]
n = len(array)
def sortArray(array):
    filtered_array = filter(array[1]>1,array)
    #for all in range(i+1,n):
       # if i > 0 and i < 2 :
        #    sorted_array = sorted(array)
        #    return sorted_array
        
    return filtered_array

print(sortArray(array))
#print(filtered_array)
    