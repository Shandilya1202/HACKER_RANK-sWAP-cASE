
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
