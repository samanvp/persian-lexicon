# Persian Lexicon
This repo uses [Uppsala Persian Corpus (UPC)](https://sites.google.com/site/mojganserajicom/home/upc) to construct a lexicon of 70664 unique words. With all the excitement around game [Wordle](https://en.wikipedia.org/wiki/Wordle), we also extracted words with different length (2, 3, 4, ..., 10) and stored them to separate files for easier access. **Please note** that these files might contain offensive words, I have not check them manually.

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
 * [Zero-width non-joiner (نیم‌فاصله)](https://en.wikipedia.org/wiki/Zero-width_non-joiner).

After applying these filters, we ended up with these number of words per file:
 * 2 letter words: 310 unique words
 * 3 letter words: 2378 unique words
 * 4 letter words: 7059 unique words
 * 5 letter words: 10043 unique words
 * 6 letter words: 9541 unique words
 * 7 letter words: 7350 unique words
 * 8 letter words: 4681 unique words
 * 9 letter words: 2529 unique words
 * 10 letter words: 1250 unique words
