import pygame

def find_screen_center(screen):
    screen_width_center = screen.get_width() / 2
    screen_height_center = screen.get_height() / 2
    return screen_width_center, screen_height_center

def main():
    print("It's nice to see another soul that likes to be challenged!")

    #pygame setup 
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    dt = 0 # stores the time in seconds since last frame, used for smooth movement
    
    player_screen_width_center, player_screen_height_center = find_screen_center(screen)
    player_car = pygame.Rect(player_screen_width_center, player_screen_height_center + 350, 100, 120)
    
    #left_line = w3
   

    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from the last frame
        screen.fill("black") # clear screen

        pygame.draw.rect(screen, "red", player_car)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_car.y > 20:
            player_car.y -= 1300 * dt
        if keys[pygame.K_s] and player_car.y < 850:
            player_car.y += 1300 * dt
        if keys[pygame.K_a] and player_car.x > 5:
            player_car.x -= 1300 * dt
        if keys[pygame.K_d] and player_car.x < 1798:
            player_car.x += 1300 * dt
        
        #print(player_car.x)


        # flip() the display to put your work on screen
        pygame.display.flip() # show the frame

        dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit

main()