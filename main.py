import pygame

def find_screen_center(screen):
    screen_width_center = screen.get_width() / 2
    screen_height_center = screen.get_height() / 2
    return screen_width_center, screen_height_center

def main():
    print("It's nice to see another soul that likes to be challenged!")

    # pygame setup 
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    clock = pygame.time.Clock()
    running = True
    dt = 0 # stores the time in seconds since last frame, used for smooth movement
    
    # --- Game Objects ---
    player_screen_width_center, player_screen_height_center = find_screen_center(screen)
    player_car_width = 80
    player_car_height = 120
    player_car = pygame.Rect(player_screen_width_center, player_screen_height_center + 350, player_car_width, player_car_height)

    # road's width
    ROAD_WIDTH = 30
    HALF_ROAD_WIDTH = ROAD_WIDTH / 2

    # original road's center points for drawing
    left_road_center = player_screen_width_center - 300
    right_road_center = player_screen_height_center + 780

    # road boundaries based on line drawing coordinates, the car's top-left x should not go below this value
    left_road_boundary = left_road_center + HALF_ROAD_WIDTH
    # the car's right-most edge (player_car.x + player_car.width) should not go above this value
    right_road_boundary = right_road_center - HALF_ROAD_WIDTH
    # to find the correct maximum value for player_car.x to clamp the x position
    max_player_x = right_road_boundary - player_car.width

    while running:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from the last frame
        screen.fill("black") # clear screen


        # added left and right lines to represent a road
        pygame.draw.line(screen, "white", (left_road_center, screen.get_height()), (left_road_center, 0), width = ROAD_WIDTH)
        pygame.draw.line(screen, "white", (right_road_center, screen.get_height()), (right_road_center, 0), width = ROAD_WIDTH)

        # draw the player's car
        pygame.draw.rect(screen, "red", player_car)

        # movement logic 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player_car.y > 20:
            player_car.y -= 1300 * dt
        if keys[pygame.K_s] and player_car.y < 900:
            player_car.y += 1300 * dt
        
        # move left and clamp position 
        if keys[pygame.K_a]:
            player_car.x -= 1300 * dt
            if player_car.x < left_road_boundary:
                player_car.x = left_road_boundary
                
       
        # move right and clamp position 
        if keys[pygame.K_d] and player_car.x:
            player_car.x += 1300 * dt
            if player_car.x > max_player_x:
                player_car.x = max_player_x
        #print(player_car.x)

        
        # flip() the display to put your work on screen
        pygame.display.flip() # show the frame

        # limits FPS to 60
        dt = clock.tick(60) / 1000 

pygame.quit

main()