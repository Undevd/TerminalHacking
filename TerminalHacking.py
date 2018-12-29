from random import randint

def word_within_threshold(answer, word, length):
    i = x = 0
    while i < length:
        if answer[i] == word[i]:
            x += 1
        i += 1
        if x >= length / 2:
            return word
    return None

def tokenise_string(line, width):
    return [line[i:i+width] for i in range(0, len(line), width)]

def print_screen(words):
    non_word_chars = '!"£$%^&*()_+[{]};:@#~,<.>/?|'
    word_char_count = len(words[0]) * len(words)
    inserts = 192 - word_char_count + len(words)
    col_1 = col_2 = col_3 = col_4 = ''
    i = x = 0
    
    positions = generate_positions(-3, 3, 192, len(words), len(words[0]))
    while i < inserts:
        #Column 1
        col_1 += '0x74AA'
        # Column 3
        col_3 += '0x74AB'
        
        if positions[0] == i and len(words) > 0:
            # add word to string
            col_2 += words[0].upper()
            col_4 += words[0].upper()
            positions.pop(0)
            words.pop(0)
        else:
            #Column 2
            rand = randint(0, len(non_word_chars) - 1)
            col_2 += non_word_chars[rand]

            # Column 4
            rand = randint(0, len(non_word_chars) - 1)
            col_4 += non_word_chars[rand]
        
        i += 1
    
    tokenised_1 = tokenise_string(col_1, 6)
    tokenised_2 = tokenise_string(col_2, 12)
    tokenised_3 = tokenise_string(col_3, 6)
    tokenised_4 = tokenise_string(col_4, 12)

    while x < len(tokenised_2): 
        print(f'{tokenised_1[x]}\t{tokenised_2[x]}\t{tokenised_3[x]}\t{tokenised_4[x]}')
        x+=1

def generate_positions(min_offset, max_offset, str_length, word_count, word_length):
    # min offset + word length + max offset
    positions = []
    i = 0
    while i < str_length - (word_count * word_length):
        #positions = [3, 17, 31, 45, 59, 73, 87, 101, 115, 129, 142, 156, 170, 184]
        positions.append(i + max_offset * 1)
        i += word_length + max_offset

    return positions

file = open('8LetterWords.txt', mode = 'r')
words = file.read().split(',')

answer = words[5]

results = []
for word in words:
    result = word_within_threshold(answer, word, len(word))
    if result is not None:
        results.append(result)

print_screen(results)