# Importing python libraries
import pygame, sys
import button
import csv

pygame.init()  # Initiate PyGame
pygame.mixer.init()
swidth = 1280  # Setting variable for width of screen
sheight = 690  # Setting variable for height of screen
win = pygame.display.set_mode((swidth, sheight))  # Creating pygame window

# Load in images and backgrounds:
splash = pygame.image.load("Assets/Backgrounds/splash_screen.jpg")
level1_img = pygame.image.load("Assets/Backgrounds/level1.png")
level2_img = pygame.image.load("Assets/Backgrounds/level2.jpeg")
level3_img = pygame.image.load("Assets/Backgrounds/level3.jpeg")
throne_room = pygame.image.load("Assets/Backgrounds/throne.jpg")
menubg = pygame.image.load("Assets/Backgrounds/starting screen.webp")
menubg = pygame.transform.scale(menubg, (swidth, sheight))
dash_img = pygame.image.load("Assets/Edmund/dash.png")
dash_icon = pygame.image.load("Assets/dash_symbol.png")
finish_flag = pygame.image.load("Assets/finish.png")

tutorial1 = pygame.image.load("Assets/Tutorial/tutorial1.png")
tutorial2 = pygame.image.load("Assets/Tutorial/tutorial2.png")
tutorial3 = pygame.image.load("Assets/Tutorial/tutorial3.png")
tutorial4 = pygame.image.load("Assets/Tutorial/tutorial4.png")
tutorial5 = pygame.image.load("Assets/Tutorial/tutorial5.png")

font = pygame.font.SysFont('Futura', 30)  # Set font for writing text

level = 1  # what level the user is in
score = 0
difficulty = 'easy'
score_array = []
max_score = 0

# Empty arrays to store player animation images:
walkLeft = []
walkRight = []
idleLeft = []
idleRight = []
jumpRight = []
jumpLeft = []
fallLeft = []
fallRight = []
attackLeft = []
attackRight = []

# Empty array to store images for the tile mapping process:
grassTilesList = []
cobbleTilesList = []
brickTilesList = []

# Empty arrays to store enemy animation images:
enemyDead = pygame.image.load("Assets/Enemy/Level1/dead.png")

enemy1Right = []
enemy1Left = []
enemy1AttackRight = []
enemy1AttackLeft = []
enemy1IdleLeft = []
enemy1IdleRight = []

enemy2Right = []
enemy2Left = []
enemy2AttackRight = []
enemy2AttackLeft = []
enemy2IdleLeft = []
enemy2IdleRight = []
enemy2DeathLeft = []
enemy2DeathRight = []

enemy3Right = []
enemy3Left = []
enemy3AttackRight = []
enemy3AttackLeft = []
enemy3IdleLeft = []
enemy3IdleRight = []
enemy3DeathLeft = []
enemy3DeathRight = []

boss1Right = []
boss1Left = []
boss1AttackRight = []
boss1AttackLeft = []
boss1DieRight = []
boss1DieLeft = []

boss2Right = []
boss2Left = []
boss2AttackRight = []
boss2AttackLeft = []
boss2DieRight = []
boss2DieLeft = []

kingRight = []
kingLeft = []
kingAttackRight = []
kingAttackLeft = []
kingDieRight = []
kingDieLeft = []

# Loading in sound effects for the game:
hitMetal = pygame.mixer.Sound("Assets/SoundEffects/hit.wav")
swing = pygame.mixer.Sound("Assets/SoundEffects/swing.wav")
buttonClicked = pygame.mixer.Sound("Assets/SoundEffects/button_clicked.wav")

# Loading in button images:
play_img = pygame.image.load("Assets/Buttons/start_btn.png")
tutorial_img = pygame.image.load("Assets/Buttons/tutorial_btn.jpg")
save_img = pygame.image.load("Assets/Buttons/save_btn.png")
load_img = pygame.image.load("Assets/Buttons/load_btn.png")
easy_img = pygame.image.load("Assets/Buttons/easy_btn.jpg")
med_img = pygame.image.load("Assets/Buttons/medium_btn.jpg")
hard_img = pygame.image.load("Assets/Buttons/hard_btn.jpg")
continue_img = pygame.image.load("Assets/Buttons/button_continue.jpg")
menu_img = pygame.image.load("Assets/Buttons/button_menu.jpg")
quit_img = pygame.image.load("Assets/Buttons/button_quit.jpg")

# for loops appending animation images to empty list for animation
for img in range(1, 10):  
    attackLeft.append(pygame.image.load(f"Assets/Edmund/Attack/Attack L{img}.png"))
    attackRight.append(pygame.image.load(f"Assets/Edmund/Attack/Attack R{img}.png"))

    idleLeft.append(pygame.image.load(f"Assets/Edmund/Idle/Idle L{img}.png"))
    idleRight.append(pygame.image.load(f"Assets/Edmund/Idle/Idle R{img}.png"))

    enemy1AttackLeft.append(pygame.image.load(f"Assets/Enemy/Level1/Attack/attack L{img}.png"))
    enemy1AttackRight.append(pygame.image.load(f"Assets/Enemy/Level1/Attack/attack R{img}.png"))

    boss2AttackRight.append(pygame.image.load(f"Assets/Enemy/Boss2/Attack/Attack R ({img}).png"))
    boss2AttackLeft.append(pygame.image.load(f"Assets/Enemy/Boss2/Attack/Attack L ({img}).png"))

    kingAttackRight.append(pygame.image.load(f"Assets/Enemy/KING/Attack/Attack R ({img}).png"))
    kingAttackLeft.append(pygame.image.load(f"Assets/Enemy/KING/Attack/Attack L ({img}).png"))

for img in range(1, 11):
    walkLeft.append(pygame.image.load(f"Assets/Edmund/Walk/Walk L{img}.png"))
    walkRight.append(pygame.image.load(f"Assets/Edmund/Walk/Walk R{img}.png"))

    enemy2Right.append(pygame.image.load(f"Assets/Enemy/Level2/Walk/Walk R ({img}).png"))
    enemy2Left.append(pygame.image.load(f"Assets/Enemy/Level2/Walk/Walk L ({img}).png"))

    enemy2AttackRight.append(pygame.image.load(f"Assets/Enemy/Level2/Attack/Attack R ({img}).png"))
    enemy2AttackLeft.append(pygame.image.load(f"Assets/Enemy/Level2/Attack/Attack L ({img}).png"))

    enemy3Right.append(pygame.image.load(f"Assets/Enemy/Level3/Walk/Walk R ({img}).png"))
    enemy3Left.append(pygame.image.load(f"Assets/Enemy/Level3/Walk/Walk L ({img}).png"))

    enemy3AttackRight.append(pygame.image.load(f"Assets/Enemy/Level3/Attack/Attack R ({img}).png"))
    enemy3AttackLeft.append(pygame.image.load(f"Assets/Enemy/Level3/Attack/Attack L ({img}).png"))

for img in range(1, 7):
    jumpLeft.append(pygame.image.load(f"Assets/Edmund/Jump/Jump L{img}.png"))
    jumpRight.append(pygame.image.load(f"Assets/Edmund/Jump/Jump R{img}.png"))

    enemy1Right.append(pygame.image.load(f"Assets/Enemy/Level1/Walk/Enemy walk R{img}.png"))
    enemy1Left.append(pygame.image.load(f"Assets/Enemy/Level1/Walk/Enemy walk L{img}.png"))

    enemy1IdleLeft.append(pygame.image.load(f"Assets/Enemy/Level1/Idle/idle L{img}.png"))
    enemy1IdleRight.append(pygame.image.load(f"Assets/Enemy/Level1/Idle/idle R{img}.png"))

for img in range(1, 5):
    fallLeft.append(pygame.image.load(f"Assets/Edmund/Jump/Falling L ({img}).png"))
    fallRight.append(pygame.image.load(f"Assets/Edmund/Jump/Falling R{img}.png"))

for img in range(1, 15):  # For loop appending all tile images to same array
    grassTilesList.append(pygame.image.load(f"Assets/Tiles/Grass/tile{img}.png"))
    cobbleTilesList.append(pygame.image.load(f"Assets/Tiles/Cobble/tile{img}.png"))
    brickTilesList.append(pygame.image.load(f"Assets/Tiles/Brick/tile{img}.png"))

