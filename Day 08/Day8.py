def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}")

greet_with("Piotr", "Krakow")


#paint calculator

#Write your code below this line ๐
def prime_checker(number):
    for i in range(2, number -1):
        if number % i == 0:
            print("It's not a prime number.")
            break
    print("It's a prime number.")




#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
