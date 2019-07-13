
class FizzBuzz(object):
    def __init__(self):
        pass

    def fizz_buzzer(self, number):
        if number%5==0 and number%3==0:
            return "fizzbuzz"
        elif number%5==0:
            return "buzz"
        elif number%3==0:
            return "fizz"
        else:
            return number

    def negfizz_buzzer(self, number): #created neg_fizzbuzz loop for negative numbers 
        if number%5==0 and number%3==0:
            return "zzubzzif"
        elif number%5==0:
            return "zzub"
        elif number%3==0:
            return "zzif"
        else:
            return number

    def fizzbuzz(self, final_number): #function which outputs fizzbuzz for all ints divisible by 3 and 5

        output = []
        if final_number >= 0:
            for number in range(1, final_number+1):
                output.append(self.fizz_buzzer(number))
        else:
            for number in range(final_number, 0+1): #called neg_fizzbuzzer in main program  
                output.append(self.negfizz_buzzer(number))
        return(output)
    
    def run(self):
        final_number = int(input("Please choose a number to fizz and buzz with:")) #hash this in to collect user input/has out to run test
        print("Thank you, your fizzbuzz list is:")
        output = self.fizzbuzz(final_number)
        print(output)

def main():
    fizzbuzz = FizzBuzz()
    fizzbuzz.run()

if __name__ == '__main__':
    main()


