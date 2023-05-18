def is_string_valid(str):
    char_freq={ }

    #count the frequency of each charcater
    for ch in str:
        char_freq[ch]= char_freq.get(ch,0) + 1
    
    # Count the frequencies of the characters
    frequency_count = {}
    for frequency in char_freq.values():
        frequency_count[frequency] = frequency_count.get(frequency, 0) + 1
    # If there is only one unique frequency, or if there are exactly two frequencies where one occurs only once,
    # the string is valid
    if len(frequency_count) == 1 or (len(frequency_count) == 2 and 1 in frequency_count.values() and frequency_count[1] == 1):
        return "YES"
    else:
        return "NO"

# Example usage:
input_1 = "abc"
result_1 = is_string_valid(input_1)
print(result_1)  # Output: YES

input_2 = "abcc"
result_2 = is_string_valid(input_2)
print(result_2)  # Output: NO

input_3 = "aabbcc"
result_3 = is_string_valid(input_3)
print(result_3)  # Output: YES

input_4 = "abbc"
result_4 = is_string_valid(input_4)
print(result_4)  # Output: No


# Explanation:

# In the first example, the string "abc" has equal frequencies for all characters, so it is valid. The frequencies are: {"a": 1, "b": 1, "c": 1}.
# In the second example, the string "abcc" has frequencies { "a": 1, "b": 1, "c": 2 }. Removing one occurrence of "c" would result in frequencies { "a": 1, "b": 1, "c": 1 }, which is not valid since not all characters have the same frequency.
# In the third example, the string "aabbcc" has frequencies { "a": 2, "b": 2, "c": 2 }. All characters have the same frequency, so the string is valid.
# In the fourth example, the string "abbc" has frequencies { "a": 1, "b": 2, "c": 1 } which is not valid since not all characters have the same frequency.
