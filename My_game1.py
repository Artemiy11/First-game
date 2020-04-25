import pygame,random,pyaudio
import os
from pathlib import Path

pygame.init()
Skeleton_Dead = [pygame.image.load('Skeleton Dead1.png'), pygame.image.load('Skeleton Dead2.png'), pygame.image.load('Skeleton Dead3.png'), pygame.image.load('Skeleton Dead4.png'), pygame.image.load('Skeleton Dead5.png'),
pygame.image.load('Skeleton Dead6.png'), pygame.image.load('Skeleton Dead7.png'), pygame.image.load('Skeleton Dead8.png'), pygame.image.load('Skeleton Dead9.png'), pygame.image.load('Skeleton Dead10.png'),
pygame.image.load('Skeleton Dead11.png'), pygame.image.load('Skeleton Dead12.png'), pygame.image.load('Skeleton Dead13.png'), pygame.image.load('Skeleton Dead14.png'), pygame.image.load('Skeleton Dead15.png')]

Skeleton_WalkR = [pygame.image.load('Skeleton WalkR1.png'), pygame.image.load('Skeleton WalkR2.png'), pygame.image.load('Skeleton WalkR3.png'), pygame.image.load('Skeleton WalkR4.png'), pygame.image.load('Skeleton WalkR5.png'),
pygame.image.load('Skeleton WalkR6.png'), pygame.image.load('Skeleton WalkR7.png'), pygame.image.load('Skeleton WalkR8.png'), pygame.image.load('Skeleton WalkR9.png'), pygame.image.load('Skeleton WalkR10.png'),
pygame.image.load('Skeleton WalkR11.png'), pygame.image.load('Skeleton WalkR12.png'), pygame.image.load('Skeleton WalkR13.png')]

Skeleton_Walk = [pygame.image.load('Skeleton Walk1.png'), pygame.image.load('Skeleton Walk2.png'), pygame.image.load('Skeleton Walk3.png'), pygame.image.load('Skeleton Walk4.png'), pygame.image.load('Skeleton Walk5.png'),
pygame.image.load('Skeleton Walk6.png'), pygame.image.load('Skeleton Walk7.png'), pygame.image.load('Skeleton Walk8.png'), pygame.image.load('Skeleton Walk9.png'), pygame.image.load('Skeleton Walk10.png'),
pygame.image.load('Skeleton Walk11.png'), pygame.image.load('Skeleton Walk12.png'), pygame.image.load('Skeleton Walk13.png')]

skeleton_idle = [pygame.image.load('Skeleton Idle11.png'), pygame.image.load('Skeleton Idle10.png'), pygame.image.load('Skeleton Idle9.png'), pygame.image.load('Skeleton Idle8.png'), pygame.image.load('Skeleton Idle7.png'),
pygame.image.load('Skeleton Idle6.png'), pygame.image.load('Skeleton Idle5.png'), pygame.image.load('Skeleton Idle4.png'), pygame.image.load('Skeleton Idle3.png'), pygame.image.load('Skeleton Idle2.png'),
pygame.image.load('Skeleton Idle.png')]

skeleton_attack = [pygame.image.load('Skeleton Attack1.png'), pygame.image.load('Skeleton Attack2.png'), pygame.image.load('Skeleton Attack3.png'), pygame.image.load('Skeleton Attack4.png'), pygame.image.load('Skeleton Attack5.png'),
pygame.image.load('Skeleton Attack6.png'), pygame.image.load('Skeleton Attack7.png'), pygame.image.load('Skeleton Attack8.png'), pygame.image.load('Skeleton Attack9.png'), pygame.image.load('Skeleton Attack10.png'),
pygame.image.load('Skeleton Attack11.png'), pygame.image.load('Skeleton Attack12.png'), pygame.image.load('Skeleton Attack13.png'), pygame.image.load('Skeleton Attack14.png'), pygame.image.load('Skeleton Attack15.png'),
pygame.image.load('Skeleton Attack16.png'), pygame.image.load('Skeleton Attack17.png'), pygame.image.load('Skeleton Attack18.png')]

