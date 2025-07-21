# AI Suggested code vi GitHub Copilot
def sort_dicts_by_key(dict_list, sort_key):
    """
    Sorts a list of dictionaries by a specific key.

    Args:
        dict_list (list): List of dictionaries to sort.
        sort_key (str): The key to sort the dictionaries by.

    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(dict_list, key=lambda d: d.get(sort_key))

# Example usage:
# data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
# sorted_data = sort_dicts_by_key(data, 'age')

# Manual Implentation
def sort_dicts_by_key_manual(data, sort_key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][sort_key] > data[j][sort_key]:
                data[i], data[j] = data[j], data[i]
    return data