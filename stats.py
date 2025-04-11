def get_num_words(book_content):
    temp = book_content.split()
    return len(temp)


def count_chars(book_content: str) -> dict:
    char_count = {}
    for i in book_content:
        char_count[i.lower()] = char_count.get(i.lower(), 0) + 1
    return char_count


def sort_on(char_count):
    return char_count["count"]


def split_to_list(char_count):
    dict_list = []
    for i in char_count:
        temp = {"char": i, "count": char_count[i]}
        dict_list.append(temp)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


len(5)
