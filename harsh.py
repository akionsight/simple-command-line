import harsh2

input_from_user = input(str("what do you want(say help to know more):-       "))
if input_from_user.lower() == "generate random number":
    harsh2.generate_random_number()
elif input_from_user == "find length":
    message = input("what is the message :-    ")
    harsh2.find_length(message)
elif input_from_user == "number to digit":
    harsh2.number_to_digit()
elif input_from_user == "square this number":
    harsh2.square()
elif input_from_user == "add two numbers":
    harsh2.add_two_numbers()
elif input_from_user == "substract two numbers":
    harsh2.substract_two_numbers()
elif input_from_user == "divide two numbers":
    harsh2.divide_two_numbers()
elif input_from_user == "multiply two numbers":
    harsh2.multiply_two_numbers()
elif input_from_user == "title a message":
    harsh2.title_a_message()
elif input_from_user == "capitalise first letter":
    harsh2.capitalise_first_letter()
elif input_from_user == "lower sentence":
    harsh2.lower_case_sentence()
elif input_from_user == "imma jooking":
    harsh2.joke()
elif input_from_user == "what is the date":
    harsh2.date()
elif input_from_user == "what is the time":
    harsh2.time()
elif input_from_user == "birthday":
    harsh2.birthday()
