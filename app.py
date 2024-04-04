

# dethär är mitt första program i python
print("hej på dig, vad heter du?")
name = input()
print("Välkommen, " + name + "! Det är trevligt att träffa dig!")
print("Hur gammal är du?")
age = int(input())
print("Jag är också " + str(age) + " år gammal!")
print("Vad är din favoritfärg?")
color = input()
if color.lower() == "grön":
    print("🤮")
elif color.lower() == "röd":
    print("🤬")
elif color.lower() == "blå":
    print("🥶")
elif color.lower() == "rosa":
    print("👅")
elif color.lower() == "orange":
    print("🎃")
elif color.lower() == "gul":
    print("🍋")
elif color.lower() == "grå":
    print("👽")
elif color.lower() == "vit":
    print("👻")
elif color.lower() == "silver":
    print("🦾")
elif color.lower() == "guld":
    print("🍯")
elif color.lower() == "brun":
    print("💩")
elif color.lower() == "lila":
    print("😈")
elif color.lower() == "svart":
    print("🥸")
else:
    print("Min favoritfärg är också " + color + "!")
print("Vad är din favoritmat?🧆")
food = input()
print("Jag tycker också om " + food + "!")
print("Vad är ditt favoritspel? 🎮")
game = input()
print("Jag tycker inte om att spela " + game + "!")
print("Vad är din favoritbok? 📕")
book = input()
print("jag gillar bara att läsa om python!")

i=0
while i < age:
    print("läsa om python!")
    i = i+1

print("Tack för att du pratade med mig, " + name + "! Ha en bra dag!")

