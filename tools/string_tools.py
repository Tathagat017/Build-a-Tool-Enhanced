"""
String analysis tools for the reasoning script.
Contains functions for counting characters, vowels, consonants, etc.
"""

import re


def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)


def count_consonants(text):
    """Count the number of consonants in a string."""
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    return sum(1 for char in text if char in consonants)


def count_letters(text):
    """Count the number of letters (alphabetic characters) in a string."""
    return sum(1 for char in text if char.isalpha())


def count_words(text):
    """Count the number of words in a string."""
    return len(text.split())


def count_characters(text):
    """Count the total number of characters in a string."""
    return len(text)


def count_characters_no_spaces(text):
    """Count the number of characters excluding spaces."""
    return len(text.replace(' ', ''))


def count_digits(text):
    """Count the number of digits in a string."""
    return sum(1 for char in text if char.isdigit())


def count_uppercase(text):
    """Count the number of uppercase letters in a string."""
    return sum(1 for char in text if char.isupper())


def count_lowercase(text):
    """Count the number of lowercase letters in a string."""
    return sum(1 for char in text if char.islower())


def count_special_characters(text):
    """Count the number of special characters (non-alphanumeric) in a string."""
    return sum(1 for char in text if not char.isalnum() and not char.isspace())


def get_word_length(word):
    """Get the length of a word (excluding spaces)."""
    return len(word.replace(' ', ''))


def find_longest_word(text):
    """Find the longest word in a string."""
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


def find_shortest_word(text):
    """Find the shortest word in a string."""
    words = text.split()
    if not words:
        return ""
    return min(words, key=len)


def count_occurrences(text, substring):
    """Count how many times a substring appears in the text."""
    return text.lower().count(substring.lower())


def is_palindrome(text):
    """Check if a string is a palindrome."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return cleaned == cleaned[::-1]


# Tool registry for easy access
STRING_TOOLS = {
    'count_vowels': count_vowels,
    'count_consonants': count_consonants,
    'count_letters': count_letters,
    'count_words': count_words,
    'count_characters': count_characters,
    'count_characters_no_spaces': count_characters_no_spaces,
    'count_digits': count_digits,
    'count_uppercase': count_uppercase,
    'count_lowercase': count_lowercase,
    'count_special_characters': count_special_characters,
    'get_word_length': get_word_length,
    'find_longest_word': find_longest_word,
    'find_shortest_word': find_shortest_word,
    'count_occurrences': count_occurrences,
    'is_palindrome': is_palindrome
} 