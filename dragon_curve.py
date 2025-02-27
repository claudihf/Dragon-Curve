# This file is to create the path's of ith's dragon curve iteration
import random
import pygame

def change_orientation(start: str, pathway: str):
    """A helper function that will keep change the orientation for each pathway made
    """
    if start == "F":
        if pathway == "right":
            return "R"
        if pathway == "left":
            return "L"
    if start == "R":
        if pathway == "right":
            return "D"
        if pathway == "left":
            return "F"
    if start == "D":
        if pathway == "right":
            return "L"
        if pathway == "left":
            return "R"
    if start == "L":
        if pathway == "right":
            return "F"
        if pathway == "left":
            return "D"

def create_path(og_path: list[str]):
    """ This function will create the basis of any path based on what is given 
    as an original path
    """
    # If side is true: The side it is on is the Right side and vice versa
    side = True

    path = ["right"]
    for direction in og_path:
        if direction == "right":
            if side is False:
                path.extend(["right", "right"])
            if side is True:
                path.extend(["right", "left"])
        if direction == "left":
            if side is False:
                path.extend(["left", "right"])
            if side is True:
                path.extend(["left", "left"])
        side = not side
    return path

def ith_path(iterations: int):
    """ This function will utilise the create_path function to make however many
    iterations of the recursive patterned path of the dragon curve
    """
    original = []
    for i in range(iterations):
        original = create_path(original)
    
    return original

# starting coords
x0 = 100
y0 = 100

orientation = "forward"

def read_next_coords(start_x, start_y, direction: str, oriented: str, amount: int):
    """ This function will take whichever coordinates given and create the next coordinate
    start_x : integer that represents x coordinate that we work from
    start_y : integer that represents y coordinate that we work from
    direction: string that is either "right" or "left"
    oriented: string tells us which way we are pointing in the direction of
    amount: integer that says how much we travel each time
    """
    
    # Turning right
    if direction == "right":
        if oriented == "F":
            return(start_x + amount, start_y)
        if oriented == "R":
            return (start_x, start_y + amount)
        if oriented == "D":
            return (start_x - amount, start_y)
        if oriented == "L":
            return (start_x, start_y - amount)
    
    # Turning left
    if direction == "left":
        
        # Depending on said turning path and then which way it is oriented, 
        # it will out put the next coordinates
        if oriented == "F":
            return (start_x - amount, start_y)
        if oriented == "R":
            return (start_x, start_y - amount)
        if oriented == "D":
            return (start_x + amount, start_y)
        if oriented == "L":
            return (start_x, start_y + amount)

def read_all_coords(path: list, ogx: int, ogy: int, amount: int):
    """ Using the helper function of read_next_coords() we will be able to input
    a list of directions it turns and can output a string of coordinates based 
    on the starting coordinate
    """
    point = "F"
    coords = [(ogx, ogy)]
    for direction in path:
        coords.append(read_next_coords(ogx, ogy, direction, point, amount))
        ogx = coords[-1][0]
        ogy = coords[-1][1]
        point = change_orientation(point, direction)
    return coords


# Displaying said dragon curve
pygame.init()
window = pygame.display.set_mode((840, 640))
clock = pygame.time.Clock()

# Base measurements
running = True
base_x = 420
base_y = 320
iteration = 10
amount = 5
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Ways that the user can adjust the measurements
        if event.type == pygame.KEYDOWN:
            
            # Increases the complexity of dragon curve
            if event.key == pygame.K_c:
                iteration = iteration + 1
            
            # Decreases the complexity of dragon curve
            if event.key == pygame.K_d:
                if iteration > 1:
                    iteration = iteration - 1
                window.fill("black")
            
            # Zooms out of the window
            if event.key == pygame.K_o:
                amount = amount * 0.8
                window.fill("black")
            if event.key == pygame.K_i:
                amount = amount * 1.2
                window.fill("black")
            
            # Move around
            if event.key == pygame.K_DOWN:
                base_y += 5
                window.fill("black")
            if event.key == pygame.K_UP:
                base_y -= 5
                window.fill("black")
            if event.key == pygame.K_RIGHT:
                base_x += 5
                window.fill("black")
            if event.key == pygame.K_LEFT:
                base_x -= 5
                window.fill("black")
    
    path = ith_path(iteration)
    coords = read_all_coords(path, base_x, base_y, amount)
    pygame.draw.lines(window, (255, 255, 255), False, coords, width =1)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()