print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input("For your first choice, you can go left or right\n")
direction = direction.lower()[0]
if direction == "l":
  action = input("You can chose to wait or to swim\n")
  action = action.lower()[0]
  if action == "w":
    door = input("What door do you wanna open? Red, Blue or Yellow\n")
    door= door.lower()
    if door == "yellow":
      print("Congrats, you've survived!")
    elif door == "red":
      print("Game Over, you've been eaten by a dragon")
    elif door =="blue":
      print("Game Over, you fell into a hole")
    else:
      print("Game Over, you tried to think outside the box")
  else:
    print("Game Over")
else:
  print("Game Over")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload