display = []
buttons = []


def make_button(n):
    return lambda: display.append(n)


for n in range(10):
    # A button is a function called when user clicks on it
    buttons.append(make_button(n))

btn = buttons[3]
btn()
print(display)
