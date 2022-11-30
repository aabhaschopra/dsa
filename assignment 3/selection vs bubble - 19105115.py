# Program to compare bubble sort and selection sort

def bubbleSort(arr):
    swaps_bubble_sort = 0
    comparisons_bubble_sort = 0
    n = len(arr)
    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                comparisons_bubble_sort = comparisons_bubble_sort+1
                swaps_bubble_sort = swaps_bubble_sort+1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return swaps_bubble_sort, comparisons_bubble_sort


def selectionSort(array):
    swaps_selection_sort = 0
    comparisons_selection_sort = 0
    size = len(array)

    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                comparisons_selection_sort = comparisons_selection_sort+1
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])
        swaps_selection_sort = swaps_selection_sort+1

    return swaps_selection_sort, comparisons_selection_sort


n = int(input("Enter the number of elements in the array: "))
arr1 = []
arr2 = []

for i in range(0, n):
    element = input("Enter " + str(i) + " index element\n")
    arr1.append(int(element))
    arr2.append(int(element))

swaps_bubble_sort, comparisons_bubble_sort = bubbleSort(arr1)
swaps_selection_sort, comparisons_selection_sort = selectionSort(arr2)

print("Bubble Sort Result: \n")
for i in range(n):
    print("%d" % arr1[i], end=" ")

print("\nswaps in bubble sort " + str(swaps_bubble_sort))
print("comparisons in bubble sort " + str(comparisons_bubble_sort))


print("\nSelection Sort Result : \n")
for i in range(n):
    print("%d" % arr2[i], end=" ")

print("\nswaps in selection sort " + str(swaps_selection_sort))
print("comparisons in selection sort " + str(comparisons_selection_sort))