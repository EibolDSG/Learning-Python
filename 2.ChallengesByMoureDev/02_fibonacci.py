"""
Challenge Nº2 by MoureDev - FIBONACCI
"""

def fibonacci():
    n0 = 0
    n1 = 1
    for i in range(1, 51):
        print(n0)
        new_num = n0 + n1
        n0 = n1
        n1 = new_num

fibonacci()
