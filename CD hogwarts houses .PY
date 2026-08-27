Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
#question 1
Answer1 = int(input("(Q1) Do you like Dawn or Dusk? 1)Dawn 2)Dusk "))
if Answer1 == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif Answer1 == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input")
#question 2
Answer2 = int(input("(Q2) When I am dead, I want people to remember me as, 1) The Good 2) The Great 3) The Wise 4) The Bold "))
if Answer2 == 1 :
  Hufflepuff += 2
elif Answer2 == 2:
  Slytherin += 2
elif Answer2 == 3:
  Ravenclaw += 2
elif Answer2 == 4:
  Gryffindor += 2
else:
  print("Wrong input")
#question3
Answer3 = int(input("(Q3) Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum "))
if Answer3 == 1:
  Slytherin += 4
elif Answer3 ==2:
  Hufflepuff += 4
elif Answer3 == 3:
  Ravenclaw += 4
elif Answer3 == 4:
  Gryffindor += 4
else :
  print("Wrong input")
  # store scores in a dictionary
houses = {
    "Gryffindor": Gryffindor,
    "Slytherin": Slytherin,
    "Hufflepuff": Hufflepuff,
    "Ravenclaw": Ravenclaw
}

# find house with max score
house_name = max(houses, key=houses.get)

print("Your house is:", house_name)

