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
                if re.search(r'[\u060C \u061B \u061F \u00AB \u00BB \u00D7]', persianWord):
                    continue # Drop other extra characters (?, Left and Right Pointing Double Angle Quotation Mark, ...)
                uniqueWords.add(persianWord)
            count += 1
    print('{} lines were scaned'.format(count))
    print('{} unique words were found'.format(len(uniqueWords)))
    sortedWords = sorted(list(uniqueWords))
    return sortedWords


def main():
    # Input from https://sites.google.com/site/mojganserajicom/home/upc
    inputfile = './UPC-2016.txt'
    outputfile = './persian-words.txt'
    words = cleanup(inputfile)

    with open(outputfile, 'w', encoding='utf8') as f:
        f.write('\n'.join(words))

if __name__ == '__main__':
    main()

