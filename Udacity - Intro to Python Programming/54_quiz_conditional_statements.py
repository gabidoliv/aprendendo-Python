points = 174  # use this input to make your submission

# write your if statement here
if 1<= points <= 50:
    prize_name = "wooden rabbit"
    result = "Congratulations! You won a " + prize_name + "!"
elif points <= 150 or points == 0:
    result = "Oh dear, no prize this time."
elif points <= 180:
    prize_name = "wafer-thin mint"
    result = "Congratulations! You won a " + prize_name + "!"
else:
   prize_name = "penguin"
   result = "Congratulations! You won a " + prize_name + "!"
print(result)