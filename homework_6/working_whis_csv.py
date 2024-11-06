import csv


def calculate_average_grade(filename="students.csv"):
    """Function for reading data"""
    total_score = 0
    student_count = 0

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_score += int(row["Оцінка"])
            student_count += 1

    if student_count == 0:
        print("Немає даних для обчислення середньої оцінки.")
        return 0
    average_grade = total_score / student_count
    print(f"Середня оцінка студентів: {average_grade:.2f}")
    return average_grade


def add_student(name, age, grade, filename="students.csv"):
    # Function to add a new student
    with open(filename, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, grade])
    print(f"Додано студента: {name}, вік: {age}, оцінка: {grade}")


calculate_average_grade()
add_student("Олена", 23, 92)
calculate_average_grade()
