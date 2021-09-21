# package samples;

import pygame

# Hard coded screen values
SCREEN_WIDTH  = 500
SCREEN_HEIGHT = 500


# Basic pygame for animation
class PygameSample:
    x = 0.0
    lastUpdateTime = 0  # Used for speed of animation

    def __init__(self):
        pygame.init()
        # Set up the drawing window
        self.screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    def run(self):
        # Run until the user asks to quit
        running = True
        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.render()
        # stop running
        print("Goodbye!")
        pygame.quit()

    def render(self):
        # Fill the background with white
        self.screen.fill((255, 255, 255))
        # Draw a solid blue circle in the center
        pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
        # Flip the display - without this, nothing is visible!
        pygame.display.flip()


if __name__ == "__main__":
    PygameSample().run()
else:
    print("Welcome to the Pygame Sample! To run, call run()")
