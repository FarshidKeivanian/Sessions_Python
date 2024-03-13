# Creating a dictionary for a student directory
student_directory = {
    'student1': {'name': 'Alex Green', 'ID': 234},
    'student2': {'name': 'Blair White', 'ID': 567},
    'student3': {'name': 'Casey Black', 'ID': 890}
}

# Outputting the second student's name and ID number
print("Second student's name:", student_directory['student2']['name'])
print("Second student's ID number:", student_directory['student2']['ID'])

# Adding a new student to the directory
student_directory['student4'] = {'name': 'Drew Red', 'ID': 112}

# Checking if a student with ID=123 exists in the student directory
id_to_check = 123
student_exists = any(student['ID'] == id_to_check for student in student_directory.values())
print("Does a student with ID=123 exist?", student_exists)

# Printing the updated student directory
for key, value in student_directory.items():
    print(f"{value['name']} (ID: {value['ID']})")
