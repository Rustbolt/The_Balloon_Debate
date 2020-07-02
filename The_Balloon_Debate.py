from pygame_functions import *
import pygame
import time
import random

mainClock = pygame.time.Clock()


# To initialise a game in pygame
screenSize(800,600,xpos=None, ypos=None, fullscreen=False)
display_width = 800
display_height = 600

# Colours used in game
black = (0, 0, 0)
white = (0, 0, 0)
red = (240, 78, 65)
green = (107, 153, 53)
text_colour = "#5f4c46"
text_colour_rgb = (95,76,70)
text_colour_light = (143,129,125)
background_colour = "#fbb3a7"
bright_red = (244, 115, 93)
bright_green = (130, 171, 75)

# pause variables
pausetime = 1000
endpause = 5000

#player names
names = []

# create a screen
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('The Balloon Debate')
clock = pygame.time.Clock()
USEREVENT = pygame.USEREVENT


# Background
background = pygame.image.load('background.png')

# Hot air Balloon
balloonImg = pygame.image.load('hot-air-balloon.png')
balloonX = 370
balloonY = 30

# list of invention
inventions = ["Money","Selfie-Stick","Computer","Toilet","Phone", "Clock"]
# how to play
about = ["You and your classmates have unexpectedly found yourselves in a hot air balloon",
         ",but the balloon is going to crash.",
         "The only way to save the majority is for one of you to jump.",
         "The twist is that you're not people, you're inventions",
         ",and if you jump the human race will have to survive without you.",
         "Each of you must put forward your case why you are the most important invention",
         ",while finding reasons why the other inventions aren't as important as you.",
         "When the time is up or you press return you will vote to decide who goes overboard."]


def balloon(x, y):
    screen.blit(balloonImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 133))
    return textSurface, textSurface.get_rect()

def text_objects_howto(text, font):
    textSurface = font.render(text, True, (95,76,70))
    return textSurface, textSurface.get_rect()

#shows message in middle of screen
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)

#prints out how to play on screen
def instruction_message(text, height, font):
    largeText = pygame.font.Font('freesansbold.ttf', font)
    TextSurf, TextRect = text_objects_howto(text, largeText)
    TextRect.center = ((display_width / 2), height)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    clock.tick(300)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(background, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        #prints title
        TextSurf, TextRect = text_objects("The Balloon Debate", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        screen.blit(TextSurf, TextRect)

        #menue buttons
        button("Play", 150, 450, 100, 50, green, bright_green, player_names)
        button("How To Play", 300, 450, 200, 50, text_colour_rgb, text_colour_light, how_to_play)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)


        pygame.display.update()
        clock.tick(15)

#if how to play button pressed
def how_to_play():
    new_line = 150
    line_name = 0

    intro = True
    screen.blit(background, (0, 0))
    instruction_message("How To Play", 50, 50)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #prints out the about list
        while line_name < 8:
            for index in range(0, len(about)):
                instruction_message(about[index], new_line, 18)
                new_line += 25
                line_name += 1

        button("Play", 150, 450, 100, 50, green, bright_green, player_names)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(30)

#assigns players inventions and stores names
def player_names():
    player_enter = True

    while player_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))
        inventions = ["Money", "Selfie-Stick", "Computer", "Toilet", "Phone", "TV", "Camera"]

        # Dictionary to add players names and give a random invention from the inventions list
        global player_invention
        player_invention = {}
        player_counter = 0
        player_index = 1
        invention_reveal_y = 250

        num_box = ""
        wordBox = ""
        while num_box == "":
            instruction_amount = makeLabel("How many players?", 40, 250, 150, text_colour, "Arial", "#fbb3a7")
            showLabel(instruction_amount)

            num_box = makeTextBox(250, 200, 300, 0, "Enter number of players", 30, 24)
            showTextBox(num_box)
            global player_amount
            player_amount = textBoxInput(num_box)


        if len(player_amount) != 0:
            hideLabel(instruction_amount)
            hideTextBox(num_box)
            screen.blit(background, (0, 0))
            player_amount = int(player_amount)

            while player_counter != player_amount:
                instructionLabel = makeLabel(f"Player {player_index} please enter your name", 40, 150, 150, text_colour, "Arial", background_colour)
                showLabel(instructionLabel)
                wordBox = makeTextBox(250, 200, 300, 0, "Enter your name here", 30, 24)
                #storing players name
                player = textBoxInput(wordBox)
                player = player.upper()
                names.append(player)
                print(player)
                player_invention[player] = random.choice(inventions)
                #takes invention from list so it is not used again
                inventions.remove(player_invention[player])
                player_counter += 1

                print(player_counter)
                player_index += 1

                global invention_reveal
                #tells the player their invention
                invention_reveal = makeLabel(f"{player}, Your invention is: {player_invention[player]}", 40, 200,
                                             invention_reveal_y, text_colour, "Arial", background_colour)
                invention_reveal_y += 50
                showLabel(invention_reveal)
                pause(pausetime)
                hideLabel(invention_reveal)
                hideLabel(instructionLabel)
                screen.blit(background, (0, 0))


            pygame.display.update()
            clock.tick(15)
            hideTextBox(wordBox)
            game_time()

