def get_words():
    with open('data/persian-words.txt', 'r', encoding='utf8') as f:
        # This adds \n to the end of each line:
        #words = f.readlines()
    
        # This drops the \n at the end of each line:
        words = f.read().splitlines()
    return words