import pygame
from particles import Particle

class EventHandler:
    def __init__(self):
        self.running = True

    def handle_events(self, event, ui, app):
        """Classifies the event type and uses the appropriate handler function.

        Args:
            event (pygame.event)
            ui (AppUI object)
            app (App object)

        Returns:
            bool: False, if user quits. Otherwise true.
        """
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.KEYDOWN:
            self.running = self._handle_keyboard_inputs(event, ui, app)

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = self._handle_mouse_inputs(event, ui, app)

        if event.type == pygame.MOUSEMOTION:
            ui.render_motion_elements(event)

        return self.running

    def _handle_mouse_inputs(self, event, ui, app):
        """Handles mouse movement and clicks.

        Uses the pygame.event, which contains mouse position data and the mouse_collide
        function to check if mouse clicks or hovers on UI elements.

        Args:
            event (pygame.event)
            ui (AppUI object)
            app (App object)

        Returns:
            bool: True, since user can't quit with mouse inputs.
        """
        if ui.mouse_collide(ui.images["coffee"], ui.pos["center"], event):
            app.apply_score()
            ui.particles.append(Particle())

        if ui.mouse_collide(ui.images["golden"], ui.pos["golden"], event):
            app.golden_click()
            ui.timers["golden"] = 0

        if ui.mouse_collide(ui.images["bars"], ui.pos["upgrade0"], event):
            if ui.show["upgrades"]:
                ui.show["upgrades"] = False
            else:
                ui.show["upgrades"] = True

        # Loops over upgrade positions on screen and checks if they're hit
        for upgrade in app.data:
            if not ui.mouse_collide(ui.images[upgrade.name], ui.pos[upgrade.name], event):
                continue
            if not ui.show["upgrades"]:
                continue
            if app.buy_upgrade(upgrade, app.cost[upgrade.name]):
                ui.cost[upgrade.name] *= 1.1
            else:
                ui.timers[upgrade.name] = 1.5*app.tickrate

        return True

    def _handle_keyboard_inputs(self, event, ui, app):
        """Handles keyboard inputs, namely quitting, saving, and cheating.

        Args:
            event (pygame.event)
            ui (AppUI object)
            app (App object)

        Returns:
            bool: False, if user quits.
        """
        if event.key == pygame.K_ESCAPE:
            return False

        if event.key == pygame.K_s:
            app.save_game()
            ui.timers["game_saved"] = 2*app.tickrate

        if event.key == pygame.K_g:
            app.score += 1000 # cheat

        return True
