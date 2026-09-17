import pygame
import Main

class Buttons :
    """classe specifique pour les boutons d'actions
    Args :
        BUTTON_SIZE : la taille de tous les boutons
        BUTTON_Y : HAUTEUR A LAQUELLE METTRE LES BOUTONS
        pet : le pet affecter par les actions des boutons
        feed_button_zone : rectangle dans lequelle se trouve le boutton "Feed"
        play_button_zone : rectangle dans lequelle se trouve le boutton "Play"
        sleep_button_zone : rectangle dans lequelle se trouve le boutton "Sleep"
        bathe_button_zone : rectangle dans lequelle se trouve le boutton "Bathe"
        visit_vet_button_zone : rectangle dans lequelle se trouve le boutton "Visit Vet"
        save_button_zone : rectangle dans lequelle se trouve le boutton "Save Game"
    """
    def __init__(self, pet):
        self.BUTTON_SIZE= [200, 50]
        self.BUTTON_Y = Main.HAUTEUR_FENETRE-100
        self.pet=pet
        self.feed_button_zone = pygame.Rect(25, self.BUTTON_Y, self.BUTTON_SIZE[0], self.BUTTON_SIZE[1])
        self.play_button_zone = pygame.Rect(275, self.BUTTON_Y, self.BUTTON_SIZE[0], self.BUTTON_SIZE[1])
        self.sleep_button_zone = pygame.Rect(500, self.BUTTON_Y, self.BUTTON_SIZE[0], self.BUTTON_SIZE[1])
        self.bathe_button_zone = pygame.Rect(725, self.BUTTON_Y, self.BUTTON_SIZE[0], self.BUTTON_SIZE[1])
        self.visit_vet_button_zone = pygame.Rect(950, self.BUTTON_Y, self.BUTTON_SIZE[0], self.BUTTON_SIZE[1])
        self.save_button_zone = pygame.Rect(50, 205, self.BUTTON_SIZE[0], self.BUTTON_SIZE[1])
        
    def draw_buttons(self, window):
        """dessine les boutons pour interagir avec le pet

        Args:
            window (Surface): fenetre dans laquelle se trouve le pet
        """
        #FEED BUTTON
        pygame.draw.rect(window, pygame.Color('greenyellow'), self.feed_button_zone)
        feed_text=Main.FONT.render('Feed', True, pygame.Color('black'))
        window.blit(feed_text, (self.feed_button_zone.x+75, self.feed_button_zone.y+15))
        #PLAY BUTTON
        pygame.draw.rect(window, pygame.Color('orange'), self.play_button_zone)
        play_text=Main.FONT.render('Play', True, pygame.Color('black'))
        window.blit(play_text, (self.play_button_zone.x+75, self.play_button_zone.y+15))
        #SLEEP BUTTON
        pygame.draw.rect(window, pygame.Color('navy'), self.sleep_button_zone)
        sleep_text=Main.FONT.render('Sleep', True, pygame.Color('white'))
        window.blit(sleep_text, (self.sleep_button_zone.x+75, self.sleep_button_zone.y+15))
        #BATHE BUTTON
        pygame.draw.rect(window, pygame.Color('turquoise1'), self.bathe_button_zone)
        bathe_text=Main.FONT.render('Bathe', True, pygame.Color('black'))
        window.blit(bathe_text, (self.bathe_button_zone.x+75, self.bathe_button_zone.y+15))
        #VISIT_VET BUTTON
        pygame.draw.rect(window, pygame.Color('firebrick'), self.visit_vet_button_zone)
        visit_vet_text=Main.FONT.render('Visit Vet', True, pygame.Color('white'))
        window.blit(visit_vet_text, (self.visit_vet_button_zone.x+50, self.visit_vet_button_zone.y+15))
        #SAVE BUTTON
        pygame.draw.rect(window, pygame.Color('darkgreen'), self.save_button_zone)
        save_text=Main.FONT.render('Save Game', True, pygame.Color('white'))
        window.blit(save_text, (self.save_button_zone.x+50, self.save_button_zone.y+15))
        
    def touche(self, x, y) :
        """verifie si un bouton (ou le pet) est toucher, puis applique l'effet du bouton sur le pet

        Args:
            x (int): coordonnee x de la souris au moment du clic
            y (int): coordonnee y de la souris au moment du clic
        """
        worked = True
        if self.feed_button_zone.collidepoint(x,y) : self.pet.feed()
        elif self.play_button_zone.collidepoint(x,y) : self.pet.play()
        elif self.sleep_button_zone.collidepoint(x,y) : self.pet.sleep()
        elif self.bathe_button_zone.collidepoint(x,y) : self.pet.bathe()
        elif self.visit_vet_button_zone.collidepoint(x,y) : self.pet.visit_vet()
        elif self.pet.rect.collidepoint(x,y) : self.pet.pet()
        elif self.save_button_zone.collidepoint(x,y) : self.pet.save()
        else : worked=False
        return worked
