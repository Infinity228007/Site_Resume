import base64
import math
import numpy as np


class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten_url(self, long_url):
        encoded_url = base64.b64encode(long_url.encode()).decode()
        short_url = encoded_url[:6]
        self.urls[short_url] = long_url
        return short_url

    def expand_url(self, short_url):
        long_url = self.urls.get(short_url)
        return long_url


def print_result(key, message):
    def get_matrix(key, message):
        new_message = message.replace(" ", "")
        every_third_char = [char for i, char in enumerate(new_message, start=1) if i % 3 == 0]
        other_chars = [char for i, char in enumerate(new_message, start=1) if i % 3 != 0]

        if len(other_chars) % 2 != 0:
            last_char = other_chars.pop()
        else:
            last_char = ""

        digraphs = [other_chars[i] + other_chars[i + 1] for i in range(0, len(other_chars), 2)]

        if last_char:
            digraphs.append(last_char)

        if len(other_chars) % 2 != 0:
            digraphs[-1] += " "

        result = [(a, b) for a, b in zip(digraphs, every_third_char)] + \
                 [(a, None) for a in digraphs[len(every_third_char):]] + \
                 [(None, b) for b in every_third_char[len(digraphs):]]

        flat_list = [item for pair in result for item in pair if item is not None]

        num_columns = len(str(key))
        num_rows = math.ceil(len(flat_list) / num_columns)

        num_spaces_to_add = num_columns - (len(flat_list) % num_columns)
        flat_list += [" "] * num_spaces_to_add

        return np.array(flat_list[:num_rows * num_columns]).reshape(num_rows, num_columns)

    def get_order(key):
        key_str = str(key)
        order = sorted(range(1, len(key_str) + 1), key=lambda x: key_str[x - 1])
        return order

    def print_columns_in_order(matrix, order):
        combined_string = "".join("".join(matrix[:, col - 1]) for col in order)
        combined_string = combined_string.replace(" ", "")
        return combined_string

    matrix = get_matrix(key, message)
    order = get_order(key)
    combined_string = print_columns_in_order(matrix, order)
    return combined_string
