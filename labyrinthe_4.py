import pygame
from pygame.locals import *
import random
import time

class Elem(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.x = 0
                self.y = 0
                self.lab = list()
                self.wall = list()
                self.finish = list()
                self.start = list()
                self.path = list()

        def extract_elem(self,  fichier):
                with open(fichier,  "r") as fichier:
                        structure = []
                        for l in fichier:
                                niveau = []
                                for c in l:
                                        if c != '\n':
                                                niveau.append(c)
                                structure.append(niveau)
                        self.lab = structure
                num_ligne = 0
                for ligne in self.lab:
                        num_case = 0
                        for case in ligne:

                            self.x = num_case * 30    
                            self.y = num_ligne * 30
                            if case == 'm':
                                self.wall.append((self.x,  self.y))
                            elif case == 'a':
                                self.finish.append((self.x,  self.y))
                            elif case == 'd':
                                 self.start.append((self.x,  self.y))

                            elif case == '0':
                                 self.path.append((self.x,  self.y))

                            num_case += 1
                        num_ligne += 1
                return self.wall, self.finish, self.start, self.path

class Wall(pygame.sprite.Sprite):
        def __init__(self, o, liste):
                pygame.sprite.Sprite.__init__(self)
                image_wall = "images/mur.png"
                self.image = pygame.image.load(image_wall).convert()
                self.rect = self.image.get_rect()
                self.rect.x, self.rect.y = liste[o]
                
class Start():
        def __init__(self):
                self.x = 0
                self.y = 0
                image_start = "images/depart.png"
                self.image = pygame.image.load(image_start).convert()
                
class Finish(pygame.sprite.Sprite):
        def __init__(self, o, liste):
                pygame.sprite.Sprite.__init__(self)
                image_finish = "images/arrivee.png"
                self.image = pygame.image.load(image_finish).convert()
                self.rect = self.image.get_rect()
                self.rect.x, self.rect.y = liste[o]
                
class Objects(pygame.sprite.Sprite):
        def __init__(self, liste, o):
                pygame.sprite.Sprite.__init__(self)
                self.x = 0
                self.y = 0
                self.list_image = ["images/objets.png", "images/objets2.png", "images/objets3.png"]
                self.image = pygame.image.load(self.list_image[o]).convert_alpha()
                self.rect = self.image.get_rect()
                self.rect.width, self.rect.height = 30, 30
                self.rect.x, self.rect.y = random.choice(liste)
                        
                        
                        
class Perso(pygame.sprite.Sprite):
        def __init__(self, image):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(image).convert_alpha()
                self.rect = self.image.get_rect()
                self.x = 0
                self.y = 0
                self.rect.x = 0
                self.rect.y = 0
                self.rect.width, self.rect.height = 30, 30
        def deplacer(self, direction):
                if direction == 'bas':
                        if self.y<14:
                                self.y += 1
                                self.rect.y = self.y* 30
                                if pygame.sprite.spritecollide(self, wallGroupSprite, False):
                                        self.y -= 1
                                        self.rect.y = self.y* 30
                                        print('collision en bas')
                if direction == 'haut':
                        if self.y > 0:
                                self.y -= 1
                                self.rect.y = self.y* 30
                                if pygame.sprite.spritecollide(self, wallGroupSprite, False):
                                        self.y += 1
                                        self.rect.y = self.y* 30
                                        print('collision en haut')                               
                if direction == 'droite':
                    if self.x < 14:
                            self.x += 1
                            self.rect.x = self.x* 30
                            if pygame.sprite.spritecollide(self, wallGroupSprite, False):
                                        self.x -= 1
                                        self.rect.x = self.x* 30
                                        print('collision à droite')                            
                if direction == 'gauche':
                        if self.x > 0:
                                self.x -= 1
                                self.rect.x = self.x* 30
                                if pygame.sprite.spritecollide(self, wallGroupSprite, False):
                                        self.x += 1
                                        self.rect.x = self.x* 30
                                        print('collision à gauche')
                return self.rect.x, self.rect.y
            
        
pygame.init()


fenetre=pygame.display.set_mode((450, 450), RESIZABLE)
image_fond = "images/fond.jpg"

text = "laby.txt"



img_macgyver = "images/macgyver.png"
macgyver = Perso(img_macgyver)

fond = pygame.image.load(image_fond).convert()
winning = pygame.image.load("images/image_victoire.png").convert()
loose = pygame.image.load("images/perdu.png").convert()

wallSprite = list()
finishSprite = list()
position_objSprite = list()


elem = Elem()
elem.extract_elem(text)
start = Start()

for i, o in enumerate(elem.wall):
        wallSprite.append(Wall(i, elem.wall))

for i, o in enumerate(elem.finish):
        finishSprite.append(Finish(i, elem.finish))

for i, o in enumerate(Objects(elem.path,i).list_image):
        position_objSprite.append(Objects(elem.path,i))



wallGroupSprite = pygame.sprite.Group(wallSprite)
macgyverSprite = pygame.sprite.Group(macgyver)
finishGroupSprite = pygame.sprite.Group(finishSprite)
catchedGroupSprite = pygame.sprite.Group()
objectsSprite = pygame.sprite.Group(position_objSprite)


fenetre.blit(fond, (0, 0))
pygame.display.flip()

play = True
while play:
        
        for elmt in elem.start:
            fenetre.blit(start.image, elmt)

        wallGroupSprite.draw(fenetre)

        finishGroupSprite.draw(fenetre)

        objectsSprite.draw(fenetre)
        
        macgyverSprite.draw(fenetre)

        catchedGroupSprite.draw(fenetre)

        
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

        if pygame.sprite.spritecollide(macgyver, objectsSprite, True):
                
                
                print('Récupération objects')
                for o in position_objSprite:
                        if o  not in  objectsSprite.sprites():
                                o.rect.x, o.rect.y = 0, (len(position_objSprite)+11)*30
                                print(o.rect.x, o.rect.y)
                                catchedGroupSprite.add(o)
                                position_objSprite.remove(o)




                
                       
                                  
                                    

        if pygame.sprite.spritecollide(macgyver, finishGroupSprite, False):
                if len(position_objSprite) == 0:
                        print('Gagné')
                        play = False
                        
                else :
                        print('perdu')
                        play = False
                        
                
           
        fenetre.blit(fond, (0, 0))            

        for elmt in elem.start:
            fenetre.blit(start.image, elmt)

        
        wallGroupSprite.draw(fenetre)

        finishGroupSprite.draw(fenetre)

        objectsSprite.draw(fenetre)
                
        macgyverSprite.draw(fenetre)
        
        
        catchedGroupSprite.draw(fenetre)
        pygame.display.flip()
        



if play is False and len(position_objSprite) == 0:
        fenetre.blit(winning, (0, 0))
        pygame.display.flip()
        time.sleep(3)
else:
        fenetre.blit(loose, (0, 0))
        pygame.display.flip()
        time.sleep(3)

pygame.quit()
