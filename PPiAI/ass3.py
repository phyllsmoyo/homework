# Activity Suggestion App
# Simple program to make suggestions on what do based on a few factors.

# Store the Factors
print("Hi, Is it a weekday? (Answer: Yes or No)")
weekday = input()
print("What is the current weather like? (Answer: nice, raining or freezing)")
current_weather = str(input())
print("How much funds do you have available to spend?")
funds_available = float(input())

weather_condition = {"nice", "raining", "freezing"}

if current_weather in weather_condition:
    if weekday == "Yes":
        print(
            "You may have work or school today, but here are some suggestions if not…"
        )
        if current_weather == "nice":
            print("The weather is nice, so let's do something outside")
            if funds_available >= 100:
                print("Let’s go to an amusement park!")

            else:
                print(": Let's go for a walk in the park")
        elif current_weather == "raining":
            print("It's raining outside, so let’s do something indoors")
            if funds_available >= 50:
                print("Let’s go to a museum!")
            else:
                print("Let’s stay in and watch movies")
        else:
            print(
                " It is freezing outside! If you leave the house, make sure to bundle up!"
            )
            if funds_available >= 150:
                print("Let’s hit the slopes and go skiing!")
            else:
                print(" Let's stay in and drink hot chocolate while watching movies")
    else:
        print("It's the weekend! Wooo! Let’s decide what to do…")
        if current_weather == "nice":
            print("The weather is nice, so let's do something outside")
            if funds_available >= 100:
                print("Let’s go to a concert at an outdoor venue!")
            else:
                print("Let's go on a hike somewhere")
        elif current_weather == "raining":
            print("It's raining outside, so let’s do something indoors")
            if funds_available >= 50:
                print("Let’s go to a comedy show somewhere")
            else:
                print(" Let’s go on some free tours of the local places of worship!")
        else:
            print(
                "It is freezing outside! If you leave the house, make sure to bundle up!"
            )
            if funds_available >= 150:
                print("Let’s check out a local bar and/or arcade and play games!")
            else:
                print(
                    "Let's just call some friends and see if they want to come over and play board games!"
                )
else:
    print("Try again. Weather condition not recognized")
