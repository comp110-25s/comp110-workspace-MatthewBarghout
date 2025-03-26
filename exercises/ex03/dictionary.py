"""main file where the function skeletons and implementations will be"""

__author__ = "730737376"


# invert function that inverts keys of dictionary
def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values of input dictionary"""
    keys = list(input_dict.keys())
    values = list(input_dict.values())
    inverted_dict = {}

    i = 0
    while i < len(keys):
        if values[i] in inverted_dict:
            raise KeyError(f"Duplicate key found when inverting:{values[i]}")
        inverted_dict[values[i]] = keys[i]
        i += 1

    return inverted_dict


# count function counts a list and returns the frequency into a dictionary
def count(values: list[str]) -> dict[str, int]:
    """Counts the frequency of each item in the input list"""
    result = {}
    i = 0
    while i < len(values):
        item = values[i]
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

        i += 1

    return result


# returns the most frequent colot and displays it
def favorite_color(favorites: dict[str, str]) -> str:
    """Returns the most frequent favorite color from a dictionary of names and favorite colors"""

    color_counts = {}

    color_list = list(favorites.values())

    i = 0
    while i < len(color_list):
        color = color_list[i]
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
        i += 1

    most_frequent_color = ""
    max_count = 0

    keys = list(color_counts.keys())
    j = 0
    while j < len(keys):
        color = keys[j]
        count = color_counts[color]
        if count > max_count:
            most_frequent_color = color
            max_count = count
        j += 1

    return most_frequent_color


# use a list and bins strings by their length into a dictionary.
def bin_len(strings: list[str]) -> dict[int, set[str]]:
    """Bins strings by their length into a dictionary"""
    result = {}
    i = 0

    while i < len(strings):
        s = strings[i]
        length = len(s)

        if length not in result:
            result[length] = set()

        result[length].add(s)

        i += 1

    return result
