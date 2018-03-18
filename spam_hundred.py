'''
A common punishment for school children is to write out a sentence
multiple times.  Write a Python stand-alone program that will write
the following sentence one hundred times: "I will never spam my friends again."
'''

def spam_hundred():
    for count in range(100):
        print('I will never spam my friends again.')
        
def main():
    spam_hundred()
    
main()
