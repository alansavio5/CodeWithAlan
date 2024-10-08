# input
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# output
# 56.00
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    sum = 0
    for key,value in student_marks.items():
        if key == query_name:
            for x in value:
                sum += x
            avg = sum / len(value)

    print("{:.2f}".format(avg))
