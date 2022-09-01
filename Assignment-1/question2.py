# Question - 2

print("Question - 2")
# Creating an empty directory called dog
dog = {}
print("Empty Dog dictionary", dog)
# Adding name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Tommy',
    'color': 'White',
    'breed': 'German Shepherd',
    'legs': 4,
    'age': '5 years'
}
print("After adding name, color, breed, legs, age to the dog dictionary", dog)
# Student dictionary
student = {
    'first_name': 'Chethan',
    'last_name': 'Kacham',
    'gender': 'Male',
    'age': 23,
    'marital_status': 'No',
    'skills': ['ReactJS', 'NodeJS', 'SpringBoot', 'DevOps', 'OpenShift'],
    'country': 'US',
    'city': 'Kansas City',
    'address': '10105 Wornall Rd, Apt. 117, Kansas City, MO 64114'
}
print("Student dictionary", student)
# Length of Student dictionary
length_student = len(student)
print("Length of Student dictionary is", length_student)
# Value and data type of skills
value_skills = student['skills']
datatype_skills = type(student['skills'])
print("Value of skills in Student dictionary are", value_skills)
print("Data type of skills in Student dictionary is", datatype_skills)
# Modifying the skills
student['skills'].extend(['Python', 'C++'])
print("Value of skills in Student dictionary after modifying are", student['skills'])
# Dictionary keys
keys_student = list(student.keys())
print("Dictionary keys as list", keys_student)
# Dictionary values
values_student = list(student.values())
print("Dictionary values as list", values_student)