# Student Gradebook

students = {}

print("=== Student Gradebook ===")
print()

while True:
    print("What do you want to do?")
    print("1. Add a student")
    print("2. View all students")
    print("3. Check a student's grade")
    print("4. Quit")
    print()

    choice = input("Enter choice (1-4): ")
    print()

    if choice == "1":
        name = input("Student name: ")
        score = float(input("Their score (0-100): "))

        if score >= 70:
            grade = "A"
        elif score >= 60:
            grade = "B"
        elif score >= 50:
            grade = "C"
        elif score >= 45:
            grade = "D"
        else:
            grade = "F"

        students[name] = {"score": score, "grade": grade}
        print(f"✅ {name} added with grade {grade}!")

    elif choice == "2":
        if len(students) == 0:
            print("No students yet! Add some first.")
        else:
            print("--- All Students ---")
            for name in students:
                score = students[name]["score"]
                grade = students[name]["grade"]
                print(f"  {name}: {score} ({grade})")

    elif choice == "3":
        name = input("Enter student name: ")
        if name in students:
            score = students[name]["score"]
            grade = students[name]["grade"]
            print(f"{name} scored {score} and got a {grade}")
        else:
            print(f"❌ {name} not found in gradebook!")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice, pick a number from 1 to 4!")

    print()