from python.hashmaprepeatedword.hashmap_repeated_word import repeated_word
import pytest


def test_repeated_words():
    string = "Once upon a time, there was a brave princess who..."
    actual= repeated_word(string)
    expected= "a"
    assert actual==expected

def test_repeated_words_empty_string():
    string = ""
    with pytest.raises(ValueError):
        repeated_word(string)

def test_repeated_words_no_repeated_word():
    string = "It was a queer, sultry summer"
    actual= repeated_word(string)
    expected= "There are no repeated words"
    assert actual==expected
