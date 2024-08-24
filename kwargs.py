# parameter thet packs all the arguments into a dictionary

def hello(**kwargs):                # function(**variable_name)
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

hello(title="Mr.",first="Alan",middle="Savio",last="K")






















