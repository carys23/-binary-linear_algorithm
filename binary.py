'''
Carys Pritchard
Version 1.0
'''
import random
import time
from timeit import default_timer as timer
import timeit


'''This function list numbers from 1 to 100 it then picks a random number. It then uses an binary algorithm
    and finds the middle of the number to find the number. It will be compared next to a linear search
    to find the quickest way to search for the number'''

#Generate numbers
def generate_numbers():
    numbers = [i for i in range(1,1002)]
    return numbers

#Pick a number
def generate_random_number(numbers):
    random_number = random.randint(1, 1002)
    print(f'Random number is {random_number} \n')
    return random_number

#Get the list and get the middle
'''This function gets the middle of the list each time and compares it to the random number genrated in other function
    Letting the computer know what the lowest number and highest number is so from there it can split in the middle each 
    time it runs the program until it finds the random number.
    Added counter to check how times it needs to loop through until it needs
    the random number'''

def binary_search( numbers, random_number):
    count = 0
    low = numbers[0]
    high = numbers[1000]

    while low <= high:
        int_mid = (low + high) / 2
        mid = int(int_mid)


        #Check the number is not the number picked
        if mid == random_number:
            count = count + 1
            print(f'Found binary search in {count} count.')

            break
        #Else it will keep running until found
        else:
            if mid > random_number:
                high = mid -1
                count = count + 1
                continue
            else:
                low = mid + 1
                count = count + 1
                continue
    return count


'''Searching for the random number from 1 to 100 in linear order
    Using the length of the numbers in generated_numbers() to check
    against random number counting up 1 each time to find the number.
    Added counter to check how times it needs to loop through until it needs
    the random number'''

def linear_search( numbers, random_number):
    count = 0
    for number_count in range(len(numbers)):
        if random_number == numbers[number_count]:
            print(f'Found linear search in {count +1} count')
            return number_count +1, count +1
        else:
            count = count + 1
            continue


'''Testing the time to the seraches to see which one was quicker binary or linear'''



def time_test_binary():
    start = timer()
    binary_search(numbers, random_number)
    # timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)
    end = timer()
    print(F'Binary search in {end - start}')

def time_test_linear():
    start = timer()
    linear_search(numbers, random_number)
    # timeit.timeit('"-".join(str(n) for n in range(100))', number=100000)
    end = timer()
    print(f'Linear search in {end - start}\n')


generate_numbers()
numbers = generate_numbers()

random_number = generate_random_number(numbers)


time_test_linear()

time_test_binary()
