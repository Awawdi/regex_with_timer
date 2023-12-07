import re
import time

def timer_decorator(func):
    def wrapper_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"The time taken is: {end_time - start_time} seconds")
        return result
    return wrapper_func

@timer_decorator
def squeeze_string(input_string: str) -> str:
    output_string = ""
    i = 0
    while i < len(input_string):
        count = 1
        while i + 1 < len(input_string) and input_string[i] == input_string[i+1]:
            i += 1
            count += 1
        output_string += input_string[i] + str(count)
        i += 1
    return output_string

@timer_decorator
def squeeze_using_re(input_string: str) -> str:
    compressed = re.sub(r'(\w)\1*', lambda m : m[0][0] + str(len(m[0])), input_string)
    return compressed if len(compressed) < len(input_string) else input_string

if __name__ == "__main__":
    print(squeeze_string(input_string="aaaaaaabbbbbbbbbbbbcccccccccc"))
    print(squeeze_using_re(input_string="aaaaaaabbbbbbbbbbbbcccccccccc"))
