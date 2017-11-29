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
                
                    
            
                


class Depart(Elem):
        def __init__(self):
                Elem.__init__(self)
                self.x=0
                self.y=0
                image_depart="images/depart.png"
                self.image=pygame.image.load(image_depart).convert()
                


class Arrivee(Elem):
        def __init__(self):
                Elem.__init__(self)
                self.x=0
                self.y=0
                image_arrivee="images/arrivee.png"
                self.image=pygame.image.load(image_arrivee).convert()
                self.image_rect=self.image.get_rect()
                arriveSprite=list()

        def arriveeSprite(self):

            for i in Elem.mur:
                
                self.image_rect.x=i[0]
                self.image_rect.y=i[1]
                arriveeSprite.append(i)
                
            return arriveeSprite
            


class Objets(Elem):
        def __init__(self):
                Elem.__init__(self)
                self.x=0
                self.y=0
                image_obj="images/objets.png"
                self.image1=pygame.image.load(image_obj).convert_alpha()
                self.image2=pygame.image.load(image_obj).convert_alpha()
                self.image3=pygame.image.load(image_obj).convert_alpha()
                self.list_image=[self.image1,self.image2,self.image3]

class Perso(pygame.sprite.Sprite):
        def __init__(self,image):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load(image).convert_alpha()
                self.rect=self.image.get_rect()
                self.x = 0
                self.y = 0
                self.rect.x=0
                self.rect.y=0
        def deplacer(self,direction):

                if direction=='bas':
                        if self.y<15:
                                self.y+=1
                                self.rect.y=self.y* 30

                if direction=='haut':
                        if self.y>0:
                                self.y-=1
                                self.rect.y=self.y* 30

                                
                if direction=='droite':
                    if self.x<=15:
                            self.x+=1
                            self.rect.x=self.x* 30

                            
                if direction=='gauche':
                        if self.x>0:
                                self.x-=1
                                self.rect.x=self.x* 30
                return self.rect.x,self.rect.y
            
        

pygame.init()



fenetre=pygame.display.set_mode((450,450),RESIZABLE)
image_fond = "images/fond.jpg"

text="laby.txt"

elem=Elem()
elem.extract_elem(text)
depart=Depart()
##mur=Mur()
arrivee=Arrivee()
obj=Objets()

img_macgyver="images/macgyver.png"
macgyver=Perso(img_macgyver)

fond=pygame.image.load(image_fond).convert()

murSprite=list()

for i,o in enumerate(elem.mur):
        murSprite.append(Mur(i,elem.mur))


murGroupSprite=pygame.sprite.Group(murSprite)




fenetre.blit(fond,(0,0))
position_obj=[]
for o in obj.list_image:
        pos=random.choice(elem.couloir)
        fenetre.blit(o,pos)
        position_obj.append(pos)
pygame.display.flip()

while 1:

        for elmt in elem.depart:
            fenetre.blit(depart.image,elmt)
        

##        for elmt in elem.mur:
##            fenetre.blit(mur.image,elmt)

        for elmt in elem.arrivee:
            fenetre.blit(arrivee.image,elmt)
        
        fenetre.blit(macgyver.image,(macgyver.rect.x,macgyver.rect.y))
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
           
        fenetre.blit(fond,(0,0))            

        for elmt in elem.depart:
            fenetre.blit(depart.image,elmt)
        

##       for elmt in elem.mur:
            ##fenetre.blit(mur.image,elmt)

        for elmt in elem.arrivee:
            fenetre.blit(arrivee.image,elmt)
        
        for i,o in enumerate(obj.list_image):
                fenetre.blit(o,position_obj[i])
                
        fenetre.blit(macgyver.image,(macgyver.rect.x,macgyver.rect.y))
        pygame.display.flip()
