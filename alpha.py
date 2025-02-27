import pygame
import random
import math
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Шрифт
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 48)

# Кнопки
buttons = {
    "start": pygame.Rect(295, 210, 200, 50),
    "exit": pygame.Rect(295, 290, 200, 50)
}

start_button = pygame.transform.scale(pygame.image.load('photo ds/start_button.png').convert_alpha(), (200, 50))
exit_button = pygame.transform.scale(pygame.image.load('photo ds/exit_button.png').convert_alpha(), (200, 50))

# Загрузка фона
main_background = pygame.image.load('photo ds/backg.jpg').convert_alpha()
backg_start = pygame.image.load('photo ds/fon.jpg').convert_alpha()
backg_start = pygame.transform.scale(backg_start, (800, 600))
backg_game = pygame.image.load('photo ds/svo2.png').convert_alpha()
backg_game = pygame.transform.scale(backg_game, (800, 600))
backg = pygame.image.load('photo ds/svo.jpg')

zaborchik = pygame.transform.scale(pygame.image.load('photo ds/заборчик.png'), (100, 100)).convert_alpha()

# бомба при артиллерии
bomb_image = pygame.image.load('photo ds/bomb.png')
bomb_image = pygame.transform.scale(bomb_image, (50, 40))
bomb_image = pygame.transform.flip(bomb_image, False, False)

hero_image1 = pygame.image.load('прыжок и статичное положение/Idle1.png').convert_alpha()  # персонаж
hero_image1 = pygame.transform.scale(hero_image1, (118, 160))
hero_image = pygame.transform.flip(hero_image1, True, False)

# Загрузка звуков
walk_sounds = [pygame.mixer.Sound('sounds/footsteps.mp3')]
door = pygame.mixer.Sound('sounds/дверь.mp3')
plane_sound = pygame.mixer.Sound('sounds/самолет.wav')
plane_sound.set_volume(0.4)
phon = pygame.mixer.music.load('sounds/dora.mp3')
pygame.mixer.music.set_volume(0.1)
arta = pygame.mixer.Sound('sounds/арта.mp3')
kyst = pygame.mixer.Sound('sounds/куст.wav')
bagr_s = pygame.mixer.Sound('sounds/задний фон.mp3')
bagr_s.set_volume(0.1)

st_serjant = pygame.image.load('photo ds/старший сержант.png').convert_alpha()
st_serjant = pygame.transform.scale(st_serjant, (630, 686))
lazy_person = pygame.transform.scale(pygame.image.load('photo ds/лентяй (1).png').convert_alpha(), (168, 150))

wall_image = pygame.image.load('photo ds/стена.png').convert_alpha()  # стена изобр
wall_image = pygame.transform.scale(wall_image, (20, 200))  # вертикальная стена
wall_image1 = pygame.transform.scale(wall_image, (2, 20))  # вертикальная стена
# walls = [pygame.Rect(0, 400, 13, 200)]  # список с вертикальными стенами

plane = pygame.image.load('photo ds/карлсон.png').convert_alpha()
plane = pygame.transform.scale(plane, (256, 100))

door_close = pygame.image.load('photo ds/closedoor.png').convert_alpha()  # закрытая дверь
door_close = pygame.transform.scale(door_close, (160, 180))
door_rect = door_close.get_rect()

door_open = pygame.image.load('photo ds/openedoor.png').convert_alpha()  # открытая дверь
door_open = pygame.transform.scale(door_open, (160, 180))

zabor = pygame.image.load('photo ds/zabor.png').convert_alpha()
zabor = pygame.transform.scale(zabor, (200, 150))
enemy_images = ['enemy/1.png', 'enemy/2.png', 'enemy/3.png', 'enemy/4.png', 'enemy/5.png',
                'enemy/6.png']  # враг и его анимации

# изображение героя при ходьбе
hero_image_go = ['герой ходьба/Walk1.png', 'герой ходьба/Walk2.png', 'герой ходьба/Walk3.png', 'герой ходьба/Walk4.png',
                 'герой ходьба/Walk5.png', 'герой ходьба/Walk6.png', 'герой ходьба/Walk7.png', 'герой ходьба/Walk8.png',
                 'герой ходьба/Walk9.png', 'герой ходьба/Walk10.png']

# изобр при статичн положении
hero_image_static = pygame.image.load('прыжок и статичное положение/Idle1.png').convert_alpha()
hero_image_static = pygame.transform.scale(hero_image_static, (110, 160))

hero_image_parashut = pygame.image.load('герой ходьба/парашют.png').convert_alpha()
hero_image_parashut = pygame.transform.scale(hero_image_parashut, (218, 260))

# изображения героя при прыжке
hero_image_jump = pygame.image.load('прыжок и статичное положение/Jump6.png').convert_alpha()
hero_image_jump = pygame.transform.scale(hero_image_jump, (110, 160))

moh = pygame.image.load('photo ds/мох.png').convert_alpha()
moh = pygame.transform.scale(moh, (200, 60))

stena2 = pygame.image.load('photo ds/стена2.png').convert_alpha()
stena2 = pygame.transform.scale(stena2, (190, 250))

box = pygame.image.load('photo ds/box.png').convert_alpha()
box = pygame.transform.scale(box, (70, 70))
box_shy = pygame.image.load('photo ds/box_shy.png').convert_alpha()
box_shy = pygame.transform.scale(box_shy, (70, 70))
# tank
tanks = ['Tank/tank1.png', 'Tank/tank2.png', 'Tank/tank3.png']

# взрыв
bum_images = ['бум/1.png', 'бум/2.png', 'бум/3.png', 'бум/4.png', 'бум/5.png', 'бум/6.png', 'бум/7.png', 'бум/8.png']

# Физика
gravity = 0.5  # Сила гравитации
jump_strength = 8  # Сила прыжка

# платформы дерева
wood1 = pygame.transform.scale(pygame.image.load('photo ds/textur_wood.jpg'), (20, 600)).convert_alpha()
wood2 = pygame.transform.scale(pygame.image.load('photo ds/textur_wood.jpg'), (20, 215)).convert_alpha()
wood3 = pygame.transform.scale(pygame.image.load('photo ds/textur_wood.jpg'), (20, 200)).convert_alpha()
wood4 = pygame.transform.scale(pygame.image.load('photo ds/textur_wood.jpg'), (600, 20)).convert_alpha()
wood5 = pygame.transform.scale(pygame.image.load('photo ds/textur_wood.jpg'), (10, 2)).convert_alpha()
wood6 = pygame.transform.scale(pygame.image.load('photo ds/textur_wood.jpg'), (280, 20)).convert_alpha()
wood7 = pygame.transform.scale(pygame.image.load('photo ds/textur_wood (1).jpg'), (9, 200)).convert_alpha()
wood8 = pygame.transform.scale(pygame.image.load('photo ds/textur_wood (1).jpg'), (9, 170)).convert_alpha()

clock = pygame.time.Clock()
direction = 1


def draw_menu():
    # Отрисовка фона
    screen.blit(main_background, (0, 0))
    title_text = font.render("Миссия альфа", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))
    # кнопки
    screen.blit(exit_button, (295, 290)), screen.blit(start_button, (295, 210))

    for button_name, button_rect in buttons.items():
        # Отрисовка текста на кнопке
        button_text = button_font.render(button_name.capitalize(), True, BLACK)
        screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2,
                                  button_rect.y + (button_rect.height - button_text.get_height()) // 2))

    pygame.display.flip()


class Bullet:
    def __init__(self, x, y, direction):
        correct = 18 if direction == -1 else 110  # корректировка выстрела
        self.rect = pygame.Rect(x + correct * direction, y + 25, 10, 5)  # Прямоугольник снаряда (ширина 10, высота 5)
        self.speed_bullet = 10 * direction  # Устанавливаем скорость в зависимости от направления
        self.sound = pygame.mixer.Sound("sounds/shot_sound.wav")
        self.sound.set_volume(0.1)
        self.channel = pygame.mixer.Channel(0)  # Используем первый канал для воспроизведения звука
        self.channel.play(self.sound)

    def update(self):
        self.rect.x += self.speed_bullet  # Двигаем снаряд в зависимости от направления

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)  # Рисуем снаряд (красный цвет)


