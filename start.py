def fizzbuzz(final_number): #function which outputs fizzbuzz for all ints divisible by 3 and 5

    output = []

    for number in range(1, final_number+1):
         output.append(fizz_buzzer(number))
    return output


def fizz_buzzer(number):
    if number%5==0 and number%3==0:
        return "fizzbuzz"
    elif number%5==0:
        return "buzz"
    elif number%3==0:
        return "fizz"
    else:
        return number
