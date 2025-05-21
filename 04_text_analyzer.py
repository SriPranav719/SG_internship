# Create a text analyzer that counts characters, words, and performs various string operations.


text_analyzer = input("Enter any text : ")
splitted_text = text_analyzer.split()
print(f"Count of the words :{len(splitted_text)}")

replace_spaces= text_analyzer.replace(" ", "")

print(f' Count of the number of characters are :{len(replace_spaces)}')