for img in range(1, 6):
    enemy2IdleLeft.append(pygame.image.load(f"Assets/Enemy/Level2/Idle/Idle L ({img}).png"))
    enemy2IdleRight.append(pygame.image.load(f"Assets/Enemy/Level2/Idle/Idle R ({img}).png"))

    enemy2DeathLeft.append(pygame.image.load(f"Assets/Enemy/Level2/Die/Death L ({img}).png"))
    enemy2DeathRight.append(pygame.image.load(f"Assets/Enemy/Level2/Die/Death R ({img}).png"))

    enemy3IdleLeft.append(pygame.image.load(f"Assets/Enemy/Level3/Idle/Idle L ({img}).png"))
    enemy3IdleRight.append(pygame.image.load(f"Assets/Enemy/Level3/Idle/Idle R ({img}).png"))

    enemy3DeathLeft.append(pygame.image.load(f"Assets/Enemy/Level3/Die/Death L ({img}).png"))
    enemy3DeathRight.append(pygame.image.load(f"Assets/Enemy/Level3/Die/Death R ({img}).png"))

    boss1Right.append(pygame.image.load(f"Assets/Enemy/Boss1/Walk/Walk R ({img}).png"))
    boss1Left.append(pygame.image.load(f"Assets/Enemy/Boss1/Walk/Walk L ({img}).png"))

    boss1DieRight.append(pygame.image.load(f"Assets/Enemy/Boss1/Die/Die R ({img}).png"))
    boss1DieLeft.append(pygame.image.load(f"Assets/Enemy/Boss1/Die/Die L ({img}).png"))

    boss2Right.append(pygame.image.load(f"Assets/Enemy/Boss2/Walk/Walk R ({img}).png"))
    boss2Left.append(pygame.image.load(f"Assets/Enemy/Boss2/Walk/Walk L ({img}).png"))

    boss2DieRight.append(pygame.image.load(f"Assets/Enemy/Boss2/Die/Die R ({img}).png"))
    boss2DieLeft.append(pygame.image.load(f"Assets/Enemy/Boss2/Die/Die L ({img}).png"))

    kingRight.append(pygame.image.load(f"Assets/Enemy/KING/Walk/Walk R ({img}).png"))
    kingLeft.append(pygame.image.load(f"Assets/Enemy/KING/Walk/Walk L ({img}).png"))

    kingDieRight.append(pygame.image.load(f"Assets/Enemy/KING/Die/Die R ({img}).png"))
    kingDieLeft.append(pygame.image.load(f"Assets/Enemy/KING/Die/Die L ({img}).png"))

for img in range(1, 9):
    boss1AttackRight.append(pygame.image.load(f"Assets/Enemy/Boss1/Attack/Attack R ({img}).png"))
    boss1AttackLeft.append(pygame.image.load(f"Assets/Enemy/Boss1/Attack/Attack L ({img}).png"))


click = False  # Global variable to see if user clicks 
finfished_game = False

# Setting number of rows and columns for tile mapping grid:
rows = 13
columns = 150
tileSize = sheight // rows  # Determine the size of each tile in the tile map

# Scroll variables:
scrollLeft = False  # Scrolling left
scrollRight = False  # Scrolling right  
scroll = 0  # The amount the screen has scrolled from the original position
bgScroll = 0
scrollSpeed = 9  # The speed of the scroll

# Counts for animation:
walkCount = 0
idleCount = 0
attackCount = 0
enemyWalkCount = 0
enemyIdleCount = 0
enemyDeathCount = 0

jumpCount = 9 # Determines how high the player will jump
facing = 'right'  # Which way the player is facing

# Booleans that represent what action the player is doing
left = False  # Moving left
right = False  # Moving right
attack = False  # Attacking
enemyAttacked = False  # If the player has attacked an enemy
jumping = False  # Jumping
dash = False  # Dashing

# Function to draw text on screen:
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	win.blit(img, (x, y))

