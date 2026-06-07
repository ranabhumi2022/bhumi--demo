monkey_position = 0
banana_position = 20

print("Monkey Banana Game Started!")

while monkey_position < banana_position:
    move = int(input("Enter steps for monkey to move: "))
    
    monkey_position = monkey_position + move
    print("Monkey position:", monkey_position)
    
    if monkey_position == banana_position:
        print("Monkey got the banana!You win!")
        break
    elif monkey_position > banana_position:
        print("Monkey crossed the banana! Try again.")
        break