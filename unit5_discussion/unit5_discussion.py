"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
- Search the list from beginning to end.

- Return the index if the target is found.

- Return -1 if the target is not found.

- Add comments explaining why linear search

      has O(n) time complexity.
    """
    # Linear search has O(n) time complexity because in the worst-case scenario
    # it must inspect every single element sequentially from start to finish.
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
- Assume the list is already sorted.

- Repeatedly reduce the search space by half.

- Return the index if the target is found.

- Return -1 if the target is not found.

- Add comments explaining how each iteration

      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        # Each iteration cuts the active search window in half by checking the middle element (O(log n))
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_dataset = [4, 12, 28, 45, 63]
    print(f"Dataset: {small_dataset}")

    # Testing existing value (28)
    print("Searching for 28 (exists):")
    print(f"Linear Search Index: {linear_search(small_dataset, 28)}")
    print(f"Binary Search Index: {binary_search(small_dataset, 28)}")

    # Testing missing value (30)
    print("Searching for 30 (does not exist):")
    print(f"Linear Search Index: {linear_search(small_dataset, 30)}")
    print(f"Binary Search Index: {binary_search(small_dataset, 30)}")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large_dataset = list(range(1000))
    target_value = 725
    print(f"Searching for {target_value} in {len(large_dataset)} elements.")

    # Binary search becomes drastically more efficient on large datasets because
    # O(log n) logarithmic growth scales gracefully, whereas O(n) linear search requires
    # checking up to every single item.
    print(f"Linear Search Index: {linear_search(large_dataset, target_value)}")
    print(f"Binary Search Index: {binary_search(large_dataset, target_value)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list (returns -1 safely)
    empty_list = []
    print("Edge Case 1 - Empty List:")
    print(f"Linear Search: {linear_search(empty_list, 10)}")
    print(f"Binary Search: {binary_search(empty_list, 10)}")

    # Edge Case 2: Single-element list (finds match immediately at index 0)
    single_list = [42]
    print("Edge Case 2 - Single-Element List:")
    print(f"Linear Search: {linear_search(single_list, 42)}")
    print(f"Binary Search: {binary_search(single_list, 42)}")


if __name__ == "__main__":
    main()
