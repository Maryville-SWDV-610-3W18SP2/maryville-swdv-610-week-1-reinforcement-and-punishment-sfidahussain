'''
Write a short Python function, is_multiple(n, m), that takes two integer
values and returns True is n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.

'''
def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

def main():
    
    # Using 10 and 5, 10 is a multiple of 5: True
    print(is_multiple(10, 5))
    
    # Using 3 and 5, 3 is not a multiple of 5: False
    print(is_multiple(3, 5))

main()



