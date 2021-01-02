# Question #: 3
# Date: Jan 1 2021
# Author: Dhanya

''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    # Input is word
    word = list(input())
    same_letter_indices = [i for i in range(len(word) - 1) if word[i] == word[i+1]]
    for ind in same_letter_indices:
        word[ind] = word[ind+2]
    
    print(''.join(word))
    return ''.join(word)

main()

