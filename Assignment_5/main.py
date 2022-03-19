import pygame
from pygame_classes import *
from sensor_model import *

pygame.init()
# Create clock object for setting the frame-rate for display update
clock = pygame.time.Clock()
FPS = 50

display_width = 500
display_height = 700
pygame_display = pygame.display.set_mode((display_width, display_height))

bot_radius = 20
white = (255, 255, 255)
black = (0,0,0)
pygame_display.fill(white)

wall_thickness = 5
w_offset = wall_thickness / 2 # w_offset is purely for visual purposes: makes walls fit perfectly to edge of screen
wall_north = [(0+w_offset, 0+w_offset), (500-w_offset, 0+w_offset)]
wall_south = [(0+w_offset, 700-w_offset), (500-w_offset, 700-w_offset)]
wall_west = [(0+w_offset, 0+w_offset), (0+w_offset, 700-w_offset)]
wall_east = [(500-w_offset, 0+w_offset),  (500-w_offset, 700-w_offset)]
wall_c1 = [(0,150),(300,150)]
wall_c2 = [(175,300), (500,300)]
wall_c3 = [(175,300),(175, 575)]
wall_c4=[(340, 450),(340, 700)]
walls = [wall_north, wall_south, wall_east, wall_west, wall_c1, wall_c2, wall_c3, wall_c4]

beacon_A = Beacon(0+w_offset, 0+w_offset)
beacon_B = Beacon(500-w_offset, 0+w_offset)
beacon_C = Beacon(0+w_offset, 150)
beacon_D = Beacon(300, 150)
beacon_E = Beacon(175, 300)
beacon_F = Beacon(500-w_offset, 300)
beacon_G = Beacon(175, 575)
beacon_H = Beacon(340, 450)
beacon_I = Beacon(0+w_offset, 700-w_offset)
beacon_J = Beacon(340, 700-w_offset)
beacon_K = Beacon(500-w_offset, 700-w_offset)
beacons = [beacon_A, beacon_B, beacon_C, beacon_D, beacon_E, beacon_F, beacon_G, beacon_H, beacon_I, beacon_J, beacon_K]

robot = Robot(pygame_display=pygame_display,
              radius=bot_radius,
              color=black,
              position=(60,60,0),
              distance_between_wheels=bot_radius*2,
              acceleration=10,
              angular_acceleration=1,
              FPS=FPS,
              current_time=0)

def simulation(display, bot, walls, beacons, FPS=50):
    while True:
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # pygame.QUIT gets called when we press the 'x' button on the window
                return  # exit out of the function call to end the display
            if event.type == pygame.KEYDOWN:
                key = event.key
        bot.move(key=key, time_elapsed=1/FPS, verbose=False)

        display.fill(white)
        bot.draw()
        for wall in walls:
            pygame.draw.line(display, black, wall[0], wall[1], wall_thickness)
        for beacon in beacons:
            pygame.draw.circle(display, (255,0,0), (beacon.x, beacon.y), 5)

        # update the display - using clock object to set frame-rate
        pygame.display.update()
        clock.tick(FPS)

# call the function simulation to keep the display running until we quit
simulation(pygame_display, robot, walls, beacons, FPS)

# End the pygame display
pygame.quit()