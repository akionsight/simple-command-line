def generate_random_number():
    import random
    x = 0
    while x != 3:
        try:
            first_number = int(input("first number:-    "))
            second_number = int(input("second number:-   "))
            random_number = random.randint(first_number, second_number)
            print(f"the random number is:- {random_number}   ")
        except ValueError:
            print("please enter values correctly")
            generate_random_number()
            x = x+1
            pass
            pass
            pass


def find_length(message):
    length = len(message)
    print(f"there are {length} charecters in the sentence ")


def number_to_digit():
    phone_number = input(" please enter your phone no.:          ")
    digits_mapping = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": " eight",
        "9": "nine",
        "0": "zero"
    }
    output = ""
    for ch in phone_number:
        output += digits_mapping.get(ch, "!") + " "
    print(output)


def square():
    number = int(input("number to be squared :- "))
    result = number * number
    print(f"the square of {number} is {result}")


def add_two_numbers():
    x = int(input("first number:-  "))
    y = int(input("second number:- "))
    res = x + y
    print(f"the sum of {x} and {y} is {res} ")


def substract_two_numbers():
    x = int(input("first number:-  "))
    y = int(input("second number:- "))
    res = x-y
    print(f"when {y} is substracted from {x} the answer is {res}")


def multiply_two_numbers():
    x = int(input("first number:-  "))
    y = int(input("second number:- "))
    print(f"the product of {x} and {y} is {x*y}")


def divide_two_numbers():
    try:
        divisor = int(input("divisor:- "))
        divedent = int(input("divedent:-  "))
        print(f"whe {divedent} is divided by {divisor} the quotient is {divedent / divisor}")
    except ZeroDivisionError:
        print("you have caused an error in the system")
        divide_two_numbers()


def title_a_message():
    message = input("what is the message:-  ")
    print(message.title())


def capitalise_first_letter():
    message = input("type sentence:- ")
    print(message.capitalize())


def lower_case_sentence():
    x = input("message = ")
    print(x.casefold())


def joke():
    var_joke = input("what is your joke")
    print(f"i did not like the joke {var_joke}")


def date():
    import datetime
    import pytz
    utc = datetime.datetime.now(tz=pytz.UTC)
    dt_mtn = utc.astimezone(pytz.timezone("Asia/Calcutta"))
    final_date = dt_mtn.strftime('%d ' '%B ' '%Y ')
    print(final_date)


def time():
    import datetime
    import pytz
    utc = datetime.datetime.now(tz=pytz.UTC)
    dt_mtn = utc.astimezone(pytz.timezone("Asia/Calcutta"))
    print(f" the exact time to the millisecond is {dt_mtn.time()}")


def birthday():
    import datetime
    import pytz
    utc = datetime.datetime.now(tz=pytz.UTC)
    dt_mtn = utc.astimezone(pytz.timezone("Asia/Calcutta"))
    final_date = dt_mtn.strftime("today is" + " " + '%d ' '%B ' '%Y ')
    print(final_date)
    if final_date == "today is 29 March 2020 ":
        print("yay, today is the day")
    else:
        print("sorry come back later")