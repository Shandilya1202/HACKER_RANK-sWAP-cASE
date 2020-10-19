# HACKER_RANK-sWAP-cASE
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.


example
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Input Format

A single line containing a string

.

Constraints

Output Format

Print the modified string

.

Sample Input 0

HackerRank.com presents "Pythonist 2".

Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".

//--------------------------------------------//
def swap_case(s):
    newstring = ''
    l = list()
    l = s
    for i in l:
        if i.isupper() == True:
            newstring+=(i.lower())
        elif i == " ":
            newstring+=i
        elif i == '"':
            newstring+= i 
        elif i.islower() == True:
            newstring+=(i.upper())
        else:
            newstring+=i
    return newstring


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
