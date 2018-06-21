s = "      Dipesh Joshi     "

'''
# 1. Substring
#s[start_index : end_index]
print(s[3:6])

# 2. String concatination (+ operator)
n = "Mr."
print(n+" "+s)

# 3. Repetition (* operator)
print(s*2)


# 4. membership (in operator)
for c in s:
    print c


# 5. Built in string methods
# 1. capitalize()
print(s.capitalize())

# 2. center(width, fillchar)
print(s.center(40, '-'))

# 3. count() - counts number of occurence
print(s.count('i'))

# 4. startswith() -
print s.startswith('Dip')

# 4. endswith(suffix)
if s.endswith("hi"):
    print "Yes"

# 5. find(str)
print(s.find('i'))

# 6. index(str)  Same as find but raises an exception if string not found
print(s.index('l'))

# 7. isalnum() Retuns true if string is alpha numeric. No space allowed.
print(s.isalnum())

# 8. isalpha() Retuns true if string contains all alphabatic characters. No space allowed.
print(s.isalpha())

# 9. isdigit() Returns true if string contains only digits and false otherwise.
print(s.isdigit())

# 10. islower() returns true if string contains only lower cased characters. space is allowed.
print(s.islower())

# 11. isupper() returns true if string contains only upper cased characters. space is allowed.
print(s.isupper())

# 12. isnumeric() Returns true if a UNICODE STRING contains only numeric characters and false otherwise.
print(s.isnumeric())

# 13. isspace() Returns true if string contains only whitespace characters and false otherwise.
print(s.isspace())

# 14. istitle() Returns true if string is properly "Title Cased" and false otherwise.
print(s.istitle())

# 15. join() the method join() returns a string in which the string elements of sequence have been joined by str separator.
p = '-'
seq = ("a", "b", "c")
print p.join(seq)

# 16. len(string) Returns lenght of the string.
print len(s)

# 17. lower() Converts all uppercase letters in string to lowercase.
print s.lower()

# 18. upper() Converts all lowercase letters in string to uppercase.
print s.upper()

# 19. s.strip() removes all trailing and leading whitespace from string.
print s.strip()

# 20. lstrip() Removes all leading whitespace in string.
print s.lstrip()

# 21. rstrip() Removes all trailing whitespace in string.
print s.rstrip()

# 22. max() Returns the max alphabetical character from the string str.
print max(s)

# 23. min(s) Returns the min alphabetical character from the string str. Return space also if in string.
print min(s)

# 24. split() Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.
print s.split(",")

# 25. replace(old, new [, max]) Replaces all occurrences of old in string with new or at most max occurrences if max given.
print(s.replace("i", "I"))

# 26. swapcase() Inverts case for all letters in string.
print s.swapcase()

# 27. title() Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.
print s.title()

# 28. translate()
from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

print s.translate(trantab)
'''
