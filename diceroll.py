import random

def diceroll():
    dice_num = random.randint(1, 6)
    if dice_num == 1:
        return( " |      |"
              "\n |  .   |"
              "\n |      |"
              )
    elif dice_num == 2:
        return (" |.     |"
              "\n |      |"
              "\n |     .|"
                )
    elif dice_num == 3:
        return (" |.     |"
              "\n |  .   |"
              "\n |     .|"
                )
    elif dice_num == 4:
        return (" |.    .|"
              "\n |      |"
              "\n |.    .|"
                )
    elif dice_num == 5:
        return (" |.    .|"
              "\n |   .  |"
              "\n |.    .|"
                )
    elif dice_num == 6:
        return (" |.    .|"
              "\n |.    .|"
              "\n |.    .|"
                )


print(diceroll())
