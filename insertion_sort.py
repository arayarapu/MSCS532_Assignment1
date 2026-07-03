"""
MSCS532 - Assignment 1
Python program for the Insertion Sort Algorithm that sorts 
in monotonically decreasing order.
"""

def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

def main():
    numbers = [12, 5, 8, 19, 3, 15, 7, 1]

    print("Original List:")
    print(numbers)

    sorted_numbers = insertion_sort_desc(numbers.copy())

    print("\nSorted List (Monotonically Decreasing):")
    print(sorted_numbers)


if __name__ == "__main__":
    main()