print "This script compares two strings to decide whether they are totally the same."

str1 = raw_input('str1 = ')
str2 = raw_input('str2 = ')
length = len(str1)
for char in str1:
    if char not in str2:
        print "They are not the same."
        break
    elif char == str1[length - 1]:
        print "They are totally the same."
