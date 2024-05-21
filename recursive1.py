# Give a string
# text=”ABCDABCDAB”
# print count of AB occurred in text using regular expression

import re
text = "ABCDABCDAB"
pattern = "AB"
count = len(re.findall(pattern, text))

print("Count of 'AB' occurred in text:", count)

# re.findall(pattern, text) finds all occurrences of the pattern "AB" in the given text.
# len() is then used to find the count of occurrences.