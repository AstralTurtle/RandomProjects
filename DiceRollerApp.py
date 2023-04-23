import flet as ft


def dieRoll(numSides, numRolls, mod):
    total = 0
    for i in range(numRolls):
        total += random.randint(1, numSides)
    total += mod
    return total


def makeDie(input):
    if (input.find('+') != -1):
        sides = int(input[input.find('d')+1:input.find('+')])
        rolls = int(input[0:input.find('d')])
        mod = int(input[input.find('+')+1:len(input)])
    elif (input.find('-') != -1):
        sides = int(input[input.find('d')+1:input.find('-')])
        rolls = int(input[0:input.find('d')])
        mod = -int(input[input.find('-')+1])
    else:
        sides = int(input[input.find('d')+1:])
        rolls = int(input[0:input.find('d')])
        mod = 0
    return dieRoll(sides, rolls, mod)


def makeDieAdv(input):
    return max(makeDie(input), makeDie(input))


def makeDieDis(input):
    return min(makeDie(input), makeDie(input))

def main(page: ft.Page):
    page.title = "Dice Roller"
    # page.add(ft.Label("Dice Roller"))
    # page.add(ft.Label("Enter your dice roll in the format 'XdY+Z'"))
    # page.add(ft.Label("Where X is the number of dice, Y is the number of sides, and Z is the modifier"))
    # page.add(ft.Label("For example, 2d6+3 would roll 2 six-sided dice and add 3 to the result"))
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    dieInput = ft.TextField(width = 100)
    page.add(dieInput)
    adv = ft.Checkbox("Advantage")
    disadv = ft.Checkbox("Disadvantage")
    page.add(adv)
    page.add(disadv)

ft.app(target=main)
    