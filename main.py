
if __name__ == '__main__':
    string = 'Kaseke'

    print(string)
    print(string[:2]+string[3:])

    index = string.index('s')
    print(index)
    print(string[:index]+string[index+1:])
