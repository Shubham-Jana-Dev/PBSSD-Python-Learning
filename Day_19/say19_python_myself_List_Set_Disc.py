"""
Day 19: Data Structures Lab
Focus: List vs. Tuple vs. Set (Mutability and Uniqueness)
"""

# --- 1. Understanding Sets & Uniqueness ---
def print_unique_elements(my_collection):
    """
    Demonstrates that passing a collection to a set 
    removes duplicates automatically.
    """
    print(my_collection) 

# Note: Using { } with single values creates a SET, not a Dictionary.
# A Dictionary requires key-value pairs {key: value}.
my_set = {1, 2, 3, 4, 5, 2, 7, 9, 90}
# print_unique_elements(my_set) 
# Output: {1, 2, 3, 4, 5, 7, 9, 90} (Duplicates like '2' are removed)


# --- 2. List to Set Conversion for Data Cleaning ---
def create_unique_list(list1):
    """Creates a new list containing only unique elements."""
    temp = set(list1)
    new_list = list(temp)
    return new_list

my_list = [1, 32, 4, 65, 4, 3, 2, 1, 6, 65, 7, 8, 7, 9, 90, 32, 4, 2, 1, 6]
unique_result = create_unique_list(my_list)
# print(f"Unique List: {unique_result}")


# --- 3. Indexing: Lists vs. Tuples ---
def check_indexing(my_list, list_index, my_tuple, tuple_index):
    """Demonstrates that both lists and tuples support positional indexing."""
    print(f"List element at {list_index}: {my_list[list_index]}")
    print(f"Tuple element at {tuple_index}: {my_tuple[tuple_index]}")

a_list = [32, 1, 65, 3, 342, 2, 6, 7, 8, 9, 90]
a_tuple = (32, 1, 65, 3, 342, 2, 6, 7, 8, 9, 90)
# check_indexing(a_list, 4, a_tuple, 4)


# --- 4. Mutability: Adding and Removing ---
""" 
List vs. Tuple vs. Set:
Lists are MUTABLE (can append/remove).
Tuples are IMMUTABLE (cannot be changed after creation).
Sets are MUTABLE (can add/remove), but unordered.
"""

def exploring_list_operations(the_lis, new_element, old_element):
    the_lis.append(new_element)      # Adding to end
    the_lis.remove(old_element)      # Removing specific value
    return the_lis

# --- 5. Set Operations (Add/Remove) ---
def exploring_set_operations(the_set, add_val, remove_val):
    the_set.add(add_val)             # Sets use .add() instead of .append()
    if remove_val in the_set:
        the_set.remove(remove_val)
    return the_set

sample_set = {1, 2, 3, 4, 5, 6, 7}
# print(exploring_set_operations(sample_set, 8, 6))


# --- 6. Updating Elements ---
def update_list_at_index(y_list, index_num, new_val):
    """Lists allow direct index updates."""
    y_list[index_num] = new_val
    return y_list

def update_set_value(y_set, old_val, new_val):
    """
    Sets are unordered and don't support indexing. 
    To 'update', we must remove the old and add the new.
    """
    if old_val in y_set:
        y_set.remove(old_val)
        y_set.add(new_val)
    return y_set

# Testing the updates
test_list = [10, 20, 30, 40]
# print(update_list_at_index(test_list, 1, 99))

test_set = {10, 20, 30, 40}
# print(update_set_value(test_set, 20, 99))