explosion = [pygame.image.load('explosion1.png'), pygame.image.load('explosion2.png'), pygame.image.load('explosion3.png'), pygame.image.load('explosion4.png'), pygame.image.load('explosion5.png'),
pygame.image.load('explosion6.png'), pygame.image.load('explosion7.png'), pygame.image.load('explosion8.png'), pygame.image.load('explosion9.png'), pygame.image.load('explosion10.png'),
pygame.image.load('explosion11.png'), pygame.image.load('explosion12.png'), pygame.image.load('explosion13.png'), pygame.image.load('explosion14.png'), pygame.image.load('explosion15.png'),
pygame.image.load('explosion16.png'), pygame.image.load('explosion17.png'), pygame.image.load('explosion18.png'), pygame.image.load('explosion19.png')]

wolfR = [pygame.image.load('wolfR1.png'), pygame.image.load('wolfR2.png'), pygame.image.load('wolfR3.png'), pygame.image.load('wolfR4.png'), pygame.image.load('wolfR5.png')]
wolfL = [pygame.image.load('wolfL1.png'), pygame.image.load('wolfL2.png'), pygame.image.load('wolfL3.png'), pygame.image.load('wolfL4.png'), pygame.image.load('wolfL5.png')]

wolf_idle = pygame.image.load('wolf_idle.png')

walkRight = [pygame.image.load('SoldatR1.png'), pygame.image.load('SoldatR2.png'), pygame.image.load('SoldatR3.png'), pygame.image.load('SoldatR4.png'), pygame.image.load('SoldatR5.png'), pygame.image.load('SoldatR6.png')]

walkLeft = [pygame.image.load('SoldatL1.png'), pygame.image.load('SoldatL2.png'), pygame.image.load('SoldatL3.png'), pygame.image.load('SoldatL4.png'), pygame.image.load('SoldatL5.png'), pygame.image.load('SoldatL6.png')]

bg = pygame.image.load('forest.png')
SoldatStand = pygame.image.load('SoldatStand.png')
playerDead = pygame.image.load('Stickman_dead.png')

pygame.mixer.music.load("highway_frenzy.ogg")	
pygame.mixer.music.play(-1)


win = pygame.display.set_mode((960,640))
pygame.display.set_caption('Game of war')

clock = pygame.time.Clock()

t = 0
c = 0
bullets = []

SkeletX = 100
SkeletY = 575
SkeletH = 300
IsSkeletJumpLeft = False 
IsSkeletJumpRight = False
SkeletStrikeCount = 0
SkeletAnimCount = 0
strikeCountS = 0
SkeletCount = 10
DeathHappend = False
DeathAnimCount = 0

wolfX = 50
wolfHealth = 500
wolfY = 575
wolfCount = 10
isWolfJumpLeft = False
isWolfJumpRight = False
strikeCount = 0
explosionHappend = False

health = 100
x = 900
y = 575
height = 71
width = 60
speed = 3
lastMove = 'right'


enemyX = 560
enemyY = 500
enemyHeight = 71
enemyWidth = 60
enemySpeed = 5

right = False
left = False

isCharge = False

isJump = False
jumpCount = 10
run = True

animCount = 0
wolfAnimCount = 0
explosionAnimCount = 0

class snaryad():
	def __init__(self, x, y, facing, radius,color):
		self.x = x
		self.y = y
		self.facing = facing
		self.radius = radius
		self.color = color
		self.vel = 8 * facing

	def draw(self,win):
		pygame.draw.circle(win, self.color,(self.x, self.y), self.radius)

