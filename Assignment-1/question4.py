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