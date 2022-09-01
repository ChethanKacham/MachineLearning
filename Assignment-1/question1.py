# Question - 1

import statistics
print("Question - 1")
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