def handleInput():
	global run
	global left
	global right
	global x
	global y
	global isCharge
	global isJump
	global jumpCount
	global animCount
	global health
	global walkRight
	global walkLeft
	global c
	global bullets
	global bullet
	global lastMove
	global wolfHealth
	global wolfX
	global wolfY
	global wolfCounter
	global wolfAnimCount
	global wolfCount
	global isWolfJumpLeft
	global isWolfJumpRight
	global SkeletCount
	global SkeletH
	global IsSkeletJumpLeft
	global SkeletX
	global IsSkeletJumpRight
	global SkeletY


	if health > 0:

		for bullet in bullets:
			if bullet.x < 960 and bullet.x > 0:
				bullet.x += bullet.vel
			else:
				bullets.pop(bullets.index(bullet))

		for bullet in bullets:
			if abs(bullet.x - SkeletX) < 5 and x < SkeletX:
				isSkeletJumpLeft = True
				SkeletH -= 20
				print(SkeletH)

		for bullet in bullets:
			if abs(bullet.x - SkeletX) < 5 and x > SkeletX:
				IsSkeletJumpRight = True
				SkeletH -= 20
				print(SkeletH)	
				
		if SkeletH > 0:
			if IsSkeletJumpLeft:	
				if SkeletCount >= -10:
					if SkeletCount < 0:
						SkeletY+= (SkeletCount ** 2) / 10
				
					else:
						SkeletY-= (SkeletCount ** 2) / 10
						SkeletX+= (SkeletCount ** 2) / 9
					SkeletCount-= 1
				else:
					IsSkeletJumpLeft = False
					SkeletCount = 10



		if SkeletH > 0:
			if IsSkeletJumpRight:	
				if SkeletCount >= -10:
					if SkeletCount < 0:
						SkeletY+= (SkeletCount ** 2) / 10
				
					else:
						SkeletY-= (SkeletCount ** 2) / 10
						SkeletX-= (SkeletCount ** 2) / 9
					SkeletCount-= 1
				else:
					IsSkeletJumpRight = False
					SkeletCount = 10							
			
		for bullet in bullets:
			if abs(bullet.x - wolfX) < 5 and x < wolfX:
				isWolfJumpLeft = True
				wolfHealth -= 20
				print(wolfHealth)

		if wolfHealth > 0:
			if isWolfJumpLeft:	
				if wolfCount >= -10:
					if wolfCount < 0:
						wolfY+= (wolfCount ** 2) / 10
				
					else:
						wolfY-= (wolfCount ** 2) / 10
						wolfX+= (wolfCount ** 2) / 9
					wolfCount-= 1
				else:
					isWolfJumpLeft = False
					wolfCount = 10

		for bullet in bullets:
			if abs(bullet.x - wolfX) < 5 and x > wolfX:
				isWolfJumpRight = True
				wolfHealth -= 20
				print(wolfHealth)
				
		if wolfHealth > 0:
			if isWolfJumpRight:	
				if wolfCount >= -10:
					if wolfCount < 0:
						wolfY+= (wolfCount ** 2) / 10
				
					else:
						wolfY-= (wolfCount ** 2) / 10
						wolfX-= (wolfCount ** 2) / 9
					wolfCount-= 1
				else:
					isWolfJumpRight = False
					wolfCount = 10
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and x > 5:
			x-= speed
			left = True
			right = False
			lastMove = 'left'

		elif keys[pygame.K_RIGHT] and x < 950 - width:
			x+= speed
			right = True
			left = False
			lastMove = 'right'

		else:
			right = False
			left = False
			animCount = 0
		if keys[pygame.K_SPACE]:
			isJump = True
		if isJump:	
			if jumpCount >= -10:
				if jumpCount < 0:
					y+= (jumpCount ** 2) / 8
				else:
					y-= (jumpCount ** 2) / 8
				jumpCount -= 1
			else:
				isJump = False
				jumpCount = 10

		if keys[pygame.K_m]:
			isCharge = True
			if isCharge and right and not isJump:
				x+= (speed ** 2) / 6
			elif isCharge and left and not isJump:
				x-= (speed ** 2) / 6

		if keys[pygame.K_n]:
			walkRight = [pygame.image.load('SoldatGR2.png'), pygame.image.load('SoldatGR3.png'), pygame.image.load('SoldatGR4.png'), pygame.image.load('SoldatGR5.png'), pygame.image.load('SoldatGR6.png'), pygame.image.load('SoldatGR7.png')]
			walkLeft = [pygame.image.load('SoldatGL2.png'), pygame.image.load('SoldatGL3.png'), pygame.image.load('SoldatGL4.png'), pygame.image.load('SoldatGL5.png'), pygame.image.load('SoldatGL6.png'), pygame.image.load('SoldatGL7.png')]
			c = 1
		if keys[pygame.K_h]:
			walkRight = [pygame.image.load('SoldatR1.png'), pygame.image.load('SoldatR2.png'), pygame.image.load('SoldatR3.png'), pygame.image.load('SoldatR4.png'), pygame.image.load('SoldatR5.png'), pygame.image.load('SoldatR6.png')]
			walkLeft = [pygame.image.load('SoldatL1.png'), pygame.image.load('SoldatL2.png'), pygame.image.load('SoldatL3.png'), pygame.image.load('SoldatL4.png'), pygame.image.load('SoldatL5.png'), pygame.image.load('SoldatL6.png')]
			с = 0
		if keys[pygame.K_b]:
			if lastMove == 'right':
				facing = 1
			else:
				facing = -1

			if c == 1:
				if len(bullets) < 6:
					 bullets.append(snaryad(round(x + 32),round(y + 10), facing, 5, (0,0,0)))






