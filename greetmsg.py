
                            #text analyzer                            
                            
text_analyzer = input("Enter any text : ")
splitted_text = text_analyzer.split()
print(f"Count of the words :{len(splitted_text)}")

replace_spaces= text_analyzer.replace(" ", "")

print(f' Count of the number of characters are :{len(replace_spaces)}')





                        #string operations
                        
#UPPER CASE


text = "hello world"

print(text.upper())



#LOWER CASE


text = "HELLO WORLD"
print(text.lower())


#REMOVING SPACES IN BETWEEN THE TEXT 


text = "HELLO WORLD HOW ARE YOU"

replace = text.replace(" ", "")

print(replace)


#Slicing
text = "ABCDEFGH"

print(text[5:]) # accessing elements after the 5th index

print(text[3]) # accessing 3 rd element

print(text[:5]) # slicing only 1st 5 elements

print(text[-1:]) # reverse accessing

print(text [:-2]) # printing elements in the reverse order , skipping last two elements


#REMOVING WHITE SPACES 

text = "   Hi How are you"
print(text.strip())


