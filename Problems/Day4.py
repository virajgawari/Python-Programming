# 04-JAN-2026

# Problem 1 :-

# Find the Second Largest Number

a = [2,3,1,5,6,7]
largest = a[0]
second_largest = a[0]
for num in a:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)

# Problem 2 :-

# Sum of Even Numbers

numbers = [1,2,3,4,5,6,7,8,9]
even_sum = 0   

for num in numbers:
    if num % 2 == 0:    
        even_sum += num 

print("Sum of even numbers:", even_sum)

