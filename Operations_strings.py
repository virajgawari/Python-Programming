# Problem 1 : Take a string and reverse it.

text = input('Enter some text: ')

a = text[::-1]
print(a)

# Problem 2 : Count Vowels in a String

text = input('Enter some text: ')
text_lower = text.lower()

count = 0

for i in range(0, len(text_lower), 1):
    if text_lower[i] == 'a':
        count += 1
    if text_lower[i] == 'e':
        count += 1
    if text_lower[i] == 'i':
        count += 1
    if text_lower[i] == 'o':
        count += 1
    if text_lower[i] == 'u':
        count += 1

print("Number of vowels:", count)