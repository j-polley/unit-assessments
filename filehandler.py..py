def read_input_file(input_file):
    """Reads student data from the input file."""
    students = {}
    with open(input_file, 'r') as file:
        for line in file:
            name, unit, mark, weight = line.strip().split(', ')
            mark, weight = float(mark), float(weight)

            if name not in students:
                students[name] = []
            students[name].append((unit, mark, weight))
    return students

def calculate_weighted_marks(students):
    """Calculates the weighted mark for each student."""
    results = {}
    for name, records in students.items():
        total_weight = sum(weight for _, _, weight in records)
        if total_weight != 100:
            raise ValueError(f"Total weight for {name} does not equal 100.")

        weighted_sum = sum(mark * (weight / 100) for _, mark, weight in records)
        results[name] = weighted_sum
    return results

def determine_grade(mark):
    """Determines the grade based on the weighted mark."""
    if mark >= 70:
        return "Distinction"
    elif mark >= 60:
        return "Merit"
    elif mark >= 50:
        return "Pass"
    else:
        return "Fail"

def write_output_file(output_file, results):
    """Writes the results to the output file."""
    with open(output_file, 'w') as file:
        for name, mark in results.items():
            grade = determine_grade(mark)
            file.write(f"{name}, {mark:.1f}, {grade}\n")

def main():
    input_file = 'students_input.txt'
    output_file = 'students_output.txt'

    # Test input file
    with open(input_file, 'w') as file:
        file.write("John, Math, 75, 50\n")
        file.write("John, Science, 50, 50\n")
        file.write("Anna, Math, 60, 40\n")
        file.write("Anna, Science, 80, 60\n")

    try:
        students = read_input_file(input_file)
        results = calculate_weighted_marks(students)
        write_output_file(output_file, results)
        print(f"Results have been written to {output_file}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
