import pygame as pg

SIZE = WIDTH, HEIGHT = 800, 600
GRAY = (128, 128, 128)

pg.init()
pg.display.set_caption("Rally")
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()


class Car(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Image/car1.png")


car1 = Car()
car1_image = car1.image
car1_w, car1_h = car1.image.get_width(), car1.image.get_height()
# print(car1_w, car1_h)
car1.x, car1.y = (WIDTH - car1_w) // 2, (HEIGHT - car1_h) // 2

game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    car1.y -= 1
    if car1.y < -car1_h:
        car1.y = HEIGHT

    screen.fill(GRAY)
    screen.blit(car1_image, (car1.x, car1.y))
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f"Rally    FPS: {int(clock.get_fps())}")

# New

import pygame as pg
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

SIZE = WIDTH, HEIGHT = 800, 600
GRAY = (128, 128, 128)

pg.init()
pg.display.set_caption('Rally')
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()
GREEN = (0, 128, 0)
WHEIT = (200, 200, 200)

bg_image = pg.image.load('Image/road.jpg')
bg_image_rect = bg_image.get_rect(topleft=(0, 0))
bg_image_2_rect = bg_image.get_rect(topleft=(0, -HEIGHT))
car1_image = pg.image.load('Image/car1.png')


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Image/car4.png')


class Car(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, s, img):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.image = pg.transform.flip(self.image, False, True)
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.speed = s
        self.rect = self.image.get_rect(center=(self.x, self.y))


play = Player()
play_image = play.image
play_w, play_h = play.image.get_width(), play.image.get_height()
play.x, play.y = (WIDTH - play_w) // 2, (HEIGHT - play_h) // 2


car1 = Car(
    WIDTH // 2 + 80, HEIGHT // 2,
    car1_image.get_width(), car1_image.get_height(), 1, car1_image)


def bg():
    pg.draw.line(screen, GREEN, (20, 0), (20, 600), 40)
    pg.draw.line(screen, GREEN, (780, 0), (780, 600), 40)
    for xx in range(10):
        for yy in range(10):
            pg.draw.line(
                screen, WHEIT,
                (40 + xx * 80, 0 if xx == 0 or xx == 9 else 10 + yy * 60),
                (40 + xx * 80, 600 if xx == 0 or xx == 9 else 50 + yy * 60), 5)


game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    bg_image_rect.y += 1
    if bg_image_rect.y > HEIGHT:
        bg_image_rect.y = 0
    bg_image_2_rect.y += 1
    if bg_image_2_rect.y > 0:
        bg_image_2_rect.y = -HEIGHT

    screen.fill(GRAY)
    # bg()
    for i in range(2):
        screen.blit(bg_image, bg_image_rect if i == 0 else bg_image_2_rect)
    screen.blit(car1.image, car1.rect)
    screen.blit(play.image, (play.x, play.y))
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f'Rally   FPS: {int(clock.get_fps())}')

# pg.image.save(screen, 'road.jpg')

# New

import pygame as pg
import random
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

SIZE = WIDTH, HEIGHT = 800, 600
GRAY = (128, 128, 128)

pg.init()
pg.display.set_caption("Rally")
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()
GREEN = (0, 128, 0)
WHEIT = (200, 200, 200)

# bg_image = pg.image.load("Image/road.jpg")
# bg_image_rect = bg_image.get_rect(topleft=(0, 0))
# bg_image_2_rect = bg_image.get_rect(topleft=(0, -HEIGHT))
cars = [pg.image.load("Image/car1.png"), pg.image.load("Image/car2.png"),
        pg.image.load("Image/car3.png")]


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Image/car4.png")
        self.orig_image = self.image
        self.angle = 0
        self.speed = 2
        self.acceleration = 0.02
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.rect = self.image.get_rect()
        self.position = pg.math.Vector2(self.x, self.y)
        self.velocity = pg.math.Vector2()

    def update(self):
        self.image = pg.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.position += self.velocity
        self.rect.center = self.position


