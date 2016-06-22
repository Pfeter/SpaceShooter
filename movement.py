for event in pygame.event.get():
	press = pygame.key.get_pressed()
	if event.type == QUIT:
		self.running = False
		self.exit()

	elif press[pygame.K_ESCAPE]:
		self.running = False
		self.exit()

	if press[pygame.K_UP]:
		direction[0] = True
	else:
		direction[0] = False
	if press[pygame.K_DOWN]:
		direction[1] = True
	else:
		direction[1] = False
	if press[pygame.K_RIGHT]:
		direction[2] = True
	else:
		direction[2] = False
	if press[pygame.K_LEFT]:
		direction[3] = True
	else:
		direction[3] = False
		# if press[pygame.K_SPACE]:
		#     self.projectiles.append(Bullet(self.spaceship.x, self.spaceship.y))
		# if press[pygame.K_a]:
		#     self.projectiles.append(Bomb(self.spaceship.x, self.spaceship.y))
		# if press[pygame.K_s]:
		#     self.projectiles.append(Laser(self.spaceship.x, self.spaceship.y, self.width))