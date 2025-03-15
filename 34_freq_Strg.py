"""n = "Python is a programming language"
l = []
for i in range(len(n)):
    print(n[i], "=", n.count(n[i]))
    if n[i] not in l:
        l.append(n[i])
l.sort()        
print(l)
for i in range(len(l)):
    max = i
    for j in range(i+1,len(l)):
        if (n.count(l[i])) < n.count(l[j]):
            max = j
            M = l[j]
            l[i],l[j] = l[max],l[i]
print(l)            
print(M)"""

'''def swap_max_min_frequency_letters(sentence):
    # Normalize the sentence to lower case and filter out non-alphabetic characters
    filtered_sentence = ''.join(filter(str.isalpha, sentence.lower()))
    print("filtered_sentence", filtered_sentence)
    
    # Count the frequency of each letter
    frequency = {}
    # for char in filtered_sentence:
    #     frequency[char] = frequency.get(char, 0) + 1
    # #print("frequency", frequency)
    
    for char in sentence:
        if char == " ":
            continue 
        elif char.lower() in frequency:
            frequency[char.lower()] += 1 
        else:
            frequency[char.lower()] = 1
            
    res = sorted(frequency.keys()) 
    print("res", res)
    # Identify the max and min frequency letters
    max_freq_letter = min_freq_letter = None
    max_freq = -1
    min_freq = float('inf')
    
    for char in sorted(frequency.keys()):
        freq = frequency[char]
        # Update max frequency letter
        if freq > max_freq:
            max_freq = freq
            max_freq_letter = char
        # Update min frequency letter
        if freq < min_freq:
            min_freq = freq
            min_freq_letter = char
    
    # Swap the letters in the original sentence
    swapped_sentence = []
    for char in sentence:
        if char.lower() == max_freq_letter:
            swapped_sentence.append(min_freq_letter)
        elif char.lower() == min_freq_letter:
            swapped_sentence.append(max_freq_letter)
        else:
            swapped_sentence.append(char)
    
    print("swapped_sentence",swapped_sentence)
    return ''.join(swapped_sentence)

# Example usage
input_sentence = "Python is a programming language"
output_sentence = swap_max_min_frequency_letters(input_sentence)
print(output_sentence)  '''

def swap_max_min_letters(sentence):

    filtered_sentence = ''.join(filter(str.isalpha, sentence.lower()))
    print("Filtered sentence is ",filtered_sentence)

    frequency = {}
    for char in sentence:
        if char == " ":
            continue
        elif char.lower() in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1    
    print(sorted(frequency.items()))
    print(frequency)

    max_freq = min_freq = None
    max_freq = -1
    min_freq = float('inf')
    
    for char in sorted(frequency.keys()):
        freq = frequency[char]
        if freq > max_freq:
            max_freq = freq
            max_freq_char = char.lower()
        if freq < min_freq:
            min_freq = freq
            min_freq_char = char

    print("Max_Frequnce char is {} and its freq is {}".format(max_freq_char,max_freq))  
    print("Min_Frequnce char is {} and its freq is {}".format(min_freq_char,min_freq))      
    swapped = []    
    for char in filtered_sentence:
        if char.lower() == max_freq_char:
            swapped.append(min_freq_char)
        elif char.lower() == min_freq_char:
            swapped.append(max_freq_char)
        else:
            swapped.append(char)

    return ''.join(swapped)                

        



n = "Python is a programming language"
print(swap_max_min_letters(n)) 
