# input
# 10                                            >>>> size of array
# 161 182 161 154 176 170 167 171 170 174       >>>> inputs

def average(array):
    s = list(set(arr))
    sum = 0
    for i in s:
        sum += i
    avg = sum/len(s)
    return avg
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)