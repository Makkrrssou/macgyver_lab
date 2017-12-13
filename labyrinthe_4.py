import pygame
from pygame.locals import *
import random

class Elem(pygame.sprite.Sprite):
		def __init__(self):
				pygame.sprite.Sprite.__init__(self)
				self.x=0
				self.y=0
				self.lab=list()
				self.mur=list()
				self.arrivee=list()
				self.depart=list()
				self.couloir=list()

		def extract_elem(self,fichier):
				with open(fichier,"r") as fichier:
						structure=[]
						for l in fichier:
								niveau=[]
								for c in l:
										if c !='\n':
												niveau.append(c)
								structure.append(niveau)
						self.lab=structure
				num_ligne = 0
				for ligne in self.lab:
						num_case = 0
						for case in ligne:
							self.x = num_case * 30    #conversion en pixels
							self.y = num_ligne * 30


							if case=='m':
								self.mur.append((self.x,self.y))


							elif case=='a':
								self.arrivee.append((self.x,self.y))


							elif case=='d':
								 self.depart.append((self.x,self.y))

							elif case=='0':
								 self.couloir.append((self.x,self.y))

							num_case+=1
						num_ligne+=1
				return self.mur,self.arrivee,self.depart,self.couloir

class Mur(pygame.sprite.Sprite):
		def __init__(self,o,liste):
				pygame.sprite.Sprite.__init__(self)
				image_mur="images/mur.png"
				self.image=pygame.image.load(image_mur).convert()
				self.rect=self.image.get_rect()
				self.rect.x,self.rect.y=liste[o]
				
					
			
				


class Depart():
		def __init__(self):
				self.x=0
				self.y=0
				image_depart="images/depart.png"
				self.image=pygame.image.load(image_depart).convert()
				


class Arrivee(pygame.sprite.Sprite):
		def __init__(self,o,liste):
				pygame.sprite.Sprite.__init__(self)
				image_arrivee="images/arrivee.png"
				self.image=pygame.image.load(image_arrivee).convert()
				self.rect=self.image.get_rect()
				self.rect.x,self.rect.y=liste[o]


			


class Objets(pygame.sprite.Sprite):
		def __init__(self,liste):
				pygame.sprite.Sprite.__init__(self)
				self.x=0
				self.y=0
				self.list_image=["images/objets.png","images/objets.png","images/objets.png"]
				for i in self.list_image:
						self.image=pygame.image.load(i).convert_alpha()
						self.rect=self.image.get_rect()
						self.rect.x,self.rect.y=random.choice(liste)
						
				


class Perso(pygame.sprite.Sprite):
		def __init__(self,image):
				pygame.sprite.Sprite.__init__(self)
				self.image = pygame.image.load(image).convert_alpha()
				self.rect=self.image.get_rect()
				self.x = 0
				self.y = 0
				self.rect.x=0
				self.rect.y=0
				self.rect.width,self.rect.height=30,30
		def deplacer(self,direction):

				if direction=='bas':
						if self.y<14:
								self.y+=1
								self.rect.y=self.y* 30
								if pygame.sprite.spritecollide(self,murGroupSprite,False):
										self.y-=1
										self.rect.y=self.y* 30
										print('collision en bas')
										

				if direction=='haut':
						if self.y>0:
								self.y-=1
								self.rect.y=self.y* 30
								if pygame.sprite.spritecollide(self,murGroupSprite,False):
										self.y+=1
										self.rect.y=self.y* 30
										print('collision en haut')

								
				if direction=='droite':
					if self.x<14:
							self.x+=1
							self.rect.x =self.x* 30
							if pygame.sprite.spritecollide(self,murGroupSprite,False):
										self.x-=1
										self.rect.x=self.x* 30
										print('collision à droite')

							
				if direction=='gauche':
						if self.x>0:
								self.x-=1
								self.rect.x=self.x* 30
								if pygame.sprite.spritecollide(self,murGroupSprite,False):
										self.x+=1
										self.rect.x=self.x* 30
										print('collision à gauche')
				return self.rect.x,self.rect.y
			
		

pygame.init()



fenetre=pygame.display.set_mode((450,450),RESIZABLE)
image_fond = "images/fond.jpg"

text="laby.txt"

elem=Elem()
elem.extract_elem(text)
depart=Depart()

img_macgyver="images/macgyver.png"
macgyver=Perso(img_macgyver)

fond=pygame.image.load(image_fond).convert()

murSprite=list()
arriveeSprite=list()

for i,o in enumerate(elem.mur):
		murSprite.append(Mur(i,elem.mur))

for i,o in enumerate(elem.arrivee):
		arriveeSprite.append(Arrivee(i,elem.arrivee))

murGroupSprite=pygame.sprite.Group(murSprite)
macgyverSprite=pygame.sprite.Group(macgyver)
arriveeGroupSprite=pygame.sprite.Group(arriveeSprite)




fenetre.blit(fond,(0,0))
position_objSprite=[]
for o in Objets(elem.couloir).list_image:
		position_objSprite.append(Objets(elem.couloir))

objetsSprite=pygame.sprite.Group(position_objSprite)
cpt_obj=0
pygame.display.flip()

jouer=True
while jouer:

		for elmt in elem.depart:
			fenetre.blit(depart.image,elmt)

		murGroupSprite.draw(fenetre)

		arriveeGroupSprite.draw(fenetre)

		objetsSprite.draw(fenetre)
		
		macgyverSprite.draw(fenetre)

		
		pygame.display.flip()
		for event in pygame.event.get():
				if event.type == KEYDOWN:
						if event.key == K_RIGHT:
							macgyver.deplacer('droite')
							
						elif event.key == K_LEFT:
							macgyver.deplacer('gauche')

						elif event.key == K_UP:
							macgyver.deplacer('haut')

						elif event.key == K_DOWN:
							macgyver.deplacer('bas')

		if pygame.sprite.spritecollide(macgyver,objetsSprite,True):
				cpt_obj+=1
				print('Récupération objets')

		if pygame.sprite.spritecollide(macgyver,arriveeGroupSprite,False):
				if cpt_obj==len(position_objSprite):
						print('Gagné')
						jouer=False
						
				else :
						print('perdu')
						jouer=False
						
				
		   
		fenetre.blit(fond,(0,0))            

		for elmt in elem.depart:
			fenetre.blit(depart.image,elmt)

		
		murGroupSprite.draw(fenetre)

		arriveeGroupSprite.draw(fenetre)

		objetsSprite.draw(fenetre)
				
		macgyverSprite.draw(fenetre)
		pygame.display.flip()


pygame.quit()
