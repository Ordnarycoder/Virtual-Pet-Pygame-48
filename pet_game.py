import pygame
import sys

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class VirtualPet:
    def __init__(self, name, image):
        self.name = name
        self.image = image  # A Pygame surface for the pet's image
        self.hunger = 50   # 0 to 100, where 100 is very hungry
        self.happiness = 50  # 0 to 100, where 100 is very happy

    def feed(self):
        # Lower hunger, increase happiness
        self.hunger = max(0, self.hunger - 10)
        self.happiness = min(100, self.happiness + 5)

    def play(self):
        # Increase happiness, slightly increase hunger
        self.happiness = min(100, self.happiness + 10)
        self.hunger = min(100, self.hunger + 5)

    def update(self):
        # Slowly increase hunger over time and reduce happiness
        self.hunger = min(100, self.hunger + 0.05)
        self.happiness = max(0, self.happiness - 0.05)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Virtual Pet Game")

    # Load pet image
    pet_image = pygame.image.load('pet_image.jpeg').convert_alpha()  # Ensure you have a pet image file
    pet = VirtualPet("Buddy", pet_image)

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Check for key presses for interactions
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    pet.feed()
                elif event.key == pygame.K_p:
                    pet.play()

        # Update pet status
        pet.update()

        # Draw everything
        screen.fill(WHITE)
        # Draw the pet image
        screen.blit(pet.image, (350, 250))
        # Draw pet status texts
        hunger_text = font.render(f"Hunger: {int(pet.hunger)}", True, BLACK)
        happiness_text = font.render(f"Happiness: {int(pet.happiness)}", True, BLACK)
        screen.blit(hunger_text, (50, 50))
        screen.blit(happiness_text, (50, 100))
        # Instructions
        instructions_text = font.render("Press 'F' to feed, 'P' to play!", True, BLACK)
        screen.blit(instructions_text, (50, 150))
        pygame.display.flip()
        clock.tick(60)
        
        # Check conditions to end the game
        # For example: if the pet is extremely hungry or very unhappy
        if pet.hunger >= 100 or pet.happiness <= 0:
            print("Your pet has run away!")
            running = False

    # Clean up and exit the game
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
# Note: Make sure to replace 'pet_image.jpeg' with the path to your pet image file.