day = "saturday"
temperature = 28
raining = True

if (day == "saturday" and temperature > 27) or not raining:     #adding the parenthesis makes it "easier" to ride in order of setting precedence. Remember, the "and" takes precedence over "or".
    print("Go swimming")
else:
    print("Learn python")