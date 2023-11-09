ringtoy = []

ringtoy.append('red')
ringtoy.append('orange')
ringtoy.append('yellow')

gojover = input("type something: ")


def reversalpurple(str):
    stack = []

    for red in str:
        stack.append(red)

    blue = " "

    while len(stack):
        blue = blue + stack.pop()
    
    return blue

print(reversalpurple(gojover))