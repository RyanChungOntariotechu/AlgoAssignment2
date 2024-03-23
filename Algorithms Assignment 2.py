from playsound import playsound
import time
n=1
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    #Dividing Array into two
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    #Recursive sort the left and right halves
    merge_sort(left_half)
    merge_sort(right_half)

    #Merge sorted halves back into the original array
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
            playsound("laser-gun-81720.mp3")  # Ensure swap_sound.mp3 exists in your working directory
        k += 1
        # Sound effect for swap
    
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    print("Current Array Sorted :", arr)  # Print each step of sorting

# Test the merge_sort function
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
print("Original array:", arr)
merge_sort(arr)
print("Sorted array:", arr)


