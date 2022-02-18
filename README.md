# Persian Lexicon
This repo uses [Uppsala Persian Corpus (UPC)](https://sites.google.com/site/mojganserajicom/home/upc) to construct a lexicon of **70528 unique words**. With all the excitement around game [Wordle](https://en.wikipedia.org/wiki/Wordle), we also extracted words with different length (2, 3, 4, ..., 10) and stored them to separate files for easier access. **Please note** that these files might contain offensive words, I have not check them manually.

`GetWords.py` can read these files and return words as a list of strings.

# Cleanup details
## Main Lexicon
The main lexicon (`data/persian-words.txt`) is build very liberally; we only filter out words that contain [ASCII characters](https://en.wikipedia.org/wiki/ASCII) or [Arabic numerals](https://en.wikipedia.org/wiki/Persian_alphabet#Deviations_from_the_Arabic_script).

## Fixed length Lexicons
More conservative filtering has been applied to files with fixed word length. We drop all words that contain any of the following characters:
 * All forms of [hamze (همزه)](https://en.wikipedia.org/wiki/Hamza).
 * All forms of [tanvin (تنوین)](https://en.wikipedia.org/wiki/Nunation).
 * All forms of [short vowels](https://en.wikipedia.org/wiki/Persian_alphabet#Short_vowels).
 * [Tashdid (تشدید)](https://en.wikipedia.org/wiki/Persian_alphabet#Ta%C5%A1did).

 Also when calculating length of words we do not take into account [Zero-width non-joiner (نیم‌فاصله) characters](https://en.wikipedia.org/wiki/Zero-width_non-joiner). For example, "پیش‌بینی‌" length is consider to be 7 rather than 8.

After applying these filters, we ended up with these number of words per file:
 * 2 letter words: 316 unique words
 * 3 letter words: 2389 unique words
 * 4 letter words: 7236 unique words
 * 5 letter words: 11024 unique words
 * 6 letter words: 12507 unique words
 * 7 letter words: 11753 unique words
 * 8 letter words: 9335 unique words
 * 9 letter words: 6113 unique words
 * 10 letter words: 3648 unique words
