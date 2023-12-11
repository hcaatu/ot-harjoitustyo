import os
import pygame
import upgrade
from particles import Particle

# path to the directory of this file
dirname = os.path.dirname(__file__)

class AppUI:
    """Class providing screen rendering functions, and at the moment particle effects.
    """
    def __init__(self):
        """Construnctor function that assigns a value to all attributes.
        """
        pygame.init()
        self.resolution = (1280, 720)
        self.window = pygame.display.set_mode(self.resolution)

        self.show = {"textbox" : False, "upgrades" : False}
        self.images = {}
        self.particles = []
        self.timers = {"game_saved": 0, "coffee_maker": 0, "aeropress": 0, "particle": 0}
        self.font = pygame.font.SysFont("Arial", 24)

        self.load_images()

        self.data = [upgrade.CoffeeMaker(), upgrade.AeroPress()]

        self.score = 0
        self.profit = 0
        self.upgrades = {"coffee_maker": 0, "aeropress" : 0}
        self.cost = {"coffee_maker": self.data[0].cost,
                     "aeropress": self.data[1].cost}

        self.pos = {}
        self.safezone = 18
        self.calculate_positions()
        
    def load_images(self):
        """Load images using pygame built in image.load function.
        """
        filenames = ["coffee", "bars", "coffee_maker", "textbox", "aeropress"]
        for name in filenames:
            self.images[name] = (pygame.image.load(
                os.path.join(dirname, "assets", name + ".png")
            ))
        self.images["small_coffee"] = self.images["coffee"]
        self.images["big_coffee"] = pygame.transform.scale_by(self.images["coffee"], [1.2, 1.2])

    def calculate_positions(self):
        """Calculates UI elements poisitions in coordinate form and stores them in dict.
        """
        self.pos["center"] = self.get_center(self.images["coffee"])
        self.pos["textbox"] = [0, 0]
        self.pos["upgrade0"] = (
            self.resolution[0] - self.images["bars"].get_width() - self.safezone, self.safezone)
        self.pos["coffee_maker"] = (self.pos["upgrade0"][0], self.pos["upgrade0"][1] + 86)
        self.pos["aeropress"] = (self.pos["coffee_maker"][0], self.pos["coffee_maker"][1] + 86)

    def render_text(self):
        """Renders text for a given window.
        """
        black = (0, 0, 0)
        font = self.font
        counter = font.render(f"Coffee: {str(int(self.score))}", True, black)
        self.window.blit(counter, (self.safezone, self.safezone))
        score_per_second = font.render(
            f"{str(self.profit)} coffee/second", True, black)
        self.window.blit(score_per_second, (self.safezone, self.safezone + 26))

    def render_with_timer(self, msg, pos=None):
        """Renders a text with a given time in seconds.

        Args:
            msg (str): Shortened code for the displayed text.
            pos (tuple, optional): Position of the upper left corner of the text. Defaults to None.
        """
        black = (0, 0, 0)
        size = 28
        font = pygame.font.SysFont("Arial", size)
        if msg == "game_saved":
            pos = (self.safezone, self.resolution[1] - size - self.safezone)
            text = font.render("Game saved!", True, black)
        else:
            pos = (self.textbox_pos[0] + 5, self.textbox_pos[1] - 35)
            text = font.render("Not enough coffee!", True, black)
            if self.score >= self.cost[msg]:
                self.timers[msg] = 0
                return
        self.window.blit(text, pos)
        self.timers[msg] -= 1

    def render_textbox(self, pos):
        """Renders a info box for an upgrade when hovering over.

        Args:
            pos (tuple): Coordinate of the upper left pixel.
        """
        margin = 15
        leading = 26
        black = (0, 0, 0)
        font = self.font
        self.window.blit(self.images["textbox"], pos)

        if self.show["textbox"] == "coffee_maker":
            display_data = ["Coffee maker", 0, "Makes more coffee"]
        if self.show["textbox"] == "aeropress":
            display_data = ["Aeropress", 1, "Presses with air :o"]
        
        self.window.blit((font.render(display_data[0], True, black)),
                    [margin + i for i in pos])
        
        if self.upgrades[self.show["textbox"]] != 0:
            count = ": " + str(self.upgrades[self.show["textbox"]])
            self.window.blit((font.render(count, True, black)),
                        (132 + pos[0], margin + pos[1]))
            
        # assigning variable before using it in f-string fixes syntax error in wsl, hence pylint comment

        decimal_format = "{:.2f}".format(self.cost[self.show["textbox"]]) # pylint: disable=consider-using-f-string

        self.window.blit((font.render(f"Cost: {decimal_format}", True, black)), (
            pos[0] + margin, pos[1] + margin + leading))
        
        self.window.blit((
            font.render(f"Produces {self.data[display_data[1]].profit} coffee per second", True, black)), (
            pos[0] + 15, pos[1] + margin + 2 * leading))
        
        italic = pygame.font.SysFont("Arial", 24, False, True)

        self.window.blit((italic.render(display_data[2], True, black)),
                    (pos[0] + 25, pos[1] + 105))

    def mouse_collide(self, icon, pos, event):
        """Detects whether or not the mouse is on top of a surface element.

        Args:
            icon (pygame.surface): A surcace element on screen.
            pos (tuple): The position of the surface.
            event (pygame.event): Current mouse position.

        Returns:
            bool: True/False if mouse is colliding with a surface object.
        """
        icon_coords = [pos[0], pos[0] + icon.get_width(), pos[1],
                       pos[1] + icon.get_height()]
        if icon_coords[0] < event.pos[0] < icon_coords[1]:
            if icon_coords[2] < event.pos[1] < icon_coords[3]:
                return True
        return False

    def render_motion_elements(self, event):
        """Renders UI elements that are generated by mouse movement.
        First checking if mouse is on top of any upgrade icons, then if on top of coffee icon.

        Args:
            event (pygame.event): Current mouse position.
        """
        count = 0
        for upgrade in self.data:
            if not self.mouse_collide(self.images[upgrade.name], self.pos[upgrade.name], event):
                count += 1
                continue
            if self.show["upgrades"]:
                self.textbox_pos = (
                    event.pos[0] - self.images["textbox"].get_width(), event.pos[1])
                self.show["textbox"] = upgrade.name

        if count == len(self.data):
            self.show["textbox"] = False
            for upgrade in self.data:
                self.timers[upgrade.name] = 0

        if self.mouse_collide(self.images["coffee"], self.pos["center"], event):
            self.images["coffee"] = self.images["big_coffee"]
            self.pos["center"] = self.get_center(self.images["coffee"])
        else:
            self.images["coffee"] = self.images["small_coffee"]
            self.pos["center"] = self.get_center(self.images["coffee"])

    
    def render_particles(self, particle):
        """Renders particles using the Particle class and tweaks parameters accordingly.

        Args:
            particle (Particle object)
        """
        pos = Particle.calculate_pos(self, particle)
        self.window.blit(particle.img, pos)
        self.timers["particle"] -= 1
        particle.timestep += 0.5
        particle.alpha -= 3
        particle.img.set_alpha(particle.alpha)

    def render_elements(self):
        """Renders all non-moving elements on the screen.
        """
        self.window.blit(self.images["coffee"], (self.pos["center"]))
        self.window.blit(self.images["bars"], (self.pos["upgrade0"]))
        grey_box = pygame.surface.Surface(
            (self.images["coffee_maker"].get_width(),
              self.images["coffee_maker"].get_height()))
        grey_box.fill((255,255,255))
        grey_box.set_alpha(100)
        if self.show["upgrades"]:
            self.window.blit(self.images["coffee_maker"], self.pos["coffee_maker"])
            self.window.blit(self.images["aeropress"], self.pos["aeropress"])
            for k, v in self.cost.items():
                if self.score < v:
                    self.window.blit(grey_box, self.pos[k])

    def fill_screen(self):
        """Fills the screen with grey color.
        """
        self.window.fill((200, 200, 200))

    def get_center(self, icon):
        """Calculates center with offset for blitting the upper left corner.

        Args:
            icon (pygame.surface): Image

        Returns:
            center (tuple): Coordinates for the topleft corner of the center icon.
        """
        center = (self.resolution[0]/2 - icon.get_width()/2,
                  self.resolution[1]/2 - icon.get_height()/2)
        return center
