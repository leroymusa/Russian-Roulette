# Import Required Libraries
import pygame
from pygame.locals import *
import time

# Initialize Pygame
pygame.init()

# Set up the Window
width, height = 800, 600  # Adjust these values to your desired window size
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bullet Animation")  # Set the window title

# Load the Bullet Image
bullet_image = pygame.image.load("bullet.png")  # Replace "bullet.png" with the path to your bullet image
bullet_rect = bullet_image.get_rect()

# Set up Animation Variables
bullet_x = -bullet_rect.width  # Starting x-coordinate of the bullet (off-screen to the left)
bullet_y = height // 2 - bullet_rect.height // 2  # Starting y-coordinate of the bullet (centered vertically)
speed = 10  # Adjust the speed of the bullet animation

# Animation Text Settings
main_text = "RUSSIAN ROULETTE"
main_text_color = (255, 255, 255)  # Set text color to white
main_text_size = 48
main_text_font = pygame.font.Font("Courier.ttc", main_text_size)

sub_text = "by Leroy Musa"
sub_text_color = (255, 255, 255)  # Set text color to white
sub_text_size = 36
sub_text_font = pygame.font.Font("cmunit.ttf", sub_text_size)

# Typewriter Animation Variables
typewriter_delay = 100  # Adjust the delay between each character
typewriter_index_main = 0
typewriter_index_sub = 0
typewriter_text_main = ""
typewriter_text_sub = ""
typewriter_complete_main = False
typewriter_complete_sub = False

# Load Sound Effect
pow_sound = pygame.mixer.Sound("russian roulette audio.wav")  # Replace "russian roulette audio.wav" with the path to your sound effect file
pow_sound_played = False

# Play Button Settings
button_width = 200
button_height = 80
button_color = (255, 255, 255)  # Set button color to white
button_text = "Play"
button_text_color = (0, 0, 0)  # Set button text color to black
button_text_size = 32
button_text_font = pygame.font.Font(None, button_text_size)  # Use default font with specified size

# Calculate the position of the button
button_x = width // 2 - button_width // 2
button_y = height // 2 - button_height // 2

# Beating Animation Variables
button_scale = 1.0
button_scale_direction = 1
button_scale_speed = 0.01

# Animation Loop
animation_running = True
game_running = False
while animation_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            animation_running = False
            game_running = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                animation_running = False
                game_running = True

    # Update Bullet Position
    bullet_x += speed  # Adjust the speed of the bullet animation

    # Clear the Window
    window.fill((0, 0, 0))

    # Draw Bullet
    window.blit(bullet_image, (bullet_x, bullet_y))

    # Check if Bullet is off-screen
    if bullet_x > width:
        if not pow_sound_played:
            # Play Sound Effect
            pow_sound.play()
            pow_sound_played = True

        # Typewriter Effect for "Russian Roulette"
        if not typewriter_complete_main:
            typewriter_text_main += main_text[typewriter_index_main]
            typewriter_index_main += 1
            if typewriter_index_main >= len(main_text):
                typewriter_complete_main = True
            time.sleep(typewriter_delay / 1000)  # Delay between each character

        # Typewriter Effect for "Leroy Musa"
        if typewriter_complete_main and not typewriter_complete_sub:
            typewriter_text_sub += sub_text[typewriter_index_sub]
            typewriter_index_sub += 1
            if typewriter_index_sub >= len(sub_text):
                typewriter_complete_sub = True
            time.sleep(typewriter_delay / 1000)  # Delay between each character

        # Display Animation Text
        main_text_surface = main_text_font.render(typewriter_text_main, True, main_text_color)
        main_text_rect = main_text_surface.get_rect(center=(width // 2, height - 200))  # Position the main text at the bottom
        sub_text_surface = sub_text_font.render(typewriter_text_sub, True, sub_text_color)
        sub_text_rect = sub_text_surface.get_rect(center=(width // 2, height - 150))  # Position the sub text below the main text

        window.blit(main_text_surface, main_text_rect)  # Draw main text
        window.blit(sub_text_surface, sub_text_rect)  # Draw sub text

        # Animate Play Button
        button_scale += button_scale_direction * button_scale_speed
        if button_scale >= 1.2 or button_scale <= 0.8:
            button_scale_direction *= -1

        scaled_button_width = int(button_width * button_scale)
        scaled_button_height = int(button_height * button_scale)
        scaled_button_x = button_x - (scaled_button_width - button_width) // 2
        scaled_button_y = button_y - (scaled_button_height - button_height) // 2

        # Draw Scaled Play Button
        pygame.draw.rect(window, button_color, (scaled_button_x, scaled_button_y, scaled_button_width, scaled_button_height))

        # Animate Play Text
        play_text_scale = button_scale  # Use the same scale as the button
        scaled_play_text_size = int(button_text_size * play_text_scale)
        play_text_font = pygame.font.Font(None, scaled_play_text_size)
        play_text_surface = play_text_font.render(button_text, True, button_text_color)
        play_text_rect = play_text_surface.get_rect(center=(width // 2, height // 2))
        play_text_rect.y = height // 2 - play_text_rect.height // 2
        window.blit(play_text_surface, play_text_rect)

    # Update the Display
    pygame.display.update()

# Game Loop
while game_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_running = False

    # Handle Button Click
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if scaled_button_x <= mouse_pos[0] <= scaled_button_x + scaled_button_width and scaled_button_y <= mouse_pos[1] <= scaled_button_y + scaled_button_height:
        if mouse_click[0] == 1:
            print("Play button clicked")  # Add your desired action here

    # Update the Display
    pygame.display.update()

# Quit Pygame
pygame.quit()
