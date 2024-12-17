def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    """Main function to handle user input for temperature conversion."""
    print("Temperature Conversion Program")
    print("1: Convert Celsius to Fahrenheit")
    print("2: Convert Fahrenheit to Celsius")

    try:
        choice = int(input("Enter your choice (1 or 2): "))

        if choice == 1:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius} °C is equal to {fahrenheit:.2f} °F")

        elif choice == 2:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} °F is equal to {celsius:.2f} °C")

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter numeric values for temperature and valid choices.")

if __name__ == "__main__":
    main()
