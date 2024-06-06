import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)


states = pd.read_csv("./50_states.csv")
dataframe = states[['state', 'x', 'y']]
data = dataframe.to_dict(orient='list')

def check_answer(input):
    for x in range(len(data['state'])):
        if input == data['state'][x]:
            return input, data['x'][x], data['y'][x]
    return "wrong", -800, -800        

turtle.shape(image)
game_is_running = True

while game_is_running:
    user_input = screen.textinput(title="Guess a State", prompt="Please guess a state")
    if user_input is not None:
        user_input = user_input.strip().title()
        state, data_x, data_y = check_answer(user_input)
        if state != "wrong":
            turt = turtle.Turtle()
            turt.penup()
            turt.hideturtle()
            turt.goto(data_x, data_y)
            turt.write(state)
    else:
        game_is_running = False

turtle.done()







turtle.mainloop()

