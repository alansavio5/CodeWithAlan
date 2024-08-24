# map() >>>>>>>> applies to each item that is iterable
# syntax >>>>>>> map(function,iterable) 

store = [("shirt",5.99),
        ("pants",7.99),
        ("shoes",10.99),
        ("jacket",11.99)]

usdt_inr = lambda data : (data[0],data[1]*83.64)

store_inr = map(usdt_inr,store)
for i in store_inr:
    print(i)

print("-----------------------------")
