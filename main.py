def main():
    path = "books/frankenstein.txt"
    text = get_file_contents(path)
    print_report(path, text)    

def get_file_contents(path):
    with open(path) as f:
        return f.read()


def word_count(text):
    return len(text.split())


def char_count(text):
    freq = {}
    for c in text:
        lower_c = c.lower()
        freq[lower_c] = freq.get(lower_c, 0) + 1
    return freq


def char_count_sorted(text):
    char_freq = char_count(text)
    list_freq = [{"character": c, "frequency": f} for c, f in char_freq.items()]
    list_freq.sort(reverse=True, key=lambda a: a["frequency"])
    return list_freq


def print_report(path, text):
    print(f"--- Begin report of {path} ---")
    print(f"Number of words: {word_count(text)}\n")

    char_freq = char_count_sorted(text)
    for i in range(len(char_freq)):
        if char_freq[i]["character"].isalpha():
            print(f"The '{char_freq[i]["character"]}' character was found {char_freq[i]["frequency"]} times")

    print(f"--- End report ---")


main()
