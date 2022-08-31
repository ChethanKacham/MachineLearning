import statistics
import math
# Question - 1

print("Question - 1")
# import statistics
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sorting the ages
ages.sort()
print("List after sorted", ages)
# Adding min age and max age again to the list
'''minimum_ages = ages[0]
maximum_ages = ages[len(ages)-1]
ages.append(minimum_ages)
ages.append(maximum_ages)'''
minimum_ages = min(ages)
maximum_ages = max(ages)
ages.extend([minimum_ages, maximum_ages])
print("List after adding minimum and maximum to the list", ages)
# Median age
"To sort the ages after adding the minimum and maximum terms again to the list"
ages.sort()
'''length = len(ages)
print(length)
if(length % 2 != 0):
    median = ages[length/2]
else:
    median = (ages[(length//2)]+ages[(length//2-1)])/2'''
median_ages = statistics.median(ages)
print("Median of ages is", median_ages)
# Average age
average_age = sum(ages) / len(ages)
print("Average of ages is", average_age)
# Range of ages
range_age = max(ages) - min(ages)
print("Range of ages is", range_age)


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


# Question - 3

print("Question - 3")
# Tuple of brothers and sisters
brothers = ('Chandrakanth', 'Chakravarthi', 'Charan')
sisters = ('Alekhya', 'Anusha', 'Pooja')
print("Bothers:", brothers)
print("Sisters:", sisters)
# Adding brothers and sisters to siblings
siblings = brothers + sisters
print("Siblings:", siblings)
# Length of sibling
length_siblings = len(siblings)
print("Total siblings are", length_siblings)
# Modifying siblings and Adding father and mother then assigning it to family_members
modify_siblings = list(siblings)
modify_siblings[5] = 'Deepika'
modify_siblings.extend(['Srinivas', 'Padma'])
family_members = tuple(modify_siblings)
print("Family members:", family_members)


# Question - 4
print("Question - 4")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Length of it_companies
length_it = len(it_companies)
print("Length of the it-companies is", length_it)
# Adding twitter to it_companies
it_companies.add('Twitter')
print("After adding twitter", it_companies)
# Inserting multiple it_companies at once
extra_itcomp = {'Wipro', 'TCS'}
it_companies.update(extra_itcomp)
print("After inserting multiple it companies at once", it_companies)
# Removing one it_company
it_companies.discard('Twitter')
print("After removing one it_company", it_companies)
# Difference between remove and discard is
"if the item to remove does not exist, remove() will raise an error and discard will not raise an error"
"it_companies.discard('Twitter')  --> Does not throw an error"
"it_companies.remove('Twitter')  --> Throws an error"
# Joining A and B
joining = A.union(B)
print("A and B", joining)
# A intersection B
intersection = A.intersection(B)
print("A intersection B", intersection)
# Is A subset of B?
subset = A.issubset(B)
print("A is subset of B?", subset)
# A and B disjoint sets
disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", disjoint)
# Join A with B and B with A
A.update(B)
B.update(A)
# Symmetric difference between A and B
sym_diff = A.symmetric_difference(B)
print("Symmetric difference between A and B", sym_diff)
# Deleting the sets completely
A.clear()
B.clear()
# Convert ages to set and compare the length of the list and the set
age_set = set(age)
print(age_set)
set_length = len(age_set)
list_length = len(age)
if set_length == list_length:
    print("All numbers are different")
else:
    print("Some numbers are similar")

# Question - 5
print("Question - 5")
# import math
radius_of_circle = 30
# Area of circle
_area_of_circle_ = math.pi * radius_of_circle * radius_of_circle
print("Area of circle is", _area_of_circle_, "square metres")
# Circumference of circle
_circum_of_circle_ = 2 * math.pi * radius_of_circle
print("Circumference of circle is", _circum_of_circle_, "metres")
# Taking radius as user input and calculating area
radius_from_user = float(input("Please enter the radius of the circle: "))
_area_of_circle_from_user = math.pi * radius_from_user * radius_from_user
print("Area of circle by taking radius as input from user", _area_of_circle_from_user)


# Question - 6
print("Question - 6")
string = "I am a teacher and I love to inspire and teach people"
str_split = string.split(" ")
print("After splitting string", str_split)
str_split_set = set(str_split)
print("Converting the split list to set", str_split_set)
length_str_words_used = len(str_split_set)
print("The number of words used are", length_str_words_used)


# Question - 7
print("Question - 7")
# Using tab escape sequence to print the required data
print("Name \t \t Age \t Country \t City \nAsabeneh \t 250 \t Finland \t Helsinki")


# Question - 8
print("Question - 8")
radius = 10
area = 3.14 * radius ** 2
# Displaying using String formatting method
print("The area of circle with radius {} is {} meters square".format(radius, area))


# Question - 9
print("Question - 9")
# Taking N(number of students) input from user
N = int(input("Enter the number of students: "))
weights_in_lbs = []
print("Enter the weights of {} students in lbs".format(N))
# Taking weights of N students in lbs
for i in range(0, N):
    weight_lb = int(input())
    weights_in_lbs.append(weight_lb)
print("{} students weights in lbs {}".format(N, weights_in_lbs))
# Converting lbs to kgs
weights_in_kgs = [i * 0.453592 for i in weights_in_lbs]
'''
weights_in_kgs = []
for i in weights_in_lbs:
    weight_kg = i * 0.453592
    weights_in_kgs.append(weight_kg)'''
print(N, "students weights in kgs", weights_in_kgs)
