import pygame
import json
import math
import Main
import Buttons

class Pet :
    """The Virtual Pet
    
    Args:
        LARGEUR_PET : dimension du pet en x
        HAUTEUR_PET : dimension du pet en y
        name : nom du pet
        rect (Rect) : rectangle dans lequelle le pet est dessine
        Stats :
            hunger : niveau de faim, min 0, max 100
            energy : niveau d'energie, min 0, max 100
            happiness : niveau de joie, min 0, max 100
        buttons : les boutons pour agir sur le pet
        age : age du pet, min 0
        is_dying : si le pet est sur le point de mourir, boolean
        is_sick : si le pet est malade, boolean
        
    """
    def __init__(self, name, x=Main.LARGUEUR_FENETRE/2, y=Main.HAUTEUR_FENETRE/2, hunger=50, energy=50, happiness=50, age=0, is_dying=False, is_sick=False):
        if (age<18) :
            self.LARGEUR_PET = 100
            self.HAUTEUR_PET = 150
        else :
            self.LARGEUR_PET = 140
            self.HAUTEUR_PET = 210
        self.name = name
        self.rect = pygame.Rect(x, y, self.LARGEUR_PET, self.HAUTEUR_PET)
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.Stats = [self.hunger, self.energy, self.happiness]
        self.buttons = Buttons.Buttons(self)
        self.age = age
        self.is_dying=is_dying
        self.is_sick=is_sick
    
    def draw(self, window, x, y):
        """dessiner le pet dans la fenetre window au coordonnees x,y

        Args:
            window (Surface): la fenetre ou dessiner le pet
            x (int): coordonnee x d'ou dessiner le pet
            y (int): coordonnee y d'ou dessiner le pet
        """
        if (self.age<18) :
            self.LARGEUR_PET = 100
            self.HAUTEUR_PET = 150
        else :
            self.LARGEUR_PET = 140
            self.HAUTEUR_PET = 210
        self.rect = pygame.Rect(x, y, self.LARGEUR_PET, self.HAUTEUR_PET)
        #HEAD
        pygame.draw.circle(window, pygame.Color('lavender'),(x+self.LARGEUR_PET/2,y+self.HAUTEUR_PET/6),(self.LARGEUR_PET/4))
        pygame.draw.circle(window, pygame.Color('black'), (x+self.LARGEUR_PET/4+self.LARGEUR_PET/2/3,y+self.HAUTEUR_PET/3/3),2)
        pygame.draw.circle(window, pygame.Color('black'), (x+self.LARGEUR_PET/4+self.LARGEUR_PET/2*2/3,y+self.HAUTEUR_PET/3/3),2)
        #si mourant ou malade = frown, sinon smile
        if self.is_dying or self.is_sick :
            pygame.draw.arc(window, pygame.Color('black'), ((x+self.LARGEUR_PET/4+self.LARGEUR_PET/2/4,y+self.HAUTEUR_PET/3*2/3),(self.LARGEUR_PET/2/2,self.HAUTEUR_PET/3/2)),math.pi/6,5*math.pi/6,2)
        else :
            pygame.draw.arc(window, pygame.Color('black'), ((x+self.LARGEUR_PET/4+self.LARGEUR_PET/2/4,y+self.HAUTEUR_PET/3/4),(self.LARGEUR_PET/2/2,self.HAUTEUR_PET/3/2)),-5*math.pi/6,-math.pi/6,2)
        #BODY
        pygame.draw.polygon(window, pygame.Color('skyblue'),((x,y+self.HAUTEUR_PET/3),(x+self.LARGEUR_PET, y+self.HAUTEUR_PET/3),(x+self.LARGEUR_PET/2, y+self.HAUTEUR_PET*2/3)))
        pygame.draw.polygon(window, pygame.Color('skyblue'),((x,y+self.HAUTEUR_PET),(x+self.LARGEUR_PET, y+self.HAUTEUR_PET),(x+self.LARGEUR_PET/2, y+self.HAUTEUR_PET*2/3)))
        
    def draw_stats(self, window):
        """dessine les statistiques du pet dans la fenetre window

        Args:
            window (Surface): fenetre ou le pet est dessine
        """
        #write out stats
        hunger_text = "Hunger : "+str(round(self.hunger,2))+"/100"
        hunger_render = Main.FONT.render(hunger_text, True, pygame.Color('black'))
        energy_text = "Energy : "+str(round(self.energy,2))+"/100"
        energy_render = Main.FONT.render(energy_text, True, pygame.Color('black'))
        happiness_text = "Happiness : "+str(round(self.happiness,2))+"/100"
        happiness_render = Main.FONT.render(happiness_text, True, pygame.Color('black'))
        #draw bars and stat text
        Stats_Text = [[hunger_text, hunger_render, self.hunger], [energy_text, energy_render, self.energy], [happiness_text, happiness_render, self.happiness]]
        for i,stat_text in enumerate(Stats_Text):
            #dessine la bar vide
            pygame.draw.rect(window, pygame.Color('grey30'), pygame.Rect(50, 50+i*(45), Main.LARGUEUR_FENETRE-100, 40))
            #met en rouge la barre si on est a 10 points de la mort
            if (("Hunger" not in stat_text[0]) and stat_text[2]<=10) or (("Hunger" in stat_text[0]) and stat_text[2]>=90): 
                pygame.draw.rect(window, pygame.Color('red'), pygame.Rect(50, 50+i*(45), (Main.LARGUEUR_FENETRE-100)*stat_text[2]/100, 40))
            else : pygame.draw.rect(window, pygame.Color('lightgreen'), pygame.Rect(50, 50+i*(45), (Main.LARGUEUR_FENETRE-100)*stat_text[2]/100, 40))
            window.blit(stat_text[1], (55, 55+i*(45)))
            
    def draw_effects(self, window):
        """ecris l'age et si le pet est malade ou mourant sous les stats

        Args:
            window (Surface): fenetre ou le pet est dessine
        """
        #ecris et affiche l'age a droit au dessus des effets
        age_text = "Age : "+str(math.floor(self.age))
        age_render = Main.FONT.render(age_text, True, pygame.Color('white'))
        window.blit(age_render, (Main.LARGUEUR_FENETRE-300, 205))
        #ecris et affiche si malade/mourant a droite en dessous de l'age
        if self.is_dying : effect_text=self.name+" is dying!!"
        elif self.is_sick : effect_text=self.name+" is sick!"
        else : effect_text=self.name+" is healthy"
        if "healthy" in effect_text : text_color=pygame.Color('lightgreen')
        else : text_color=pygame.Color('red')
        effect_render = Main.FONT.render(effect_text, True, text_color)
        window.blit(effect_render, (Main.LARGUEUR_FENETRE-300, 250))
    
    ###actions qu'on peut appliquer sur le pet###
    def feed(self) :
        self.hunger = max(0, self.hunger-10)
        
    def play(self) :
        self.happiness = min(100, self.happiness+10)
        self.energy= max(0, self.energy-10)
    
    def sleep(self) :
        self.energy = min(100, self.energy+20)
        self.age += 1
        
    def bathe(self) :
        self.happiness = min(100, self.happiness+15)
        
    def visit_vet(self) :
        self.hunger = max(0, self.hunger-5)
        self.energy = min(100, self.energy+5)
        self.is_sick = False
        
    def pet(self) :
        self.happiness = min(100, self.happiness+5)
    ###
        
    def time_passes(self) :
        """effet du temps sur les stats du pet, pire s'il est malade
        """
        if self.is_sick :
            self.hunger = min(100, self.hunger+0.003)
            self.energy = max(0, self.energy-0.005)
            self.happiness = max(0, self.happiness-0.003)
        else :
            self.hunger = min(100, self.hunger+0.002)
            self.energy = max(0, self.energy-0.002)
            self.happiness = max(0, self.happiness-0.001)
        self.age += (1/60/60) #+1 age a chaque minute
        #verifie que le pet n'est pas mort
        if self.hunger>=100 : raise Main.Death("starvation")
        elif self.energy<=0 : raise Main.Death("tiredness")
        elif self.happiness<=0 : raise Main.Death("boredom")
        #verifie que le pet n'est pas mourant
        elif self.hunger>=90 or self.energy<=10 or self.happiness<=10 : self.is_dying=True
        else : self.is_dying=False
        
    ###methodes load et save pour enregistrer les donnees du pet entre les sessions de jeux###
    @classmethod
    def load(cls, name):
        try:
            with open(f"{name}_save.json", "r") as file:
                data = json.load(file)
            print("Game loaded!")
            return cls(**data)
        except FileNotFoundError:
            print("Save file not found. Creating a new pet.")
            return None
        
    def save(self):
        data = {
            'name': self.name,
            'hunger': self.hunger,
            'happiness': self.happiness,
            'energy': self.energy,
            'age': self.age,
            'is_dying': self.is_dying,
            'is_sick' : self.is_sick
        }
        with open(f"{self.name}_save.json", "w") as file:
            json.dump(data, file)
        print("Game saved!")
    ###
  