#Asks for game duration
def game_time():
    time_input = ""
    player_enter = True

    while player_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))
        instruction_time = makeLabel("How long would you like to play for?", 40, 150, 150, text_colour, "Arial", "#fbb3a7")
        showLabel(instruction_time)

        while not time_input.isdigit():
            time_box = makeTextBox(250, 200, 300, 0, "Enter desired time here", 30, 24)
            showTextBox(time_box)
            time_input = textBoxInput(time_box)

        #Calculate fall time for balloon
        duration = float(time_input)
        time_input = int(time_input) * 60000
        print(duration)

        pygame.display.update()
        clock.tick(15)
        pause(pausetime)
        hideLabel(instruction_time)
        hideTextBox(time_box)
        game_loop(time_input, duration)

#pauses game using spacebar
def pause_game():
    paused = True

    while paused == True:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                paused = False


        message_display('Paused')

    pygame.display.update()
    clock.tick(5)

#Takes player votes to reveal the loser.
def player_vote():
    player_enter = True

    while player_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(background, (0, 0))

        #Variables to store votes and loser
        player_counter = 0
        votesdict = {"": 0}
        loser = ""
        draw = []
        big = 0

        while player_counter != player_amount:
            instructionLabel = makeLabel(f"{names[player_counter]} please cast your vote", 40, 250, 150, text_colour, "Arial", background_colour)
            showLabel(instructionLabel)
            voteBox = makeTextBox(250, 200, 300, 0, "Enter your vote here", 30, 24)

            vote = textBoxInput(voteBox)
            vote = vote.upper()
            #check if new vote or not
            if vote in player_invention:
                if vote in votesdict:
                    votesdict[vote] += 1
                else:
                    votesdict[vote] = 1
                player_counter += 1


        #Check who got the most votes outside the for loop
        for name in votesdict:
            if votesdict[name] > votesdict[loser]:
                loser = name
            if votesdict[name] > big:
                big = votesdict[name]
            if votesdict[name] == big:
                draw.append(name)
        print(len(draw))
        if len(draw) == 3:
            hideLabel(instructionLabel)
            hideTextBox(voteBox)
            global loser_reveal
            loser_reveal = makeLabel(
                f"There is a draw between {player_invention[draw[1]]} and {player_invention[draw[2]]}.Play Rock, Paper, Scissors to decide who stays.",
                20, 20, 350, "#5f4c46", "Arial", background_colour)
            showLabel(loser_reveal)
        if len(draw) == 4:
            hideLabel(instructionLabel)
            hideTextBox(voteBox)
            loser_reveal = makeLabel(
                f"There is a draw between {player_invention[draw[1]]} , {player_invention[draw[2]]} and {player_invention[draw[3]]}. Play Rock, Paper, Scissors to decide who stays.",
                20, 5, 350, "#5f4c46", "Arial", background_colour)
            showLabel(loser_reveal)
        if len(draw) < 3:
            hideLabel(instructionLabel)
            hideTextBox(voteBox)
            screen.blit(background, (0, 0))
            loser_reveal = makeLabel(f"{player_invention[loser]} has been thrown overboard by popular vote", 35, 50, 350,
                                     "#5f4c46", "Arial", background_colour)
            showLabel(loser_reveal)
        print(loser_reveal)
        pygame.display.update()
        clock.tick(15)
        screen.blit(background, (0, 0))
        pause(endpause)
        hideLabel(instructionLabel)
        hideTextBox(voteBox)
        hideLabel(loser_reveal)
        hideLabel(instructionLabel)
        blank = makeLabel("", 35, 10, 350, "#5f4c46", "Arial", background_colour)
        showLabel(blank)
        play_again()



# When Balloon reaches end
def crash():
    # global balloonY
    message_display('Time is up!')

#option to play again
def play_again():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(background, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("Play Again?", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        screen.blit(background, (0, 0))
        screen.blit(TextSurf, TextRect)


        button("Play", 150, 450, 100, 50, green, bright_green, player_names)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)
        pygame.display.update()
        clock.tick(15)



# A quit function so that i'm not calling two functions in other places when i want to quit
def quit_game():
    pygame.quit()
    quit()

#main loop t d arguments taken from game_time
def game_loop(t, d):
    global balloonX
    global balloonY
    global paused

    #sets game timer
    pygame.time.set_timer(USEREVENT+1, t)

    #sets balloon's rate of descent
    balloon_fallrate = .41 / d

    running = True
    while running:

        screen.fill((0, 0, 0))
        # how much to move the balloon image along the y axis every framerate
        balloonY += balloon_fallrate
        # Background image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == USEREVENT+1:
                balloonY = 390
                crash()
                pause(pausetime)
                player_vote()
                pause(pausetime)
            # Press enter to skip to voting
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                player_vote()
            #press space to pause the game
            elif keys[pygame.K_SPACE]:
                pause_game()



        if balloonY <=0:
            balloonY = 0
        elif balloonY >= 390:
            balloonY = 390
            crash()
            # pause(pausetime)
            # player_vote()
            # pause(pausetime)

        balloon(balloonX, balloonY)
        pygame.display.update()
        clock.tick(30)

# Finds the coordinates of buttons.
def button(msg, x, y, width, height, inactive_col, active_col, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_col, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()


    else:
        pygame.draw.rect(screen, inactive_col, (x, y, width, height))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(TextSurf, TextRect)

game_intro()

