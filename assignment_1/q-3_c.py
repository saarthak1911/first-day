text = input("Enter the sentence: ")
count = 0
for i in text :
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
        count = count + 1

print("Total Number of Vovels in sentence is",count)