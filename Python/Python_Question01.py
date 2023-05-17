def highest_frequency_word_len(input_str):
    # Split the input string into words
    words = input_str.split()

    # Count the frequency of each word
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
        

    # Find the highest frequency
    max_frequency = max(word_freq.values())
    

    # Find the length of the highest-frequency word
    highest_frequency_word_length = 0
    for word, frequency in word_freq.items():
        if frequency == max_frequency:
            highest_frequency_word_length = max(highest_frequency_word_length, len(word))

    return highest_frequency_word_length


# print the results
str_1 = "write write write all the number from from from 1 to 100"
result_1 = highest_frequency_word_len(str_1)
print("Length of the highest-frequency word:", result_1)

str_2 = "the sun shines brightly in the sky."
result_2 = highest_frequency_word_len(str_2)
print("Length of the highest-frequency word:", result_2)

str_3 = "She sells seashells by the seashore."
result_3 = highest_frequency_word_len(str_3)
print("Length of the highest-frequency word:", result_3)

# Explanation:
# In 1st string "write write write all the number from from from 1 to 100 "  write appears 3 times and from appears 2 times. 
# Length of the highest frequency word(write) is 5.

# In 2nd string "the sun shines brightly in the sky."  The word "the" appears 2 times. 
# Length of the highest frequency word(the) is 3.

# In 3rd string "She sells seashells by the seashore." Every word appears only once. 
# Length of the highest frequency word(seashells) is 9.

