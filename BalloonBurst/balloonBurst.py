import pygame
import random
pygame.init()
pygame.font.init()
pygame.display.set_caption('Balloon Burst')
pop=pygame.mixer.Sound("Balloon_Burst/audio/pop.wav")
screen=pygame.display.set_mode((1000, 500))
balloons=[pygame.image.load("Balloon_Burst/images/balloon1.png"),pygame.image.load("Balloon_Burst/images/balloon2.png"),pygame.image.load("Balloon_Burst/images/balloon3.png"),pygame.image.load("Balloon_Burst/images/balloon4.png"),pygame.image.load("Balloon_Burst/images/balloon5.png")]
sky=pygame.image.load("Balloon_Burst/images/sky.png")
sky = pygame.transform.scale(sky, (1000, 625))
pause=pygame.image.load("Balloon_Burst/images/pause.png")
pause=pygame.transform.scale(pause, (50, 50))
play=pygame.image.load("Balloon_Burst/images/play.png")
play=pygame.transform.scale(play, (50, 50))
playAgain=pygame.image.load("Balloon_Burst/images/play_again.png")
life=pygame.image.load("Balloon_Burst/images/life.png")
life=pygame.transform.scale(life, (30, 30))
done=False
def main():
	global done
	screen.fill((255,255,255))
	score=0
	pygame.font.init()
	myfont = pygame.font.SysFont('Arial', 20)
	exitFont=pygame.font.SysFont('Arial', 40)
	exit=exitFont.render('Press Any Key to End', False, (0, 0, 0))
	lives=myfont.render('Lives: ', False, (0, 0, 0))
	textsurface = myfont.render('Score: '+str(score), False, (0, 0, 0))
	welcome=pygame.font.SysFont('Arial', 50)
	welcomeMessage = welcome.render('Welcome to Balloon Burst!', False, (0, 0, 0))
	cont=myfont.render('Press Any Key to Start', False, (0, 0, 0))
	screen.blit(welcomeMessage,(150,150))
	screen.blit(cont,(350,220))
	pygame.display.flip()
	start=False
	while not start and not done:
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				start=True
			if event.type==pygame.QUIT:
				done=True

	current=[balloons[random.randint(0,len(balloons)-1)]]
	speeds=[]
	for s in range (0,len(current)):
		speeds.append(balloons.index(current[s])+1)
	X=[]
	for x in range (0,len(current)):
		X.append(random.randint(0,850))
	Y=[]
	for y in range (0,len(current)):
		Y.append(500)
	numLives=5
	while not done:
		if ((int(score/100)+1)>len(current)):
			current.append(balloons[random.randint(0,len(balloons)-1)])
			X.append(random.randint(0,850))
			Y.append(500)
			speeds.append(balloons.index(current[int(score/100)])+1)
		paused=False
		over=False
		sizes=[]
		if (numLives==0):
			over=True
		for s in range (0,len(current)):
			sizes.append(current[s].get_size())
		screen.blit(sky,(0,0))
		screen.blit(textsurface,(10,10))
		screen.blit(lives,(260,10))
		for y in range (0,len(Y)):
			Y[y]-=speeds[y]
		screen.blit(pause,(945,10))
		for b in range (0,len(current)):
			screen.blit(current[b],(X[b],Y[b]))
		for l in range (0,numLives):
			screen.blit(life,(35*l+320,10))
		pygame.display.flip()
		for d in range (0,len(current)):
			if (Y[d]<=-10-sizes[d][1]):
				score-=(6-speeds[d])
				current[d]=balloons[random.randint(0,len(balloons)-1)]
				X[d]=random.randint(0,850)
				Y[d]=500
				speeds[d]=balloons.index(current[d])+1
				textsurface = myfont.render('Score: '+str(score), False, (0, 0, 0))
				screen.blit(textsurface,(10,10))
				numLives-=1
				pygame.display.flip()
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				done=True
			if event.type==pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for p in range (0,len(current)):
					if (pos[0]>=X[p] and pos[0]<=(X[p]+sizes[p][0]) and pos[1]>=Y[p] and pos[1]<=(Y[p]+sizes[p][1])):
						pop.play()
						score+=speeds[p]
						textsurface = myfont.render('Score: '+str(score), False, (0, 0, 0))
						screen.blit(textsurface,(10,10))
						pygame.display.flip()
						current[p]=balloons[random.randint(0,len(balloons)-1)]
						X[p]=random.randint(0,850)
						Y[p]=500
						speeds[p]=balloons.index(current[p])+1
						break
				if (pos[0]<=995 and pos[0]>=945 and pos[1]>=10 and pos[1]<=60):
					screen.blit(play,(945,10))
					paused=True
					screen.blit(exit,(300,200))
					pygame.display.flip()
					while paused:
						for event in pygame.event.get():
							if event.type==pygame.QUIT:
								done=True
								paused=False
							if event.type==pygame.MOUSEBUTTONDOWN:
								pos = pygame.mouse.get_pos()
								if (pos[0]<=995 and pos[0]>=945 and pos[1]>=10 and pos[1]<=60):
									paused=False
							if event.type==pygame.KEYDOWN:
								over=True
								paused=False
		if (over):
			screen.fill((242, 174, 174))
			font = pygame.font.SysFont('Arial', 80)
			gameOver=font.render('GAME OVER', False, (255, 0, 0))
			scorePrint = myfont.render('Score: '+str(score), False, (0, 0, 0))
			screen.blit(gameOver,(250,150))
			screen.blit(scorePrint,(450,270))
			high_score_file = open("balloonBurstHighScore.txt", "r")
			high_score = int(high_score_file.read())
			high_score_file.close()
			if (high_score<score):
				high_score=score
				high_score_file = open("balloonBurstHighScore.txt", "w")
				high_score_file.write(str(high_score))
				high_score_file.close()
			highScore = myfont.render('High Score: '+str(high_score), False, (0, 0, 0))
			screen.blit(highScore,(420,300))
			screen.blit(playAgain,(395,360))
			pygame.display.flip()
			while not done:
				for event in pygame.event.get():
					if event.type==pygame.MOUSEBUTTONDOWN:
						pos=pygame.mouse.get_pos()
						if (pos[0]>=395 and pos[0]<=601 and pos[1]>=360 and pos[1]<=416):
							main()
					if event.type==pygame.QUIT:
						done=True
			break
main()