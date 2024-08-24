#****** Indexing ******
#string[start:stop:step]
#start : starting index
#stop : stopping index
#step : only the characters after nth index

name="Alan Savio"
first_name=name[0:5]
last_name=name[5:10]
print(first_name)
print(last_name)

name="Alan Savio"
first_name=name[:5]
last_name=name[5:]
code_name=name[0:10:2]
reverse_name=name[::-1]
print(first_name)
print(last_name)
print(code_name)
print(reverse_name)


#********** Slicing *******
#slice=slice(start,stop,step)
#print(string[slice])

website1="https://google.com"
slice=slice(8,-4)
print(website1[slice])

website2="https://youtube.com"
print(website2[slice])

