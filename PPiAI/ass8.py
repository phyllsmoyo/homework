# QUESTION 1


def func_1(x, y):
    """
    This function will be used to multiply each value in the list, y, by x passed and
    return the resulting list after this multiplication has been applied.

    Function accepts 2 arguments:
    x: a numeric value
    y: a list of numeric values

    For example:
     if I gave the inputs 2 and [1,2,3,4,5]
     the result would be [2,4,6,8,10]

    """
    # Create an empty list to keep the multiplied values
    z = []
    # iterate through the list values
    for i in y:
        # multiply each list value and append to the list
        z.append(x * i)

    return z


# Question 2


def fahrenheit_to_celcius(temperature):
    """
    This function is used to convert temperature in Fahrenheit to Celciusself.

    The function accepts 1 argument, that is, the temperature in Fahrenheit.

    For example:
    32°F is equal to 32°C, and
    212°F is equal to 100°C and 212
    """
    return (temperature - 32) * 5 / 9


# Question 3


def temperature_converter(temperature, indicator, current_weather):
    """
    This function is used to covert temperature as follows:
    If indicator is F (meaning the temperature is in Fahrenheit) then the temperature will be converted to °C
    if indicator is C (meaning the temperature is in Celcius) then the temperature will be converted to °F

    The function accepts 3 arguments;
    temperature: the temperature a numeric value
    indicator: °F or °C
    current_weather: cloudy, rainy or sunny

    The function will print out what the caller should wear based on the values entered.

    For example:
    If the temperature is below 0°C (freezing) the function will print out: it is probably best to stay in today

    """
    indicators = ["F", "C"]
    weather_conditions = ["cloudy", "raining", "sunny"]
    if not isinstance(temperature, (float, int)):
        print("Temperature value should be a number")

    elif indicator not in indicators:
        print("Indicator can only be a F or a C")

    elif current_weather not in weather_conditions:
        print('current_weather can only be: "cloudy", "raining", or "sunny"')

    else:
        if indicator == "F":
            temp_in_C = fahrenheit_to_celcius(temperature)
            if temp_in_C < 0:
                print("It is probably best to stay in today")

            else:
                print("It's warm enough to go outside ", end="")
                if current_weather == "sunny":
                    print("and you should bring sunglasses ", end="")
                    if temp_in_C < 10:
                        print(" and you should bring a jacket")
                    elif temp_in_C > 10 and temp_in_C < 15:
                        print("and you should bring a sweatshirt")
                    else:
                        print("and you don't need any extra layers!!!")
                elif current_weather == "raining":
                    print("but you should bring an umbrella ", end="")
                    if temp_in_C < 10:
                        print(" and you should bring a jacket")
                    elif temp_in_C > 10 and temp_in_C < 15:
                        print("and you should bring a sweatshirt")
                    else:
                        print("and you don't need any extra layers!!!")
                else:
                    print(
                        "you do not need an umbrella, and you may not need sunglasses ",
                        end="",
                    )
                    if temp_in_C < 10:
                        print("and you should bring a jacket")
                    elif (
                        temp_in_C >= 10 and temp_in_C < 15
                    ):  # I added an equal to because the code misbehaves here if I just say >10 as per the question
                        print("and you should bring a sweatshirt")
                    else:
                        print("and you don't need any extra layers!!!")

        else:
            if temperature < 0:
                print("It is probably best to stay in today")

            else:
                print("It's warm enough to go outside ", end="")
                if current_weather == "sunny":
                    print("and you should bring sunglasses ", end="")
                    if temperature < 10:
                        print(" and you should bring a jacket")
                    elif temperature > 10 and temperature < 15:
                        print("and you should bring a sweatshirt")
                    else:
                        print("and you don't need any extra layers!!!")
                elif current_weather == "raining":
                    print("but you should bring an umbrella ", end="")
                    if temperature < 10:
                        print(" and you should bring a jacket")
                    elif temperature > 10 and temperature < 15:
                        print("and you should bring a sweatshirt")
                    else:
                        print("and you don't need any extra layers!!!")
                else:
                    print(
                        "you do not need an umbrella, and you may not need sunglasses ",
                        end="",
                    )
                    if temperature < 10:
                        print("and you should bring a jacket")
                    elif (
                        temperature >= 10 and temperature < 15
                    ):  # I added an equal to because the code misbehaves here if I just say >10 as per the question
                        print("and you should bring a sweatshirt")
                    else:
                        print("and you don't need any extra layers!!!")


