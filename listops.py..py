def create_list():
    """Create and return a list of 10 integers."""
    return [2, 3, 5, 7, 8, 10, 15, 12, 21, 19]

def print_list(lst):
    """Print the list."""
    print("List:", lst)

def sum_of_elements(lst):
    """Print the sum of all elements in the list."""
    print("Sum of elements:", sum(lst))

def largest_element(lst):
    """Print the largest element in the list."""
    print("Largest element:", max(lst))

def reverse_list(lst):
    """Print the list in reverse order."""
    print("Reversed list:", lst[::-1])

def smallest_element(lst):
    """Print the smallest element in the list."""
    print("Smallest element:", min(lst))

def main():
    """Main function to call list operations."""
    my_list = create_list()

    print_list(my_list)
    sum_of_elements(my_list)
    largest_element(my_list)
    reverse_list(my_list)
    smallest_element(my_list)

if __name__ == "__main__":
    main()