def render():
	global win
	global enemyX
	global enemyY
	global enemyWidth
	global enemyHeight
	global x
	global y
	global left
	global right
	global walkLeft
	global walkRight
	global SoldatStand
	global animCount
	global wolfY
	global wolfX
	global wolfAnimCount
	global wolfHealth
	global health
	global strikeCount
	global explosionAnimCount
	global explosion
	global explosionHappend
	global SkeletX
	global SkeletH
	global SkeletY
	global SkeletAnimCount
	global skeleton_idle
	global IsSkeletJumpLeft
	global isWolfJumpRight
	global strikeCountS
	global DeathHappend
	global DeathAnimCount

	win.blit(bg,(0,0))

	if SkeletH == 0 or SkeletH < 0:
		win.blit(Skeleton_Dead[SkeletAnimCount // 5], (SkeletX,SkeletY))
		SkeletAnimCount += 1

	if SkeletH > 0:
		if x < SkeletX:
			win.blit(Skeleton_Walk[SkeletAnimCount // 5], (SkeletX,SkeletY))
			SkeletAnimCount += 1
			if not IsSkeletJumpLeft:
				SkeletX -= 3

	if SkeletH > 0:
		if x > SkeletX:
			win.blit(Skeleton_WalkR[SkeletAnimCount // 5], (SkeletX,SkeletY))
			SkeletAnimCount += 1
			if not IsSkeletJumpRight:
				SkeletX += 3

	if abs(SkeletX - x) < 10 and strikeCountS % 30 == 0 and health != 0:
		health-= 15
		print('your health is ' + str(health) + '%')	

	if DeathAnimCount + 1 >= 30:
		DeathAnimCount = 0
		DeathHappend = True

	if DeathHappend:
		SkeletX = 890


	strikeCountS += 1

	if strikeCountS + 1 >= 30:
		strikeCountS = 0		

	if SkeletAnimCount + 1 >= 55:
		SkeletAnimCount = 0

	if explosionAnimCount + 1 >= 95:
		explosionAnimCount = 0
		explosionHappend = True

	if explosionHappend:
		explosionAnimCount = -1

	if health == 0 or health < 0:	
		pygame.quit()

	strikeCount += 1

	if strikeCount + 1 >= 30:
		strikeCount = 0

	if abs(wolfX - x) < 10 and strikeCount % 30 == 0 and health != 0:
		health-= 25
		print('your health is ' + str(health) + '%')

	if wolfHealth > 0:
		if x < wolfX:
			win.blit(wolfL[wolfAnimCount // 5], (wolfX,wolfY))
			wolfAnimCount += 1
			if not isWolfJumpLeft:
				wolfX -= 3

		if x > wolfX:
			win.blit(wolfR[wolfAnimCount // 5], (wolfX,wolfY))
			wolfAnimCount += 1
			if not isWolfJumpLeft:
				wolfX += 3

	for bullet in bullets:
		bullet.draw(win)

	if animCount + 1 >= 30:
		animCount = 0

	if wolfAnimCount + 1 >= 25:
		wolfAnimCount = 0

	if health == 0 or health < 0:
		win.blit(playerDead,(x,y))

	if wolfHealth <= 0:
		win.blit(explosion[explosionAnimCount // 5], (wolfX,wolfY - 70))
		explosionAnimCount += 1

	if health > 0:
		if left:
			win.blit(walkLeft[animCount // 5], (x,y))
			animCount += 1
		elif right:
			win.blit(walkRight[animCount // 5], (x,y))
			animCount += 1
		else:
			win.blit(SoldatStand,(x,y))

	pygame.display.update()

while run:
	clock.tick(30)
	t+=1
	render()
	handleInput()



pygame.quit()
