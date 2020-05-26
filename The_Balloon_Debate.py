from pygame_functions import *
import pygame
import time
import random

mainClock = pygame.time.Clock()


# TODO when space is pressed stop game
# TODO make full-screen


# To initialise a game in pygame

screenSize(800,600)
display_width = 800
display_height = 600

# Colours used in game
black = (0, 0, 0)
white = (0, 0, 0)
red =  (240, 78, 65)
green =(107, 153, 53)
text_colour = "#5f4c46"
background_colour = "#fbb3a7"
bright_red = (244, 115, 93)
bright_green =(130, 171, 75)
pausetime = 1000
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


def balloon(x, y):
    screen.blit(balloonImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 133))
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(background, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("The Balloon Debate", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        screen.blit(TextSurf, TextRect)

        button("Play", 150, 450, 100, 50, green, bright_green, player_names)
        button("Quit", 550, 450, 100, 50, red, bright_red, quit_game)

        pygame.display.update()
        clock.tick(15)


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
        # global names
        # names = []
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
            print(player_amount)
        if len(player_amount) != 0:
            hideLabel(instruction_amount)
            hideTextBox(num_box)
            screen.blit(background, (0, 0))
            player_amount = int(player_amount)
            # print(type(player_amount))
            # print(type(player_counter))
            while player_counter != player_amount:
                # player = input(f"Player {player_index}, Please enter your name\n>> ")

                instructionLabel = makeLabel(f"Player {player_index} please enter your name", 40, 150, 150, text_colour, "Arial", background_colour)
                showLabel(instructionLabel)
                wordBox = makeTextBox(250, 200, 300, 0, "Enter your name here", 30, 24)
                player = textBoxInput(wordBox)
                player = player.upper()
                names.append(player)
                print(player)
                player_invention[player] = random.choice(inventions)
                inventions.remove(player_invention[player])
                player_counter += 1

                print(player_counter)
                player_index += 1
                # Delete inventon from list so doesn't repeat
                global invention_reveal
                invention_reveal = makeLabel(f"{player}, Your invention is: {player_invention[player]}", 40, 200,
                                             invention_reveal_y, text_colour, "Arial", background_colour)
                invention_reveal_y += 50
                showLabel(invention_reveal)
                pause(pausetime)
                hideLabel(invention_reveal)
                # print(f"{player}, Your invention is: {Player_names[player]}")
                hideLabel(instructionLabel)
                screen.blit(background, (0, 0))
                # hideLabel(invention_reveal)

            pygame.display.update()
            clock.tick(15)
            hideTextBox(wordBox)
            game_time()

def game_time():
    time_input = ""
    player_enter = True

    while player_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(background, (0, 0))
        instruction_time = makeLabel("How long would you like to play for?", 40, 250, 150, text_colour, "Arial", "#fbb3a7")

        showLabel(instruction_time)
        while not time_input.isdigit():


            time_box = makeTextBox(250, 200, 300, 0, "Enter desired time here", 30, 24)
            showTextBox(time_box)

            time_input = textBoxInput(time_box)

        duration = float(time_input)
        time_input = int(time_input) * 60000
        print(duration)

        # for the time in time_input fall_rate is
        # ballonY += fall_rate
        # fps = 30
        # ballonY start position is y 30
        # end pos is 390
        # time
        pygame.display.update()
        clock.tick(15)
        pause(pausetime)
        game_loop(time_input, duration)

def pause_game():
    message_display('Paused')

def player_vote():
    player_enter = True

    while player_enter:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(background, (0, 0))
    # global player_amount
    # Dictionary to add players names and give a random invention from the inventions list

        player_counter = 0

        votesdict = {"": 0}
        loser = ""
        draw = []
        big = 0
        print(f"Player amount{player_amount}")
        # print(type(player_amount))
        # print(type(player_counter))
        while player_counter != player_amount:

            # player = input(f"Player {player_index}, Please enter your name\n>> ")
            instructionLabel = makeLabel(f"{names[player_counter]} please cast your vote", 40, 250, 150, text_colour, "Arial", background_colour)
            showLabel(instructionLabel)
            voteBox = makeTextBox(250, 200, 300, 0, "Enter your vote here", 30, 24)


            vote = textBoxInput(voteBox)
            vote = vote.upper()
            if vote in player_invention:
                if vote in votesdict:
                    votesdict[vote] += 1
                else:
                    votesdict[vote] = 1
                player_counter += 1
                print(f"player counter ..{player_counter}")
                hideLabel(instructionLabel)
        #Check who got the most votes outside the while loop
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
            loser_reveal = makeLabel(f"{player_invention[loser]} has been thrown overboard by popular vote", 35, 10, 350,
                                     "#5f4c46", "Arial", background_colour)
            showLabel(loser_reveal)
        print(loser_reveal)
        # pygame.display.update()
        # clock.tick(15)
        pause(pausetime)

# When Balloon reaches end
def crash():
    # global balloonY
    message_display('Time is up!')


# A quit function so that i'm not calling two functions in other places when i want to quit
def quit_game():
    pygame.quit()
    quit()

def input_box():
    instructionLabel = makeLabel("Please enter your name",40,display_width//2,display_height//2,"blue","yellow")
    showLabel(instructionLabel)

    wordBox = makeTextBox(10,80,300,0,"Enter your name here",5,24)
    showTextBox(wordBox)
    entry = textBoxInput(wordBox)


def game_loop(t, d):
    global balloonX
    global balloonY
    # balloonX = 370
    # balloonY = 30
    pygame.time.set_timer(USEREVENT+1, t)

    balloon_fallrate = .41 / d

    running = True
    while running:

        screen.fill((0, 0, 0))
        # global balloonY
        balloonY += balloon_fallrate
        # Background image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == USEREVENT+1:
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
            if keys[pygame.K_SPACE]:
                pause_game()
            # if event.type == pygame.K_:
            #     paused
            # if event.type == keydown enter key:
            #     player_vote()


        if balloonY <=0:
            balloonY = 0
        elif balloonY >= 390:
            balloonY = 390
            # crash()
            # pause(pausetime)
            # player_vote()
            # pause(pausetime)

        balloon(balloonX, balloonY)
        pygame.display.update()
        clock.tick(30)

# Finds the coordinates of play and quit buttons.
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


pygame.init()

game_intro()

