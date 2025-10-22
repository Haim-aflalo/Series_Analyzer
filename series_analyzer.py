import string
import sys
from optparse import check_choice


def is_digit(lst):
    for num in lst:
        if num.isdigit():
            return True
    return False

def negative_num(lst):
        for num in lst:
            if float(num) > 0:
                return True
        return False

def ask_choice():
    while True:
        choice = input("Enter a series of positive numbers")
        lst_choice = choice.split()
        if len(lst_choice) < 3:
            print("Try Again")
            continue
        elif not is_digit(lst_choice):
            print("Try Again")
            continue
        elif not negative_num(lst_choice):
            print("try again")
            continue

        else:
            break

    new_choice = input("""------------------------------------------------------------
Series Analyzer - Menu
1. Input a new series
2. Display the series (original order)
3. Display the series (reversed order)
4. Display the series (sorted low→high)
5. Display the Max value
6. Display the Min value
7. Display the Average value
8. Display the Number of elements
9. Display the Sum of the series
0. Exit
------------------------------------------------------------
    """)
    if new_choice == '1':
        ask_choice()
    elif new_choice == '2':
        print(choice)
    elif new_choice == '3':
        print(choice[::-1])
    elif new_choice == '4':
        sorted_lst = sorted(lst_choice)
        sorted_str = ' '.join(map(str,sorted_lst))
        print(sorted_str)
    elif new_choice == '5':
        print(max(lst_choice))
    elif new_choice == '6':
        print(min(lst_choice))
    elif new_choice == '7':
        sum_elements = 0
        for i in lst_choice:
            sum_elements += int(i)
        average = sum_elements/ len(lst_choice)
        print(average)
    elif new_choice == '8':
        print(len(lst_choice))
    elif new_choice == '9':
        sum_lst = 0
        for i in lst_choice:
            sum_lst += int(i)
        print(sum_lst)
    elif new_choice == '0':
        sys.exit()


ask_choice()