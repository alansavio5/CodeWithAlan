# input >>>> abracadabra
# output >>> abrackdabra

def mutate_string(string, position, character):
    lis = list(string)
    lis.pop(position)
    lis.insert(position,character)
    result = "".join(lis)
    return result

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    