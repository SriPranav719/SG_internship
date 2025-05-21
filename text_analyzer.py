#text analyzer                            
                            
text_analyzer = input("Enter any text : ")
splitted_text = text_analyzer.split()
print(f"Count of the words :{len(splitted_text)}")

replace_spaces= text_analyzer.replace(" ", "")

print(f' Count of the number of characters are :{len(replace_spaces)}')
