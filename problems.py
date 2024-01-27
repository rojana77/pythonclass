

def count_vowels(word):
    word = word.lower()

    vowels = ('a', 'e', 'i', 'o', 'u')

    vowel_count = sum(1 for char in word if char in vowels)
    
    return vowel_count

word = input("Enter any words: ")
result = count_vowels(word)
print(f"The word '{word}' has {result} vowels.")