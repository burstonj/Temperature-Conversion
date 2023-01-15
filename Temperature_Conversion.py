def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
#convert Fahrenheit to Celsius
def to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
#convert Celsius to Fahrenheit

# the main function is used to test the other functions
# this code isn't run if this module isn't the main module
def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celsius(temp), 2),
              "Celsius")
    #Display Fahrenheit conversion
    for temp in range(0, 100, 20):
        print(temp, "Celsius =", round(to_fahrenheit(temp), 2),
              "Fahrenheit")
#Display Celsuis conversion 

# to test the other functions
if __name__ == "__main__":
    main()

