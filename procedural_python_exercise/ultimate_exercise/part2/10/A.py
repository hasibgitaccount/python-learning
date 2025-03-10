# A. Implement the bubble sort and selection sort algorithms.
# an algorithm is just a set of steps to solve a problem.
def bubble_sort(x1):

    n = len(x1)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if x1[j] > x1[j+1]:
                x1[j], x1[j+1] = x1[j+1],x1[j]
                swapped = True
            
        if not swapped:
            break
    return x1

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Bubble Sort Result:", bubble_sort(numbers.copy()))

def selection_sort(x1):
    n = len(x1)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if x1[j] < x1[min_index]:
                min_index = j

        x1[i], x1[min_index] = x1[min_index], x1[i] 
    
    return x1

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Selection Sort Result:", selection_sort(numbers.copy()))