from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding = 'utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exists.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('alice.txt')
count_words(path)