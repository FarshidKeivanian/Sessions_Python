#!/usr/bin/env python
# coding: utf-8

# In[4]:


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = text.split('.')
    return len(sentences) - 1  # Subtract 1 because the last split is usually empty

def calculate_word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

def replace_word(text, old_word, new_word):
    return text.replace(old_word, new_word)

def process_text(file_path, old_word=None, new_word=None):
    text = read_file(file_path)
    word_count = count_words(text)
    sentence_count = count_sentences(text)
    word_frequency = calculate_word_frequency(text)

    if old_word and new_word:
        text = replace_word(text, old_word, new_word)

    print(f'Word count: {word_count}')
    print(f'Sentence count: {sentence_count}')
    print('Word frequencies:')
    for word, frequency in word_frequency.items():
        print(f'{word}: {frequency}')
    
    if old_word and new_word:
        print(f'\nText after replacing "{old_word}" with "{new_word}":\n{text}')

# Example usage
file_path = file_path = 'C:\\example.txt' # Replace 'example.txt' with the path to your text file
process_text(file_path, 'oldWord', 'newWord')


# In[ ]:




