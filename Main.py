import pygame
import random
import Pet

pygame.init()
LARGUEUR_FENETRE = 1200
HAUTEUR_FENETRE = 1000
fenetre = pygame.display.set_mode((LARGUEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption('Virtual Pet')
FONT=pygame.font.Font(None, 32)
horloge = pygame.time.Clock()

class Death(Exception):
    """exception to call if pet dies

    Args:
        cause (str): cause of death
    """
    def __init__(self, cause):
        self.cause=cause

def main() :
    
    #essaye de loader un pet existant sinon en cree un nouveau
    pet_name = input("What is your pet's name? ")
    pet1 = Pet.Pet.load(pet_name)
    if pet1==None : pet1=Pet.Pet(pet_name)

    fin = False
    while not fin :
        event = pygame.event.poll()
        if event.type == pygame.QUIT :
            fin = True #ferme le jeux quand on quitte
        else :
            #verifie si un bouton est clique, applique son effet
            if event.type == pygame.MOUSEBUTTONUP : pet1.buttons.touche(event.pos[0], event.pos[1])
            try :
                #applique le passage du temp
                pet1.time_passes()
                fenetre.fill(pygame.Color('grey10'))
            except Death as death : #si le pet est mort, on indique la fin du jeu
                pygame.draw.rect(fenetre, pygame.Color('red'), pet1.rect)
                text = FONT.render(pet1.name+" died of "+death.cause+"!! Please close the game :(", True, pygame.Color('red'))
                fenetre.blit(text, [200, 500])
            else : #si le pet est encore en vie, on redessine tout!
                #deplacement aleatoire du pet, 10% de chance de se deplacer de max 25 pixel a gauche ou a droite a tous les ticks
                if random.randrange(0, 10, 1)==1 : 
                    new_x = pet1.rect.x+random.randrange(-25,25,1)
                    if new_x<LARGUEUR_FENETRE-pet1.LARGEUR_PET and new_x>=0 : pet1.rect.x=new_x
                #0.5% de chance de tomber malade par sec
                if random.randrange(0, 1200, 1)==1 : pet1.is_sick=True
                #dessine les objets dans la fenetre
                pet1.draw(fenetre, pet1.rect.x, pet1.rect.y)
                pet1.draw_stats(fenetre)
                pet1.draw_effects(fenetre)
                pet1.buttons.draw_buttons(fenetre)
            #met a jour le display
            pygame.display.flip()
            horloge.tick(60) #60 ticks/frames par seconde

    pygame.quit()
    
if __name__ == "__main__":
    main()