# Question 4
def factorial(number):
    """
    This functions finds the factorial of a numberself.

    Number: is a positive integer

    Example:
    4! = 4 * 3 * 2 * 1 = 24
    3! =     3 * 2 * 1 = 6
    2! =         2 * 1 = 2
    1! =             1 = 1
    0! is given as     = 1

    Therefore:
    n! = n * (n-1)!
    """
    if isinstance(number, int):
        if number >= 0:
            # Factorial of 0 is 1 and Factorial of 1 is 1
            if number == 0 or number == 1:
                return 1
            else:
                # Factorial of numbers greater than 1 is n* factorial of n-1
                return (number) * factorial(number - 1)
        else:
            # Dealing with negative numbers
            print("Cannot find factorial of a negative number")

    else:
        # Dealing with input other than a number
        print("number can only be a positive integer")


# Question 5


def imperial_to_metric(unit, measure):
    """
    Function to convert US imperial to Metrics


    unit: any number to be converted
    measure: US Imperial or Metric Measure

    The function currently has the ability to convert between the following:
    a. Feet/inches and meters (and vice versa)
    b. Miles and kilometers (and vice versa)
    c. Fluid ounces and milliliters (and vice versa)
    d. Gallons and liters (and vice versa)

    More conversions will be added soon

    """
    unit = float(unit)
    measure = measure.lower()
    measures = [
        "inches",
        "in",
        "inch",
        "centimeters",
        "centimeter",
        "cm",
        "feet",
        "foot",
        "ft",
        "metres",
        "m",
        "metre",
        "miles",
        "mile",
        "kilometres",
        "kilometre",
        "km",
        "fluid ounces",
        "fl oz",
        "fluid ounce",
        "millilitres",
        "ml",
        "millilitre",
        "gallons",
        "gallon",
        "litres",
        "litre",
        "l",
    ]

    if measure in measures:

        # Feet/inches and meters (and vice versa)
        if measure == "inches" or measure == "in" or measure == "inch":
            print(
                "Inches [in] are U.S. customary units and will be converted to centimeters [cm] in metric units"
            )
            return f"{unit} [in] = {unit*2.54} [cm]"

        elif measure == "centimeters" or measure == "centimeter" or measure == "cm":
            print(
                " Centimeters [cm] are metric units and will be converted to Inches [in] in U.S. customary units "
            )
            return f"{unit} [cm] = {unit/2.54} [in]"

        elif measure == "feet" or measure == "foot" or measure == "ft":
            print(
                "Feet [ft] are U.S. customary units and will be converted metres [m] in metric units"
            )
            return f"{unit} [ft] = {unit*0.3048} [m]"

        elif measure == "metres" or measure == "m" or measure == "metre":
            print(
                " Meters [m] are metric units and will be converted to feet [ft] in U.S. customary units "
            )
            return f"{unit} [m] = {unit/0.3048} [ft]"

        # Miles and kilometers (and vice versa)
        elif measure == "miles" or measure == "mile":
            print(
                "Miles are U.S. customary units and will be converted kilometers [km] in metric units"
            )
            return f"{unit} [miles] = {unit*1.6093} [km]"

        elif measure == "kilometres" or measure == "km" or measure == "kilometre":
            print(
                " Kilometers [km] are metric units and will be converted to miles in U.S. customary units "
            )
            return f"{unit} [km] = {unit/1.6093} [miles]"

        # Fluid ounces and milliliters (and vice versa)
        elif (
            measure == "fluid ounces" or measure == "fl oz" or measure == "fluid ounce"
        ):
            print(
                "Fluid ounces are U.S. customary units and will be converted millilitres [ml] in metric units"
            )
            return f"{unit} [fl oz] = {unit*29.574} [ml]"

        elif measure == "millilitres" or measure == "ml" or measure == "millilitre":
            print(
                "Millilitres [ml] are metric units and will be converted to fluid ounces [fl oz] in U.S. customary units "
            )
            return f"{unit} [ml] = {unit/29.574} [fl oz]"

        # Gallons and liters (and vice versa)
        elif measure == "gallons" or measure == "gallon":
            print(
                "Gallons are U.S. customary units and will be converted litres [l] in metric units"
            )
            return f"{unit} [gal] = {unit*3.7854} [l]"

        elif measure == "litres" or measure == "l" or measure == "litre":
            print(
                "Litres [l] are metric units and will be converted to gallons [gal] in U.S. customary units "
            )
            return f"{unit} [l] = {unit/3.7854} [gal]"

    else:
        print(
            "Check the spelling and try again, otherwise the measure is currently not supported"
        )
