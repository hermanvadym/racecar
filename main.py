import pygame

def find_screen_center(screen):
    screen_width = screen.get_width() / 2
    screen_height = screen.get_height() / 2
    return screen_width, screen_height

def main():
    print("It's nice to see another soul that likes to be challenged!")

    #pygame setup 
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    dt = 0 # stores the time in seconds since last frame, used for smooth movement
    
    player_screen_width, player_screen_height = find_screen_center(screen)
    player_car = pygame.Rect(player_screen_width, player_screen_height + 350, 100, 120)
   

    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from the last frame
        screen.fill("black") # clear screen

        pygame.draw.rect(screen, "red", player_car)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_car.y -= 300 * dt
        if keys[pygame.K_s]:
            player_car.y += 300 * dt
        if keys[pygame.K_a]:
            player_car.x -= 300 * dt
        if keys[pygame.K_d]:
            player_car.x += 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip() # show the frame

        dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit

main()