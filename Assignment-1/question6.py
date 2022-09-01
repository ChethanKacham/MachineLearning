# Question - 6

print("Question - 6")
string = "I am a teacher and I love to inspire and teach people"
str_split = string.split(" ")
print("After splitting string", str_split)
str_split_set = set(str_split)
print("Converting the split list to set", str_split_set)
length_str_words_used = len(str_split_set)
print("The number of words used are", length_str_words_used)