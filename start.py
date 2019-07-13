def fizz_buzzer(number):
    if number%5==0 and number%3==0:
        return "fizzbuzz"
    elif number%5==0:
        return "buzz"
    elif number%3==0:
        return "fizz"
    else:
        return number

def negfizz_buzzer(number): #created neg_fizzbuzz loop for negative numbers 
    if number%5==0 and number%3==0:
        return "zzubzzif"
    elif number%5==0:
        return "zzub"
    elif number%3==0:
        return "zzif"
    else:
        return number

def fizzbuzz(final_number): #function which outputs fizzbuzz for all ints divisible by 3 and 5

    output = []

    for number in range(1, final_number+1):
        output.append(fizz_buzzer(number))
    for number in range(final_number, 0+1): #called neg_fizzbuzzer in main program  
        output.append(negfizz_buzzer(number))
    print(output)
    return(output)

final_number = int(input("Please choose a number to fizz and buzz with:")) #hash this in to collect user input/has out to run test
final_number = int() #hash this in to run test/hash out to collect user input/run full program
print("Thank you, your fizzbuzz list is:")
fizzbuzz(final_number)

