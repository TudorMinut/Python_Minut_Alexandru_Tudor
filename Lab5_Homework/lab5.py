# Exercitiul 1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

# Exercitiul 2
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

# Exercitiul 3
class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.data = [[0 for _ in range(m)] for _ in range(n)]

    def get(self, row, col):
        return self.data[row][col]

    def set(self, row, col, value):
        self.data[row][col] = value

    def transpose(self):
        transposed_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed_matrix.set(j, i, self.get(i, j))
        return transposed_matrix

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns of the first matrix must be equal to the number of rows of the second matrix.")

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum_val = 0
                for k in range(self.cols):
                    sum_val += self.get(i, k) * other.get(k, j)
                result.set(i, j, sum_val)
        return result

    def apply(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.set(i, j, func(self.get(i, j)))
