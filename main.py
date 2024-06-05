import turtle

screen = turtle.Screen()
screen.title("us states game")
image = "./blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game_is_running =  True
while game_is_running:
    user_input = screen.textinput(title="guess a state",prompt = "please guess a state").lower()
    user_input = user_input[0].upper() + user_input[1:]
    print(user_input)







turtle.mainloop()

