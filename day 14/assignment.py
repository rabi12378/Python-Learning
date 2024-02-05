# WAP tpo create a decorator function which calculates the total time to execute the following function

# import time

# starttime=time.time()
# endtime=time.time()
    
def function(func):
    def innerfunc(*args,**kwargs):
        import time
        start_time=time.time()
        result = func (*args,**kwargs)
        end_time=time.time()
        total_time=end_time-start_time
        print(f"the execution time is {total_time}")
        return result
    return innerfunc

@function
def finc():
    for i in range(1000000000):
        continue
    print("loop completed")
finc()







    # Create a decorator function which changes a lower case input in a function to upper case

# def to_upper(func):
#     def inner_func(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#     return inner_func


# # @to_upper
# def get_message(msg):
#     return msg


# print(get_message("hello world"))


# @to_upper
# def another_messg(msg):
#     return msg


# print(another_messg("another message"))

