# input : sequence = "ababc",  word = "ab"
# output : 2

sequence = "ababc"
word = "ab"

def max_times_word(sequence,word):
    if(word not in sequence):
        return 0                                     
    s = word                                         
    c = 0
    while(len(s)<=len(sequence)):                  # Swipe Up and Look Oncee
        if(s in sequence):
            c += 1
            s += word
        else:
            break
    return c
print(max_times_word(sequence,word))

   
    
            









# sequence = "ababc"
# word = "ab"

# def maximum_times(sequence,word):
#     if word not in sequence:
#         return 0
#     count = 0    
#     s = word
#     while (len(sequence)>=len(s)):        # 5 >= 2                         5 >= 4             5 >= 6
#         if(s in sequence):              # ab in ababc   True              abab in ababc       condition False
#             s += word                  # s = abab                        s = ababab           
#             count += 1                 # count = 1                      count = 2             Exit from the loop
#         else:                                 
#             break
        
#     return count
    
    
# print(maximum_times(sequence,word))    
    
            










# sequence = "ab"
# s = ""
# s += sequence  
# s += sequence                            
# s += sequence
# print(s)             
