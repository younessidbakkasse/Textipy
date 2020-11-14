""" This game is made by Youness ID BAKKASSE; https://github.com/younessidbakkasse/
its a school project to initiat with Python programming 
for more informations and licence please check README file attached to the folder."""

# Importing modules: pygame is a module that allows us to draw on screen
import pygame, sys

# Colors
colors = {
    "black" : (15, 15, 15),
    "white" : (245, 245, 245),
    "yellow": (249, 200, 51),
    "brown" : (49, 45, 46),
    "orange" : (238, 117, 57)
}

DISPLAY_HEIGHT = 500
DISPLAY_WIDTH = 400


class Scene():
    pygame.init()
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    def __init__(self):
        """ Set up the game display """
        self.running, self.click = True, False 
        self.buttons = {}

    def run_scene(self):
        """ scene main loop : basicly each scene has its own loop """
        while self.running:
            Scene.display.fill(colors["brown"])
            self.render()
            self.get_events()
            pygame.display.update()
            Scene.clock.tick(60)

    def get_events(self):
        """ This function collects keyboard and mouse clicks from the user """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.scene_events(event)

    def render_text(self, text, x, y, color, size = 20):
        """ Draws any text on the scene window """
        game_font = pygame.font.Font("./assets/fonts/Minecraft.ttf", size)
        text_surface = game_font.render(text, False, color)
        text_rect = text_surface.get_rect(center = (int(x), int(y)))
        Scene.display.blit(text_surface, text_rect)
        return text_rect

    def render_image(self, path, x, y):
        """ Renders images on the screen """
        image = pygame.image.load(path)
        image_rect = image.get_rect(center = (int(x), int(y)))
        Scene.display.blit(image, image_rect)
        return image_rect



class Menu(Scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    def __init__(self, path):
        super().__init__()
        self.music_icon_path = path
    
    def render(self):
        # logo
        self.render_text("woods", int(DISPLAY_WIDTH/2), 55, colors["yellow"], 32)
        self.render_text("runner", int(DISPLAY_WIDTH/2), 100, colors["yellow"], 80)

        # menu items
        self.buttons["new game"] = self.render_text("New game", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2), colors["orange"], 40)
        self.buttons["options"] = self.render_text("Options", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2) + 50, colors["orange"], 40)        
        self.buttons["credit"] = self.render_text("Credit", int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT/2) + 100, colors["orange"], 40)

        # render sound icon
        self.buttons["music on"] = self.render_image(self.music_icon_path, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 50))

    def scene_events(self, event):
       if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button:
                self.click = True
                for button in self.buttons: 
                    controle.to_destination_scene()


class Description(Scene):
    """ This is a sub class from scene base class ; sceneMenu = a variant of scene with a menu """
    back_icon_path = "./assets/icons/back_icon.png"
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def render(self):
        # menu item
        self.render_text(self.name, int(DISPLAY_WIDTH/2), 70, colors["orange"], 40)

        # render sound icon
        self.buttons["back_icon"] = self.render_image(Description.back_icon_path, int(DISPLAY_WIDTH/2), int(DISPLAY_HEIGHT - 50))

    def scene_events(self, event):
       if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button:
                self.click = True
                for button in self.buttons: 
                    controle.to_destination_scene()

class Controle: 
    def __init__(self):
        self.scenes = {}
        self.scenes["menu_music_on"] = Menu("./assets/icons/music_on_icon.png")
        self.scenes["menu_music_off"] = Menu("./assets/icons/music_off_icon.png")
        self.scenes["option_menu_description"] = Description("Options")

    def to_destination_scene(self):
        """ Checks if mouse points to a text or button (rect) """
        self.mx, self.my = pygame.mouse.get_pos()
        if self.scenes["menu_music_on"].buttons["music on"].collidepoint((self.mx, self.my)) and self.scenes["menu_music_on"].click:
            self.scenes["menu_music_on"].click = False
            self.scenes["menu_music_off"].run_scene()
        elif self.scenes["menu_music_on"].buttons["music on"].collidepoint((self.mx, self.my)) and self.scenes["menu_music_off"].click:
            self.scenes["menu_music_off"].click = False
            self.scenes["menu_music_on"].run_scene()

    def run_scene(self):
        self.scenes["option_menu_description"].run_scene()

    

controle = Controle()
controle.run_scene()


    
       



