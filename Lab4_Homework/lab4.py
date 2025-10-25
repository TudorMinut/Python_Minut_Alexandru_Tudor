# 1
def list_set_operations(a, b):
    set_a = set(a)
    set_b = set(b)
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    a_minus_b = set_a.difference(set_b)
    b_minus_a = set_b.difference(set_a)
    return [intersection, union, a_minus_b, b_minus_a]

print("1: ", list_set_operations([1, 2, 3, 4], [3, 4, 5, 6]))


# 2
def count_characters(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

print("2: ", count_characters("Ana has apples."))


# 3
def compare_dictionaries(d1, d2):
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        return d1 == d2

    if sorted(d1.keys()) != sorted(d2.keys()):
        return False

    for key in d1:
        if key not in d2 or not compare_dictionaries(d1[key], d2[key]):
            return False
            
    return True

dict1 = {'a': 1, 'b': {'c': 3, 'd': [4, 5]}}
dict2 = {'b': {'d': [4, 5], 'c': 3}, 'a': 1}
dict3 = {'a': 1, 'b': 2}
print("3 (True): ", compare_dictionaries(dict1, dict2))
print("3 (False): ", compare_dictionaries(dict1, dict3))


# 4
def build_xml_element(tag, content, **attributes):
    attrs = ' '.join([f'{key.replace("_", "")}="{value}"' for key, value in attributes.items()])
    if attrs:
        return f'<{tag} {attrs}>{content}</{tag}>'
    else:
        return f'<{tag}>{content}</{tag}>'

print("4: ", build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid"))


# 5
def validate_dict(rules, d):
    if set(rule[0] for rule in rules) != d.keys():
        return False

    for key, prefix, middle, suffix in rules:
        value = d.get(key, "")
        if not (value.startswith(prefix) and 
                value.endswith(suffix) and 
                middle in value[len(prefix):len(value)-len(suffix)]):
            return False
    return True

ruleset = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dict_false = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
dict_true = {"key1": "come inside, it's too cold out", "key2": "start with a middle in the winter"}
print("5 (False): ", validate_dict(ruleset, dict_false))
print("5 (True): ", validate_dict(ruleset, dict_true))


# 6
def count_unique_and_duplicates(lst):
    unique_elements = set(lst)
    num_unique = len(unique_elements)
    num_duplicates = len(lst) - num_unique
    return (num_unique, num_duplicates)

print("6: ", count_unique_and_duplicates([1, 1, 2, 2, 3, 4, 5, 5, 5]))


# 7
def set_operations(*sets):
    from itertools import combinations
    result = {}
    for a, b in combinations(sets, 2):
        result[f"{a} | {b}"] = a.union(b)
        result[f"{a} & {b}"] = a.intersection(b)
        result[f"{a} - {b}"] = a.difference(b)
        result[f"{b} - {a}"] = b.difference(a)
    return result

print("7: ", set_operations({1,2}, {2, 3}))


# 8
def find_loop(mapping):
    path = []
    visited = set()
    current_key = mapping['start']
    
    while current_key not in visited:
        visited.add(current_key)
        path.append(current_key)
        current_key = mapping.get(current_key)
        if current_key is None:
             break
        
    return path

print("8: ", find_loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# 9
def count_positional_in_keyword_values(*args, **kwargs):
    count = 0
    kwarg_values = set(kwargs.values())
    for arg in args:
        if arg in kwarg_values:
            count += 1
    return count

print("9: ", count_positional_in_keyword_values(1, 2, 3, 4, x=1, y=2, z=3, w=5))
