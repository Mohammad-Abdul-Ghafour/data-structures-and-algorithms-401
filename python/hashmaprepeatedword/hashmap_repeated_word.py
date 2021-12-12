from python.hashtable.hash_table import HashTable
import re

def repeated_word(string):
    if string :
        arr = re.findall(r"[A-z]*\w", string)
        hash_map = HashTable()
        for i in arr:
            is_contain = hash_map.contains(i.lower())
            if is_contain:
                return i
            hash_map.add(i.lower(),i)
        return 'There are no repeated words'
    else:
        raise ValueError("This is an empty string")

if __name__ == "__main__":
    string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of"
    print(repeated_word(string))