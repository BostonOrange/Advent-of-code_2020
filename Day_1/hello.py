import math
# import timeit

# code_to_test = '''
years = open("Day_1/input.txt", "r")

lines = years.read().split()
lines = [int(x) for x in lines]
lines.sort()
print(lines)

i = 0

target = 2020

for x in lines :

    left = i+1
    right = len(lines) - 1

    while left < right :
        combYear = lines[left] + lines[right] + lines[i]
        if combYear == target :
            answer = lines[left] * lines[right] * lines[i]
            break
        elif target < lines[left]+lines[right] + lines[i] :
            right = right - 1
        else :
            left = left + 1

    i = i + 1

print(answer)



# '''
# elapsed_time = timeit.timeit(code_to_test, number=100)/100

# print(elapsed_time)