'''Given an array, find a product of all array elements.

**Example 1:**

Input  : arr[] = {1, 2, 3, 4, 5}
Output : 120
**Example 2:**

Input  : arr[] = {1, 6, 3}
Output : 18'''

def product_of_array(arr):
    # Initialize the product as 1
    product = 1
    # Iterate through the array and multiply each element with the product
    for num in arr:
        product *= num
    # Return the final product
    return product

# Test the function with examples
arr1 = [1, 2, 3, 4, 5]
print(product_of_array(arr1)) 

arr2 = [1, 6, 3]
print(product_of_array(arr2))  
