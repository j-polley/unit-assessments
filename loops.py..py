def calculate_factorials():
    try:
        # Taking input from the user
        num = int(input("Enter a non-negative integer: "))

        if num < 0:
            print("Please enter a non-negative integer.")
            return

        factorial = 1

        # Loop to calculate and print factorials up to the input number
        for i in range(1, num + 1):
            factorial *= i
            print(f"{i}: {factorial}")

    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

# Call the function
calculate_factorials()

