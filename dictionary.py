#dictionary >>>>>>> achangable, unordered collection of unique key:value pairs

capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

print(capitals["India"])                        #to print the element associated with India

print(capitals.get("Germany"))                  #to check whether an alemen is present in the dictionary

print(capitals.keys())                          #print the keys only

print(capitals.values())                        #print the values only

print(capitals.items())                         #print the entire items

for keys,values in capitals.items():
    print(f"{keys} : {values}")

capitals.update({"Germany":"Berlin"})           #add a new key and value to a dictionary

for keys,values in capitals.items():
    print(f"{keys} : {values}")

capitals.pop("China")

capitals.clear()
