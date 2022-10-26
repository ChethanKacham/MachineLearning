import numpy as np

# Creating the random vector of size 15 having only Integers in the range 1-20
arr = np.random.randint(1, 20, 15, dtype=int)
print("Original array:")
print(arr)
# Reshaping the array to 3 by 5
reshape_arr = arr.reshape(3, 5)
print("Reshaped array:")
print(reshape_arr)
# Printing the array shape
print("Array shape:")
print(reshape_arr.shape)
# Replacing the max in each row by zero
# Copying into the new array and then assigning the maximum value to zero in each row
new_arr = np.copy(reshape_arr)
new_arr[np.arange(len(reshape_arr)), np.argmax(reshape_arr, axis=1)] = 0
print("Updated array after replacing the max in each row by zero(First occurrence):")
print(new_arr)
# Another method for replacing the max in each row by zero using while loop
new_arr1 = np.where(reshape_arr == [
        [i]
        for i in np.amax(reshape_arr, axis=1)
    ], 0, reshape_arr)
print("Updated array after replacing the max in each row by zero(All occurrence):")
print(new_arr1)