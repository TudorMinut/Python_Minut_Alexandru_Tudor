# 1
def fibonacci(n):
    if n <= 0:
        return []
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(fibonacci(7))


# 2
def primes_in_list(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return [x for x in lst if is_prime(x)]

print(primes_in_list([1,2,3,4,5,6,7,8,9,10]))


# 3
def list_operations(a, b):
    a_set, b_set = set(a), set(b)
    return (list(a_set & b_set), list(a_set | b_set), list(a_set - b_set), list(b_set - a_set))

print(list_operations([1,2,3], [2,3,4]))


# 4
def compose(notes, moves, start_pos):
    result = []
    pos = start_pos
    n = len(notes)
    result.append(notes[pos])
    for move in moves:
        pos = (pos + move) % n
        result.append(notes[pos])
    return result

print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


# 5
def zero_below_diagonal(matrix):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            if i > j:
                row.append(0)
            else:
                row.append(matrix[i][j])
        result.append(row)
    return result

print(zero_below_diagonal([[1,2,3],[4,5,6],[7,8,9]]))


# 6
def elements_appearing_x_times(*lists, x):
    from collections import Counter
    counter = Counter()
    for lst in lists:
        counter.update(set(lst))
    return [item for item, count in counter.items() if count == x]

print(elements_appearing_x_times([1,2,3], [2,3,4],[4,5,6],[4,1,"test"], x=2))


# 7
def palindrome_info(lst):
    palindromes = [x for x in lst if str(x) == str(x)[::-1]]
    if palindromes:
        return (len(palindromes), max(palindromes))
    return (0, None)

print(palindrome_info([121, 131, 20, 33, 44, 10]))


# 8
def ascii_filter(x=1, strings=[], flag=True):
    result = []
    for s in strings:
        if flag:
            filtered = [ch for ch in s if ord(ch) % x == 0]
        else:
            filtered = [ch for ch in s if ord(ch) % x != 0]
        result.append(filtered)
    return result

print(ascii_filter(2, ["test", "hello", "lab002"], False))


# 9
def spectators_blocked(matrix):
    blocked = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(1, rows):
        for j in range(cols):
            for k in range(i):
                if matrix[k][j] > matrix[i][j]:
                    blocked.append((i, j))
                    break
    return blocked

matrix = [
 [1, 2, 3, 2, 1, 1],
 [2, 4, 4, 3, 7, 2],
 [5, 5, 2, 5, 6, 4],
 [6, 6, 7, 6, 7, 5]
]
print(spectators_blocked(matrix))


# 10
def zip_with_none(*lists):
    max_len = max(len(lst) for lst in lists)
    result = []
    for i in range(max_len):
        result.append(tuple(lst[i] if i < len(lst) else None for lst in lists))
    return result

print(zip_with_none([1,2,3], [5,6,7], ["a", "b", "c"]))


# 11
def sort_by_3rd_char(tuples):
    return sorted(tuples, key=lambda t: t[1][2] if len(t[1]) > 2 else "")

print(sort_by_3rd_char([('abc', 'bcd'), ('abc', 'zza')]))


# 12
def group_by_rhyme(words):
    rhyme_dict = {}
    for w in words:
        rhyme = w[-2:] if len(w) >= 2 else w
        rhyme_dict.setdefault(rhyme, []).append(w)
    return list(rhyme_dict.values())

print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
