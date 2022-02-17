import re

def cleanup(filename):
    uniqueWords = set()
    with open(filename, 'r', encoding='utf8') as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            words = line.split()
            if len(words) == 2:
                persianWord = words[0].strip()
                if re.search(r'[\u0000-\u007F]', persianWord):
                    continue # Drop any word with ascii letter
                if re.search(r'[\u06F0-\u06F9 \u0660-\u0669]', persianWord):
                    continue # Drop any word with arabic digits
                if re.search(r'[\u060C \u061B \u061F \u00AB \u00BB \u00D7 \u200F]', persianWord):
                    continue # Drop other extra characters (?, Left and Right Pointing Double Angle Quotation Mark, ...)
                uniqueWords.add(persianWord)
            count += 1
    print('{} lines were scaned from the source file.'.format(count))
    print('{} unique words were found.\n'.format(len(uniqueWords)))
    sortedWords = sorted(list(uniqueWords))
    return sortedWords

def storeWords(words, filename, length=0):
    selectedWords = list()
    if length == 0:
        selectedWords = words
    elif length < 0:
        raise ValueError('Lenght has to be positive.')
    else:
        selectedWords = words.copy()
        for word in words:
            if len(word) != length or containsDiacritics(word):
                selectedWords.remove(word)
        print('Out of {} words, {} are stored with lenght {}.'.format(len(words), len(selectedWords), length))
    
    with open(filename, 'w', encoding='utf8') as f:
        f.write('\n'.join(selectedWords))

def containsDiacritics(word):
    # Some characters might affect the length undesierably.
    # For more information please take a look at this page:
    # en.wikipedia.org/wiki/Persian_alphabet
    # Hamze
    if re.search(r'[\u0621 \u0623 \u0624 \u0625 \u0626 \u0654 \u0654 \u065F \u0672-\u0678 \u06C0 \u06C2 \u06C3 \u06D3]', word):
        return True
    # Tāʼ marbūṭah (en.wikipedia.org/wiki/Taw#T%C4%81%CA%BC_marb%C5%AB%E1%B9%ADah)
    if re.search(r'[\u0629, \uFE93, \uFE94]', word):
        return True   
    # Short vowels
    if re.search(r'[\u064E \u064F \u0650]', word):
        return True
    # Tanvin
    if re.search(r'[\u064B \u064C \u064D]', word):
        return True
    # Tashdid
    if re.search(r'[\u0651]', word):
        return True
    # Other Characters
    if re.search(r'[\u0640 \uFDF2 \u2026]', word):
        return True
    # Zero-width non-joiner: Dropping words with this character feels really wrong but for now it's the quickest solution.
    # en.wikipedia.org/wiki/Zero-width_non-joiner
    if re.search(r'[\u200C]', word):
        return True   
    return False

def main():
    # Input from https://sites.google.com/site/mojganserajicom/home/upc
    inputfile = './data/UPC-2016.txt'
    words = cleanup(inputfile)

    # Words are added very liberally, we only drop ascii codes and digits.
    outputfile = './data/persian-words.txt'
    storeWords(words, outputfile)

    # When size is set words are added very conservetively. We drop all Diacritics, see containsDiacritics() for more details.
    filenameTemplate = './data/persian-words-{}letter.txt'    
    for length in range(2, 11):
        storeWords(words, filenameTemplate.format(length), length)

if __name__ == '__main__':
    main()