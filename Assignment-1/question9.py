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