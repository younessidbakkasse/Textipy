from scene import Scene, StoryScene, Gui
from template import (
    home_template,
    menu_template,
    inventory_template,
    credit_template,
    howtoplay_template,
    stats_template,
    store_template, 
    quests_template,
    fight_template,
    gameover_template,
)   

class Game:
    def __init__(self):
        # Constructing GUI scenes 
        self.scenes = {
            # Paused scenes ##################################################
            'Home' : Scene('home', home_template),
            'Menu' : Scene('menu', menu_template),
            'Inventory' : Scene('inventory', inventory_template),
            'Credit' : Scene('credit', credit_template),
            'Help' : Scene('how to play', howtoplay_template),
            'Stats' : Scene('stats', stats_template),
            'Quests' : Scene('quests', quests_template),
            'Store' : Scene('store',store_template),
            'Fight' : Scene('fight', fight_template),
            'Game Over' : Scene('game over', gameover_template),

            # Creating main game scenes ########################################
            'Pregame' : StoryScene('Pregame', [['Start playing', 'Beach', 'normal']], 'Hi there, this is a story game. are you sure you wanna play. its scary out there !'),
            'Beach' : StoryScene('Beach', [['Explore the beach', 'Nothing', 'normal']], 'Washed ashore, you have only vague recollections of what happened. The past seems unimportant now. Shivering, you watch the bodies float among the debris. No ships can be seen on the horizon.'),
            'Nothing' : StoryScene('Nothing', [['Examine the object', 'Coin', 'normal']], 'There is nothing but sand and gravel. Or so it may seem. You feel a painful sensation in your left foot, causing you to take a step backwards. Glimmering in the sun, a sharp object is revealed.'),
            'Coin' : StoryScene('Coin', [['Continue exploring', 'Footprints', 'normal']], "At first, you are unable to make sense of it. You pick it to get a closer look. it's a silver coin. Something about the unusual coin seems familiar."),
            'Footprints' : StoryScene('Footprints', [['Study the footprints', 'Person', 'normal'], ['Follow the footprints', 'Something', 'normal']], "You discover footprints in the sand, leading north. it's late in the afternoon. If there's another survivor out there, you should find this person before it gets dark."),
            # One step scene
            'Person' : StoryScene('Person', [['Follow the footprints', 'Something', 'normal']], 'They are somewhat small and delicate. You arrive at the concusion that they were made by a person below average height, walking barefoot.'),
            'Something' : StoryScene('Something', [['Fight him', 'Lagoon', 'fight-wild dog'], ['Take the knife', 'Lagoon', 'loot-knife']], "Something near the water has caught your attention, prompting you to take a quick look. Closer scrutiny reveals a rusty knife. While hardly ideal, it's better than nothing."),
            # Lagoon
            'Lagoon' : StoryScene('Lagoon', [['Take a look around', 'First enemy', 'normal']], "Further north, the beach gives way to a flourishing wetland. You discover a lagoon, surrounded by red pines. At this point there are no more footprints."),
            # Fight scene
            'First enemy' : StoryScene('First enemy', [['Fight', ' ', 'fight-great snake'], ['get the map', 'Second loot', 'loot-map']], "Something is moving through the reeds on the other side. A wild dog emerges. Growling, it runs towards you across the shallows."),
            }

    def run(self):
        self.scenes['Home'].run_scene()  

game = Game()