class Car(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.flip(img, False, True)
        # self.w, self.h = self.image.get_width(), self.image.get_height()
        self.speed = random.randint(2, 3)
        self.rect = self.image.get_rect(center=(x, y))


class Road(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface(screen.get_size())
        self.image.fill(GRAY)
        pg.draw.line(self.image, GREEN, (20, 0), (20, 600), 40)
        pg.draw.line(self.image, GREEN, (780, 0), (780, 600), 40)
        for xx in range(10):
            for yy in range(10):
                pg.draw.line(
                    self.image, WHEIT,
                    (40 + xx * 80, 0 if xx == 0 or xx == 9 else 10 + yy * 60),
                    (40 + xx * 80, 600 if xx == 0 or xx == 9 else 50 + yy * 60), 5)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0


all_sprite = pg.sprite.Group()
for r in range(2):
    all_sprite.add(Road(0, 0 if r == 0 else -HEIGHT))
player = Player()

list_x = []
n = 0
while n < 6:
    x = random.randrange(80, WIDTH, 80)
    if x in list_x:
        continue
    else:
        list_x.append(x)
        all_sprite.add(Car(x, -cars[0].get_height(), random.choice(cars)))
        n += 1

all_sprite.add(player)

game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    all_sprite.update()
    all_sprite.draw(screen)
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f"Rally   FPS: {int(clock.get_fps())}")

# pg.image.save(screen, 'road.jpg')

# New

import pygame as pg
import random
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

SIZE = WIDTH, HEIGHT = 800, 600
GRAY = (128, 128, 128)

pg.init()
pg.display.set_caption("Rally")
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()
GREEN = (0, 128, 0)
WHEIT = (200, 200, 200)
block = False

# bg_image = pg.image.load("Image/road.jpg")
# bg_image_rect = bg_image.get_rect(topleft=(0, 0))
# bg_image_2_rect = bg_image.get_rect(topleft=(0, -HEIGHT))
cars = [pg.image.load("Image/car1.png"), pg.image.load("Image/car2.png"),
        pg.image.load("Image/car3.png")]


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Image/car4.png")
        self.orig_image = self.image
        self.angle = 0
        self.speed = 2
        self.acceleration = 0.02
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.rect = self.image.get_rect()
        self.position = pg.math.Vector2(self.x, self.y)
        self.velocity = pg.math.Vector2()

    def update(self):
        self.image = pg.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.position += self.velocity
        self.rect.center = self.position

        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.velocity.x = self.speed
            self.angle -= 1
            if self.angle < -25:
                self.angle = -25
        elif keys[pg.K_LEFT]:
            self.velocity.x = -self.speed
            self.angle += 1
            if self.angle > 25:
                self.angle = 25
        else:
            self.velocity.x = 0
            if self.angle < 0:
                self.angle += 1
            elif self.angle > 0:
                self.angle -= 1
        if keys[pg.K_UP]:
            self.velocity.y -= self.acceleration
            if self.velocity.y < -self.speed:
                self.velocity.y = -self.speed
        elif keys[pg.K_DOWN]:
            self.velocity.y += self.acceleration
            if self.velocity.y > self.speed:
                self.velocity.y = self.speed
        else:
            if self.velocity.y < 0:
                self.velocity.y += self.acceleration
                if self.velocity.y > 0:
                    self.velocity.y = 0
            elif self.velocity.y > 0:
                self.velocity.y -= self.acceleration
                if self.velocity.y < 0:
                    self.velocity.y = 0


class Car(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.flip(img, False, True)
        # self.w, self.h = self.image.get_width(), self.image.get_height()
        self.speed = random.randint(2, 3)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0

            list_x.remove(self.rect.centerx)
            while True:
                self.rect.centerx = random.randrange(80, WIDTH, 80)
                if self.rect.centerx in list_x:
                    continue
                else:
                    list_x.append(self.rect.centerx)
                    self.speed = random.randint(2, 3)
                    break


class Road(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface(screen.get_size())
        self.image.fill(GRAY)
        pg.draw.line(self.image, GREEN, (20, 0), (20, 600), 40)
        pg.draw.line(self.image, GREEN, (780, 0), (780, 600), 40)
        for xx in range(10):
            for yy in range(10):
                pg.draw.line(
                    self.image, WHEIT,
                    (40 + xx * 80, 0 if xx == 0 or xx == 9 else 10 + yy * 60),
                    (40 + xx * 80, 600 if xx == 0 or xx == 9 else 50 + yy * 60), 5)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0


all_sprite = pg.sprite.Group()
cars_group = pg.sprite.Group()
for r in range(2):
    all_sprite.add(Road(0, 0 if r == 0 else -HEIGHT))
player = Player()

list_x = []
n = 0
while n < 6:
    x = random.randrange(80, WIDTH, 80)
    if x in list_x:
        continue
    else:
        list_x.append(x)
        cars_group.add(Car(x, -cars[0].get_height(), random.choice(cars)))
        n += 1

all_sprite.add(cars_group, player)

game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    if pg.sprite.spritecollideany(player, cars_group):
        if not block:
            player.position[0] += 50 * random.randrange(-1, 2, 2)
            player.angle = 50 * random.randrange(-1, 2, 2)
            block = True
    else:
        block = False

    all_sprite.update()
    all_sprite.draw(screen)
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f"Rally   FPS: {int(clock.get_fps())}")

# pg.image.save(screen, 'road.jpg')

# New

import pygame as pg
import random
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

SIZE = WIDTH, HEIGHT = 800, 600
GRAY = (128, 128, 128)
GREEN = (0, 128, 0)
WHEIT = (200, 200, 200)
block = False
car_accident = 0

pg.init()
pg.display.set_caption("Rally")
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()

cars = [pg.image.load("Image/car1.png"), pg.image.load("Image/car2.png"),
        pg.image.load("Image/car3.png")]
sound_car_accident = pg.mixer.Sound("Sound/udar.wav")
font = pg.font.Font(None, 32)


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Image/car4.png")
        self.orig_image = self.image
        self.angle = 0
        self.speed = 2
        self.acceleration = 0.02
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.rect = self.image.get_rect()
        self.position = pg.math.Vector2(self.x, self.y)
        self.velocity = pg.math.Vector2()

    def update(self):
        self.image = pg.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.position += self.velocity
        self.rect.center = self.position

        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.velocity.x = self.speed
            self.angle -= 1
            if self.angle < -25:
                self.angle = -25
        elif keys[pg.K_LEFT]:
            self.velocity.x = -self.speed
            self.angle += 1
            if self.angle > 25:
                self.angle = 25
        else:
            self.velocity.x = 0
            if self.angle < 0:
                self.angle += 1
            elif self.angle > 0:
                self.angle -= 1
        if keys[pg.K_UP]:
            self.velocity.y -= self.acceleration
            if self.velocity.y < -self.speed:
                self.velocity.y = -self.speed
        elif keys[pg.K_DOWN]:
            self.velocity.y += self.acceleration
            if self.velocity.y > self.speed:
                self.velocity.y = self.speed
        else:
            if self.velocity.y < 0:
                self.velocity.y += self.acceleration
                if self.velocity.y > 0:
                    self.velocity.y = 0
            elif self.velocity.y > 0:
                self.velocity.y -= self.acceleration
                if self.velocity.y < 0:
                    self.velocity.y = 0


class Car(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.flip(img, False, True)
        self.speed = random.randint(2, 3)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0

            list_x.remove(self.rect.centerx)
            while True:
                self.rect.centerx = random.randrange(80, WIDTH, 80)
                if self.rect.centerx in list_x:
                    continue
                else:
                    list_x.append(self.rect.centerx)
                    self.speed = random.randint(2, 3)
                    break


class Road(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface(screen.get_size())
        self.image.fill(GRAY)
        pg.draw.line(self.image, GREEN, (20, 0), (20, 600), 40)
        pg.draw.line(self.image, GREEN, (780, 0), (780, 600), 40)
        for xx in range(10):
            for yy in range(10):
                pg.draw.line(
                    self.image, WHEIT,
                    (40 + xx * 80, 0 if xx == 0 or xx == 9 else 10 + yy * 60),
                    (40 + xx * 80, 600 if xx == 0 or xx == 9 else 50 + yy * 60), 5)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0


all_sprite = pg.sprite.Group()
cars_group = pg.sprite.Group()
for r in range(2):
    all_sprite.add(Road(0, 0 if r == 0 else -HEIGHT))
player = Player()

list_x = []
n = 0
while n < 6:
    x = random.randrange(80, WIDTH, 80)
    if x in list_x:
        continue
    else:
        list_x.append(x)
        cars_group.add(Car(x, -cars[0].get_height(), random.choice(cars)))
        n += 1

all_sprite.add(cars_group, player)


def screen1():
    sc = pg.Surface(screen.get_size())
    bg = pg.image.load("Image/road.jpg")
    visual_car = pg.image.load("Image/car4.png")
    start_button = pg.image.load("Image/start_button.png")
    stop_button = pg.image.load("Image/stop_button.png")
    screen.blit(sc, (0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(visual_car, (375, 250))
    screen.blit(start_button, (250, 100))
    screen.blit(stop_button, (250, 400))


game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
        elif e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                if stop_button.collidepoint(e.pos):
                    pass

    if pg.sprite.spritecollideany(player, cars_group):
        if not block:
            player.position[0] += 50 * random.randrange(-1, 2, 2)
            player.angle = 50 * random.randrange(-1, 2, 2)
            sound_car_accident.play()
            car_accident += 1
            block = True
    else:
        block = False

    # all_sprite.update()
    # all_sprite.draw(screen)
    # screen.blit(font.render(f"{car_accident = }", 1, GREEN), (45, 10))
    screen1()
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f"Rally   FPS: {int(clock.get_fps())}")

# pg.image.save(screen, 'road.jpg')

import pygame as pg
import random
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"

SIZE = WIDTH, HEIGHT = 800, 600
GRAY = (128, 128, 128)
GREEN = (0, 128, 0)
WHEIT = (200, 200, 200)
block = False
car_accident = 0
scr1 = True

pg.init()
pg.display.set_caption("Rally")
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()

cars = [pg.image.load("Image/car1.png"), pg.image.load("Image/car2.png"),
        pg.image.load("Image/car3.png")]
sound_car_accident = pg.mixer.Sound("Sound/udar.wav")
font = pg.font.Font(None, 32)

sc_bg = pg.image.load("Image/road.jpg")
visual_car = pg.image.load("Image/car4.png")
start_button = pg.image.load("Image/start_button.png")
start_button_rect = start_button.get_rect(center=(250 + 100, 100))
stop_button = pg.image.load("Image/stop_button.png")
stop_button_rect = stop_button.get_rect(center=(250 + 100, 400))


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("Image/car4.png")
        self.orig_image = self.image
        self.angle = 0
        self.speed = 2
        self.acceleration = 0.02
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.rect = self.image.get_rect()
        self.position = pg.math.Vector2(self.x, self.y)
        self.velocity = pg.math.Vector2()

    def update(self):
        self.image = pg.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.position += self.velocity
        self.rect.center = self.position

        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.velocity.x = self.speed
            self.angle -= 1
            if self.angle < -25:
                self.angle = -25
        elif keys[pg.K_LEFT]:
            self.velocity.x = -self.speed
            self.angle += 1
            if self.angle > 25:
                self.angle = 25
        else:
            self.velocity.x = 0
            if self.angle < 0:
                self.angle += 1
            elif self.angle > 0:
                self.angle -= 1
        if keys[pg.K_UP]:
            self.velocity.y -= self.acceleration
            if self.velocity.y < -self.speed:
                self.velocity.y = -self.speed
        elif keys[pg.K_DOWN]:
            self.velocity.y += self.acceleration
            if self.velocity.y > self.speed:
                self.velocity.y = self.speed
        else:
            if self.velocity.y < 0:
                self.velocity.y += self.acceleration
                if self.velocity.y > 0:
                    self.velocity.y = 0
            elif self.velocity.y > 0:
                self.velocity.y -= self.acceleration
                if self.velocity.y < 0:
                    self.velocity.y = 0


class Car(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.flip(img, False, True)
        self.speed = random.randint(2, 3)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0

            list_x.remove(self.rect.centerx)
            while True:
                self.rect.centerx = random.randrange(80, WIDTH, 80)
                if self.rect.centerx in list_x:
                    continue
                else:
                    list_x.append(self.rect.centerx)
                    self.speed = random.randint(2, 3)
                    break


class Road(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface(screen.get_size())
        self.image.fill(GRAY)
        pg.draw.line(self.image, GREEN, (20, 0), (20, 600), 40)
        pg.draw.line(self.image, GREEN, (780, 0), (780, 600), 40)
        for xx in range(10):
            for yy in range(10):
                pg.draw.line(
                    self.image, WHEIT,
                    (40 + xx * 80, 0 if xx == 0 or xx == 9 else 10 + yy * 60),
                    (40 + xx * 80, 600 if xx == 0 or xx == 9 else 50 + yy * 60), 5)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1

    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT:
            self.rect.bottom = 0


all_sprite = pg.sprite.Group()
cars_group = pg.sprite.Group()
for r in range(2):
    all_sprite.add(Road(0, 0 if r == 0 else -HEIGHT))
player = Player()

list_x = []
n = 0
while n < 6:
    x = random.randrange(80, WIDTH, 80)
    if x in list_x:
        continue
    else:
        list_x.append(x)
        cars_group.add(Car(x, -cars[0].get_height(), random.choice(cars)))
        n += 1

all_sprite.add(cars_group, player)


def screen1():
    sc = pg.Surface(screen.get_size())
    screen.blit(sc, (0, 0))
    screen.blit(sc_bg, (0, 0))
    screen.blit(visual_car, (375, 250))
    screen.blit(start_button, (250, 100))
    screen.blit(stop_button, (250, 400))


game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False
        elif e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                if start_button_rect.collidepoint(e.pos):
                    scr1 = False
                elif stop_button_rect.collidepoint(e.pos):
                    game = False

    if pg.sprite.spritecollideany(player, cars_group):
        if not block:
            player.position[0] += 50 * random.randrange(-1, 2, 2)
            player.angle = 50 * random.randrange(-1, 2, 2)
            sound_car_accident.play()
            car_accident += 1
            block = True
    else:
        block = False

    if scr1:
        screen1()
    else:
        all_sprite.update()
        all_sprite.draw(screen)
        screen.blit(font.render(f"{car_accident = }", 1, GREEN), (45, 10))

    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f"Rally   FPS: {int(clock.get_fps())}")

# pg.image.save(screen, 'road.jpg')
