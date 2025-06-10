# Divide and get the value

roman_maps = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }

number = 450
roman_number = ""

# Loop through the maps then check the number is greater than equal to current map value
# then append the alphabet and subract the current map value from the number
for value, letter in roman_maps.items():
    while number >= value:
        roman_number += letter
        number -= value

print(roman_number)
