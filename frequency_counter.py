
# frequency_counter_of words in a text 
    
    
my_dict = {}

enter_the_words = input("Enter your text :")

for i in enter_the_words.split():
    
    if i in my_dict:
        
        my_dict[i] += 1
        
    else:
        my_dict[i] = 1
    
    
print(my_dict)