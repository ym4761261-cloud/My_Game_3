import random

# التعرف علي اللعبه و سؤال اللاعب اذا كان جاهز او لا

print("Welcome to the game of searching for the rabbit in the field! 🐇🌿")
ready = input("press enter to start").lower()

# تجهيز الحقل و وضع الارنب في مكان عشوائي

field = [["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"], ["🌿", "🌿", "🌿"]]
print(f"{field[0]}\n{field[1]}\n{field[2]}")

# تحديد اختيار الكمبيوتر و اخفأه عن المستخدم

comp_choise = random.choice(field[0] or field[1] or field[2] ) 

# بدا اللعب

print("Write from 01 to 33 please")
position = input("choose where the rabbit is hiding: 🐇")
row = int(position[0])
column = int(position[1])
field[row-1][column-1] = "🐇"

if position == comp_choise:
    print("You Win! 🥳")
else:
    print("ops!")
    print("You lose! 😑")
    print("Try again 😊")