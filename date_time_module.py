import time

print(time.ctime(0))             # used to convert a time expressed in seconds since the epoch (January 1, 1970, 00:00:00 UTC) 
                                    # to a string representing local time.
                                        # If no argument is provided, time.ctime() returns the current local time.

print(time.time())              # current seconds since epoch

time_object = time.localtime()

print(time_object)

local_time = time.strftime("%d %B %Y %H:%M:%S",time_object)

print(local_time)

now_time = "2024,July,29"
time_obj = time.strptime(now_time,"%Y,%B,%d")
print(time_obj)
