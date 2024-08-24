# input
#   ABCDCDC
#   CDC

# output
#   2

def count_substring(string, sub_string):
    c = 0
    s_list = list(string)
    sub_list = list(sub_string)
    for i in sub_list:
        for j in s_list:
            if i == j:
                c += 1
                break

    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)