"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
- Use a list operation to insert the value.

- Add comments explaining what happens to existing elements

      after an insertion occurs.
- Use comments to explain how insertion performance may vary depending on

      where the insertion occurs.
    """
    # Insert the value at the specified index
    lst.insert(index, value)
    # Existing elements from this index onward shift one position to the right.
    # Inserting at the beginning or middle is slower (O(n)) because elements must shift,
    # while appending to the very end is faster (O(1)) since no shifts are needed.


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
- Validate that the index exists.

- Return the removed value.

- Return None if the index is invalid.

- Add comments explaining why index validation and safe deletion are important.

    """
    # Validate that the index is within the valid bounds of the list
    if -len(lst) <= index < len(lst):
        # Remove and return the value at the specified index
        return lst.pop(index)
    # Return None if the index is invalid to prevent an IndexError crash
    return None
    # Index validation and safe deletion are important to protect the application
    # from crashing when users or programs try to access or delete out-of-bounds memory.


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
- Return the index if the value is found.

- Return -1 if the value is not found.

- Add comments explaining why this is a linear search and why it scans sequentially.

    """
    # Loop through the list to find the value
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    # Return -1 if the value is not present in the list
    return -1
    # This is a linear search because it scans sequentially through elements one by one
    # from start to finish, resulting in O(n) time complexity for unsorted lists.


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")

    # 1. Create a list containing several values.
    my_list = [10, 20, 30]

    # 2. Display the original list.
    print("Original list:", my_list)

    # 3. Test insertion at the beginning, middle, and end.
    # Insert at the beginning (index 0)
    insert_at(my_list, 0, 5)
    print("After inserting 5 at the beginning (index 0):", my_list)

    # Insert at the middle (index 2)
    insert_at(my_list, 2, 15)
    print("After inserting 15 in the middle (index 2):", my_list)

    # Insert at the end (using index equal to length)
    insert_at(my_list, len(my_list), 40)
    print("After inserting 40 at the end:", my_list)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")

    # 1 & 2. Delete an item from the beginning, middle, and end, and display the removed value.
    removed_beginning = delete_at(my_list, 0)
    print(f"Removed value from beginning: {removed_beginning} | Updated list: {my_list}")

    removed_middle = delete_at(my_list, 1)
    print(f"Removed value from middle: {removed_middle} | Updated list: {my_list}")

    removed_end = delete_at(my_list, len(my_list) - 1)
    print(f"Removed value from end: {removed_end} | Updated list: {my_list}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")

    # Reset list for clear searching demonstration
    search_list = [100, 200, 300, 400]
    print("Current list for searching:", search_list)

    # 1. Search for a value that exists.
    found_index = search_value(search_list, 300)
    print(f"Searching for 300 -> Found at index: {found_index}")

    # 2. Search for a value that does not exist.
    missing_index = search_value(search_list, 999)
    print(f"Searching for 999 -> Returned index: {missing_index}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge Case 1: Delete using an invalid index out of bounds
    invalid_delete = delete_at(search_list, 10)
    print(f"Attempting to delete at invalid index 10 -> Result: {invalid_delete}")

    # Edge Case 2: Delete from an empty list
    empty_list = []
    empty_delete = delete_at(empty_list, 0)
    print(f"Attempting to delete from an empty list -> Result: {empty_delete}")


if __name__ == "__main__":
    main()
