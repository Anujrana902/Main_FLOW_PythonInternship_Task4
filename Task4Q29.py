def is_pythagorean_triplet(a, b, c):
    nums = sorted([a, b, c])
    return nums[0]**2 + nums[1]**2 == nums[2]**2

def main():
    print("3, 4, 5 is triplet:", is_pythagorean_triplet(3, 4, 5))
    print("5, 6, 7 is triplet:", is_pythagorean_triplet(5, 6, 7))

if __name__ == "__main__":
    main()
