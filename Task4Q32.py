def find_subarray_with_sum(arr, target_sum):
    start = 0
    current_sum = 0
    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > target_sum and start <= end:
            current_sum -= arr[start]
            start += 1
        if current_sum == target_sum:
            return (start, end)
    return -1

def main():
    arr = [1, 4, 20, 3, 10, 5]
    target_sum = 33
    result = find_subarray_with_sum(arr, target_sum)
    if result != -1:
        print(f"Subarray with sum {target_sum} found from index {result[0]} to {result[1]}")
    else:
        print(f"No subarray with sum {target_sum} found")

if __name__ == "__main__":
    main()