# Defining the player sprite:
class Player(pygame.sprite.Sprite):  # Define the main player
    def __init__(self, path, x, y):  # Class initiation
        super().__init__()  
        self.image = path  # The image of the player
        self.x = x # x position
        self.y = y  # y position
        self.movey = 0  # how much the player has to move on the y axis
        self.vel = 9  # speed of player
        self.freeRun = True  # if the player is walking without scroll
        self.inAir = True  # if player is in the air
        self.power = 75
        self.rect = self.image.get_rect(center = (x,y))  # The dimensions and position of the player
        self.right = pygame.Rect(self.rect.x, self.rect.y, 10, self.rect.height)  # right hitbox
        self.left = pygame.Rect(self.rect.x+50, self.rect.y, 10, self.rect.height)  # left hitbox
        self.bottom = pygame.Rect(self.rect.x+10, self.rect.bottom+70, 70, 10)  # bottom hitbox
        self.max_health = 350  # max health
        self.current_health = 350  # the current health
        self.dashCooldown = False  # if user has used dash, cooldown the ability
        self.dashCountdown = 100  # how long the cooldown lasts

        self.weapon = pygame.Rect(self.rect.right-25, self.rect.y+35, 25, 25)  # weapon hitbox

    def update(self):
        # update every method of the player:
        self.collision()
        self.attack()
        self.move()
        self.gravity()
        self.dash()
        self.health()

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x + self.rect.width >= 1290:
            self.rect.x = 1290 - self.rect.width

    def move(self):  # Player movement
        global walkCount, idleCount, attackCount, jumpCount
        global left, right
        global attack, jumping, dash

        if left:  # If the player is moving left
            if self.freeRun:  # if the player can move without scroll
                self.rect.x -= self.vel
            if attack:  # If the player is attacking
                self.image = attackLeft[attackCount]  # Change the image of the player to create attack animation 
                attackCount += 1  # Increment the attack counter to change attack animation 
            else:  # If the player is not attacking
                self.image = walkLeft[walkCount//2]   # Change the image of the player to create walk animation 
                walkCount += 1  # Increment the attack counter to change walk animation 

        elif right:  # If player is moving right
            if self.freeRun:
                self.rect.x += self.vel
            if attack:
                self.image = attackRight[attackCount]
                attackCount += 1
            else:
                self.image = walkRight[walkCount//2]
                walkCount += 1

        else:  # If player is standing still
            if facing == 'left':  # If the player is facing left
                if attack:  # If the player is attacking
                    self.image = attackLeft[attackCount]
                    attackCount += 1
                else:  # If the player is standing still
                    self.image = idleLeft[idleCount//2]
            elif facing == 'right':  # If the player is facing right
                if attack:
                    self.image = attackRight[attackCount]
                    attackCount += 1
                else:
                    self.image = idleRight[idleCount//2]
            idleCount += 1  # Increment the idle count

        if jumping: # If player is jumping
            self.inAir = True  # player is in the air
            walkCount = 0
            if jumpCount >= 0:  # if the jump count is still positive
                self.rect.y -= (jumpCount**2) * 0.5  # move the player up relative to the jump count
                jumpCount -= 1  # decrement the jump count
            else:  # if the jump count becomes negative
                jumping = False  # the player is no longer jumping
                jumpCount = 9  # reset jump count
        
        if walkCount >= 20:
            walkCount = 0  # If the walk count is greater than 20, reset it
        if idleCount >= 18:
            idleCount = 0  # If the idle count is greater than 18, reset it
        if attackCount >= 9:
            attack = False  # no longer attacking
            attackCount = 0   # If the attack count is greater than 9, reset it
    
    def collision(self):  # Player colliding with the tiles
        global left, right, scrollLeft, scrollRight

        if facing == 'left':  # if the player is facing left
            # Change the hitbox location and size relative to what way the player is facing:
            self.left = pygame.Rect(self.rect.x+70, self.rect.y, 10,self.rect.height-10)
            self.right = pygame.Rect(self.rect.right-10, self.rect.y, 10,self.rect.height-10)
            self.bottom = pygame.Rect(self.rect.x+85, self.rect.bottom-10, 40, 10)
        elif facing == 'right':  # if the player is facing right
            # Change the hitbox location and size relative to what way the player is facing:
            self.left = pygame.Rect(self.rect.x, self.rect.y, 10,self.rect.height-10)
            self.right = pygame.Rect(self.rect.x+75, self.rect.y, 10,self.rect.height-10)
            self.bottom = pygame.Rect(self.rect.x+25, self.rect.bottom-10, 40, 10) 
        
        for tile in world.obstacle_list:  # for tiles that player can interact with        
            if tile[1].colliderect(self.right):  # if player's right side hits tile
                # make sure the player can no longer move right:
                right = False
                scrollRight = False
            
            if tile[1].colliderect(self.left):  # if player's right side hits tile
                # make sure the player can no longer move left:
                left = False
                scrollLeft = False

    def attack(self):  # Player attacking
        global score
        if facing == 'right':  # if player is facing right
            # change the hitbox location and size relative to which way the player is facing
            self.weapon = pygame.Rect(self.rect.right-25, self.rect.y+35, 25, 25)
        elif facing == 'left':  # if player is facing right
            # change the hitbox location and size relative to which way the player is facing
            self.weapon = pygame.Rect(self.rect.left, self.rect.y+35, 25, 25)

        if attackCount == 1:
            swing.play()  # Play swing sound

        for enemy in enemies.sprites():  # for all enemies in the map
            if attack and attackCount == 4:  # if the player is in a certain point in his attack
                if self.weapon.colliderect(enemy.rect):  # if the weapon hitbox hits the enemy
                    hitMetal.play()  # play hit sound
                    enemy.current_health -= self.power  # lower the enemy's health by a certain amount
                    if enemy.current_health <= 0:
                        if difficulty == "easy":
                             score += 100
                        elif difficulty == "medium":
                            score += 200
                        elif difficulty == "hard":
                            score += 300
                        
        if level >= 5:
            if self.weapon.colliderect(bosses.sprite.body):
                if attack and attackCount == 4:
                    hitMetal.play()
                    if level == 5:
                        bosses.sprite.current_health -= self.power
                        if bosses.sprite.current_health <= 0:
                            if difficulty == "easy":
                                score += 150
                            elif difficulty == "medium":
                                score += 250
                            elif difficulty == "hard":
                                score += 350
                    elif level == 6:
                        bosses.sprite.current_health -= self.power
                        if bosses.sprite.current_health <= 0:
                            if difficulty == "easy":
                                score += 150
                            elif difficulty == "medium":
                                score += 250
                            elif difficulty == "hard":
                                score += 350
                    elif level == 7:
                        bosses.sprite.current_health -= self.power
                        if bosses.sprite.current_health <= 0:
                            if difficulty == "easy":
                                score += 150
                            elif difficulty == "medium":
                                score += 250
                            elif difficulty == "hard":
                                score += 350
        
    def gravity(self):  # Player being affected by gravity
        self.movey += 1  # always have the player's move y be incremented to simulate gravity
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.bottom):  # if bottom hitbox hits the tile
                if not jumping:  # if the player is not jumping:
                    self.rect.y = tile[1].top - self.rect.height + 10  # set the player's y position to be on top of the tile
                self.movey = 0  # do not move the player
                self.inAir = False  # Player is not in the air
        self.rect.y += self.movey  # add the amount moved to the player's y position
    
    def dash(self):  # Player dash
        global dash, scroll

        win.blit(dash_icon, (50, 60))  # blit the dash icon

        border = pygame.Rect(45,55, 65, 65)

        if self.dashCooldown:  # if player has used the dash
            self.dashCountdown -= 1  # decrement the count down
            pygame.draw.rect(win, (222,23,56), border, 5)  # redraw the border with red colour 
        else:
            pygame.draw.rect(win, (144,238,144), border, 5)  # redraw the border with green colour 

        if self.dashCountdown <= 0:  # if the cooldown is less than 0
            self.dashCooldown = False  # no longer in cooldown
            self.dashCountdown = 100  # reset count down

        if dash:  # if the player has dashed
            win.blit(dash_img, (0,0))  # show the dash effect
            if facing == 'left':  # if the player is facing left
                if 1 <= level <= 4:
                    if self.freeRun:  # if the player is in free run mode
                        self.rect.x -= 100  # move the player quickly to the left
                    else:  # if not free run
                        scroll -= 100  # scroll the screen quickly to the left
                else:
                    self.rect.x -= 300
            elif facing == 'right':  # if the player is facing right
                if 1 <= level <= 4:
                    if self.freeRun:
                        self.rect.x += 100  # to the right
                    else:
                        scroll += 100  # scroll to the right
                else:
                    self.rect.x += 300
            dash = False  # turn dash to false
    
    def health(self):  # Player health
        max_healthBar = pygame.Rect(20,20, self.max_health, 30)  # rectangle for the max health
        current_healthBar = pygame.Rect(20,20, self.current_health, 30)  # rectangle for current health
        
        pygame.draw.rect(win, (255,0,0), max_healthBar)  # draw the max health bar as red
        pygame.draw.rect(win, (0,255,0), current_healthBar)  # draw the current health bar as green

# Defining the enemy sprite:
class Enemy(pygame.sprite.Sprite):  # Define the enemies
    def __init__(self, path, x, y, vel):  # Class initiation
        super().__init__()
        self.image = path  # Image of the enemy
        self.x = x  # x position
        self.y = y  # y position
        self.movey = 0  # how much the enemy has to move on the y axis
        self.vel = -vel  # The speed of the enemy
        self.rect = self.image.get_rect(center = (x,y))  # The dimensions and position of the enemy
        self.bottom = pygame.Rect(self.x, self.rect.bottom, 50, 10)
        self.weapon = pygame.Rect(self.x, self.rect.y+20, 30, 30)
        self.facing = 'right'
        self.startingPoint = x  # The original x xposition of the enemy
        self.waypoint1 = self.x - 200  # The waypoint of where the enemy will patrol
        self.status = 'alive'  # If the enemy is alive or dead
        self.enemyMoved = 0  # how much the enemy has moved from the original x position
        self.attackCount = 0  # enemy's attackc count
        self.max_health = 150  # max health
        self.current_health = 150  # current health
        self.dying = False
        self.deathCountdown = 100

    def update(self):
        global score
        self.move()
        self.gravity()

        max_healthbar = pygame.Rect(self.rect.x-20,self.rect.top-30, self.max_health, 15)
        current_healthbar = pygame.Rect(self.rect.x-20,self.rect.top-30, self.current_health, 15)

        pygame.draw.rect(win, (255,0,0), max_healthbar)  # enemy healthbar rectangles
        pygame.draw.rect(win, (0,255,0), current_healthbar)  # display of current enemy health

        if self.current_health <= 0:  # checking if an enemy is dead and changing status accordingly           
            self.dying = True
            self.status = 'dead'

    def move(self):
        global facing, enemyWalkCount, enemyIdleCount, enemyDeathCount
        global enemyAttacked
        global score

        if self.rect.y >= 690:
            self.kill()

        if self.vel < 0:
            self.facing = 'right'  # extending hitbox to match enemies weapon, depending on orientation
            self.weapon = pygame.Rect(self.rect.x+50, self.rect.y+50, 60, 50)
        if self.vel > 0:
            self.facing = 'left'
            self.weapon = pygame.Rect(self.rect.x, self.rect.y+50, 60, 50)

        if self.status == 'dead':  # If the enemy is dead
            if level == 1:
                self.image = enemyDead
            elif level == 2:
                if enemyDeathCount >= 10:
                    self.dying = False
                    if self.facing == 'right':
                        self.image = enemy2DeathRight[4]
                    if self.facing == 'left':
                        self.image = enemy2DeathLeft[4]

                if self.dying:
                    if self.facing == 'right':
                        self.image = enemy2DeathRight[enemyDeathCount//2]
                    if self.facing == 'left':
                        self.image = enemy2DeathLeft[enemyDeathCount//2]
                    enemyDeathCount += 1
            
            elif level == 3:
                if enemyDeathCount >= 10:
                    self.dying = False
                    if self.facing == 'right':
                        self.image = enemy3DeathRight[4]
                    if self.facing == 'left':
                        self.image = enemy3DeathLeft[4]

                if self.dying:
                    if self.facing == 'right':
                        self.image = enemy3DeathRight[enemyDeathCount//2]
                    if self.facing == 'left':
                        self.image = enemy3DeathLeft[enemyDeathCount//2]
                    enemyDeathCount += 1

            self.rect.centerx = self.startingPoint - scroll - self.enemyMoved
            self.rect.width =  self.image.get_width()
            self.rect.height =  self.image.get_height() - 30

            self.deathCountdown -= 1
            if self.deathCountdown <= 0:
                self.kill()
        
        if self.status == 'alive':  # If the enemy is alive
                self.enemyMoved += self.vel  # Change how much the enemy moved from the original position
                self.rect.centerx = self.startingPoint - scroll - self.enemyMoved  # Move the enemy

                if self.facing == 'right':
                    self.bottom = pygame.Rect(self.rect.x+15, self.rect.bottom-10, 40, 10)
                elif self.facing == 'left':
                    self.bottom = pygame.Rect(self.rect.x+65, self.rect.bottom-10, 40, 10)

                for tile in world.obstacle_list:
                    if self.rect.right >= tile[1].left and self.rect.right - 20 <= tile[1].left:
                        if tile[1].bottom-10 <= self.rect.bottom:
                            self.rect.bottom = tile[1].top
                    if self.rect.left <= tile[1].right and self.rect.left + 20 >= tile[1].right:
                        if tile[1].bottom-10 <= self.rect.bottom:
                            self.rect.bottom = tile[1].top

                if level == 1:
                    if self.facing == 'left':
                        self.image = enemy1Left[enemyWalkCount//10]

                    elif self.facing == 'right':
                        self.image = enemy1Right[enemyWalkCount//10]

                    enemyWalkCount += 1
                    if enemyWalkCount >= 60:
                        enemyWalkCount = 0
                    

                elif level == 2:
                    if self.facing == 'left':
                        self.image = enemy2Left[enemyWalkCount//10]

                    elif self.facing == 'right':
                        self.image = enemy2Right[enemyWalkCount//10]
                    
                    enemyWalkCount += 1
                    if enemyWalkCount >= 100:
                        enemyWalkCount = 0
                
                elif level == 3:
                    if self.facing == 'left':
                        self.image = enemy3Left[enemyWalkCount//5]

                    elif self.facing == 'right':
                        self.image = enemy3Right[enemyWalkCount//5]

                    enemyWalkCount += 1
                    if enemyWalkCount >= 50:
                        enemyWalkCount = 0
                    

                if self.rect.y - 10 <= edmund.sprite.rect.y and self.rect.bottom + 10 >= edmund.sprite.rect.bottom:
                    if self.rect.x >= edmund.sprite.rect.x and self.rect.x - 400 <= edmund.sprite.rect.x:
                        if self.facing == 'right':
                            self.vel *= -1

                        if self.weapon.colliderect(edmund.sprite.right):
                                self.weapon = pygame.Rect(self.rect.x, self.rect.y+50, 60, 50)
                                self.vel = 0
                                if level == 1:
                                    self.image = enemy1AttackLeft[self.attackCount//2]
                                    if self.attackCount == 17:
                                        edmund.sprite.current_health -= 10
                                        if difficulty == "easy":
                                            score -= 10
                                        elif difficulty == "medium":
                                            score -= 20
                                        elif difficulty == "hard":
                                            score -= 30
                                    self.attackCount += 1
                                    if self.attackCount >= 18:
                                        self.attackCount = 0

                                if level == 2:
                                    self.image = enemy2AttackLeft[self.attackCount//2]
                                    if self.attackCount == 19:
                                        edmund.sprite.current_health -= 12
                                        if difficulty == "easy":
                                            score -= 10
                                        elif difficulty == "medium":
                                            score -= 20
                                        elif difficulty == "hard":
                                            score -= 30
                                    self.attackCount += 1
                                    if self.attackCount >= 20:
                                        self.attackCount = 0
                                
                                if level == 3:
                                    self.image = enemy3AttackLeft[self.attackCount//2]
                                    if self.attackCount//2 == 19:
                                        edmund.sprite.current_health -= 14
                                        if difficulty == "easy":
                                            score -= 10
                                        elif difficulty == "medium":
                                            score -= 20
                                        elif difficulty == "hard":
                                            score -= 30
                                    self.attackCount += 1
                                    if self.attackCount >= 20:
                                        self.attackCount = 0
                                
                        else:
                            self.vel = 4

                    elif self.rect.x <= edmund.sprite.rect.x and self.rect.x + 400 >= edmund.sprite.rect.x:
                        if self.facing == 'left':
                            self.vel *= -1
                        
                        if self.weapon.colliderect(edmund.sprite.left):
                                self.weapon = pygame.Rect(self.rect.x+50, self.rect.y+50, 60, 50)
                                self.vel = 0
                                if level == 1:
                                    self.image = enemy1AttackRight[self.attackCount//2]
                                    if self.attackCount//2 == 7:
                                        edmund.sprite.current_health -= 10
                                    self.attackCount += 1
                                    if self.attackCount >= 18:
                                        self.attackCount = 0

                                if level == 2:
                                    self.image = enemy2AttackRight[self.attackCount//2]
                                    if self.attackCount//2 == 7:
                                        edmund.sprite.current_health -= 12
                                    self.attackCount += 1
                                    if self.attackCount >= 20:
                                        self.attackCount = 0
                                
                                if level == 3:
                                    self.image = enemy3AttackRight[self.attackCount//2]
                                    if self.attackCount//2 == 7:
                                        edmund.sprite.current_health -= 14
                                    self.attackCount += 1
                                    if self.attackCount >= 20:
                                        self.attackCount = 0                          

                        else:
                            self.vel = -4
                
                else:
                    if self.rect.centerx < self.waypoint1 - scroll:  # If enemy is left of the waypoint
                        self.vel = -4
                    elif self.rect.centerx > self.startingPoint - scroll:  # If enemy is right of the original point
                        self.vel = 4
                

    def gravity(self):
        self.movey += 1
        for tile in world.obstacle_list:
            if self.status == 'alive':
                if tile[1].colliderect(self.bottom):
                    self.rect.y = tile[1].top - self.rect.height + 10
                    self.movey = 0
            else:
                if tile[1].colliderect(self.rect):
                    self.rect.y = tile[1].top - self.rect.height + 10
                    self.movey = 0
        
        self.rect.y += self.movey

class Boss(pygame.sprite.Sprite):
    def __init__(self, path, x, y, health):
        super().__init__()
        self.image = path
        self.x = x
        self.y = y
        self.movey = 0
        self.rect = self.image.get_rect(center = (x, y))
        self.body = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)
        self.vel = 4
        self.walkCount = 0
        self.attackCount = 0
        self.max_health = health
        self.current_health = health
        self.status = 'alive'
        self.facing = 'left'
        self.dying = False
        self.deathCount = 0
        self.deathCountdown = 100

    def update(self):
        self.move()
        self.gravity()
        self.health()

        if self.current_health <= 0:
            self.dying = True
            self.status = 'dead'

    def move(self):
        global level, score, finfished_game
        if self.status == 'dead':  # If the enemy is dead
            if self.deathCount >= 10:
                self.dying = False
                if level == 5:
                    if self.facing == 'right':
                        self.image = boss1DieRight[4]
                    if self.facing == 'left':
                        self.image = boss1DieLeft[4]
                elif level == 6:
                    if self.facing == 'right':
                        self.image = boss2DieRight[4]
                    if self.facing == 'left':
                        self.image = boss2DieLeft[4]
                elif level == 7:
                    if self.facing == 'right':
                        self.image = kingDieRight[4]
                    if self.facing == 'left':
                        self.image = kingDieLeft[4]

            if self.dying:
                if level == 5:
                    if self.facing == 'right':
                        self.image = boss1DieRight[self.deathCount//2]
                    if self.facing == 'left':
                        self.image = boss1DieLeft[self.deathCount//2]
                elif level == 6:
                    if self.facing == 'right':
                        self.image = boss2DieRight[self.deathCount//2]
                    if self.facing == 'left':
                        self.image = boss2DieLeft[self.deathCount//2]
                elif level == 7:
                    if self.facing == 'right':
                        self.image = kingDieRight[self.deathCount//2]
                    if self.facing == 'left':
                        self.image = kingDieLeft[self.deathCount//2]
                self.deathCount += 1

            self.rect.width =  self.image.get_width()
            self.rect.height =  self.image.get_height() - 30

            self.deathCountdown -= 1
            if self.deathCountdown <= 0:
                self.kill()
                if level == 5:
                    stage2()
                if level == 6:
                    stage3()
                if level == 7:
                    finfished_game = True
                    end_game()

        if self.status == 'alive':
            self.rect.x += self.vel
            if edmund.sprite.rect.centerx <= self.rect.centerx:
                self.facing = 'left'
                self.body = pygame.Rect(self.rect.x+175, self.rect.y, 300, self.rect.height)
                if self.body.colliderect(edmund.sprite.rect):
                    self.vel = 0
                    if level == 5:
                        self.image = boss1AttackLeft[self.attackCount//2]
                        if self.attackCount == 15:
                            edmund.sprite.current_health -= 5
                            if difficulty == "easy":
                                score -= 10
                            elif difficulty == "medium":
                                score -= 20
                            elif difficulty == "hard":
                                score -= 30
                        self.attackCount += 1
                        if self.attackCount >= 16:
                            self.attackCount = 0
                        
                    elif level == 6:
                        self.image = boss2AttackLeft[self.attackCount//2]
                        if self.attackCount == 17:
                            edmund.sprite.current_health -= 10
                            if difficulty == "easy":
                                score -= 10
                            elif difficulty == "medium":
                                score -= 20
                            elif difficulty == "hard":
                                score -= 30
                        self.attackCount += 1
                        if self.attackCount >= 18:
                            self.attackCount = 0
                        
                    elif level == 7:
                        self.image = kingAttackLeft[self.attackCount//2]
                        if self.attackCount == 17:
                            edmund.sprite.current_health -= 10
                            if difficulty == "easy":
                                score -= 10
                            elif difficulty == "medium":
                                score -= 20
                            elif difficulty == "hard":
                                score -= 30
                        self.attackCount += 1
                        if self.attackCount >= 18:
                            self.attackCount = 0
                else:
                    self.vel = -4
                    if level == 5:
                        self.image = boss1Left[self.walkCount//2]
                    elif level == 6:
                        self.image = boss2Left[self.walkCount//2]
                    elif level == 7:
                        self.image = kingLeft[self.walkCount//2]

                    self.walkCount += 1
                    if self.walkCount >= 10:
                        self.walkCount = 0

            elif edmund.sprite.rect.centerx > self.rect.centerx:
                self.facing = 'right'
                self.body = pygame.Rect(self.rect.x+30, self.rect.y, 300, self.rect.height)
                if self.body.colliderect(edmund.sprite.rect):
                    self.vel = 0       
                    if level == 5: 
                        self.image = boss1AttackRight[self.attackCount//2]
                        if self.attackCount == 16:
                            edmund.sprite.current_health -= 5
                            if difficulty == "easy":
                                score -= 10
                            elif difficulty == "medium":
                                score -= 20
                            elif difficulty == "hard":
                                score -= 30
                        self.attackCount += 1
                        if self.attackCount >= 16:
                            self.attackCount = 0
                        
                    elif level == 6:
                        self.image = boss2AttackRight[self.attackCount//2]
                        if self.attackCount == 18:
                            edmund.sprite.current_health -= 10
                            if difficulty == "easy":
                                score -= 10
                            elif difficulty == "medium":
                                score -= 20
                            elif difficulty == "hard":
                                score -= 30
                        self.attackCount += 1
                        if self.attackCount >= 18:
                            self.attackCount = 0

                    elif level == 7:
                        self.image = kingAttackRight[self.attackCount//2]
                        if self.attackCount == 8:
                            edmund.sprite.current_health -= 10
                            if difficulty == "easy":
                                score -= 10
                            elif difficulty == "medium":
                                score -= 20
                            elif difficulty == "hard":
                                score -= 30
                        self.attackCount += 1
                        if self.attackCount >= 18:
                            self.attackCount = 0
                        
                else:
                    self.vel = 4
                    if level == 5:
                        self.image = boss1Right[self.walkCount//2]
                    elif level == 6:
                        self.image = boss2Right[self.walkCount//2]
                    elif level == 7:
                        self.image = kingRight[self.walkCount//2]

                    self.walkCount += 1
                    if self.walkCount >= 10:
                        self.walkCount = 0

    def health(self):
        max_healthBar = pygame.Rect(500,20, self.max_health, 15)  # rectangle for the max health
        current_healthBar = pygame.Rect(500,20, self.current_health, 15)  # rectangle for current health
        
        pygame.draw.rect(win, (0,0,0), max_healthBar)  # draw the max health bar as red
        pygame.draw.rect(win, (255,0,0), current_healthBar)  # draw the current health bar as green

    def gravity(self):
        self.movey += 1
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.rect.y = tile[1].top - self.rect.height + 10
                self.movey = 0
        
        self.rect.y += self.movey
    
# Defining the world that players interact with
class World():
    def __init__(self):
        self.obstacle_list = []
    
    def proccess(self, data):
        self.obstacle_list.clear()
        for y, row in enumerate(data):
            for x, tileVal in enumerate(row):
                if tileVal >= 0:
                    if level == 1 or level == 5:
                        img = grassTilesList[tileVal]
                        
                    elif level == 2 or level == 6:
                        img = cobbleTilesList[tileVal]
                    
                    elif level == 3 or level == 7:
                        img = brickTilesList[tileVal]

                    img_rect = img.get_rect()
                    img_rect.x = x * tileSize - scroll
                    img_rect.y = y * tileSize
                    tile_data = (img, img_rect)

                    if 0 <= tileVal <= 3 or 5 <= tileVal <= 8 or 9 <= tileVal <= 10 or tileVal == 13:
                            self.obstacle_list.append(tile_data)


bosses = pygame.sprite.GroupSingle()
enemies = pygame.sprite.Group()  # Creating the enemy sprite group

# Creating the player sprite:
Edmond_Prox = Player(idleRight[0], 300, 400)  # Definition
edmund = pygame.sprite.GroupSingle()
edmund.add(Edmond_Prox)  # Adding the player to the sprite group

# Function that will contain all assets of the levels
def mainAssets():
    global walkCount, idleCount, attackCount
    global scroll, bgScroll
    global attack, enemyAttacked
    global level
    global score

    if level == 1:
        for i in range(4):  # creating a looping background
            win.blit(level1_img, ((i*level1_img.get_width()) - scroll,0))
        win.blit(finish_flag, (4500-scroll, 400))
    if level == 2:
        win.blit(level2_img, (-bgScroll,0))
        win.blit(finish_flag, (5300-scroll, 500))
    if level == 3:
        for i in range(4):  # creating a looping background
            win.blit(level3_img, ((i*level3_img.get_width()) - scroll,0))
        win.blit(finish_flag, (4600-scroll, 500))
    
    if level == 5:
        for i in range(4):  # creating a looping background
            win.blit(level1_img, ((i*level1_img.get_width()) - scroll,0))
    if level == 6:
        win.blit(level2_img, (-bgScroll,0))
    if level == 7:
        win.blit(throne_room, (0,0))
        

    drawLevel()  # Draw the tilemap
    bosses.draw(win)
    bosses.update()
    edmund.draw(win)  # Draw the player
    edmund.update()  # Update the player
    enemies.draw(win)  # Draw the enemies
    enemies.update()  # Update the enemies

    if 1 <= level <= 3 or 5 <= level <= 7:
        draw_text(f'Score: {score}', font, (255,255,255), 1100, 10)  # drawing current score in the top right corner 

    if level == 1:
        draw_text(f'Stage 1: {difficulty}', font, (255,255,255), 900, 10)  # drawing the current level and difficulty next to score
    if level == 2:
        draw_text(f'Stage 2: {difficulty}', font, (255,255,255), 900, 10)
    if level == 3:
        draw_text(f'Stage 3: {difficulty}', font, (255,255,255), 900, 10)
    if level == 5:
        draw_text(f'Boss 1: {difficulty}', font, (255,255,255), 900, 10)
    if level == 6:
        draw_text(f'Boss 2: {difficulty}', font, (255,255,255), 900, 10)
    if level == 7:
        draw_text(f'King Battle: {difficulty}', font, (255,255,255), 900, 10)

    pygame.display.update()

# Function to draw the grid for tilemapping:
def grid():
    global sheight #screen width and height
    global swidth

    global rows  # number of tile rows
    global columns  # number of tile columns
    global tileSize  # size of individual tile

    for c in range(columns+1):  # Draw the columns
        pygame.draw.line(win, (255,255,255), (c*tileSize-scroll, 0), (c*tileSize-scroll, sheight))
    
    for r in range(rows+1):  # Draw the rows
        pygame.draw.line(win, (255,255,255), (0, r*tileSize), (swidth+500, r*tileSize))

# Function that controlls how the map scrolls:
def map_scroll():
    global scrollLeft
    global scrollRight
    global scroll
    global scrollSpeed, bgScroll

    if scroll < 0:  # Reset the scroll if it is negative
        scroll = 0

    # When the scroll is going left:
    if scrollLeft and scroll > 0:
        scroll -= scrollSpeed
        if level == 2 or level == 6:
            bgScroll -= 0.25
        else:
            bgScroll -= scrollSpeed

    # When the scroll is going right:
    if scrollRight:
        scroll += scrollSpeed
        if level >= 2 or level == 6:
            bgScroll += 0.25
        else:
            bgScroll += scrollSpeed


save_button = button.Button(1100, 500, save_img, 1)  # Using self made button class to place a button image at a specified location
load_button = button.Button(1100, 600, load_img, 1)
currentTile = -1  # The current tile being placed in the tile map
tileX = 0  # The x position the cursor is at on the tile map
tileY = 0  # The y position the cursor is at on the tile map
worldData = []  # List to store all the information of each tile
for row in range(rows):
    r = [-1] * columns
    worldData.append(r)

def drawLevel():
    global level
    global scroll

    for y, row in enumerate(worldData):
        for x, tileVal in enumerate(row):
            if tileVal >= 0:
                if level == 1 or level == 5:
                    win.blit(grassTilesList[tileVal], ((x*tileSize)-scroll, y*tileSize))
                elif level == 2 or level == 6:
                    win.blit(cobbleTilesList[tileVal], ((x*tileSize)-scroll, y*tileSize))
                elif level == 3 or level == 7:
                    win.blit(brickTilesList[tileVal], ((x*tileSize)-scroll, y*tileSize))

play_button = button.Button(290,200, play_img, 1)  # creating clickable buttons with self made button class
tutorial_button = button.Button(330,375, tutorial_img, 1)  # all buttons for all menus
easy_button = button.Button(300,200, easy_img, 1)
med_button = button.Button(300,300, med_img, 1)
hard_button = button.Button(300,400, hard_img, 1)
continue_button = button.Button(300,200, continue_img, 1)
menu_button = button.Button(300,300, menu_img, 1)
quit_button = button.Button(300,400, quit_img, 1)

def paused():  # function for when player presses escape to pause
    global click  # click variable to determine when mouse is being clicked
    pygame.display.set_caption("Paused")
    pause = True  # while pause is true, the pause menu will stay up

    while pause:  # while pause is true
        click = False  
        win.blit(menubg, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # checking to see if mouse is being clicked and changing click variable accordingly
                if event.button == 1:
                    click = True
        
        mx, my = pygame.mouse.get_pos()  # getting mouse position

        continue_button.draw(win)  # drawing three pause menu buttons on the screen
        menu_button.draw(win)
        quit_button.draw(win)
        
        if continue_button.rect.collidepoint((mx,my)):  # if cursor is over continue button
            if click:  # and mouse is being clicked
                buttonClicked.play()  # play button clicking sound
                pause = False  # cancel pause function, unpause and resume game
        
        if menu_button.rect.collidepoint((mx,my)):  # if cursor is over menu button
            if click:  # and mouse is being clicked
                buttonClicked.play()  # play button clicking sound
                menu()  # call menu function and go to menu
        
        if quit_button.rect.collidepoint((mx,my)):  # if cursor is over quit button
            if click:  # and mouse is being clicked
                buttonClicked.play()  # play button clicking sound
                pygame.quit()
                sys.exit()  # exit game
        
        pygame.display.update()


def menu():  # main menu function
    global click, score
    score = 0
    pygame.mixer.music.load("Assets/Songs/menuSong.mp3")  # loading up and playing menu music
    pygame.mixer.music.set_volume(0.1)  # volume
    pygame.mixer.music.play(-1)
    pygame.display.set_caption("Menu")  # menu screcaption
    splashCounter = 1000  #determining duration of splash screen
    while True:
        click = False  # click variable to check if mouse is being clicked

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # checking for mouse click and changing click variable accordingly
                if event.button == 1:
                    click = True

        if splashCounter <= 0:  # when splash counter equals zero, menu comes on
            win.blit(menubg, (0,0))
        
            mx, my = pygame.mouse.get_pos()  # getting mouse position

            play_button.draw(win)  # drawing main menu buttons
            tutorial_button.draw(win)
            
            if play_button.rect.collidepoint((mx,my)):  # if cursor is over play button
                if click:  # and mouse is being clicked 
                    buttonClicked.play()  # play button sound
                    diff_selec()  # move to difficulty select menu
            
            if tutorial_button.rect.collidepoint((mx,my)):  # if cursor is over tutorial button
                if click:  # and mouse is being clicked
                    buttonClicked.play()  # play button sound
                    tutorial()  # move to tutorial gameplay
            
        else:
            win.blit(splash, (0,0))
            splashCounter -= 1

        pygame.display.update()  

def diff_selec():  # Difficulty selection function
    global level
    global click
    global difficulty
    pygame.display.set_caption("Select Difficulty")  # window caption
    click = False
    while True:
        click = False
        win.blit(menubg, (0,0))  # Menu background pasted on to screen

        for event in pygame.event.get():  # Checking for user quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()  # Getting the x and y position of the mouse on the screen and storing them into variables
        
        easy_button.draw(win)  # Drawing easy, medium, and hard buttons onto screen
        med_button.draw(win)
        hard_button.draw(win)

        if easy_button.rect.collidepoint((mx,my)):  # Checking if the stored mouse position is over the easy button
            if click:  # if so, and click is equal to true, meaning the mouse button is clicked down, than stage one is called easy difficulty
                buttonClicked.play()
                difficulty = 'easy'
                stage1()
        
        if med_button.rect.collidepoint((mx,my)):
            if click:  # Stage one called on medium difficulty
                buttonClicked.play()
                difficulty = 'normal'
                stage1()

        if hard_button.rect.collidepoint((mx,my)):
            if click:  # stage one called on hard difficulty
                buttonClicked.play()
                difficulty = 'hard'
                stage1()
        
        pygame.display.update()  # update display at end of loop
        
   
world = World()
def createLevels():  # tilemapping function, used to create and customize terrain of each level
    global scrollLeft, scrollRight, scroll  # Scrolling variables
    global level 
    global click
    global currentTile      

    while True:
        click = False
        pygame.time.delay(40)
        if level == 1 or level == 4 or level == 5:  # Checking which level is to be customized
            for i in range(4):
                win.blit(level1_img, ((i*level1_img.get_width()) - scroll,0))
        if level == 2 or level == 6:
            for i in range(4):
                win.blit(level2_img, ((i*level2_img.get_width()) - bgScroll,0))
        if level == 3 or level == 7:
            for i in range(4):
                win.blit(level3_img, ((i*level3_img.get_width()) - scroll,0))
        grid()
        drawLevel()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    scrollLeft = True
                    scrollRight = False
                
                elif event.key == pygame.K_RIGHT:
                    scrollLeft = False
                    scrollRight = True

                if event.key == pygame.K_UP: 
                    level += 1
                
                if level > 0:
                    if event.key == pygame.K_DOWN:
                        level -= 1

            if event.type == pygame.KEYUP: 
                scrollLeft = False
                scrollRight = False   
        
        pygame.draw.rect(win, (144, 238, 144), (1000,0, 300,700))
        if level == 1 or level == 4 or level == 5:
            for tiles in range(3):
                win.blit(grassTilesList[tiles], (1025+(tiles*90), 50))
            for tiles in range(3):
                win.blit(grassTilesList[3+tiles], (1025+(tiles*90), 110))
            for tiles in range(3):
                win.blit(grassTilesList[6+tiles], (1025+(tiles*90), 170))
            for tiles in range(3):
                win.blit(grassTilesList[9+tiles], (1025+(tiles*90), 230))
            for tiles in range(2):
                win.blit(grassTilesList[12+tiles], (1025+(tiles*90), 290))
        elif level == 2 or level == 6:
            for tiles in range(3):
                win.blit(cobbleTilesList[tiles], (1025+(tiles*90), 50))
            for tiles in range(3):
                win.blit(cobbleTilesList[3+tiles], (1025+(tiles*90), 110))
            for tiles in range(3):
                win.blit(cobbleTilesList[6+tiles], (1025+(tiles*90), 170))
            for tiles in range(3):
                win.blit(cobbleTilesList[9+tiles], (1025+(tiles*90), 230))
            for tiles in range(2):
                win.blit(cobbleTilesList[12+tiles], (1025+(tiles*90), 290))
        elif level == 3 or level == 7:
            for tiles in range(3):
                win.blit(brickTilesList[tiles], (1025+(tiles*90), 50))
            for tiles in range(3):
                win.blit(brickTilesList[3+tiles], (1025+(tiles*90), 110))
            for tiles in range(3):
                win.blit(brickTilesList[6+tiles], (1025+(tiles*90), 170))
            for tiles in range(3):
                win.blit(brickTilesList[9+tiles], (1025+(tiles*90), 230))
            for tiles in range(2):
                win.blit(brickTilesList[12+tiles], (1025+(tiles*90), 290))
        
        mx,my = pygame.mouse.get_pos()

        tileX = (mx + scroll) // tileSize
        tileY = my // tileSize

        tile1 = pygame.Rect(1025,50, 53,53)
        tile2 = pygame.Rect(1115,50, 53,53)
        tile3 = pygame.Rect(1205,50, 53,53)
        tile4 = pygame.Rect(1025,110, 53,53)
        tile5 = pygame.Rect(1115,110, 53,53)
        tile6 = pygame.Rect(1205,110, 53,53)
        tile7 = pygame.Rect(1025,170, 53,53)
        tile8 = pygame.Rect(1115,170, 53,53)
        tile9 = pygame.Rect(1205,170, 53,53)
        tile10 = pygame.Rect(1025,230, 53,53)
        tile11 = pygame.Rect(1115,230, 53,53)
        tile12 = pygame.Rect(1205,230, 53,53)
        tile13 = pygame.Rect(1025,290, 53,53)
        tile14 = pygame.Rect(1115,290, 53,53)

        if click:
            if tile1.collidepoint((mx,my)):
                currentTile = 0
            elif tile2.collidepoint((mx,my)):
                currentTile = 1
            elif tile3.collidepoint((mx,my)):
                currentTile = 2
            elif tile4.collidepoint((mx,my)):
                currentTile = 3
            elif tile5.collidepoint((mx,my)):
                currentTile = 4
            elif tile6.collidepoint((mx,my)):
                currentTile = 5
            elif tile7.collidepoint((mx,my)):
                currentTile = 6
            elif tile8.collidepoint((mx,my)):
                currentTile = 7
            elif tile9.collidepoint((mx,my)):
                currentTile = 8
            elif tile10.collidepoint((mx,my)):
                currentTile = 9
            elif tile11.collidepoint((mx,my)):
                currentTile = 10
            elif tile12.collidepoint((mx,my)):
                currentTile = 11
            elif tile13.collidepoint((mx,my)):
                currentTile = 12
            elif tile14.collidepoint((mx,my)):
                currentTile = 13

        if currentTile == 0:
            pygame.draw.rect(win, (255,0,0), tile1, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 0
        elif currentTile == 1:
            pygame.draw.rect(win, (255,0,0), tile2, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 1
        elif currentTile == 2:
            pygame.draw.rect(win, (255,0,0), tile3, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 2
        elif currentTile == 3:
            pygame.draw.rect(win, (255,0,0), tile4, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 3
        elif currentTile == 4:
            pygame.draw.rect(win, (255,0,0), tile5, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 4
        elif currentTile == 5:
            pygame.draw.rect(win, (255,0,0), tile6, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 5
        elif currentTile == 6:
            pygame.draw.rect(win, (255,0,0), tile7, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 6
        elif currentTile == 7:
            pygame.draw.rect(win, (255,0,0), tile8, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 7
        elif currentTile == 8:
            pygame.draw.rect(win, (255,0,0), tile9, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 8
        elif currentTile == 9:
            pygame.draw.rect(win, (255,0,0), tile10, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 9
        elif currentTile == 10:
            pygame.draw.rect(win, (255,0,0), tile11, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 10
        elif currentTile == 11:
            pygame.draw.rect(win, (255,0,0), tile12, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 11
        elif currentTile == 12:
            pygame.draw.rect(win, (255,0,0), tile13, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 12
        elif currentTile == 13:
            pygame.draw.rect(win, (255,0,0), tile14, 3)
            if mx < 1000:
                if pygame.mouse.get_pressed()[0] == 1:
                    worldData[tileY][tileX] = 13

        if pygame.mouse.get_pressed()[2] == 1:
            worldData[tileY][tileX] = -1

        draw_text(f'Level: {level}', font, (255,255,255), 1030, 10)

        save_button.draw(win)
        load_button.draw(win)
        if click:
            if save_button.rect.collidepoint((mx,my)):
                with open(f'level{level}_data.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter = ',')
                    for row in worldData:
                        writer.writerow(row)   

            if load_button.rect.collidepoint((mx,my)):
                with open(f'level{level}_data.csv', newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter = ',')
                    for x, row in enumerate(reader):
                        for y, tileVal in enumerate(row):
                            worldData[x][y] = int(tileVal)          
        
        map_scroll()
        pygame.display.update()

def tutorial():
    global click
    global facing

    global scroll, scrollLeft, scrollRight, scrollSpeed

    global left, right
    global attack, enemyAttacked
    global walkCount

    global jumping, dash
    scroll = 0
    enemies.empty()
    edmund.sprite.rect.x = 300
    edmund.sprite.rect.y = 400

    enemy = Enemy(enemy1Left[0], 1773, 150, 4)
    enemies.add(enemy)

    while True:
        pygame.time.delay(40)
        
        with open('level4_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tileVal in enumerate(row):
                    worldData[x][y] = int(tileVal)
        world.proccess(worldData)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    attack = True
                    left = False
                    right = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            paused()

        if keys[pygame.K_a] and edmund.sprite.rect.x > 25:
            left = True
            right = False
            if facing == 'right':
                edmund.sprite.rect.x -= 60
                edmund.sprite.image = walkLeft[0]
            facing = 'left'
            if scroll == 0 or edmund.sprite.rect.x+scroll >=4000:
                scrollLeft = False
                edmund.sprite.freeRun = True
            else:
                edmund.sprite.freeRun = False
                scrollLeft = True
                scrollRight = False

        elif keys[pygame.K_d] and edmund.sprite.rect.x < 1230:
            left = False
            right = True
            if facing == 'left':
                edmund.sprite.rect.x += 60
                edmund.sprite.image = walkRight[0]
            facing = 'right'
            if edmund.sprite.rect.x <= 600 or edmund.sprite.rect.x+scroll >= 4445:
                scrollRight = False
                edmund.sprite.freeRun = True
            else:
                edmund.sprite.freeRun = False
                scrollLeft = False
                scrollRight = True       
        else:
            left = False
            right = False
            scrollLeft = False
            scrollRight = False
            walkCount = 0
        
        if keys[pygame.K_LSHIFT] and not edmund.sprite.dashCooldown:
            dash = True
            edmund.sprite.dashCooldown = True

        if not jumping and not edmund.sprite.inAir:
            if keys[pygame.K_SPACE]:
                scrollSpeed = 8.5
                jumping = True

        mainAssets()
        map_scroll()

        win.blit(tutorial1, (20-scroll, 200))
        win.blit(tutorial2, (500-scroll, 200))
        win.blit(tutorial3, (1350-scroll, 200))
        win.blit(tutorial4, (1000-scroll, 275))
        win.blit(tutorial5, (1700-scroll, 275))

        if edmund.sprite.rect.y >= 750:
            scroll = 0
            edmund.sprite.rect.x = 300
            edmund.sprite.rect.y = 400
        
        if len(enemies) == 0:
            menu()
    
        pygame.display.update()

menu_button2 = button.Button(550,350, menu_img, 1)
quit_button2 = button.Button(550,450, quit_img, 1)
def end_game():
    global score
    global level
    global score_array, max_score
    global click
    
    while True:
        pygame.time.delay(40)
        click = False
        win.blit(menubg, (0,0))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused()

        score_array.append(score)
        max_score = max(score_array)
        if finfished_game:
            draw_text(f'Congratulations! You beat the game with a score of: {score}', pygame.font.SysFont('Futura', 80), (255,255,255), 400, 200)
        else:
            draw_text(f'You died :( Your score was {score}', pygame.font.SysFont('Futura', 80), (255,255,255), 300, 200)

        mx, my = pygame.mouse.get_pos()

        menu_button2.draw(win)
        quit_button2.draw(win)

        if menu_button2.rect.collidepoint((mx,my)):
            if click:
                buttonClicked.play()
                menu()
        
        if quit_button2.rect.collidepoint((mx,my)):
            if click:
                buttonClicked.play()
                pygame.quit()
                sys.exit()

        pygame.display.update()


def stage1():
    # Make global variables local
    global level
    global click
    global facing

    global scroll
    global scrollLeft
    global scrollRight
    global scrollSpeed

    global left
    global right
    global attack, enemyAttacked
    global walkCount

    global jumping, dash

    # reset variables, lists, and player positioning
    scroll = 0
    enemies.empty()
    edmund.sprite.rect.x = 300
    edmund.sprite.rect.y = 400

    # Play music
    pygame.mixer.music.load("Assets/Songs/stage1.mp3") 
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    if difficulty == 'easy':
        edmund.sprite.power = 75
        for i in range(1000, 4800, 600):
            enemy = Enemy(enemy1Left[0], i, 150, 4)
            enemies.add(enemy)
    if difficulty == 'normal':  # change the number of enemies as well as there speed
        edmund.sprite.power = 50
        for i in range(1000, 4800, 500):
            enemy = Enemy(enemy1Left[0], i, 150, 5)
            enemies.add(enemy)
    if difficulty == 'hard':    # change the number of enemies as well as there speed
        edmund.sprite.power = 37.5
        for i in range(1000, 4800, 400):
            enemy = Enemy(enemy1Left[0], i, 150, 6)
            enemies.add(enemy)

    while True:
        level = 1  # Level 1
        pygame.time.delay(40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # If user has clicked mouse button
                if event.button == 1:
                    click = True
                    attack = True
                    left = False
                    right = False
                    
        click = False

        with open('level1_data.csv', newline='') as csvfile:  # Loading tilemap data
            reader = csv.reader(csvfile, delimiter = ',')  # Read the file
            for x, row in enumerate(reader):  # for the rows in the excel spreadsheet:
                for y, tileVal in enumerate(row):  # for the columns in the excel spreadsheet:
                    worldData[x][y] = int(tileVal)  # Change the world data to the level data
        world.proccess(worldData)  # process the world data to find obstacles
            
        if edmund.sprite.rect.x+scroll >= 4500:  # If the player passes this point, he will go to next level
                boss1()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:  # Pause game when escape is pressed
            paused()
            
        if keys[pygame.K_a] and edmund.sprite.rect.x > 25:
            left = True  # Go left
            right = False
            if facing == 'right':
                edmund.sprite.rect.x -= 60  # move character to align itself
                edmund.sprite.image = walkLeft[0]
            facing = 'left'
            if scroll == 0:  # If scroll is not applied, free run is true
                scrollLeft = False
                edmund.sprite.freeRun = True
            else:  # else, scroll
                edmund.sprite.freeRun = False
                scrollLeft = True
                scrollRight = False

        elif keys[pygame.K_d] and edmund.sprite.rect.x < 1230:
            left = False
            right = True  # Go right
            if facing == 'left':
                edmund.sprite.rect.x += 60 # move character to align itself
                edmund.sprite.image = walkRight[0]
            facing = 'right'
            if edmund.sprite.rect.x <= 600 or edmund.sprite.rect.x+scroll >= 4445:  # If scroll is not applied, free run is true
                scrollRight = False
                edmund.sprite.freeRun = True
            else:  # else, scroll
                edmund.sprite.freeRun = False
                scrollLeft = False
                scrollRight = True       
        else:  # If no key pressed, no action is true
            left = False
            right = False
            scrollLeft = False
            scrollRight = False
            walkCount = 0
            
        if keys[pygame.K_LSHIFT] and not edmund.sprite.dashCooldown:  # if dash and not in cooldown, dash is true
            dash = True
            edmund.sprite.dashCooldown = True

        if not jumping and not edmund.sprite.inAir:  # if player is not already in the air, jump is possible
            if keys[pygame.K_SPACE]:
                jumping = True
                  
        mainAssets()  # import assets
        map_scroll()  # apply scroll


def boss1():
    global level
    global click
    global facing

    global scroll
    global scrollLeft
    global scrollRight
    global scrollSpeed

    global left
    global right
    global attack, enemyAttacked
    global walkCount

    global jumping, dash
    
    scroll = 0
    enemies.empty()
    edmund.sprite.rect.x = 300
    edmund.sprite.rect.y = 400

    pygame.mixer.music.load("Assets/Songs/stage1.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    pygame.display.set_caption("Boss 1", difficulty)

    boss = Boss(boss1Left[0], 1000, 200, 750)
    bosses.add(boss)

    while True:
        pygame.time.delay(40)
        click = False
        level = 5
        
        with open('level5_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tileVal in enumerate(row):
                    worldData[x][y] = int(tileVal)
        world.proccess(worldData)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    attack = True
                    left = False
                    right = False
        
        draw_text(f'Boss 1: {difficulty}', font, (255,255,255), 1000, 10)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            paused()

        if keys[pygame.K_a] and edmund.sprite.rect.x > 0:
            left = True
            right = False
            edmund.sprite.freeRun = True
            if facing == 'right':
                edmund.sprite.rect.x -= 60
                edmund.sprite.image = walkLeft[0]
            facing = 'left'

        elif keys[pygame.K_d] and edmund.sprite.rect.right < 1280:
            left = False
            right = True
            edmund.sprite.freeRun = True
            if facing == 'left':
                edmund.sprite.rect.x += 60
                edmund.sprite.image = walkRight[0]
            facing = 'right'  
        else:
            left = False
            right = False
            walkCount = 0
        
        if keys[pygame.K_LSHIFT] and not edmund.sprite.dashCooldown:
            dash = True
            edmund.sprite.dashCooldown = True

        if not jumping and not edmund.sprite.inAir:
            if keys[pygame.K_SPACE]:
                jumping = True
            
        mainAssets()

def stage2():
    global level
    global click
    global facing

    global scroll, bgScroll
    global scrollLeft
    global scrollRight
    global scrollSpeed

    global left
    global right
    global attack, enemyAttacked
    global walkCount

    global jumping, dash

    bgScroll = 0
    scroll = 0
    enemies.empty()
    edmund.sprite.rect.x = 300
    edmund.sprite.rect.y = 400

    pygame.mixer.music.load("Assets/Songs/stage2.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    pygame.display.set_caption("Stage 2", difficulty)

    if difficulty == 'easy':
        edmund.sprite.power = 75
        for i in range(1000, 4800, 600):
            enemy = Enemy(enemy2Left[0], i, 150, 4)
            enemies.add(enemy)
    if difficulty == 'normal':
        edmund.sprite.power = 50
        for i in range(1000, 4800, 500):
            enemy = Enemy(enemy2Left[0], i, 150, 5)
            enemies.add(enemy)
    if difficulty == 'hard':
        edmund.sprite.power = 37.5
        for i in range(1000, 4800, 400):
            enemy = Enemy(enemy2Left[0], i, 150, 6)
            enemies.add(enemy)

    while True:
        pygame.time.delay(40)
        click = False
        level = 2
        
        with open('level2_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tileVal in enumerate(row):
                    worldData[x][y] = int(tileVal)
        world.proccess(worldData)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    attack = True
                    left = False
                    right = False
        
        if edmund.sprite.rect.x+scroll >= 5300:
            boss2()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            paused()

        if keys[pygame.K_a] and edmund.sprite.rect.x > 25:
            left = True
            right = False
            if facing == 'right':
                edmund.sprite.rect.x -= 60
                edmund.sprite.image = walkLeft[0]
            facing = 'left'
            if scroll == 0:
                scrollLeft = False
                edmund.sprite.freeRun = True
            else:
                edmund.sprite.freeRun = False
                scrollLeft = True
                scrollRight = False

        elif keys[pygame.K_d] and edmund.sprite.rect.x < 1230:
            left = False
            right = True
            if facing == 'left':
                edmund.sprite.rect.x += 60
                edmund.sprite.image = walkRight[0]
            facing = 'right'
            if edmund.sprite.rect.x <= 600 or edmund.sprite.rect.x+scroll >= 5200:
                scrollRight = False
                edmund.sprite.freeRun = True
            else:
                edmund.sprite.freeRun = False
                scrollLeft = False
                scrollRight = True       
        else:
            left = False
            right = False
            scrollLeft = False
            scrollRight = False
            walkCount = 0
        
        if keys[pygame.K_LSHIFT] and not edmund.sprite.dashCooldown:
            dash = True
            edmund.sprite.dashCooldown = True

        if not jumping and not edmund.sprite.inAir:
            if keys[pygame.K_SPACE]:
                scrollSpeed = 8.5
                jumping = True
            
        mainAssets()
        map_scroll()

        pygame.display.update()

def boss2():
    global level
    global click
    global facing

    global scroll
    global scrollLeft
    global scrollRight
    global scrollSpeed

    global left
    global right
    global attack, enemyAttacked
    global walkCount

    global jumping, dash
    
    scroll = 0
    enemies.empty()
    edmund.sprite.rect.x = 300
    edmund.sprite.rect.y = 400

    pygame.mixer.music.load("Assets/Songs/stage2.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    pygame.display.set_caption("Boss 2", difficulty)

    boss = Boss(boss2Left[0], 1000, 200, 750)
    bosses.add(boss)

    while True:
        pygame.time.delay(40)
        click = False
        level = 6
        
        with open('level5_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tileVal in enumerate(row):
                    worldData[x][y] = int(tileVal)
        world.proccess(worldData)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    attack = True
                    left = False
                    right = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused()

        if keys[pygame.K_a]:
            left = True
            right = False
            edmund.sprite.freeRun = True
            if facing == 'right':
                edmund.sprite.rect.x -= 60
                edmund.sprite.image = walkLeft[0]
            facing = 'left'

        elif keys[pygame.K_d]:
            left = False
            right = True
            edmund.sprite.freeRun = True
            if facing == 'left':
                edmund.sprite.rect.x += 60
                edmund.sprite.image = walkRight[0]
            facing = 'right'  
        else:
            left = False
            right = False
            walkCount = 0
        
        if keys[pygame.K_LSHIFT] and not edmund.sprite.dashCooldown:
            dash = True
            edmund.sprite.dashCooldown = True

        if not jumping and not edmund.sprite.inAir:
            if keys[pygame.K_SPACE]:
                jumping = True
            
        mainAssets()

def stage3():

    global level
    global click
    global facing

    global scroll
    global scrollLeft
    global scrollRight
    global scrollSpeed

    global left
    global right
    global attack, enemyAttacked
    global walkCount

    global jumping, dash

    scroll = 0
    enemies.empty()
    edmund.sprite.rect.x = 300
    edmund.sprite.rect.y = 400

    pygame.mixer.music.load("Assets/Songs/stage3.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    pygame.display.set_caption("Stage 3", difficulty)

    if difficulty == 'easy':
        edmund.sprite.power = 75
        for i in range(1000, 4800, 600):
            enemy = Enemy(enemy3Left[0], i, 150, 4)
            enemies.add(enemy)
    if difficulty == 'normal':
        edmund.sprite.power = 50
        for i in range(1000, 4800, 500):
            enemy = Enemy(enemy3Left[0], i, 150, 5)
            enemies.add(enemy)
    if difficulty == 'hard':
        edmund.sprite.power = 37.5
        for i in range(1000, 4800, 400):
            enemy = Enemy(enemy3Left[0], i, 150, 6)
            enemies.add(enemy)

    while True:
        pygame.time.delay(40)
        click = False
        level = 3
        
        with open('level3_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tileVal in enumerate(row):
                    worldData[x][y] = int(tileVal)
        world.proccess(worldData)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    attack = True
                    left = False
                    right = False

        if edmund.sprite.rect.x+scroll >= 4500:
            KingBattle()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused()

        if keys[pygame.K_a] and edmund.sprite.rect.x > 25:
            left = True
            right = False
            if facing == 'right':
                edmund.sprite.rect.x -= 60
                edmund.sprite.image = walkLeft[0]
            facing = 'left'
            if scroll == 0 :
                scrollLeft = False
                edmund.sprite.freeRun = True
            else:
                edmund.sprite.freeRun = False
                scrollLeft = True
                scrollRight = False

        elif keys[pygame.K_d] and edmund.sprite.rect.x < 1230:
            left = False
            right = True
            if facing == 'left':
                edmund.sprite.rect.x += 60
                edmund.sprite.image = walkRight[0]
            facing = 'right'
            if edmund.sprite.rect.x <= 600 or edmund.sprite.rect.x+scroll >= 4445:
                scrollRight = False
                edmund.sprite.freeRun = True
            else:
                edmund.sprite.freeRun = False
                scrollLeft = False
                scrollRight = True       
        else:
            left = False
            right = False
            scrollLeft = False
            scrollRight = False
            walkCount = 0
        
        if keys[pygame.K_LSHIFT] and not edmund.sprite.dashCooldown:
            dash = True
            edmund.sprite.dashCooldown = True

        if not jumping and not edmund.sprite.inAir:
            if keys[pygame.K_SPACE]:
                scrollSpeed = 8.5
                jumping = True
            
        mainAssets()
        map_scroll()

def KingBattle():
    # Make global variables local
    global level
    global click
    global facing

    global scroll
    global scrollLeft
    global scrollRight
    global scrollSpeed

    global left
    global right
    global attack, enemyAttacked
    global walkCount

    global jumping, dash
    
    #  Reset variables, lists, and player positioning
    scroll = 0
    enemies.empty()
    edmund.sprite.rect.x = 300
    edmund.sprite.rect.y = 400

    # play music:
    pygame.mixer.music.load("Assets/Songs/stage3.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    boss = Boss(kingLeft[0], 1000, 200, 750)  # create the boss
    bosses.add(boss)

    while True:
        pygame.time.delay(40)  # set delay
        click = False
        level = 7  # Level 7
        
        # Draw tilemap (described on line 1696):
        with open('level5_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter = ',')
            for x, row in enumerate(reader):
                for y, tileVal in enumerate(row):
                    worldData[x][y] = int(tileVal)
        world.proccess(worldData)

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  # Check if user wants to exit the window
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Check if user has clicked
                if event.button == 1:
                    click = True
                    attack = True
                    left = False
                    right = False

        # Movement code explained on line 1706:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            paused()

        if keys[pygame.K_a]:
            left = True
            right = False
            edmund.sprite.freeRun = True
            if facing == 'right':
                edmund.sprite.rect.x -= 60
                edmund.sprite.image = walkLeft[0]
            facing = 'left'

        elif keys[pygame.K_d]:
            left = False
            right = True
            edmund.sprite.freeRun = True
            if facing == 'left':
                edmund.sprite.rect.x += 60
                edmund.sprite.image = walkRight[0]
            facing = 'right'  
        else:
            left = False
            right = False
            walkCount = 0
        
        if keys[pygame.K_LSHIFT] and not edmund.sprite.dashCooldown:
            dash = True
            edmund.sprite.dashCooldown = True

        if not jumping and not edmund.sprite.inAir:
            if keys[pygame.K_SPACE]:
                jumping = True
            
        mainAssets()  # import game assets


menu()  # call the menu function
