#Write a Python program to create a 4X4 2D matrix with below elements using loop and list comprehension both.
#Output:- [[0,0,0,0],[0,1,2,3],[0,2,4,6],[0,3,6,9]]

arr = [[i*0 for i in range(4)], [j for j in range(4)], [k*2 for k in range(4)], [l*3 for l in range(4)]]
print(arr)