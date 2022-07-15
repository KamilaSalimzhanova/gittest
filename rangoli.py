#Hi
def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #fisrt half centerlevel == size
    my_alphabet = [char for char in alphabet[:size]]
    my_alphabet.reverse()
    char = my_alphabet[0]
    word = my_alphabet[0]
    my_list = []
    for i in range(size):
        if i != 0:
            prev = char
            char = my_alphabet[i]
            my_list.append(prev)
            part_word = '-'.join(my_list)
            word = part_word + '-' + char + '-' + part_word[::-1]
        print(str(word).center((size*2-1)+(size*2-2), '-'))
    
    
    for j in range(size-1):
        partword = '-'.join(my_list)
        my_list = my_list[:-1]
        word = partword + '-' + '-'.join(my_list[::-1])
        print(str(word).center((size*2-1)+(size*2-2), '-'))
        
while True:
    try: 
        n = int(input())
        print_rangoli(n)
    except Exception as err:
        print(f"oh no! something went wrong: {err}")
    finally:
        break