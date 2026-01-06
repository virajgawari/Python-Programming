# 05-JAN-2026

# Problem 1 :-

# Remove Duplicate Words

sentence = input("Enter a sentence: ")

words = sentence.split()
seen = set()
result = []

for word in words:
    if word not in seen:
        result.append(word)
        seen.add(word)

output = " ".join(result)
print("Output:", output)


# Problem 2 :-

# Find First Non-Repeating Character

text = input("Enter a string: ")

char_count = {}

for ch in text:
    char_count[ch] = char_count.get(ch, 0) + 1

for ch in text:
    if char_count[ch] == 1:
        print("First non-repeating character:", ch)
        break
else:
    print("No non-repeating character found")
