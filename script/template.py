from gui import Gui
from entities import Entity
from scene import *

# Eng : global variables
# Fr : 
DISPLAY_HEIGHT = 500
DISPLAY_WIDTH = 400

# create a gui
gui = Gui()
# create a player 
player = Entity()

##########################
#CREATING FONCTIONS AS TEMPLATES
###########################
def layout(template):
    def render_gui():
        # render big centered logo
        gui.render_logo(30, False)
        # render UI buttons
        gui.render_ui_buttons()
        template()
    return render_gui

def layout_paused(template):
    def render_gui():
        # render big centered logo
        gui.render_logo(30, False)
        # render UI buttons
        gui.render_ui_buttons(pause=True)
        template()
    return render_gui
 
################################# Story Template #################################
@layout
def before_game():
    #story text
    gui.render_text('Hi there, this is a story game.', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 80), size = 18)
    gui.render_text('are you sure you wanna play its', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 58), size = 18)
    gui.render_text('scary out there !', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2- 36), size = 18)
    # render left direction buttons
    game.ux_scenes['before game'].buttons['game'] = gui.render_button('button_large', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))
    gui.render_text('Play', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))

################################# Menu Template #################################
@layout_paused
def menu():
    # render frame 
    gui.render_frame('normal', 'pause')
    # render menu options
    game.ux_scenes['menu'].buttons["home"] = gui.render_text('New Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 30), size = 30)
    game.ux_scenes['menu'].buttons["exit"] = gui.render_text('Exit Game', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 10), size = 30)
    game.ux_scenes['menu'].buttons["credit"] = gui.render_text('Credit', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 50), size = 30)
    
################################# Monster Fight Template #################################
@layout
def fight():
    # render frame
    gui.render_frame('normal', 'fight')

################################# Game Credit Template #################################
def credit():
    ## render frame
    gui.render_frame('big', 'credit')
    # render credit
    gui.render_text('Game design & production', int(DISPLAY_WIDTH/2), 160, size = 15)
    gui.render_text('Youness Id bakkasse', int(DISPLAY_WIDTH/2), 200, size = 25)
    gui.render_text('Sound effects', int(DISPLAY_WIDTH/2), 250, size = 15)
    gui.render_text('Soundhound.com', int(DISPLAY_WIDTH/2), 290, size = 25)

################################# Stats Template #################################
@layout_paused
def stats():
    # render frame
    gui.render_frame('normal', 'stats')

    # render stats
    gui.render_text(f'Gold {int(player.gold)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 40))
    gui.render_text(f'Attack {int(player.attack)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 - 20))
    gui.render_text(f'Diffence {int(player.defence)}', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2))
    
    # render player's health bar
    gui.render_image('./assets/frames/bar.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 30))
    # render player's armor bar
    gui.render_image('./assets/frames/bar.png', int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2 + 65))

    # render icons
    gui.render_image('./assets/icons/heart.png', int(DISPLAY_WIDTH/2 - 65), int(DISPLAY_HEIGHT/2 + 30))
    gui.render_image('./assets/icons/level.png', int(DISPLAY_WIDTH/2 - 65), int(DISPLAY_HEIGHT/2 + 65))

    # render dynamique bar for both health and levels
    gui.render_rect(int(DISPLAY_WIDTH/2 - 50), int(DISPLAY_HEIGHT/2 + 20), int(125 * player.health/player.max_health), 20, Gui.colors['red'])
    gui.render_rect(int(DISPLAY_WIDTH/2 - 50), int(DISPLAY_HEIGHT/2 + 55), int(125 * player.current_xp/player.max_xp), 20, Gui.colors['yellow'])

    # render stats on bars
    gui.render_text(f'{int(player.health)}/{int(player.max_health)}', int(DISPLAY_WIDTH/2 + 10), int(DISPLAY_HEIGHT/2 + 32), size = 13)
    gui.render_text(f'Level {int(player.level)}', int(DISPLAY_WIDTH/2 + 10), int(DISPLAY_HEIGHT/2 + 67), size = 13)

################################# HomeTemplate #################################
def home():
    # render big centered logo
    gui.render_logo(150, True)
    # start game button
    game.ux_scenes['home'].buttons['before game'] = gui.render_button("button_game", DISPLAY_WIDTH/2, DISPLAY_HEIGHT- 160) 

################################# How to play Template #################################
def howtoplay():
    # render frame
    gui.render_frame('big', 'how to play')
    # render how to play content
    gui.render_text('Use your mouse to play', int(DISPLAY_WIDTH/2), 120, size = 15)

################################# Inventory Template #################################
def inventory():
    # render frame
    gui.render_frame('big', 'inventory')

    #render inventory boxes
    for i in range(3):
        for j in range(4):
            gui.render_image('./assets/frames/tall.png', int(80 * j + 80), int(150 + i * 120))

################################# Quests Template #################################
@layout_paused
def quests():
    # render frame
    gui.render_frame('normal', 'quests')
    # render how to play content
    gui.render_text('current quest: Kill the boss', int(DISPLAY_WIDTH/2), 250)

################################# Quests Template #################################
def store():
    # render frame
    gui.render_frame('big', 'store')
    # render how to play content
    gui.render_text('this is the store', int(DISPLAY_WIDTH/2), 250)

################################# Game Story Template  (important) #################################
@layout
def game():
    pass