class Game:
    def __init__(self):
        self.napr_enemy_und = 0
        self.x, self.y = 690, 40  # координаты персонажа
        self.xp, self.yp = 540, 30  # координаты plane
        self.x_backg = 0
        self.y_backg = 0
        self.velocity_y = 0  # Вертикальная скорость
        self.on_ground = False  # Флаг, указывающий, находится ли персонаж на земле
        self.on_platf = False
        self.move_speed = 3
        self.hero = hero_image
        self.hero_rect = pygame.Rect(self.x, self.y, 110, 160)  # Получаем прямоугольник для героя
        self.hero_rect.topleft = (self.x, self.y)  # Устанавливаем позицию героя
        self.action_cooldown = 0
        self.st_serjant_rect = st_serjant.get_rect()  # прямоугольник для ст сержанта
        self.st_serjant_rect.topleft = (400, 450)  # Устанавливаем позицию старшего сержанта
        self.door = door_close

        # Анимация врага
        self.enemy_images = [pygame.image.load(img).convert_alpha() for img in enemy_images]
        self.flag = True
        self.flag1 = False
        self.flag2 = True
        self.hero_jump = hero_image_static  # текущее изображение
        self.napr = 0  # направление персонажа
        self.napr_enemy = 0  # для определения направления пуль
        self.current_enemy_frame = 0  # Индекс текущего кадра
        self.enemy_animation_speed = 0.1  # Скорость анимации
        self.enemy_animation_timer = 0  # Таймер для анимации
        # изображения при ходьбе и изменение размеров
        self.hero_image_go = [pygame.transform.scale(pygame.image.load(img),
                                                     (118, 160)).convert_alpha() for img in hero_image_go]

        self.current_hero_frame = 0  # Индекс текущего кадра у гл г
        self.hero_animation_timer = 0  # Таймер для анимации главн героя
        self.hero_timer = 0
        self.hero_hide_flag = False
        self.hero_hide = pygame.transform.scale(pygame.image.load('Предметы/трава.png'), (200, 150))

        self.bullets = []  # Список снарядов
        self.shoot_timer = 60  # Таймер для стрельбы
        self.shoot_delay = 15  # Задержка между выстрелами (в кадрах)

        #  танк анимации, фото
        self.tanks = [pygame.transform.scale(pygame.image.load(img),
                                             (432, 144)).convert_alpha() for img in tanks]
        self.tank = self.tanks[0]
        self.tank_timer = 0
        self.current_tank_frame = 0
        self.count = 0  # счет для переключения событий в танках
        self.mig = 0  # мигающий текст
        self.left_Fire = False

        self.babah_timer = 0  # числа для анимации бомбы
        self.current_babah_frame = 0
        # изображения при взрыве
        self.babah_images = [pygame.transform.scale(pygame.image.load(img),
                                                    (140, 140)).convert_alpha() for img in bum_images]

    def game_end(self):
        # Загрузка фона
        background_game_over = pygame.image.load("photo ds/fon_gameover.jpg")
        background_game_over = pygame.transform.scale(background_game_over, (800, 600))

        # Заливка фона
        screen.blit(background_game_over, (0, 0))

        # Настройка шрифта
        small_font = pygame.font.SysFont("Comic Sans MS", 40)  # Уменьшите размер шрифта, если нужно
        game_over_text = "Поздравляю, боец! Ты выполнил задание, как настоящий ветеран боевых действий!"

        # Разбиваем текст на строки
        words = game_over_text.split(' ')
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + ' '
            if small_font.size(test_line)[0] <= 800:  # 800 - максимальная ширина
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + ' '

        lines.append(current_line)  # Добавляем последнюю строку

        # Отрисовка текста
        y_offset = HEIGHT // 2 - (len(lines) * small_font.get_height()) // 2  # Центрируем текст по вертикали
        for line in lines:
            rendered_line = small_font.render(line, True, (0, 0, 0))
            screen.blit(rendered_line, (WIDTH // 2 - rendered_line.get_width() // 2, y_offset))
            y_offset += small_font.get_height()  # Смещаем вниз для следующей строки

        pygame.display.flip()  # Обновляем экран

        # Ожидание нажатия клавиши R для перезапуска
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def start(self):
        timer = 0
        walls = [pygame.Rect(-20, 400, 13, 200), pygame.Rect(800, 400, 13, 200)]  # список с вертикальными стенами
        current_walk_sound = None
        door_opened = False
        is_walking = False
        plane_sound.play(0)
        bagr_start = True
        while True:
            if bagr_start:
                bagr_s.play(-1)
                bagr_start = False
            if self.flag1:  # проверка на то был ли прыжок
                self.hero = hero_image_static  # статичн изобр персонажа
            screen.fill(WHITE)  # Очистка экрана
            screen.blit(backg_start, (self.x_backg, self.y_backg))  # Отрисовка фона игры
            screen.blit(backg_start, (self.x_backg + backg_start.get_width(), self.y_backg))

            if self.xp != -300:  # если самолёт не долетел убавляем коорд
                self.xp -= 10

            if self.x > 110 and not self.flag1:  # падение персонажа с парашюта
                self.hero = hero_image_parashut
                self.x -= 4
                self.y += 1.5
            else:
                self.hero = hero_image_static
                self.flag1 = True

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            if self.action_cooldown > 0:  # заморозка игры
                self.action_cooldown -= 1  # Уменьшаем таймер блокировки

            else:
                if self.flag1:
                    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                        if self.on_ground:  # Движение влево
                            self.hero = self.hero_image_go[self.update_hero_animation_left('go')]
                        self.napr = -1
                        self.x -= self.move_speed

                        # Воспроизведение звука ходьбы
                        if not is_walking:
                            current_walk_sound = random.choice(walk_sounds)
                            current_walk_sound.play(-1)  # Воспроизводим в цикле
                            is_walking = True

                    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:  # Движение вправо
                        if self.on_ground:  # Движение влево
                            self.hero = self.hero_image_go[self.update_hero_animation_left('go')]
                        self.napr = 1
                        self.x += self.move_speed

                        # Воспроизведение звука ходьбы
                        if not is_walking:
                            is_walking = True
                            current_walk_sound = random.choice(walk_sounds)
                            current_walk_sound.play(-1)  # Воспроизводим в цикле
                            is_walking = True

                    if keys[pygame.K_SPACE] and self.on_ground:  # Прыжок
                        self.hero = hero_image_jump
                        self.velocity_y = -jump_strength
                        self.on_ground = False

                    else:
                        # Если персонаж не движется, останавливаем звук
                        if is_walking:
                            current_walk_sound.stop()  # Останавливаем звук
                            is_walking = False

            # Обновление физики
            if not self.on_ground and self.flag1:
                self.velocity_y += gravity  # Применение гравитации
                self.y += self.velocity_y  # Обновление вертикальной позиции
                self.hero = hero_image_jump

                # Проверка на столкновение с "землёй"
                if self.y >= 400:  # Предположим, что 400 - это высота земли
                    self.y = 400
                    self.on_ground = True
                    self.velocity_y = 0  # Сброс вертикальной скорости

            # Обновление позиции прямоугольника героя
            self.hero_rect.topleft = (self.x, self.y)

            # Проверка на столкновение со стеной
            for wall in walls:  # горизонт стены
                if self.hero_rect.colliderect(wall):
                    if keys[pygame.K_LEFT]:  # Если движется влево
                        self.x = wall.right  # Останавливаемся у стены
                    if keys[pygame.K_RIGHT]:
                        self.x = wall.left - self.hero_rect.width

            if self.x_backg <= -backg_start.get_width():  # Если фон полностью сдвинулся влево, сбрасываем его позицию
                self.x_backg = 0

            if 250 <= self.hero_rect.y <= 500 and 570 <= self.hero_rect.x <= 780:  # открытие и закрытие двери
                self.door = door_open
                if not door_opened:
                    door_opened = True
                    door.play(0)

                if keys[pygame.K_e]:  # Устанавливаем флаг, чтобы звук не воспроизводился повторно
                    bagr_s.stop()  # Устанавливаем флаг, чтобы звук не воспроизводился повторно
                    self.game1()
                    return False
            else:
                self.door = door_close
                if door_opened:
                    door.stop()
                    door_opened = False

            # Отрисовка
            screen.blit(stena2, (630, 308))  # стена для двери
            screen.blit(moh, (622, 272))  # мох на  стене
            if self.door == door_close:
                screen.blit(self.door, (633, 380))
            else:
                screen.blit(self.door, (633, 380))
            screen.blit(st_serjant, (128, 120))
            screen.blit(zabor, (380, 420))

            for wall in walls:  # отрисовка стен
                screen.blit(wall_image, wall.topleft)
            screen.blit(box, (12, 480)), screen.blit(box, (78, 480)), screen.blit(box, (128, 480)), \
                screen.blit(box, (128, 440)), screen.blit(box, (78, 440))
            screen.blit(lazy_person, (15, 400))
            if self.napr == -1:
                screen.blit(pygame.transform.flip(self.hero, True, False), (self.x, self.y))
            else:
                screen.blit(self.hero, (self.x, self.y))
            screen.blit(plane, (self.xp, self.yp))
            # отрисовка приказа
            if self.x >= 371 and self.on_ground and timer <= 300:
                self.action_cooldown = 1
                timer += 1
            if self.x >= 371 and 1 <= timer < 300:
                if keys[pygame.K_e]:
                    timer = 300
                    self.action_cooldown = 0
                screen.blit(pygame.transform.scale(pygame.image.load('photo ds/order.png'), (740, 550)), (40, 20))

            pygame.display.flip()  # Обновление экрана

            # Задержка для управления скоростью
            clock.tick(60)  # Задержка в миллисекундах

    def fire(self, x, y):  # для врага и танково игры
        if self.napr_enemy:
            direction = 1 if self.napr_enemy == 1 else -1  # Определяем направление в зависимости от врага
        else:
            if self.left_Fire:
                direction = -1
            else:
                direction = 1
        bullet = Bullet(x, y, direction)  # Создаем снаряд на позиции врага с заданным направлением
        self.bullets.append(bullet)  # Добавляем снаряд в список

    def fire_en(self, x, y):  # для врага 2
        global direction
        if self.napr_enemy_und:
            direction = 1 if self.napr_enemy_und == 1 else -1  # Определяем направление в зависимости от врага

        bullet = Bullet(x, y, direction)  # Создаем снаряд на позиции врага с заданным направлением
        self.bullets.append(bullet)  # Добавляем снаряд в список

    def update_bullets(self):
        for bullet in self.bullets:
            bullet.update()  # Обновляем позицию снаряда
            if bullet.rect.x < 0:  # Если снаряд вышел за пределы экрана
                self.bullets.remove(bullet)  # Удаляем снаряд из списка

    def draw_bullets(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)  # Рисуем снаряд на экране

    def fade_to_black(self, duration, game):
        """Плавное затемнение экрана."""
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill(BLACK)
        self.door = door_close
        if game == 1:
            for alpha in range(0, 255, 5):  # Увеличиваем альфа-канал от 0 до 255
                fade_surface.set_alpha(alpha)
                screen.blit(backg_start, (0, 0))  # Отрисовка фона
                # Накладываем затемняющий слой на все объекты
                screen.blit(stena2, (630, 308))  # стена для двери
                screen.blit(moh, (622, 272))  # мох на  стене
                screen.blit(self.door, (632, 386))
                screen.blit(st_serjant, (128, 120))
                screen.blit(zabor, (380, 420))
                screen.blit(box, (12, 480)), screen.blit(box, (78, 480)), screen.blit(box, (128, 480)), \
                    screen.blit(box, (128, 440)), screen.blit(box, (78, 440))
                screen.blit(lazy_person, (15, 400))
                screen.blit(fade_surface, (0, 0))
                pygame.display.flip()
                pygame.time.delay(duration // 51)  # Задержка для управления скоростью затемнения
        elif game == 2:
            for alpha in range(0, 255, 5):  # Увеличиваем альфа-канал от 0 до 255
                fade_surface.set_alpha(alpha)
                screen.blit(backg, (0, 0))  # Отрисовка фона
                screen.blit(wood1, (782, -230)), screen.blit(wood2, (350, 163)), screen.blit(wood3, (540, 0)), \
                    screen.blit(wood4, (200, 368)), screen.blit(wood5, (546, 195)), screen.blit(wood6, (540, 180)), \
                    screen.blit(wood8, (282, 388))
                screen.blit(zaborchik, (220, 460))
                screen.blit(wood7, (200, 385))
                screen.blit(box, (710, 300)), screen.blit(box, (634, 113)), screen.blit(box, (562, 113))
                enemy_images = self.enemy_images[self.current_enemy_frame]
                enemy_images = pygame.transform.scale(enemy_images, (120, 180))
                if self.flag:
                    enemy_images = pygame.transform.flip(enemy_images, True, False)
                screen.blit(enemy_images, (self.xp, self.yp))  # Позиция врага
                screen.blit(fade_surface, (0, 0))  # Отрисовка затемняющего слоя
                pygame.display.flip()
                pygame.time.delay(duration // 51)
        elif game == 3:
            for alpha in range(0, 255, 5):  # Увеличиваем альфа-канал от 0 до 255
                fade_surface.set_alpha(alpha)
                fade_surface.set_alpha(255 - alpha)
                screen.blit(backg_game, (self.x_backg, self.y_backg))

                screen.blit(fade_surface, (0, 0))  # Отрисовка затемняющего слоя
                pygame.display.flip()
                pygame.time.delay(duration // 51)  # Задержка для управления скоростью затемнения

    def anti_fade_to_black(self, duration, game):
        """Плавное растемнение экрана."""
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.fill(BLACK)
        if game == 1:
            for alpha in range(0, 255, 5):  # Увеличиваем альфа-канал от 0 до 255
                fade_surface.set_alpha(255 - alpha)
                screen.blit(backg, (0, 0))  # Отрисовка фона
                screen.blit(wood1, (782, -230)), screen.blit(wood2, (350, 163)), screen.blit(wood3, (540, 0)), \
                    screen.blit(wood4, (200, 368)), screen.blit(wood5, (546, 195)), screen.blit(wood6, (540, 180)), \
                    screen.blit(wood8, (282, 388))
                screen.blit(zaborchik, (220, 460))
                screen.blit(wood7, (200, 385))
                screen.blit(box, (710, 300)), screen.blit(box, (634, 113)), screen.blit(box, (562, 113))
                enemy_images = self.enemy_images[self.current_enemy_frame]
                enemy_images = pygame.transform.scale(enemy_images, (120, 180))
                if self.flag:
                    enemy_images = pygame.transform.flip(enemy_images, True, False)
                screen.blit(enemy_images, (self.xp, self.yp))  # Позиция врага
                screen.blit(self.hero, (self.x, self.y))
                screen.blit(fade_surface, (0, 0))  # Отрисовка затемняющего слоя
                pygame.display.flip()
                pygame.time.delay(duration // 51)  # Задержка для управления скоростью затемнения
        elif game == 2:
            for alpha in range(0, 255, 5):  # Увеличиваем альфа-канал от 0 до 255
                fade_surface.set_alpha(255 - alpha)
                screen.blit(backg_game, (self.x_backg, self.y_backg))
                screen.blit(self.hero, (self.x, self.y))
                screen.blit(fade_surface, (0, 0))  # Отрисовка затемняющего слоя
                pygame.display.flip()
                pygame.time.delay(duration // 51)  # Задержка для управления скоростью затемнения
        elif game == 3:
            for alpha in range(0, 255, 5):  # Увеличиваем альфа-канал от 0 до 255
                fade_surface.set_alpha(255 - alpha / 2)
                screen.blit(backg_game, (self.x_backg, self.y_backg))
                screen.blit(self.tanks[0], (20, 450))
                pygame.display.flip()
                pygame.time.delay(duration // 51)

    def update_enemy_animation(self):  # анимации врага
        self.enemy_animation_timer += self.enemy_animation_speed
        if self.enemy_animation_timer >= 1:  # Каждые 1 секунду переключаем кадр
            self.current_enemy_frame += 1
            if self.current_enemy_frame == 6:
                self.current_enemy_frame = 0
            self.enemy_animation_timer = 0

    def update_hero_animation_left(self, kind):  # анимации при движении
        self.hero_timer += 0.15
        if kind == 'go':
            if self.hero_timer >= 1:  # Каждые 1 секунду переключаем кадр
                self.current_hero_frame += 1
                if self.current_hero_frame == len(self.hero_image_go):
                    self.current_hero_frame = 0
                self.hero_timer = 0
        return self.current_hero_frame

    def update_animation_tank(self):  # анимации при движении танка
        self.tank_timer += 0.15
        if self.tank_timer >= 1:  # Каждые 1 секунду переключаем кадр
            self.current_tank_frame += 1
            if self.current_tank_frame == len(self.tanks):
                self.current_tank_frame = 0
            self.tank_timer = 0
        return self.current_tank_frame

    def update_animation_vertolet(self):  # анимации при движении танка
        self.tank_timer += 0.15
        if self.tank_timer >= 1:  # Каждые 1 секунду переключаем кадр
            self.current_tank_frame += 1
            if self.current_tank_frame == 4:
                self.current_tank_frame = 0
            self.tank_timer = 0
        return self.current_tank_frame

    def update_animation_bah(self):  # анимации при взрывек
        self.babah_timer += 0.11
        if self.babah_timer >= 1:  # Каждые 1 секунду переключаем кадр
            self.current_babah_frame += 1
            if self.current_babah_frame == len(self.babah_images):
                self.current_babah_frame = 0
            self.babah_timer = 0
        return self.current_babah_frame

    def game_over(self, end):
        print("Игра окончена!")  # Замените на нужное действие

        with open("messages.txt", "r", encoding="utf-8") as file:
            messages = file.readlines()  # Читаем все строки в список
        random_message = random.choice(messages).strip()

        small_font = pygame.font.SysFont("Comic Sans MS", 40)

        game_over_text = small_font.render(random_message, True, (62, 180, 137))  # Красный текст
        restart_text = small_font.render("Нажмите R, чтобы начать заново", True, (62, 180, 137))
        # Красный текст
        background_game_over = pygame.image.load("photo ds/fon_gameover.png")

        background_game_over = pygame.transform.scale(background_game_over, (800, 600))

        # Заливка черным цветом
        screen.blit(background_game_over, (0, 0))
        screen.blit(game_over_text,
                    (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2 - 50))
        screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 - 20))
        pygame.display.flip()

        # Ждем, пока игрок не нажмет клавишу R
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Если нажата клавиша R
                        waiting = False
                        if end == 1:
                            self.game_instance = Game()
                            self.game_instance.game1()
                        elif end == 2:
                            self.game_instance = Game()
                            self.game_instance.game2()
                        elif end == 3:
                            self.game_instance = Game()
                            self.game_instance.game_tank()
                        elif end == 4:
                            self.game_instance = Game()
                            self.game_instance.game_plante_bomb()

    def game1(self):
        jump_strength = 16  # Сила прыжка
        box_rect = box.get_rect()  # прямоуг для коробки и координаты
        box_rect.topleft = (710, 300)
        # Создание платформ
        platforms = [pygame.Rect(200, 368, 600, 20), pygame.Rect(546, 195, 10, 2), pygame.Rect(-100, 0, 1000, 1),
                     pygame.Rect(550, 180, 280, 20)]
        # список с вертикальными стенами(используется для блокировки)
        stops = [pygame.Rect(197, 370, 20, 1)]
        stop_platform = [pygame.Rect(354, 163, 10, 2)]
        walls = [pygame.Rect(767, -300, 20, 600), pygame.Rect(350, 170, 20, 200), pygame.Rect(540, -20, 20, 200),
                 pygame.Rect(-20, 0, 20, 600)]
        self.x, self.y = 0, 400
        self.xp, self.yp = 658, 400  # координаты врага
        self.fade_to_black(420, 1)  # затемнение экрана
        self.anti_fade_to_black(720, 1)  # растемнение экрана
        is_walking = False
        current_walk_sound = None
        bagr_start = True
        while True:
            if bagr_start:
                bagr_s.play(-1)
                bagr_start = False
            self.shoot_timer += 1  # уыелечение таймера для стрельбы

            if self.on_ground:
                self.hero = hero_image_static

            screen.fill(WHITE)  # Очистка экрана
            screen.blit(backg, (self.x_backg, self.y_backg))  # Отрисовка фона игры
            screen.blit(backg, (self.x_backg + backg_start.get_width(), self.y_backg))
            keys = pygame.key.get_pressed()

            if self.action_cooldown > 0:
                self.action_cooldown -= 1  # Уменьшаем таймер блокировки
                if self.action_cooldown == 0:
                    self.hero_hide_flag = True

            else:
                if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    if self.on_ground:  # Движение влево
                        self.hero = self.hero_image_go[self.update_hero_animation_left('go')]
                    self.napr = -1
                    self.x -= self.move_speed
                    if not is_walking:
                        current_walk_sound = random.choice(walk_sounds)
                        current_walk_sound.play(-1)  # Воспроизводим в цикле
                        is_walking = True
                if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:  # Движение вправо
                    if self.on_ground:  # Движение влево
                        self.hero = self.hero_image_go[self.update_hero_animation_left('go')]
                    self.napr = 1
                    self.x += self.move_speed
                    if not is_walking:
                        current_walk_sound = random.choice(walk_sounds)
                        current_walk_sound.play(-1)  # Воспроизводим в цикле
                        is_walking = True
                if keys[pygame.K_SPACE] and self.on_ground:  # Прыжок
                    self.hero = hero_image_jump
                    self.velocity_y = -jump_strength
                    self.on_ground = False
                    if not is_walking:
                        current_walk_sound = random.choice(walk_sounds)
                        current_walk_sound.play(-1)  # Воспроизводим в цикле
                        is_walking = True
                else:
                    # Если персонаж не движется, останавливаем звук
                    if is_walking:
                        current_walk_sound.stop()  # Останавливаем звук
                        is_walking = False

            if self.xp > 440 and self.flag:  # передвижение врага
                self.napr_enemy = -1
                self.xp -= 2
                if self.xp == 440:
                    self.flag = False
            else:
                self.napr_enemy = 1
                self.xp += 2
                if self.xp == 658:
                    self.flag = True

            # столкновение с коробкой и ее изобр, получение предметов
            if self.hero_rect.colliderect(box_rect) and not self.hero_hide_flag:
                bx = box_shy
                if keys[pygame.K_e]:
                    self.action_cooldown = 250
                    # даём возможность использовать куст
            else:
                bx = box

            if keys[pygame.K_r] and self.hero_hide_flag and not keys[pygame.K_SPACE] \
                    and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and self.on_ground:  # герой скрывается
                self.hero = self.hero_hide

            # Обновление физики
            if not self.on_ground and not self.on_platf:
                self.velocity_y += gravity  # Применение гравитации
                self.y += self.velocity_y  # Обновление вертикальной позиции

                # Проверка на столкновение с "землёй"
                if self.y >= 420:  # Предположим, что 400 - это высота земли
                    self.y = 420
                    self.on_ground = True
                    self.velocity_y = 0  # Сброс вертикальной скорости

            # Обновление позиции прямоугольника героя
            self.hero_rect.topleft = (self.x, self.y)

            for bullet in self.bullets:
                if self.hero_rect.colliderect(bullet.rect):
                    bagr_s.stop()
                    self.game_over(1)

            # Проверка на столкновение со стеной
            for wall in stops:  # горизонт стены(блокирующие стены)
                if self.hero_rect.colliderect(wall) and wall.left < self.x + self.hero_rect.width + 12 < wall.right:
                    if keys[pygame.K_LEFT]:  # Если движется влево
                        self.x = wall.right  # Останавливаемся у стены
                    if keys[pygame.K_RIGHT]:
                        self.x = wall.left - self.hero_rect.width
                    break

            for wall in walls:  # горизонт стены
                if self.hero_rect.colliderect(wall):
                    if self.hero_rect.y + 148 >= wall.y:
                        if keys[pygame.K_LEFT]:  # Если движется влево
                            self.x = wall.right  # Останавливаемся у стены
                        if keys[pygame.K_RIGHT]:
                            self.x = wall.left - self.hero_rect.width
                    break

            for platform in stop_platform:  # платформы(невидимые) для ходьбы сверху стены
                if self.hero_rect.colliderect(platform):
                    # реализация движения на этой платформе стоп
                    if (keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]) or \
                            (keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]):
                        self.hero = self.hero_image_go[self.update_hero_animation_left('go')]
                    else:
                        self.hero = hero_image_static
                    self.flag2 = False  # Проверка на столкновение с платформой
                    if self.velocity_y >= 0 and self.hero_rect.y < platform.y:  # условие для столкновения с плитами
                        # Проверка, что нижняя часть персонажа ниже верхней части платформы
                        self.y = platform.top - self.hero_rect.height  # Устанавливаем персонажа на платформу
                        self.on_ground = True
                        self.velocity_y = 0  # Сброс вертикальной скорости
                    break  # Выходим из цикла, если столкновение произошло
            else:
                # Если не произошло столкновения с любой платформой
                if self.y < 420:
                    self.on_ground = False  # Устанавливаем on_ground в False, если персонаж не на земле

            for platform in platforms:  # платформы по которым можно ходить
                if self.hero_rect.colliderect(platform):
                    self.flag2 = False  # Проверка на столкновение с платформой
                    if self.velocity_y >= 0 and self.hero_rect.y < platform.y:  # условие для столкновения с плитами
                        # Проверка, что нижняя часть персонажа ниже верхней части платформы
                        self.y = platform.top - self.hero_rect.height  # Устанавливаем персонажа на платформу
                        self.on_ground = True
                        self.on_platf = True
                        self.velocity_y = 0  # Сброс вертикальной скорости
                    elif self.velocity_y < 0:
                        self.y = platform.bottom  # Не позволяем персонажу проходить через платформу
                        self.velocity_y = 0  # Сброс вертикальной скорости
                    break  # Выходим из цикла, если столкновение произошло
            else:
                # Если не произошло столкновения с любой платформой
                self.on_platf = False
                if self.y < 420:
                    self.on_ground = False  # Устанавливаем on_ground в False, если персонаж не на земле

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.x >= 790:  # переход в новую игру
                bagr_s.stop()
                self.game2()

            # Отрисовка платформ
            for platform in platforms:
                pygame.draw.rect(screen, GRAY, platform)

            # Обновление анимации врага
            self.update_enemy_animation()
            enemy_images = self.enemy_images[self.current_enemy_frame]
            enemy_images = pygame.transform.scale(enemy_images, (120, 180))
            enemy_rect = enemy_images.get_rect()
            # создание пуль
            if self.on_ground and not self.hero == self.hero_hide and not self.on_platf \
                    and self.shoot_timer >= self.shoot_delay and (self.napr_enemy == -1 and self.x < self.xp or
                                                                  self.x > self.xp and self.napr_enemy == 1):
                self.shoot_timer = 0
                self.fire(self.xp, self.yp)

            if self.flag:
                enemy_images = pygame.transform.flip(enemy_images, True, False)

            # Отрисовка
            # Обновление пуль
            self.update_bullets()

            # Отрисовка пуль
            self.draw_bullets(screen)
            screen.blit(enemy_images, (self.xp, self.yp))  # Позиция врага 1
            # отрисовка коробок
            screen.blit(bx, (710, 300)), screen.blit(box, (634, 113)), screen.blit(box, (562, 113))
            # отрисовка древянных платформ, стен, опоры
            screen.blit(wood1, (782, -230)), screen.blit(wood2, (350, 163)), screen.blit(wood3, (540, 0)), \
                screen.blit(wood4, (200, 368)), screen.blit(wood5, (546, 195)), screen.blit(wood6, (540, 180)), \
                screen.blit(wood8, (282, 388))

            # забор рядом с врагом
            screen.blit(zaborchik, (220, 460))

            # отрисовка персонажа
            if self.hero == self.hero_hide:
                screen.blit(pygame.transform.flip(self.hero, True, False), (self.x, self.y + 40))
            else:
                if self.napr == -1:
                    screen.blit(pygame.transform.flip(self.hero, True, False), (self.x, self.y))
                else:
                    screen.blit(self.hero, (self.x, self.y))
                if self.action_cooldown > 0:
                    screen.blit(pygame.transform.scale(pygame.image.load('Предметы/1предмет.png'),
                                                       (500, 500)), (150, 20))  # заморозка игры
            # опора для лесов
            screen.blit(wood7, (200, 385))
            pygame.display.flip()
            clock.tick(70)

    def game2(self):
        self.bullets.clear()
        is_walking = False
        current_walk_sound = None
        arta.play()
        bombs = []  # Список для хранения бомб
        self.x, self.y = 0, 400
        self.on_ground = True
        self.velocity_y = 0
        self.hero_rect.topleft = (self.x, self.y)
        self.fade_to_black(420, 2)  # затемнение экрана
        self.anti_fade_to_black(720, 2)

        # Переменные для танка
        tank_image = pygame.image.load("Tank/танк.png")
        tank_image = pygame.transform.flip(tank_image, False, False)
        tank_image = pygame.transform.scale(tank_image, (tank_image.get_width() // 2, tank_image.get_height() // 2))
        tank_x = -600
        tank_y = 300  # Позиция по Y
        tank_speed = 2  # Скорость движения танка
        tank_visible = False  # Флаг видимости танка

        # Создание текста
        small_font = pygame.font.Font(None, 65)
        title_text = small_font.render("Огонь артиллерии", True, (255, 0, 0))
        display_text = True
        blink_timer = 0
        blink_interval = 500
        total_time = 0
        max_display_time = 7000
        start_ticks = pygame.time.get_ticks()

        # Создание маски для героя
        hero_mask = pygame.mask.from_surface(self.hero)

        # Поворот изображения бомбы на -45 градусов
        bomb_image_rotated = pygame.transform.rotate(bomb_image, -90)

        angle = math.radians(45)  # 45 градусов
        velocity = 5

        bomb_spawn_time = 4000  # 4 секунды в миллисекундах
        bombs_started = False  # Флаг, чтобы отслеживать, начали ли появляться бомбы

        # Таймер
        timer_start = 60  # 60 секунд
        timer_font = pygame.font.Font(None, 50)  # Шрифт для таймера
        timer_ticks = pygame.time.get_ticks()  # Время для отслеживания таймера
        timer_started = False  # Флаг для отслеживания, когда таймер должен начать

        help_text_font = pygame.font.Font(None, 35)  # Шрифт для текста
        help_text = help_text_font.render("До подмоги осталось:", True, 'red')  # Красный цвет

        tanks_without_person = [pygame.transform.scale(pygame.image.load('Tank/tank_without_person.png').
                                                       convert_alpha(), (482, 174)),
                                pygame.transform.scale(
                                    pygame.image.load('Tank/tank_without_person2.png').convert_alpha(),
                                    (482, 174)),
                                pygame.transform.scale(
                                    pygame.image.load('Tank/tank_without_person3.png').convert_alpha(),
                                    (482, 174))]  # танк без человека
        timer = 0  # для преходва в другую игру
        flag = False
        bagr_start = True
        while True:
            if bagr_start:
                bagr_s.play(-1)
                bagr_start = False
            # ограничение ходьбы персонажа
            if self.x < 0:
                self.x = 0
            if self.x > 691:
                self.x = 691

            # статичное фото персонажа при ничего не деланьи
            if self.on_ground:
                self.hero = hero_image_static
            timer += 1
            print(timer)
            screen.fill(WHITE)
            screen.blit(backg_game, (self.x_backg, self.y_backg))
            screen.blit(backg_game, (self.x_backg + backg_game.get_width(), self.y_backg))
            print(self.on_ground)

            current_ticks = pygame.time.get_ticks()
            elapsed_time = current_ticks - start_ticks
            blink_timer += elapsed_time
            start_ticks = current_ticks

            if blink_timer >= blink_interval:
                display_text = not display_text
                blink_timer = 0

            total_time += elapsed_time

            if display_text and total_time < max_display_time:
                screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 150))

            # Таймер
            if total_time >= 4000:  # Если прошло 4 секунды
                if not timer_started:
                    timer_started = True  # Начинаем отсчет таймера
                    timer_ticks = current_ticks  # Сбрасываем время для отслеживания таймера
                if timer_start > 0:
                    if current_ticks - timer_ticks >= 1000:  # Каждую секунду
                        timer_start -= 1
                        timer_ticks = current_ticks
                else:
                    tank_visible = True

            minutes = timer_start // 60
            seconds = timer_start % 60
            timer_text = f"{minutes:02}:{seconds:02}"  # Форматирование с ведущими нулями
            # Отображение таймера
            timer_surface = timer_font.render(timer_text, True, 'red')
            screen.blit(timer_surface, (10, 40))  # Отображаем таймер в верхнем левом углу

            screen.blit(help_text, (10, 10))

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                if self.on_ground:  # Движение влево
                    self.hero = self.hero_image_go[self.update_hero_animation_left('go')]
                self.napr = -1
                self.x -= self.move_speed
                if not is_walking:
                    current_walk_sound = random.choice(walk_sounds)
                    current_walk_sound.play(-1)  # Воспроизводим в цикле
                    is_walking = True
            if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:  # Движение вправо
                if self.on_ground:  # Движение влево
                    self.hero = self.hero_image_go[self.update_hero_animation_left('go')]
                self.napr = 1
                self.x += self.move_speed
                if not is_walking:
                    current_walk_sound = random.choice(walk_sounds)
                    current_walk_sound.play(-1)  # Воспроизводим в цикле
                    is_walking = True
            if keys[pygame.K_SPACE] and self.on_ground:  # Прыжок
                self.hero = hero_image_jump
                self.velocity_y = -12
                self.on_ground = False
                if is_walking:
                    current_walk_sound.stop()
                    is_walking = False

            else:
                # Если персонаж не движется, останавливаем звук
                if is_walking:
                    current_walk_sound.stop()  # Останавливаем звук
                    is_walking = False

            # Обновление физики
            if not self.on_ground and not self.on_platf:
                self.velocity_y += gravity  # Применение гравитации
                self.y += self.velocity_y  # Обновление вертикальной позиции

                # Проверка на столкновение с "землёй"
                if self.y >= 420:  # Предположим, что 400 - это высота земли
                    self.y = 420
                    self.on_ground = True
                    self.velocity_y = 0  # Сброс вертикальной скорости

                if self.velocity_y < -12:  # Установите -5 как значение для ограничения
                    self.velocity_y = -12

            self.hero_rect.topleft = (self.x, self.y)

            if bombs_started and random.randint(1, 100) <= 3:  # % шанс появления бомбы
                # Генерация случайной координаты X в пределах ширины экрана
                start_x = random.randint(0, WIDTH - bomb_image_rotated.get_width())  # Появление внутри экрана по оси X
                # Генерация фиксированной координаты Y для появления бомбы выше экрана
                start_y = random.randint(-100, 0)  # Бомбы будут появляться выше экрана
                bombs.append({'x': start_x, 'y': start_y,
                              'velocity_x': 0,  # Скорость по оси X равна 0
                              'velocity_y': velocity})  # Скорость по оси Y
                # Проверка, прошло ли 60 секунд, чтобы остановить появление бомб
            if timer_start > 0:  # Если таймер все еще идет
                if total_time >= 4000:  # Если прошло 4 секунды
                    if not bombs_started:
                        bombs_started = True  # Устанавливаем флаг, что бомбы начали появляться
            else:
                bombs_started = False

            # Обновление позиции бомб
            for bomb in bombs:
                bomb['y'] += bomb['velocity_y']  # Движение вниз по оси Y
                # Удаление бомб, которые вышли за пределы экрана
                if bomb['y'] > HEIGHT:
                    bombs.remove(bomb)

            # Обновление и отрисовка бомб
            for bomb in bombs[:]:  # Используем срез для безопасного удаления
                bomb_rect = pygame.Rect(bomb['x'], bomb['y'], bomb_image_rotated.get_width(),
                                        bomb_image_rotated.get_height())  # Используем размеры повернутого изображения
                screen.blit(bomb_image_rotated, (bomb['x'], bomb['y']))  # Отрисовка повернутой бомбы

                # Создание маски для бомбы
                bomb_mask = pygame.mask.from_surface(bomb_image_rotated)

                # Проверка на столкновение с героем
                offset = (bomb['x'] - self.x, bomb['y'] - self.y)  # Смещение для маски
                if hero_mask.overlap(bomb_mask, offset):
                    bagr_s.stop()
                    self.game_over(2)

                    # Вызов функции game_over при попадании бомбы

                # Удаление бомб, которые вышли за пределы экрана
                if bomb['y'] > HEIGHT or bomb['x'] < 0 or bomb['x'] > WIDTH:
                    bombs.remove(bomb)

            self.tank = tanks_without_person[self.update_animation_tank()]  # анимации танка
            # Движение танка
            if tank_visible:
                tank_x += tank_speed  # Двигаем танк вправо

                # Проверка, достиг ли танк правой границы экрана
                if tank_x > WIDTH - tank_image.get_width():  # Если танк достиг правой границы
                    tank_x = WIDTH - tank_image.get_width()  # Останавливаем танк у правой границы
                    self.tank = tanks_without_person[0]

                # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        timer = 0
                        # Проверка, находится ли герой рядом с танком
                        if (tank_x <= self.x <= tank_x + tank_image.get_width()) and (
                                tank_y <= self.y <= tank_y + tank_image.get_height()) and tank_x == \
                                WIDTH - tank_image.get_width():
                            flag = True
            if flag:
                self.tank = pygame.transform.scale(self.tanks[0], (482, 174))
                self.hero = None
            if timer > 50 and flag:  # время до перехода в новый гамис
                bagr_s.stop()
                self.game_tank()
            if tank_visible:
                screen.blit(self.tank, (tank_x, 350))
            if self.hero:
                if self.napr == -1:
                    screen.blit(pygame.transform.flip(self.hero, True, False), (self.x, self.y))
                else:
                    screen.blit(self.hero, (self.x, self.y))

            pygame.display.flip()  # Обновляем экран только один раз за кадр
            clock.tick(60)  # Ограничиваем FPS до 60

    def game_tank(self):
        self.bullets.clear()
        self.fade_to_black(420, 3)  # затемнение экрана
        self.anti_fade_to_black(720, 3)
        backg_speed = 1  # скорость фона
        action_cooldown = 0  # заморозка ходьбы
        self.napr_enemy = None
        zabor_x = 1300
        # фото снарядов
        bb = pygame.transform.scale(pygame.image.load('бум/снаряды/бб.png').convert_alpha(), (56, 54))
        pb = pygame.image.load('бум/снаряды/пб.jpg').convert_alpha()
        of = pygame.transform.scale(pygame.image.load('бум/снаряды/оф.png').convert_alpha(), (56, 54))
        # прямоуг снарядов
        rects = [pygame.Rect(609, 100, 56, 54), pygame.Rect(349, 100, 56, 54), pygame.Rect(109, 100, 56, 54)]

        our_tank_x = 20
        click = False
        anti_tank = pygame.transform.scale(pygame.image.load('Tank/пушка.png').convert_alpha(), (300, 110))
        x_text, y_text = 230, 20
        text_surface = font.render('Проводятся баллистические расчёты...', True, (207, 25, 37))
        text_surface = pygame.transform.scale(text_surface, (369, 50))

        zabor_image = pygame.transform.scale(pygame.image.load('photo ds/забор.png').convert_alpha(), (20, 90))
        btns = {
            "8": pygame.Rect(310, 80, 50, 50),
            "-4": pygame.Rect(380, 80, 50, 50),
            "2": pygame.Rect(450, 80, 50, 50)
        }
        btns_1 = {
            "Бронебойный": pygame.Rect(130, 80, 0, 0),
            "Фугасный": pygame.Rect(350, 80, 50, 0),
            "Подкалиберный": pygame.Rect(640, 80, 0, 0)
        }
        tank_x = 800  # Начальная позиция пушки (вне экрана)
        target_x = 500  # Целевая позиция, куда пушка должна выехать
        speed = 0  # Скорость, с которой пушка будет выезжать
        timer = 0
        x_bah, y_bah = 600, 440
        check = 0  # нужно для отслеживания клика так как (click) не сработал

        # вражеский бомбардировщик и бомба
        enemy_fly = pygame.image.load('enemy/самолет_враг.png').convert_alpha()
        width_fly, height_fly, x_fly, y_fly = 0, 0, 0, 0
        bomb = pygame.image.load('photo ds/бомба.png')
        width_bomb, height_bomb, x_bomb, y_bomb = 0, 0, 0, 0

        # подсказка
        text_surface_bomb = font.render('!!!Покиньте технику "E" !!!', True, (207, 25, 37))
        text_surface_bomb = pygame.transform.scale(text_surface_bomb, (369, 50))

        # шалаш и человечик с рпг и координаты
        schalach_not_boom = pygame.transform.scale(pygame.image.load('photo ds/шалашик.png').convert_alpha(),
                                                   (250, 250))
        rpg_person = pygame.transform.scale(pygame.image.load('enemy/челсрпгС.png').convert_alpha(),
                                            (150, 150))
        without_rpg_person = pygame.transform.scale(pygame.image.load('enemy/челсрпгБ.png').convert_alpha(),
                                                    (150, 150))
        schalach_boom = pygame.transform.scale(pygame.image.load('photo ds/шалашик_бабах.png').convert_alpha(),
                                               (270, 265))

        schalach = schalach_not_boom

        # флаги для коррекции отрисовки
        antitanf_flag = False  # влаг для смещения
        flag_bomb = False  # флаг для выстрела по зданию
        antitank_person_flag = True
        bomb_activate = False
        flag_rpg = False
        check_person = True
        flag_tank_damaged = False
        flag_leave = False

        # подбитый танк и танк без человека
        tank_damaged = pygame.transform.scale(pygame.image.load('Tank/tank_damaged.png').convert_alpha(),
                                              (432, 144))
        tank_without_person = pygame.transform.scale(
            pygame.image.load('Tank/tank_without_person.png').convert_alpha(),
            (432, 144))

        # personash
        self.hero = pygame.transform.scale(hero_image_static, (100, 100))
        self.x, self.y = 20, 490  # координаты персонажа

        # дом(переход в новую локацию)
        x_house = 1070  # коорд дома
        dom = pygame.transform.scale(pygame.image.load('photo ds/dom.png').convert_alpha(),
                                     (650, 650))
        # упр-ий антитанком
        antitank_voenni = pygame.transform.scale(pygame.image.load('enemy/военный_антитанк.png').convert_alpha(),
                                                 (130, 150))
        # хар-ки персонажа
        speed_hero = 0
        jump_strength = 8
        svist = pygame.mixer.Sound('sounds/свист.wav')
        tank_sound = pygame.mixer.Sound('sounds/танкдвиж.wav')
        tank_fire = pygame.mixer.Sound('sounds/танквыстрел.mp3')
        babah = pygame.mixer.Sound('sounds/babax.wav')
        tank_fire.set_volume(0.3)
        is_sound_playing = False
        is_walking = True

        bagr_start = True
        while True:
            if bagr_start:
                bagr_s.play(-1)
                bagr_start = False
            print(timer)
            print(self.count)

            if self.on_ground:
                self.hero = hero_image_static
            if self.action_cooldown > 0:
                self.action_cooldown -= 1
            else:
                if self.x < 800:
                    self.x_backg -= 1
                    if not is_sound_playing:
                        tank_sound.play(-1)  # Воспроизводим в цикле
                        is_sound_playing = True

            # Логика остановки фона
            if self.count == 1 and not click:  # остановка фона
                self.x_backg += 1
                if is_sound_playing:
                    tank_sound.stop()
                    is_sound_playing = False

            elif self.count == 2 and check == 1:
                self.x_backg += 1
                if is_sound_playing:
                    tank_sound.stop()
                    is_sound_playing = False

            elif flag_bomb and y_bomb > 470:
                self.x_backg += 1
                if is_sound_playing:
                    tank_sound.stop()
                    is_sound_playing = False

            if self.count == 2 and check == 0:  # забор уезжает после выстрела
                zabor_x -= 1

            if antitanf_flag:  # смещение антитанка после смерти
                tank_x -= 1

            timer += 1
            screen.fill(WHITE)  # Очистка экрана
            screen.blit(backg_game, (self.x_backg, self.y_backg))  # Отрисовка фона игры
            screen.blit(backg_game, (self.x_backg + backg_start.get_width(), self.y_backg))
            keys = pygame.key.get_pressed()

            if timer == 0:
                tank_fire.play()

            if action_cooldown > 0:
                action_cooldown -= 1  # Уменьшаем таймер блокировки
            elif bomb_activate:  # разрешаеи ходить после взрыва бомбы
                if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    self.hero = hero_image_static
                    self.napr = -1
                    self.x -= 0

                if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and self.x <= 515:  # Движение вправо
                    if self.count == 4:
                        if not is_walking:
                            current_walk_sound = random.choice(walk_sounds)
                            current_walk_sound.play(-1)  # Воспроизводим в цикле
                            is_walking = True
                        # 4е событие
                        if x_house == 300:
                            backg_speed = 0
                            speed_hero = 1.5

                        else:
                            x_house -= 1
                    if self.on_ground:  # Движение вправо
                        self.hero = self.hero_image_go[self.update_hero_animation_left('go')]
                    self.napr = 1
                    self.x += speed_hero
                    our_tank_x -= 1
                    self.x_backg -= backg_speed

                if keys[pygame.K_SPACE] and self.on_ground:  # Прыжок
                    self.hero = hero_image_jump
                    self.velocity_y = -jump_strength
                    self.on_ground = False

            # Обновление физики
            if not self.on_ground and not self.on_platf:
                self.velocity_y += gravity  # Применение гравитации
                self.y += self.velocity_y  # Обновление вертикальной позиции

                # Проверка на столкновение с "землёй"
                if self.y >= 490:  # Предположим, что 400 - это высота земли
                    self.y = 490
                    self.on_ground = True
                    self.velocity_y = 0  # Сброс вертикальной скорости
            # Перемещение пушки
            if tank_x > target_x and self.count == 0:  # Если пушка еще не достигла целевой позиции
                tank_x -= speed  # Перемещаем пушку влево

            self.mig += 1  # миг текст
            if self.count == 1 and not click:
                text_surface = font.render('x² + 8x + 16 = 0   x-?', True, (207, 25, 37))
                x_text = 200
                timer += 1
            if self.x_backg <= -720:  # движение антитанка
                speed = 3.2
            else:
                speed = 0

            self.tank = self.tanks[self.update_animation_tank()]
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and ((not click and self.count == 1) or (not click and self.count == 2)):
                        mouse_pos = event.pos
                        # 1 игра
                        if btns["8"].collidepoint(mouse_pos) and self.count == 1:
                            timer = -13
                            click = True
                            self.left_Fire = True
                            self.fire(570, 460)
                            x_bah, y_bah = 230, 440
                            text_surface = font.render('Неудача', True, (207, 25, 37))
                            x_text += 90
                        elif btns["-4"].collidepoint(mouse_pos) and self.count == 1:
                            x_bah, y_bah = 600, 440
                            antitanf_flag = True
                            tank_x -= 1
                            timer = -13
                            click = True
                            self.left_Fire = False
                            self.fire(327, 457)
                            text_surface = font.render('Расчёты подведены', True, (207, 25, 37))
                            check = 1
                            x_text -= 40
                        elif btns["2"].collidepoint(mouse_pos) and self.count == 1:
                            x_bah, y_bah = 230, 440
                            timer = -13
                            click = True
                            self.left_Fire = True
                            self.fire(570, 460)
                            text_surface = font.render('Неудача', True, (207, 25, 37))
                            x_text += 90
                        # 2 игра
                        if rects[0].collidepoint(mouse_pos) and self.count == 2:
                            flag_rpg = True  # для смены изобр противника
                            text_surface = None  # убираем текст
                            x_bah, y_bah = 230, 440
                            timer = -18
                            self.left_Fire = True
                            self.fire(570, 480)
                            check = 0
                        elif rects[1].collidepoint(mouse_pos) and self.count == 2:
                            text_surface = None
                            x_bah, y_bah = 600, 440
                            timer = -13
                            self.left_Fire = False
                            self.fire(327, 457)
                            check = 0
                        elif rects[2].collidepoint(mouse_pos) and self.count == 2:
                            flag_rpg = True  # для смены изобр противника
                            text_surface = None
                            x_bah, y_bah = 230, 440
                            timer = -18
                            self.left_Fire = True
                            self.fire(570, 480)
                            check = 0

            if timer == 2000 and self.count == 1:  # время на размышления при антитанке
                click = True
                timer = -13
                x_bah, y_bah = 230, 440
                self.left_Fire = True
                self.fire(570, 460)

            if timer == 1400 and self.count == 2:  # время на размышления при лагере
                click = True
                timer = -13
                x_bah, y_bah = 230, 425
                self.left_Fire = True
                self.fire(570, 480)
                flag_rpg = True  # для смены изобр противника

            if click and self.count == 2:  # сброс флага (клик)
                click = False

            for bullet in self.bullets:  # проверка на столкновения с пулями
                if anti_tank and anti_tank.get_rect(topleft=(tank_x + 100, 420)).colliderect(bullet.rect):
                    anti_tank = pygame.transform.scale(pygame.image.load('Tank/пушка_ded.png').convert_alpha(),
                                                       (300, 110))  # заменяем фото пушки
                    text_surface = font.render('', True, (207, 25, 37))
                    x_text = -1000
                    self.bullets.remove(bullet)  # Удаляем пулю после столкновения
                    antitank_person_flag = False
                    break  # Выходим из цикла, чтобы не проверять другие пули
                tank_rect = self.tank.get_rect(
                    topleft=(our_tank_x, 450))  # прямоугольник танка правильно установле
                if self.count == 1:  # н
                    if tank_rect.colliderect(bullet.rect) and timer > 10:
                        bagr_s.stop()
                        tank_sound.stop()
                        self.game_over(3)
                        # Вызываем функцию окончания игры
                        self.bullets.remove(bullet)  # Удаляем пулю после столкновения
                        text_surface = None
                elif self.count == 2:
                    if tank_rect.colliderect(bullet.rect) and timer > 5:
                        tank_sound.stop()
                        bagr_s.stop()
                        self.game_over(3)
                        # Вызываем функцию окончания игры
                        self.bullets.remove(bullet)  # Удаляем пулю после столкновения
                        text_surface = None

            if self.x_backg <= -backg_start.get_width():
                self.x_backg = 0
                self.count += 1  # обновляем события

            if check == 1 and self.count == 1:  # отодвигаем забор до нужной позиции
                zabor_x -= 1

            # отрисовка
            # прямоуг где будут отобр ответы
            if self.mig >= 55:
                if text_surface:
                    screen.blit(text_surface, (x_text - 9, y_text))
                    if self.mig == 110:
                        self.mig = 0

            if self.count == 1 and not click:
                screen.blit(text_surface, (x_text - 9, y_text))
                for button_name, button_rect in btns.items():
                    pygame.draw.rect(screen, GRAY, button_rect)
                    button_text = button_font.render(button_name.capitalize(), True, BLACK)
                    screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2,
                                              button_rect.y + (button_rect.height - button_text.get_height()) // 2))
                self.tank = self.tanks[0]

            if self.count == 2 and check == 1:  # встреча со 2м врагом
                text_surface = font.render('Выбор снярядов...', True, (207, 25, 37))
                text_surface = pygame.transform.scale(text_surface, (329, 40))
                x_text = 240  # позиция текста
                for button_name, button_rect in btns_1.items():
                    button_text = button_font.render(button_name.capitalize(), True, (224, 224, 224))
                    button_text = pygame.transform.scale(button_text, (150, 40))  # отрисовка текста
                    screen.blit(button_text, (button_rect.x + (button_rect.width - button_text.get_width()) // 2,
                                              button_rect.y + (button_rect.height - button_text.get_height()) // 2))
                    screen.blit(pb, (609, 100)), screen.blit(of, (349, 100)), screen.blit(bb, (109, 100)),
                self.tank = self.tanks[0]

            if flag_bomb and y_bomb == 480:
                self.tank = self.tanks[0]

            if flag_tank_damaged:  # изображение танка при подрыве
                self.tank = tank_damaged
            elif flag_leave:
                self.tank = tank_without_person

            if self.count == 3 and timer == 1420:  # самолет логика
                flag_bomb = True
                plane_sound.play(0)
                plane_sound.set_volume(0.6)
                svist.play(0)
                width_fly, height_fly, x_fly, y_fly = 440, 330, -250, 170
            if self.count == 3 and timer > 1420 and height_fly > 30:
                x_fly += 5
                width_fly -= 1
                height_fly -= 1
                y_fly -= 2

            if flag_bomb and timer == 1450:  # бомба логика
                width_bomb, height_bomb, x_bomb, y_bomb = 50, 50, 120, 300

            if self.count == 3 and timer > 1450 and y_bomb != 480:
                x_bomb += 2.9
                y_bomb += 2

            if self.count == 4 and 525 >= self.x >= 434 and keys[pygame.K_e]:
                bagr_s.stop()
                self.game_plante_bomb()

            # отрисовка

            # бомба
            if not bomb_activate:
                screen.blit(pygame.transform.scale(bomb, (width_bomb, height_bomb)), (x_bomb, y_bomb))

            # zabors
            screen.blit(zabor_image, (zabor_x - 10, 450)), screen.blit(zabor_image, (zabor_x + 20, 470))
            screen.blit(zabor_image, (zabor_x + 50, 490))

            # фото шалашика
            if schalach == schalach_not_boom:
                screen.blit(schalach, (zabor_x + 45, 290))
            else:
                screen.blit(schalach, (zabor_x + 40, 286))
            # house

            screen.blit(dom, (x_house - 40, 70))
            print(timer)
            if anti_tank:
                screen.blit(anti_tank, (tank_x, 420))  # Отрисовка пушки на обновленной позиции
            if antitank_person_flag:
                screen.blit(antitank_voenni, (tank_x + 140, 420))  # управляющий антитанком
            # pygame.draw.rect(screen, (51, 156, 131), (210, 0, 400, 170))
            screen.blit(self.tank, (our_tank_x, 450))
            if click and 3 < timer < 40:  # отрисовка взрыва
                vzriv = self.babah_images[self.update_animation_bah()]
                screen.blit(vzriv, (x_bah, y_bah))

            if self.count == 3 and 1880 > timer > 1800:  # отрисовка взрыва от бомбы самолёта
                if timer == 1810:
                    babah.set_volume(0.3)
                    babah.play(0)
                    flag_tank_damaged = True
                bomb_activate = True
                vzriv = self.babah_images[self.update_animation_bah()]
                screen.blit(pygame.transform.scale(vzriv, (310, 310)), (x_bomb - 180, 300))
                if not flag_leave and timer == 1820:
                    bagr_s.stop()
                    self.tank = self.tanks[0]
                    self.game_over(3)

            if self.count == 3 and 1800 >= timer >= 1600:  # отрисовка подсказки
                action_cooldown = 100
                if keys[pygame.K_e]:
                    flag_leave = True
                screen.blit(text_surface_bomb, (215, 20))

            # персонаж
            if flag_leave:
                if self.napr == -1:
                    screen.blit(pygame.transform.flip(pygame.transform.scale(self.hero, (70, 100)), True, False),
                                (self.x, self.y))
                else:
                    screen.blit(pygame.transform.scale(self.hero, (70, 100)), (self.x, self.y))

            # самолет
            screen.blit(pygame.transform.scale(enemy_fly, (width_fly, height_fly)), (x_fly, y_fly))
            # Обновление пуль
            self.update_bullets()

            # Отрисовка пуль
            self.draw_bullets(screen)
            # фото чел рпг
            if check_person:  # отображение врага с рпг
                if not flag_rpg:
                    screen.blit(rpg_person, (zabor_x + 45, 420))
                else:
                    screen.blit(without_rpg_person, (zabor_x + 45, 420))
            if 5 < timer < 100 and self.count == 2 and not flag_rpg:  # отрисовка взрыва'
                schalach = schalach_boom
                x_bah -= 1
                if timer == 24:
                    check_person = None  # убираем персонажа
                self.bullets.clear()
                vzriv = self.babah_images[self.update_animation_bah()]
                screen.blit(pygame.transform.scale(vzriv, (210, 210)), (x_bah - 42, y_bah - 60))
            pygame.display.flip()
            clock.tick(60)

    def game_plante_bomb(self):
        # self.fade_to_black(420)  # затемнение экрана
        # self.anti_fade_to_black(720)  # растемнение экрана
        flag_en = True  # напр врага сверху
        timer = 2000
        self.flag = False  # напр врага снизу
        flag = True  # нужен для отлеживания минирования
        home_backg = pygame.image.load('photo ds/фон дома.png').convert_alpha()
        home_bomb_backg = pygame.image.load('photo ds/home_backg_bomb.png').convert_alpha()
        home_bomb_backg_min = pygame.image.load('photo ds/home_backg_bomb_minn.png').convert_alpha()
        # Создание платформ(невидимые)
        platforms = [pygame.Rect(664, 424, 70, 10), pygame.Rect(539, 278, 300, 10), pygame.Rect(-35, 278, 387, 10)]
        self.hero_rect = pygame.Rect(self.x, self.y, 110, 160)
        # список с вертикальными стенами(используется для блокировки)
        jump_strength = 12
        stops = []
        # стены верт-ые
        walls = [pygame.Rect(0, 0, 1, 800), pygame.Rect(800, 0, 1, 800)]
        walls_draw = []
        self.x, self.y = 330, 400
        x_enemy, y_enemy = 100, 100
        self.xp, self.yp = 458, 400  # координаты врага
        # self.fade_to_black(420)  # затемнение экрана
        # self.anti_fade_to_black(720)  # растемнение экрана
        backg = None
        is_walking = False
        current_walk_sound = None
        napr_enemy = 0
        bomb_pik = pygame.mixer.Sound('sounds/бомбапик.mp3')
        babah = pygame.mixer.Sound('sounds/babax.wav')
        bomb_start = True

        bagr_start = True
        while True:
            if bagr_start:
                bagr_s.play(-1)
                bagr_start = False
            # Обновление анимации врага
            self.update_enemy_animation()
            enemy_images = self.enemy_images[self.current_enemy_frame]
            enemy_images = pygame.transform.scale(enemy_images, (120, 180))
            enemy_images_up = enemy_images
            enemy_rect = enemy_images.get_rect()

            keys = pygame.key.get_pressed()
            if flag:
                backg = home_backg

            if 40 > self.x > 0 and 118 >= self.y >= 80:
                if bomb_start:
                    bomb_pik.play(0)
                    bomb_start = False
                # меняем фон в процессе минирования бомбы
                if keys[pygame.K_e]:
                    backg = home_bomb_backg
                    flag = False
                if flag:
                    backg = home_bomb_backg_min

            self.shoot_timer += 1  # уdелечение таймера для стрельбы

            if not flag:  # время до взрыва
                timer -= 1
                if timer == 0:
                    babah.play(0)
                    babah.set_volume(0.2)
                    bomb_pik.stop()
                    bagr_s.stop()
                    self.game_over(4)

            if not flag and 40 > self.x > 0 and 400 == self.y:
                if keys[pygame.K_e]:
                    self.game_finall()

            if self.on_ground:
                self.hero = hero_image_static

            screen.fill(WHITE)  # Очистка экрана
            screen.blit(backg, (0, 0))  # Отрисовка фона игры

            if self.action_cooldown > 0:
                self.action_cooldown -= 1  # Уменьшаем таймер блокировки

            else:
                if keys[pygame.K_LEFT]:  # Движение влево
                    if self.on_ground:
                        self.hero = self.hero_image_go[self.update_hero_animation_left('go')]

                    self.napr = -1
                    self.x -= self.move_speed
                elif keys[pygame.K_RIGHT]:  # Движение вправо
                    if self.on_ground:
                        self.hero = self.hero_image_go[self.update_hero_animation_left('go')]
                    self.napr = 1
                    self.x += self.move_speed
                if keys[pygame.K_SPACE] and self.on_ground:  # Прыжок
                    self.hero = hero_image_jump
                    self.velocity_y = -jump_strength
                    self.on_ground = False

            if self.xp > 140 and self.flag:  # передвижение врага
                self.napr_enemy = -1
                self.xp -= 2
                if self.xp == 140:
                    self.flag = False
            else:
                self.napr_enemy = 1
                self.xp += 2
                if self.xp == 658:
                    self.flag = True

            if x_enemy > 2 and flag_en:  # передвижение врага 2
                self.napr_enemy_und = -1
                enemy_images_up = pygame.transform.flip(enemy_images_up, True, False)
                x_enemy -= 2
                if x_enemy == 2:
                    flag_en = False
            else:
                self.napr_enemy_und = 1
                enemy_images_up = pygame.transform.flip(enemy_images_up, False, False)
                x_enemy += 2
                if x_enemy == 340:
                    flag_en = True

            if keys[pygame.K_r] and not keys[pygame.K_SPACE] \
                    and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and self.on_ground:  # герой скрывается
                self.hero = self.hero_hide

            # Обновление физики
            if not self.on_ground:
                self.velocity_y += gravity  # Применение гравитации
                self.y += self.velocity_y  # Обновление вертикальной позиции

                # Проверка на столкновение с "землёй"
                if self.y >= 400:  # Предположим, что 400 - это высота земли
                    self.y = 400
                    self.on_ground = True
                    self.velocity_y = 0  # Сброс вертикальной скорости

            # Обновление позиции прямоугольника героя
            self.hero_rect.topleft = (self.x, self.y + 2)

            # проверка на столкновение с пулями
            for bullet in self.bullets:
                if self.hero_rect.colliderect(bullet.rect):
                    bomb_pik.stop()
                    bagr_s.stop()
                    self.game_over(4)

            # Проверка на столкновение со стеной
            for wall in stops:  # горизонт стены(блокирующие стены)
                if self.hero_rect.colliderect(wall) and wall.left < self.x + self.hero_rect.width + 12 < wall.right:
                    if keys[pygame.K_LEFT]:  # Если движется влево
                        self.x = wall.right  # Останавливаемся у стены
                    if keys[pygame.K_RIGHT]:
                        self.x = wall.left - self.hero_rect.width
                    break

            for wall in walls:  # горизонт стены
                if self.hero_rect.colliderect(wall):
                    if self.hero_rect.y + 148 >= wall.y:
                        if keys[pygame.K_LEFT]:  # Если движется влево
                            self.x = wall.right  # Останавливаемся у стены
                        if keys[pygame.K_RIGHT]:
                            self.x = wall.left - self.hero_rect.width
                    break
            for platform in platforms:  # платформы, по которым можно ходить
                if self.hero_rect.colliderect(platform):  # Проверяем столкновение с платформой
                    # Проверка, что персонаж падает (velocity_y >= 0) и
                    # нижняя часть персонажа выше верхней части платформы
                    if self.velocity_y >= 0 and self.hero_rect.bottom <= platform.bottom:
                        if self.y == 264:
                            self.on_platf = False
                        else:
                            self.on_platf = True
                        # Устанавливаем персонажа на платформу
                        self.y = platform.top - self.hero_rect.height
                        self.on_ground = True
                        self.velocity_y = 0  # Сброс вертикальной скорости

                        break  # Выходим из цикла, если столкновение произошло
            else:
                # Если не произошло столкновения с любой платформой
                self.on_platf = False
                if self.y < 400:
                    self.on_ground = False  # Устанавливаем on_ground в False, если персонаж не на земле

            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Отрисовка платформ

            # создание пуль
            # нижний враг
            if self.on_ground and not self.hero == self.hero_hide and not self.on_platf \
                    and self.shoot_timer >= self.shoot_delay and (self.napr_enemy == -1 and self.x < self.xp or
                                                                  self.x > self.xp and self.napr_enemy == 1):
                self.shoot_timer = 0
                self.fire(self.xp, self.yp - 15)
            # врехний враг
            if not self.hero == self.hero_hide and self.on_platf and self.y != 264 \
                    and self.shoot_timer >= self.shoot_delay and (self.napr_enemy_und == -1 and self.x < x_enemy or
                                                                  self.x > x_enemy and self.napr_enemy_und == 1):
                self.shoot_timer = 0
                self.fire_en(x_enemy, y_enemy + 8)

            if self.flag:
                enemy_images = pygame.transform.flip(enemy_images, True, False)

            # Отрисовка
            # отрисовка персонажа
            if self.hero == self.hero_hide:
                if self.y == 400:
                    y = -5
                else:
                    y = 20
                screen.blit(pygame.transform.flip(self.hero, True, False), (self.x, self.y + y))
            else:
                if self.napr == -1:
                    screen.blit(pygame.transform.flip(self.hero, True, False), (self.x, self.y))
                else:
                    screen.blit(self.hero, (self.x, self.y))

            # враги
            screen.blit(enemy_images, (self.xp, self.yp - 15))  # Позиция врага 1
            screen.blit(enemy_images_up, (x_enemy, y_enemy))
            # Обновление пуль
            self.update_bullets()

            # Отрисовка пуль
            self.draw_bullets(screen)

            for img in walls_draw:
                pygame.draw.rect(screen, GRAY, img)

            pygame.display.flip()
            clock.tick(70)

    def game_finall(self):
        zabor_image = pygame.transform.scale(pygame.image.load('photo ds/забор.png').convert_alpha(), (20, 90))
        zabor_x = 600
        # верт фото
        vertolet = [pygame.transform.scale(pygame.image.load('вертолёт/frame_0.png').convert_alpha(), (540, 250)),
                    pygame.transform.scale(pygame.image.load('вертолёт/frame_1.png').convert_alpha(), (540, 250)),
                    pygame.transform.scale(pygame.image.load('вертолёт/frame_2_delay-0.1s.png').convert_alpha(),
                                           (540, 250)),
                    pygame.transform.scale(pygame.image.load('вертолёт/frame_верт3.png').convert_alpha(),
                                           (540, 250))]
        # коорд верт
        vert_x, vert_y = 1200, 300
        # чел рядом с вертолётом
        person_near_vert = pygame.image.load('photo ds/character_frame2_aseprite (2)1.png')
        self.napr = 1
        # дом
        dom = pygame.transform.scale(pygame.image.load('photo ds/dombabah.png').convert_alpha(),
                                     (850, 850))
        backg = pygame.image.load('photo ds/svo2.png')
        x_house, y_house = 20, 200
        self.x, self.y = 420, 400
        # self.fade_to_black(420)  # затемнение экрана
        # self.anti_fade_to_black(720)  # растемнение экрана
        timer = 0  # таймер для отрисовки взрывов
        babah = pygame.mixer.Sound('sounds/babax.wav')
        babah.set_volume(0.2)
        babah.play(0)
        vert_sound = pygame.mixer.Sound('sounds/верт.wav')
        vert_start = True

        bagr_start = True
        while True:
            if bagr_start:
                bagr_s.play(-1)
                bagr_start = False
            timer += 1
            if self.on_ground:
                self.hero = hero_image_static

            screen.fill(WHITE)  # Очистка экрана
            screen.blit(backg, (self.x_backg, self.y_backg))  # Отрисовка фона игры
            screen.blit(backg, (self.x_backg + backg_start.get_width(), self.y_backg))
            keys = pygame.key.get_pressed()

            if vert_start:
                vert_sound.play(-1)
                vert_start = False

            if self.action_cooldown > 0:
                self.action_cooldown -= 1  # Уменьшаем таймер блокировки
                if self.action_cooldown == 0:
                    self.hero_hide_flag = True

            else:
                if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    self.napr = -1
                    self.x -= 0
                if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:  # Движение вправо
                    self.x_backg -= 2
                    vert_x -= 2
                    zabor_x -= 2
                    if self.on_ground:  # Движение влево
                        self.hero = self.hero_image_go[self.update_hero_animation_left('go')]
                    self.napr = 1
                    self.x += 0
                    x_house -= 2
                if keys[pygame.K_SPACE] and self.on_ground:  # Прыжок
                    self.hero = hero_image_jump
                    self.velocity_y = -jump_strength
                    self.on_ground = False

            # Обновление физики
            if not self.on_ground and not self.on_platf:
                self.velocity_y += gravity  # Применение гравитации
                self.y += self.velocity_y  # Обновление вертикальной позиции

                # Проверка на столкновение с "землёй"
                if self.y >= 420:  # Предположим, что 400 - это высота земли
                    self.y = 420
                    self.on_ground = True
                    self.velocity_y = 0  # Сброс вертикальной скорости

            # Обновление позиции прямоугольника героя
            self.hero_rect.topleft = (self.x, self.y)
            # Обработка событий
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.x_backg <= -backg_start.get_width():  # Если фон полностью сдвинулся влево, сбрасываем его позицию
                self.x_backg = 0
                self.count += 1  # обновляем события

            if vert_x <= 230:
                vert_sound.stop()
                bagr_s.stop()
                self.game_end()

            # отрисовка
            # вертолет
            screen.blit(vertolet[self.update_animation_vertolet()], (vert_x, vert_y))
            # человек у вертолёта
            screen.blit(pygame.transform.scale(person_near_vert, (120, 190)), (vert_x - 70, 360))
            # zabors
            screen.blit(zabor_image, (zabor_x - 10, 450)), screen.blit(zabor_image, (zabor_x + 20, 470))
            screen.blit(zabor_image, (zabor_x + 50, 490))
            # персонаж
            if self.napr == -1:
                screen.blit(pygame.transform.flip(self.hero, True, False), (self.x, self.y))
            else:
                screen.blit(self.hero, (self.x, self.y))
            # дом
            screen.blit(dom, (x_house - 350, y_house - 325))
            # взрывы
            vzriv = self.babah_images[self.update_animation_bah()]
            if timer <= 150:
                screen.blit(vzriv, (x_house + 190, 215))
                screen.blit(pygame.transform.scale(vzriv, (240, 240)), (x_house - 20, 185))
                screen.blit(vzriv, (x_house + 180, 365))
            pygame.display.flip()
            clock.tick(70)


def main_menu():
    while True:
        draw_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левый клик мыши
                    mouse_pos = event.pos
                    if buttons["start"].collidepoint(mouse_pos):
                        game_instance = Game()
                        game_instance.game_tank()
                    elif buttons["exit"].collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()


if __name__ == "__main__":
    main_menu()
