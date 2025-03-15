def swap_max_min_frequency_letters(sentence):
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
print(output_sentence)