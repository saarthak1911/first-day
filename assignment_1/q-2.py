num = list(map(int, input ("Enter the numbers (comma-seperated): ").split(',')))
size = len(num)

even = []
odd = []
count_eve = 0
count_odd = 0

for i in num:
    if i % 2 == 0:
        even.append(i)
        count_eve +=1
    else:
        odd.append(i)
        count_odd +=1

print("Total even Numbers :",count_eve)
print("Even numbers are:",even)

print("Total odd Numbers :",count_odd)
print("Odd numbers are:",odd)