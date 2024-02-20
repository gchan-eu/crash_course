numbers = list(range(1,10))
text = ""
for number in numbers:
    if number == 1:
        text = "st"
    elif number == 2:
        text = "nd"
    elif number == 3:
        text = "rd"
    else:
        text = "th"
    print(str(number) + text)

