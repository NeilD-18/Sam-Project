import pygame, time, random

# Initialize pygame and set up the display window
pygame.init()

WIDTH = 640
HEIGHT = 480
RADIUS = 10
MY_WIN = pygame.display.set_mode((WIDTH, HEIGHT))

SHIP_DX = 5
LASER_DY = 5
SCORE = 0

def collide(circ1, circ2):
    ((x1, y1), r1) = circ1
    ((x2, y2), r2) = circ2
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return d <= r1 + r2

def fire_laser(lasers, ship):
    lasers.append(ship)

def move_ship_left(ship):
    (sx, sy) = ship
    sx = sx - SHIP_DX
    if sx < 0:
        sx = 0
    return (sx, sy)

def move_ship_right(ship):
    (sx, sy) = ship
    sx = sx + SHIP_DX
    if sx > WIDTH:
        sx = WIDTH
    return (sx, sy)

def draw_ship(ship):
    global MY_WIN
    (sx, sy) = ship
    outline = [(sx, sy + 10), (sx - 10, sy - 10), (sx + 10, sy - 10)]
    pygame.draw.polygon(MY_WIN, pygame.color.Color('blue'), outline)

def draw_lasers(lasers):
    global MY_WIN
    for laser in lasers:
        (bx, by) = laser
        pygame.draw.circle(MY_WIN, pygame.color.Color('white'), (bx, by), RADIUS)

def move_lasers(lasers):
    global LASER_DY, RADIUS, HEIGHT
    new_lasers = []
    for laser in lasers:
        (bx, by) = laser
        by = by + LASER_DY
        if by <= HEIGHT + RADIUS:
            new_lasers.append((bx, by))
    return new_lasers

def draw_background():
    global MY_WIN
    background_img = pygame.image.load('space.bmp').convert()
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
    MY_WIN.blit(background_img, (0, 0))

def draw_score():
    global SCORE, MY_WIN, WIDTH
    font = pygame.font.SysFont("monospace", 20)
    score_display = font.render("Score: %d" % SCORE, 0, (255, 255, 255))
    MY_WIN.blit(score_display, (WIDTH - 150, 20))

def move_alien(alien, x, y):
    (ax, ay) = alien
    ax = ax + x
    ay = ay + y
    return (ax, ay)

def move_aliens(aliens):
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    for i in range(len(aliens)):
        aliens[i] = move_alien(aliens[i], x, y)

def draw_alien(alien):
    global MY_WIN
    pygame.draw.rect(MY_WIN, pygame.color.Color('red'), (alien[0], alien[1], 10, 10))

def draw_aliens(aliens):
    for alien in aliens:
        draw_alien(alien)

def remove_aliens(aliens, lasers):
    global RADIUS, SCORE
    new_aliens = []
    for alien in aliens:
        collided = False
        for laser in lasers:
            if collide((alien, RADIUS), (laser, RADIUS)):
                print("Hit Alien!")
                SCORE += 1
                collided = True
                pygame.mixer.music.load("pop.wav")
                pygame.mixer.music.play(1)
                break
        if collided:
            lasers.remove(laser)
        else:
            new_aliens.append(alien)
    return (new_aliens, lasers)

def add_aliens(aliens):
    global HEIGHT, WIDTH
    if random.randint(0, 10) == 0:
        aliens.append((random.randint(0, WIDTH), random.randint(100, HEIGHT)))

def update_game(aliens, firing, lasers, ship, west, east, pause):
    if not pause:
        add_aliens(aliens)
        if firing:
            fire_laser(lasers, ship)
        if west == 1:
            ship = move_ship_left(ship)
        if east == 1:
            ship = move_ship_right(ship)
        lasers = move_lasers(lasers)
        move_aliens(aliens)
        (aliens, lasers) = remove_aliens(aliens, lasers)
    return (aliens, lasers, ship)

def run_game():
    FPS = 60
    global ship
    ship = (320, 50)
    lasers = []
    aliens = []
    frame = 0
    has_won = False
    firing = False
    west = -1
    east = -1
    pause = False

    while not has_won:
        frame += 1
        time.sleep(1.0 / FPS)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                key_pressed = event.dict['key']
                if key_pressed == pygame.K_LEFT:
                    west = 1
                elif key_pressed == pygame.K_RIGHT:
                    east = 1
                elif key_pressed == ord(" "):
                    firing = True
                elif key_pressed == ord('q'):
                    pygame.quit()
                    return
                elif key_pressed == ord('p'):
                    pause = not pause
            elif event.type == pygame.KEYUP:
                key_released = event.dict['key']
                if key_released == pygame.K_LEFT:
                    west = -1
                if key_released == pygame.K_RIGHT:
                    east = -1
                if key_released == ord(" "):
                    firing = False

        (aliens, lasers, ship) = update_game(aliens, firing, lasers, ship, west, east, pause)
        draw_background()
        draw_lasers(lasers)
        draw_aliens(aliens)
        draw_ship(ship)
        draw_score()
        pygame.display.update()
    pygame.quit()

run_game()
