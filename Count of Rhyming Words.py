The program must accept a string S containing multiple words as the input. The program must print the number of rhyming words in the given string S as the output. If two or more words are said to be rhyming words,
the second half of the words are equal by ignoring the case. Note: The second half of a word W is equal to the last (L+1)/2 characters of W (where L is the length of the word W).

Example Input/Output 1:
Input:
ring yin min gym bang
Output: 
4
Explanation:
The given string is "ring yin min gym bang". The words "ring" and "bang" are rhyming words. Similarly, the words "yin" and "min" are rhyming words. There are 4 rhyming words in the string S. So 4 is printed as the
output.

Example Input/Output 2:
Input: 
ring yum NOODLES GINGER
Output: 
0

Example Input/Output 3:
Input: 
BOOK CAT Apple took ATE COOK FLAT LOOK Apple
Output: 
8
Explanation:
The given string is "BOOK CAT Apple took ATE COOK FLAT LOOK Apple".
The words "BOOK", "took", "COOK", and "LOOK" are rhyming words. The words "CAT" and "FLAT" are rhyming words.
The words "Apple" and "Apple" are rhyming words. There are 8 rhyming words in the string S. So 8 is printed as the output.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def get_second_half(word):
    length = len(word)
    half_length = length // 2 
    return word[half_length:].lower()

words = input().split()
rhyme_count = {}
for word in words:
    rhyme_part = get_second_half(word)
    print(rhyme_part)
    if rhyme_part in rhyme_count:
        rhyme_count[rhyme_part] += 1
    else:
        rhyme_count[rhyme_part] = 1

total_rhyming_words = 0
for count in rhyme_count.values():
    if count > 1:
        total_rhyming_words += count

print(total_rhyming_words)
