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