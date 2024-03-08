# -*- coding: utf-8 -*-

import random



#Fonction d'affichage des grilles
def afficher_jeu(grille_debut,grille_mileu,grille_fin):
    
    print("Grille de debut de partie: (1)")
    print("  ","   ".join(LetterList))
    for i in range(len(grille_debut)):
        print(NumList[i], end= '  ')
        
        print(" | ".join(grille_debut[i]))
        print("  ---+---+---+---+---+---+---")


    print("Grille de mileu de partie: (2)")
    print("  ","   ".join(LetterList))
    for i in range(len(grille_mileu)):
        print(NumList[i], end= '  ')
        
        print(" | ".join(grille_mileu[i]))
        print("  ---+---+---+---+---+---+---")


    print("Grille de fin de partie: (3)")
    print("  ","   ".join(LetterList))
    for i in range(len(grille_fin)):
        print(NumList[i], end= '  ')
        
        print(" | ".join(grille_fin[i]))
        print("  ---+---+---+---+---+---+---")        
    
    return 'Grilles de tests'




#a partir de 3 grille, on affiche que la grille choisi par le joueur
def choix_grille(grille):
    print("  ","   ".join(LetterList))
    for i in range(len(grille)):
        print(NumList[i], end= '  ')
        
        print(" | ".join(grille[i]))
        print("  ---+---+---+---+---+---+---")
    return grille    

#Fonction de test
def test_choix_grille():

    assert choix_grille(grille_debut_test)==grille_debut_test, 'Erreur de choix de grille'
    assert choix_grille(grille_mileu_test)==grille_mileu_test, 'Erreur de choix de grille'
    assert choix_grille(grille_fin_test)==grille_fin_test, 'Erreur de choix de grille'
    


#fonction qui compte a chaque tour le nombre de pions dans la grille,
#on utilise cette fonction pour definir la condition de fin de programme
def nb_pions(grille):
    pionX=0
    pionO=0
    for ligne in grille:
        for pion in ligne:
            if pion == "x":
                pionX += 1
            elif pion == "o":
                pionO += 1
    print("Pions du joueur X:", pionX, "Pions du joueur O:",pionO)
    if pionX==0 or pionO==0:
        return False
    else:
        return True


#Fonction de test
def test_nb_pion():
    assert nb_pions(grille_debut_test)==True, 'Erreur nombre de pions'
    assert nb_pions(grille_mileu_test)==True, 'Erreur nombre de pions'
    assert nb_pions(grille_fin_test)==True, 'Erreur nombre de pions'




#fonction qui print le tour du joueur
def tour_du_joueur(tour):
    #if tour=1 => tour de x ; else tour de o
    if tour==1:
        print('Tour du joueur X')
    else:
        print('Tour du joueur O')
      




      
#Fonction de verification de format de choix de pion
def est_au_bon_format(colonne,ligne):
    print('Selectionner votre pion: ')
    colonne=input('Colonne= ') #input de colonne te de ligne
    ligne= input('Ligne= ')
    message=colonne+ligne #combinaison de chaine de caractère dans un message
    while est_dans_grille(colonne,ligne)==False or pion_choisi(grille,message)==False: #Boucle d'erreur
        print("Format non valide! Choisir un pion: \n")
        print('Choisir un pion: ')
        colonne=input('Colonne= ') #re-saisi
        ligne= input('Ligne= ')
        message=colonne+ligne
    print('Format valide!\n')
    return message  










#Fonction de verification de format de (deplacement)
def est_au_bon_format2(DepColonne,DepLigne):
    print("Deplacement: \n Sélectionnez vos cordonné d'arriver:  ")
    DepColonne=input('Colonne= ') #input de colonne et ligne de deplacement
    DepLigne= input('Ligne= ')
    DepMessage=DepColonne+DepLigne #Message de deplacement
    format=False #validiter de format
    while est_dans_grille(DepColonne,DepLigne)==False: #boucle d'erreur
        print("Format non valide!  \n")
        print("Deplacement: \n Sélectionnez vos cordonné d'arriver:  ")
        DepColonne=input('Colonne= ') #re-saisi
        DepLigne= input('Ligne= ') 
        DepMessage=DepColonne+DepLigne
    print('Format valide!\n')
    format=True
    return format,DepMessage  




  

    


  
   
#Fonction de verifications des coordonnées
def est_dans_grille(colonne,ligne): 
    colonne_valide=False
    ligne_valide=False 
    #recherche de ligne et colonne choisi
    if len(colonne+ligne)>2:
        return False  
    for i in LetterList: #parcourir les colonnes
        if i==colonne:
            colonne_valide=True

    for i in NumList:
        if i==ligne: #parcourir les lignes
            ligne_valide=True 

    if colonne_valide==False or ligne_valide==False:  #si la saisi de colonne ou ligne n'appatient pas au grille    
        return False
    return True
    




  

#Fonction de test de format
def test_est_dans_grille():
    assert est_dans_grille('', '') == False, "erreur coordonnee vide"
    assert est_dans_grille(('G'),('10')) == False, "erreur de test"
    assert est_dans_grille(('C'),('K')) == False, "erreur de test"
    assert est_dans_grille(('8') ,('82')) == False, "erreur de test"
    assert est_dans_grille(('3'),('a')) == False, "erreur majuscule"
    assert est_dans_grille(('ddzasd'),('é"&')) == False, "erreur de test"








#verification du pion choisi ou si la case est vide
def pion_choisi(grille,message):

    if grille[int(message[1])-1][alphabet.index(message[0])]==' ': #Si les coordonnées sont vides
        print("Coordonnées vide!")
    elif grille[int(message[1])-1][alphabet.index(message[0])]=='x': #Si les coordonnées choisi sont occupées
        #verification de pion selectionner
        if tour==1: #tour de x
            return True
    else:
        if tour==0: #tour de o
            return True
    return False
          
    
#Fonction de test
def test_pion_choisi():
    assert pion_choisi(grille_mileu_test,('A1'))==False, 'Message invalide'
    assert pion_choisi(grille_mileu_test,('F3'))==True, 'Message invalide'
    assert pion_choisi(grille_debut_test,('D4'))==False, 'Message invalide'
    assert pion_choisi(grille_fin_test,('E2'))==True, 'Message invalide'
    assert pion_choisi(grille_fin_test,('A2'))==False, 'Message invalide'






#Fonction qui verifie la possibilité de captuer un pion au sud
def ordi_capture_sud(ligne, colonne, grille,joueur_enemie,taille):
    if ligne < taille - 2: # condition pour ne pas sortir de la grille
        if grille[ligne + 1][colonne] == joueur_enemie and grille[ligne + 2][colonne] == " ": #si il est possible de capturer un enemie
            return True
    return False        



#Fonction de test
def test_ordi_capture_sud():
    assert ordi_capture_sud(2,4, grille_mileu_test,'x',len(grille_mileu_test))==True, 'Erreur capture'
    assert ordi_capture_sud(4,4, grille_fin_test,'x',len(grille_fin_test))==False, 'Erreur capture'    
    assert ordi_capture_sud(2,5, grille_mileu_test,'o',len(grille_mileu_test))==False, 'Erreur capture'
    assert ordi_capture_sud(4,5, grille_debut_test,'o',len(grille_debut_test))==False, 'Erreur capture'






#Fonction qui verifie la possibilité de captuer un pion au nord
def ordi_capture_nord(ligne, colonne, grille,joueur_enemie):
    if ligne > 1:
        if grille[ligne - 1][colonne] == joueur_enemie and grille[ligne - 2][colonne] == " ":
            return True
    return False        



#Fonction de test
def test_ordi_capture_nord():
    assert ordi_capture_nord(3,4, grille_mileu_test,'o')==True, 'Erreur capture'
    assert ordi_capture_nord(5,4, grille_fin_test,'o')==True, 'Erreur capture'    
    assert ordi_capture_nord(2,5, grille_mileu_test,'o')==False, 'Erreur capture'
    assert ordi_capture_nord(4,5, grille_debut_test,'o')==False, 'Erreur capture'






#Fonction qui verifie la possibilité de captuer un pion au est
def ordi_capture_est(ligne, colonne, grille,joueur_enemie,taille):
    if colonne < taille - 2:
        if grille[ligne][colonne + 1] == joueur_enemie and grille[ligne][colonne + 2] == " ":
            return True
    return False            




#Fonction de test
def test_ordi_capture_est():
    assert ordi_capture_est(2,4, grille_mileu_test,'x',len(grille_mileu_test))==True, 'Erreur capture'
    assert ordi_capture_est(4,1, grille_mileu_test,'x',len(grille_mileu_test))==True, 'Erreur capture'    
    assert ordi_capture_est(2,4, grille_fin_test,'o',len(grille_fin_test))==False, 'Erreur capture'
    assert ordi_capture_est(4,5, grille_debut_test,'o',len(grille_debut_test))==False, 'Erreur capture'






#Fonction qui verifie la possibilité de captuer un pion au ouest
def ordi_capture_ouest(ligne, colonne, grille,joueur_enemie):
    if colonne > 1:
        if grille[ligne][colonne - 1] == joueur_enemie and grille[ligne][colonne - 2] == " ":
            return True
    return False 




#Fonction de test
def test_ordi_capture_ouest():
    assert ordi_capture_ouest(4,2, grille_mileu_test,'o')==True, 'Erreur capture'
    assert ordi_capture_ouest(2,5, grille_mileu_test,'o')==True, 'Erreur capture'    
    assert ordi_capture_ouest(2,3, grille_fin_test,'o')==False, 'Erreur capture'
    assert ordi_capture_ouest(1,4, grille_debut_test,'o')==False, 'Erreur capture'







#Fonction qui verifie la possibilité de captuer un pion au nord ouest
def ordi_capture_nord_ouest(ligne, colonne, grille,joueur_enemie):
    if ligne > 1 and colonne > 1:
        if grille[ligne - 1][colonne - 1] == joueur_enemie and grille[ligne - 2][colonne - 2] == " ":
            return True
    return False            




#Fonction de test
def test_ordi_capture_nord_ouest():
    assert ordi_capture_nord_ouest(4,1, grille_mileu_test,'o')==False, 'Erreur capture'
    assert ordi_capture_nord_ouest(2,5, grille_mileu_test,'o')==False, 'Erreur capture'    
    assert ordi_capture_nord_ouest(2,4, grille_fin_test,'o')==False, 'Erreur capture'
    assert ordi_capture_nord_ouest(4,5, grille_debut_test,'o')==False, 'Erreur capture'







#Fonction qui verifie la possibilité de captuer un pion au nord est
def ordi_capture_nord_est(ligne, colonne, grille,joueur_enemie,taille):
    if ligne > 1 and colonne < taille - 2:
        if grille[ligne - 1][colonne + 1] == joueur_enemie and grille[ligne - 2][colonne + 2] == " ":
            return True
    return False       




#Fonction de test
def test_ordi_capture_nord_est():
    assert ordi_capture_nord_est(4,1, grille_mileu_test,'o',len(grille_mileu_test))==False, 'Erreur capture'
    assert ordi_capture_nord_est(2,5, grille_mileu_test,'o',len(grille_mileu_test))==False, 'Erreur capture'    
    assert ordi_capture_nord_est(2,3, grille_fin_test,'x',len(grille_fin_test))==True, 'Erreur capture'
    assert ordi_capture_nord_est(4,5, grille_debut_test,'o',len(grille_debut_test))==False, 'Erreur capture'






#Fonction qui verifie la possibilité de captuer un pion au sud ouest
def ordi_capture_sud_ouest(ligne, colonne, grille,joueur_enemie,taille):
    if ligne < taille - 2 and colonne > 1:
        if grille[ligne + 1][colonne - 1] == joueur_enemie and grille[ligne + 2][colonne - 2] == " ": 
            return True
    return False       


#Fonction de test
def test_ordi_capture_sud_ouest():
    assert ordi_capture_sud_ouest(1,4, grille_fin_test,'o',len(grille_fin_test))==True, 'Erreur capture'
    assert ordi_capture_sud_ouest(2,5, grille_mileu_test,'o',len(grille_mileu_test))==False, 'Erreur capture'
    assert ordi_capture_sud_ouest(4,5, grille_debut_test,'o',len(grille_debut_test))==False, 'Erreur capture'
    





#Fonction qui verifie la possibilité de captuer un pion au sud est
def ordi_capture_sud_est(ligne, colonne, grille,joueur_enemie,taille):
    if colonne < taille - 2 and ligne < taille - 2:
        if grille[ligne + 1][colonne + 1] == joueur_enemie and grille[ligne + 2][colonne + 2] == " ": 
            return True
    return False     



 #Fonction de test
def test_ordi_capture_sud_est():
    assert ordi_capture_sud_est(4,1, grille_mileu_test,'o',len(grille_mileu_test))==False, 'Erreur capture'
    assert ordi_capture_sud_est(2,5, grille_mileu_test,'o',len(grille_mileu_test))==False, 'Erreur capture'    
    assert ordi_capture_sud_est(2,4, grille_fin_test,'o',len(grille_fin_test))==False, 'Erreur capture'
    assert ordi_capture_sud_est(4,5, grille_debut_test,'o',len(grille_debut_test))==False, 'Erreur capture'






#Fonction qui calcule si l'ordinateur peut capturer avec un pion
def attaque_possibles_ordinateur(ligne, colonne, grille, taille):
    NbMouvements=0
    mouvements=[]
    joueur_enemie='x'
    capture=False
    if ordi_capture_sud(ligne, colonne, grille,joueur_enemie,taille)==True:
        mouvements+= [[ligne + 2, colonne]] #on ajoute ce mouvement dans la liste des mouvements possibles
        NbMouvements+=1
        capture=True #Capture enemie sud
  
    if ordi_capture_nord(ligne, colonne, grille,joueur_enemie)==True:
        mouvements+= [[ligne - 2, colonne]]
        NbMouvements+=1
        capture=True #Capture enemie nord


    if ordi_capture_est(ligne, colonne, grille,joueur_enemie,taille)==True:
        mouvements+= [[ligne, colonne + 2]]
        NbMouvements+=1
        capture=True #Capture enemie est


    if ordi_capture_ouest(ligne, colonne, grille,joueur_enemie)==True:
        mouvements+= [[ligne, colonne - 2]]
        NbMouvements+=1
        capture=True #Capture enemie ouest


    if ordi_capture_nord_ouest(ligne, colonne, grille,joueur_enemie)==True:
        mouvements+= [[ligne - 2, colonne - 2]]
        NbMouvements+=1
        capture=True #Capture enemie nord ouest


    if ordi_capture_nord_est(ligne, colonne, grille,joueur_enemie,taille)==True:
        mouvements+= [[ligne - 2, colonne + 2]]
        NbMouvements+=1
        capture=True #Capture enemie nord est


    if ordi_capture_sud_ouest(ligne, colonne, grille,joueur_enemie,taille)==True:
        mouvements+= [[ligne + 2, colonne - 2]] 
        NbMouvements+=1
        capture=True #Capture enemie sud ouest


    if ordi_capture_sud_est(ligne, colonne, grille,joueur_enemie,taille)==True:
        mouvements+= [[ligne + 2, colonne + 2]] 
        NbMouvements+=1
        capture=True #Capture enemie sud est
    return NbMouvements,mouvements,capture
      
    
    
#Fonction de test
def test_attaque_possibles_ordinateur():
    assert attaque_possibles_ordinateur(4,4, grille_fin_test, len(grille_fin_test))==(0,[],False), 'Erreur attaque possible AI'
    assert attaque_possibles_ordinateur(2,2, grille_mileu_test, len(grille_mileu_test))==(0,[],False), 'Erreur attaque possible AI'
    assert attaque_possibles_ordinateur(1,1, grille_debut_test, len(grille_debut_test))==(0,[],False), 'Erreur attaque possible AI'
    assert attaque_possibles_ordinateur(3,1, grille_debut_test, len(grille_debut_test))==(0,[],False), 'Erreur attaque possible AI'
    
    




#Mouvements simples possible pour l'ordinateur
def mouvements_possibles_ordinateur(ligne, colonne, grille, taille):
    NbMouvements=0
    mouvements=[]  

    if colonne < taille - 2 and grille[ligne][colonne + 1] == ' ': # si la case à côté est vide
            mouvements += [[ligne, colonne + 1]] #on ajoute ces coordonnées dans une liste mouvement
            NbMouvements+=1 #compteur de mouvements possibles
    if colonne > 0 and grille[ligne][colonne - 1] == ' ': #si la case à gauche est vide
            mouvements+= [[ligne, colonne - 1]] 
            NbMouvements+=1
    if ligne < taille - 1 and grille[ligne + 1][colonne] == ' ': #si la case au dessus est vide
            mouvements+= [[ligne + 1, colonne]]
            NbMouvements+=1
    if ligne > 0 and grille[ligne - 1][colonne] == ' ': #si la case au dessous est vide
            mouvements+= [[ligne - 1, colonne]]
            NbMouvements+=1
    

    return NbMouvements,mouvements



#Fonction de test
def test_mouvements_possibles_ordinateur():
    assert mouvements_possibles_ordinateur(1,1, grille_debut_test,len(grille_debut_test))==(0,[]), 'Erreur deplacement simple AI'
    assert mouvements_possibles_ordinateur(2,2, grille_debut_test,len(grille_debut_test))==(0,[]), 'Erreur deplacement simple AI'







#Fonction qui effectue les déplacements de l'ordinateur
def deplacement_ordinateur_avancée(grille,taille):
    mouvements_total=[]
    #Parcourir les possiblités de captures
    for ligne in range(len(grille)):
        for colonne in range(len(grille)): #parcours de grille
            if grille[ligne][colonne]=="o":
                #priorité pour captuer (l'ordinateur ne considère que les mouvements de capture possible)
                NbMouvements,mouvements,capture=attaque_possibles_ordinateur(ligne,colonne,grille,taille)
                for pion in range(NbMouvements):
                    mouvements_total+=[[ligne,colonne]+mouvements[pion]]

    if mouvements_total!=[]: # Si la liste d'attaque n'est pas vide
        #Choix aléatoire entre les mouvements possibles
        random_choice=mouvements_total[random.randint(0, len(mouvements_total)-1)] 
        #On sauvegarde les deplacements aléatoire choisi par l'ordianteur
        ligne1=random_choice[0]
        colonne1=random_choice[1]
        ligne2=random_choice[2]
        colonne2=random_choice[3]     
        #On met nos coordonnées aléatoires comme paramètre dans la fonction qui va effectuer le déplacement
        grille=tour_ordinateur_saut(ligne1,colonne1,ligne2,colonne2,grille)
        #Tant que enchainement possible --> executer l'enchainement
        while enchainement_ordinateur_possible(ligne2,colonne2)==True:            
            grille,ligne2,colonne2=execution_echainement_ordinateur(grille,ligne2,colonne2)
        return grille,ligne2,colonne2  #retourne l'etat final de la grille
      
    else: #sinon on effectue un deplacement simple
        #Parcourir les possibilité de déplacements simples
        for ligne in range(len(grille)):
            for colonne in range(len(grille)): #parcours de grille
                if grille[ligne][colonne]=="o":
                      NbMouvements,mouvements=mouvements_possibles_ordinateur(ligne,colonne,grille,taille) #mouvement simple
                for pion in range(NbMouvements): #parcourir la liste de mouvement
                        mouvements_total+=[[ligne,colonne]+mouvements[pion]] #ajouter ces mouvements à la liste total de mouvements

        #choix aléatoire entre les mouvements possibles
        random_choice=mouvements_total[random.randint(0, len(mouvements_total)-1)]
        #On sauvegarde les deplacements aléatoire choisi par l'ordianteur
        ligne1=random_choice[0]
        colonne1=random_choice[1]
        ligne2=random_choice[2]
        colonne2=random_choice[3]   
        #On met nos coordonnées aléatoires comme paramètre dans la fonction qui va effectuer le déplacement
        grille=tour_ordinateur_simple(random_choice[0],random_choice[1],random_choice[2],random_choice[3],grille) 
        return grille,ligne2,colonne2 #retourne l'etat final de la grille






#Fonction qui verifie si l'ordinateur peut effectuer un enchaînement
def enchainement_ordinateur_possible(DepLigne,DepColonne):
    format=False
    if attaque_possibles_ordinateur(DepLigne,DepColonne,grille,taille)!=(0,[],False): #Si il est possible d'effecuter un enchaînement
        format=True  
        return format
    return format






# Fonction qui execute l'enchainement de l'ordinateur
def execution_echainement_ordinateur(grille,DepLigne,DepColonne):
    mouvements_total=[]
    NbMouvements,mouvements,capture=attaque_possibles_ordinateur(DepLigne,DepColonne,grille,taille)
    for pion in range(NbMouvements): #parcourir la liste de mouvement
        mouvements_total+=[[DepLigne,DepColonne]+mouvements[pion]] #ajouter la liste de capture possible
    random_choice=mouvements_total[random.randint(0, len(mouvements_total)-1)]
    grille=tour_ordinateur_saut(random_choice[0],random_choice[1],random_choice[2],random_choice[3],grille)
    ligne2=random_choice[2]
    colonne2=random_choice[3] #sauvgarder les variables pour l'enchainement prochain
    choix_grille(grille) #affiche la grille
    print("L'ordinateur a effectuer un ehcaînement")
    return grille,ligne2,colonne2
    
  


#Fonction qui execute l'affichage d'un mouvement simple
def tour_ordinateur_simple(ligne1, colonne1, ligne2, colonne2, grille):
    grille[int(ligne2)][colonne2]="o" #coordonnées d'arrivée du pion
    grille[int(ligne1)][colonne1]=' ' #coorodnnées initiale du pion
    return grille





#Fonction qui execute l'affichage d'un mouvement de capture
def tour_ordinateur_saut(ligne1, colonne1, ligne2, colonne2, grille): #prend comme paramètre des deplacements possible aléatoirement
    
    grille[int(ligne2)][colonne2]="o" #coordonnées d'arrivée du pion
    grille[int(ligne1)][colonne1]=' ' #coordonnées initiale du pion
    grille[abs(ligne1+ligne2)//2][abs(colonne2+colonne1)//2]=" " #coordonnées de l'adversaire capturer
    return grille







#fonction de déplacement de type capture  
def deplacement_capture(grille,message):
    format=False      
    format_valide,DepMessage=est_au_bon_format2(LetterList,NumList)
    if format_valide==True and pion_choisi(grille,message)==True:    #si l'entrée est bien saisie
        if attaque_valide(grille,DepMessage,message)==True: #si capture possible
            format=True
            choix_grille(grille) #<-- affichage de la grille
            if nb_pions(grille)==False:
                return format,message
            message=DepMessage #update position enchaînement 
            if enchainement_possible(grille,message)==True: #Fonction qui detecte si il existe des adversaires possible a attaquer
                if choix_enchainement()==True: #<-- demander au joueur si il veut faire un enchainement
                    format=False
                    return format,message #On retourne un format false pour r'appeler cette fonction une autre fois
                else:
                    return format,message #On retourne format qui est True et on passe le tour
            else:
                return format,message  #Si non, on passe le tour sans demander au joueur si il veut faire un enchaînement                          
        else:
            print('Deplacement invalide!')
            return format,message #sinon on retourne false qui appel cette fonction une autre fois pour la re-saisi
            
            
    return format,message #sinon on retourne false



  




#fonction de déplacement simple
def deplacement_simple(grille,message):
    format=False

    if tour==1:
        pion='x'
    else:
        pion='o' #initialisation du tour de pion

    format_valide,DepMessage=est_au_bon_format2(LetterList,NumList) #saisie de deplacement
    if format_valide==True and pion_choisi(grille,message)==True: #evaluation de saisi
        if deplacement_valide(grille,message,DepMessage)==True: #evaluation de deplacement
            grille[int(DepMessage[1])-1][alphabet.index(DepMessage[0])]=pion
            grille[int(message[1])-1][alphabet.index(message[0])]=' ' #affectation du deplacement
            format=True
        else:
            print('Deplacement invalide!')        
    return format







# fonction de choix de type de déplacement
def choix_deplacement(grille,message):
    erreur="Choisir entre 1 et 2!"
    print("Choisir le type de deplacement: \n 1. Déplacer un pion \n 2. Capturer un pion")
    choix=input('deplacement: ')

    while not choix in {"1","2"}: #boucle d'erreur de syntaxe
        print(erreur)
        print("Choisir le type de deplacement: \n 1. Déplacer un pion \n 2. Capturer un pion")
        choix=input('deplacement: ')  

    if choix=="1":
        dep_valide=deplacement_simple(grille,message)
        while dep_valide==False: #boucle d'erreur deplacement simple
            dep_valide= deplacement_simple(grille,message)
            if dep_valide==True:
                choix_grille(grille)
                         

    else:
        capture_valide,message=deplacement_capture(grille,message) 
        while capture_valide==False: #boucle d'erreur deplacement capture
            capture_valide,message=deplacement_capture(grille,message)
    return grille
          











#choisir si on souhaite d'effectuer un enchaînement
def choix_enchainement():
    print(" Voulez vous effectuer un enchaînement ?\n  1. capturer\n  2. passer le tour\n")
    erreur="Choisisez entre 1 ou 2!"
    choix=False

    saisie=input("Choix: ")
    while not saisie in {'1', '2'}: #boucle d'erreur de syntaxe
        print(erreur)
        saisie=input("Choix: ")
    if saisie=='1':
        choix=True
	
    return choix







# fonction qui cherche si on peut effectuer un enchaînement
#si on peut alors on demande au joueur si il veut faire cette enchaînement
def enchainement_possible(grille,message):  
    if tour==1:
        pion_enemie='o'
    else:
        pion_enemie='x'

    if int(message[1])>=2 and alphabet.index(message[0])>=1: # condition pour ne pas sortir de la grille
        if grille[int(message[1])-2][alphabet.index(message[0])-1] == pion_enemie and grille[int(message[1])-3][alphabet.index(message[0])-2] == ' ':  # s'il y a un pion adverse en nord ouest 
            return True  # on peut prendre
              
    if int(message[1])>=2 and alphabet.index(message[0])<=len(alphabet)-2:  # condition pour ne pas sortir de la grille     
        if grille[int(message[1])-2][alphabet.index(message[0])+1] == pion_enemie and grille[int(message[1])-2][alphabet.index(message[0])+2] == ' ':# nord east
            return True  # on peut prendre
            
    if int(message[1])>=2:     # condition pour ne pas sortir de la grille  
        if grille[int(message[1])-2][alphabet.index(message[0])] == pion_enemie and grille[int(message[1])-3][alphabet.index(message[0])] == ' ': #nord
            return True  # on peut prendre
            
    if int(message[1])<=len(grille)-2 and alphabet.index(message[0])<=len(alphabet)-2: # condition pour ne pas sortir de la grille   
        if grille[int(message[1])][alphabet.index(message[0])+1] == pion_enemie and grille[int(message[1])+1][alphabet.index(message[0])+2] == ' ': #sud east
            return True  # on peut prendre
              
    if int(message[1])<len(grille)-2: # condition pour ne pas sortir de la grille 
        if grille[int(message[1])][alphabet.index(message[0])] == pion_enemie and grille[int(message[1])+1][alphabet.index(message[0])] == ' ': #sud
            return True  # on peut prendre
            
    if int(message[1])<=len(grille)-2 and alphabet.index(message[0])>=2: # condition pour ne pas sortir de la grille     
        if grille[int(message[1])][alphabet.index(message[0])-1] == pion_enemie and grille[int(message[1])+1][alphabet.index(message[0])-2] == ' ': #sud ouest
            return True  # on peut prendre                
            
    if alphabet.index(message[0])>2:  # condition pour ne pas sortir de la grille    
        if grille[int(message[1])-1][alphabet.index(message[0])-1] == pion_enemie and grille[int(message[1])-1][alphabet.index(message[0])-2] == ' ': #ouest
            return True  # on peut prendre
            
    if alphabet.index(message[0])<len(LetterList)-2:  # condition pour ne pas sortir de la grille     
        if grille[int(message[1])-1][alphabet.index(message[0])+1] == pion_enemie and grille[int(message[1])-1][alphabet.index(message[0])+2] == ' ': #east
            return True  # on peut prendre
    return False            





#fonction de test
def test_enchainement_possible():
    assert enchainement_possible(grille_fin_test,"E4")==True, 'Erreur echainement possible'
    assert enchainement_possible(grille_mileu_test,"D4")==True, 'Erreur echainement possible'
    assert enchainement_possible(grille_fin_test,"A1")==False, 'Erreur echainement possible'
    assert enchainement_possible(grille_debut_test,"A1")==False, 'Erreur echainement possible'
    assert enchainement_possible(grille_debut_test,"D4")==False, 'Erreur echainement possible'
  



  

#fonction qui verifie si un deplacement est valide et retourne un bool
def deplacement_valide(grille,message,DepMessage):
    if grille[int(DepMessage[1])-1][alphabet.index(DepMessage[0])] == ' ':
        if (int(message[1])-2)==(int(DepMessage[1])-1) and [alphabet.index(message[0])-1]==[alphabet.index(DepMessage[0])]:#nord ouest
            return True
        elif  int(message[1])-2==int(DepMessage[1])-1 and [alphabet.index(message[0])+1]==[alphabet.index(DepMessage[0])]:#nord east
            return True
        elif int(message[1])==int(DepMessage[1])-1 and [alphabet.index(message[0])-1]==[alphabet.index(DepMessage[0])]: #sud ouest
            return True
        elif int(message[1])==int(DepMessage[1])-1 and [alphabet.index(message[0])+1]==[alphabet.index(DepMessage[0])]:#sud east
            return True
        elif int(message[1])-2==int(DepMessage[1])-1 and [alphabet.index(message[0])]==[alphabet.index(DepMessage[0])]:#nord
            return True
        elif int(message[1])==int(DepMessage[1])-1 and [alphabet.index(message[0])] ==[alphabet.index(DepMessage[0])]:#sud
            return True
        elif int(message[1])-1==int(DepMessage[1])-1 and [alphabet.index(message[0])-1]==[alphabet.index(DepMessage[0])]:#ouest
            return True    
        elif int(message[1])-1==int(DepMessage[1])-1 and [alphabet.index(message[0])+1]==[alphabet.index(DepMessage[0])]:#east
            return True
    return False






#fonction de test
def test_deplacement_valide():
    assert deplacement_valide(grille_fin_test,'E2','D2')==True, 'Erreur deplacement valide'
    assert deplacement_valide(grille_mileu_test,'F6','D2')==False, 'Erreur deplacement valide'
    assert deplacement_valide(grille_debut_test,'D5','D4')==True, 'Erreur deplacement valide'
    assert deplacement_valide(grille_fin_test,'E7','D6')==True, 'Erreur deplacement valide'


  



  
# Fonction qui verifie la possibilité de capture en nord ouest
def attaque_nord_ouest(grille,message,pion_enemie,pion,ligne,colonne):
    if grille[int(message[1])-2][alphabet.index(message[0])-1] == pion_enemie and grille[int(message[1])-3][alphabet.index(message[0])-2] == ' ':  
        # s'il y a un pion adverse en nord ouest
        if int(message[1])-3==ligne and alphabet.index(message[0])-2== colonne:
            grille[int(message[1])-3][alphabet.index(message[0])-2]=pion
            grille[int(message[1])-2][alphabet.index(message[0])-1]=' '
            grille[int(message[1])-1][alphabet.index(message[0])]=' '
            return True  # on peut prendre    
    return False  





#fonction de test
def test_attaque_nord_ouest():
    assert attaque_nord_ouest(grille_fin_test,'F6','o','x',3,3)==True, 'Erreur capture'
    assert attaque_nord_ouest(grille_fin_test,'E4','o','x',1,2)==True, 'Erreur capture'



  

# Fonction qui verifie la possibilité de capture en nord est
def attaque_nord_est(grille,message,pion_enemie,pion,ligne,colonne):
    if grille[int(message[1])-2][alphabet.index(message[0])+1] == pion_enemie and grille[int(message[1])-2][alphabet.index(message[0])+2] == ' ':
    # nord east
        if int(message[1])-3==ligne and alphabet.index(message[0])+2==colonne:
            grille[int(message[1])-3][alphabet.index(message[0])+2]=pion
            grille[int(message[1])-2][alphabet.index(message[0])+1]=' '
            grille[int(message[1])-1][alphabet.index(message[0])]=' '
            return True  # on peut prendre
    return False  




#fonction de test
def test_attaque_nord_est():
    assert attaque_nord_est(grille_fin_test,'D6','o','x',3,5)==False, 'Erreur capture'
    assert attaque_nord_est(grille_mileu_test,'B4','o','x',1,3)==True, 'Erreur capture'

          


  
# Fonction qui verifie la possibilité de capture en nord
def attaque_nord(grille,message,pion_enemie,pion,ligne,colonne):
    if grille[int(message[1])-2][alphabet.index(message[0])] == pion_enemie and grille[int(message[1])-3][alphabet.index(message[0])] == ' ': 
        #nord
        if int(message[1])-3==ligne and alphabet.index(message[0])==colonne:
            grille[int(message[1])-3][alphabet.index(message[0])]=pion
            grille[int(message[1])-2][alphabet.index(message[0])]=' '
            grille[int(message[1])-1][alphabet.index(message[0])]=' '
            return True  # on peut prendre
    return False  




#fonction de test
def test_attaque_nord():
    assert attaque_nord(grille_fin_test,'D4','o','x',1,3)==False, 'Erreur capture'
    assert attaque_nord(grille_mileu_test,'E4','o','x',1,4)==True, 'Erreur capture'
    assert attaque_nord(grille_mileu_test,'E2','o','x',3,4)==False, 'Erreur capture'
  


  
# Fonction qui verifie la possibilité de capture en nord est
def attaque_sud_est(grille,message,pion_enemie,pion,ligne,colonne):
    if grille[int(message[1])][alphabet.index(message[0])+1] == pion_enemie and grille[int(message[1])+1][alphabet.index(message[0])+2] == ' ':
    #sud east
        if int(message[1])+1==ligne and alphabet.index(message[0])+2==colonne:
            grille[int(message[1])+1][alphabet.index(message[0])+2]=pion
            grille[int(message[1])][alphabet.index(message[0])+1]=' '
            grille[int(message[1])-1][alphabet.index(message[0])]=' '
            return True  # on peut prendre
    return False  



#fonction de test
def test_attaque_sud_est():
    assert attaque_sud_est(grille_fin_test,'D4','o','x',1,3)==False, 'Erreur capture'
    assert attaque_sud_est(grille_mileu_test,'C3','o','x',1,4)==False, 'Erreur capture'
    assert attaque_sud_est(grille_mileu_test,'A1','o','x',3,4)==False, 'Erreur capture'  



  
  
# Fonction qui verifie la possibilité de capture en sud
def attaque_sud(grille,message,pion_enemie,pion,ligne,colonne):
    if grille[int(message[1])][alphabet.index(message[0])] == pion_enemie and grille[int(message[1])+1][alphabet.index(message[0])] == ' ': 
    #sud
        if int(message[1])+1==ligne and alphabet.index(message[0])==colonne:
            grille[int(message[1])+1][alphabet.index(message[0])]=pion
            grille[int(message[1])][alphabet.index(message[0])]=' '
            grille[int(message[1])-1][alphabet.index(message[0])]=' '
            return True  # on peut prendre
    return False  



#fonction de test
def test_attaque_sud():
    assert attaque_sud(grille_fin_test,'E5','x','o',6,5)==False, 'Erreur capture'
    assert attaque_sud(grille_mileu_test,'E3','o','x',4,4)==False, 'Erreur capture'
    assert attaque_sud(grille_debut_test,'A1','o','x',3,4)==False, 'Erreur capture'  





  
# Fonction qui verifie la possibilité de capture en sud ouest
def attaque_sud_ouest(grille,message,pion_enemie,pion,ligne,colonne):
    if grille[int(message[1])][alphabet.index(message[0])-1] == pion_enemie and grille[int(message[1])+1][alphabet.index(message[0])-2] == ' ': 
        #sud ouest
        if int(message[1])+1==ligne and alphabet.index(message[0])-2==colonne:
            grille[int(message[1])+1][alphabet.index(message[0])-2]=pion
            grille[int(message[1])][alphabet.index(message[0])-1]=' '
            grille[int(message[1])-1][alphabet.index(message[0])]=' '
            return True  # on peut prendre  
    return False  




#fonction de test
def test_attaque_sud_ouest():
    assert attaque_sud_ouest(grille_fin_test,'A2','o','x',3,2)==False, 'Erreur capture'
    assert attaque_sud_ouest(grille_mileu_test,'E3','o','x',4,4)==False, 'Erreur capture'
    assert attaque_sud_ouest(grille_debut_test,'A1','o','x',3,4)==False, 'Erreur capture'  
  


  

  
# Fonction qui verifie la possibilité de capture en ouest
def attaque_ouest(grille,message,pion_enemie,pion,ligne,colonne):
    if grille[int(message[1])-1][alphabet.index(message[0])-1] == pion_enemie and grille[int(message[1])-1][alphabet.index(message[0])-2] == ' ': 
        #ouest
        if int(message[1])-1==ligne and alphabet.index(message[0])-2==colonne:
            grille[int(message[1])-1][alphabet.index(message[0])-2]=pion
            grille[int(message[1])-1][alphabet.index(message[0])-1]=' '
            grille[int(message[1])-1][alphabet.index(message[0])]=' '
            return True  # on peut prendre
    return False  





#fonction de test
def test_attaque_ouest():
    assert attaque_ouest(grille_fin_test,'C2','o','x',1,2)==False, 'Erreur capture'
    assert attaque_ouest(grille_mileu_test,'D3','o','x',2,3)==False, 'Erreur capture'
    assert attaque_ouest(grille_debut_test,'D1','o','x',3,4)==False, 'Erreur capture'  

  


  
  
# Fonction qui verifie la possibilité de capture en est
def attaque_est(grille,message,pion_enemie,pion,ligne,colonne):
    if grille[int(message[1])-1][alphabet.index(message[0])+1] == pion_enemie and grille[int(message[1])-1][alphabet.index(message[0])+2] == ' ': 
        #east
        if int(message[1])-1==ligne and alphabet.index(message[0])+2==colonne:
            grille[int(message[1])-1][alphabet.index(message[0])+2]=pion
            grille[int(message[1])-1][alphabet.index(message[0])+1]=' '
            grille[int(message[1])-1][alphabet.index(message[0])]=' ' 
            return True  # on peut prendre
    return False  




#fonction de test
def test_attaque_est():
    assert attaque_est(grille_fin_test,'C2','o','x',3,2)==False, 'Erreur capture'
    assert attaque_est(grille_mileu_test,'B3','o','x',2,4)==False, 'Erreur capture'
    assert attaque_est(grille_debut_test,'E5','o','x',3,5)==False, 'Erreur capture'  


  


# fonction qui verifie si une attaque est valide et effectue cette attaque
def attaque_valide(grille,DepMessage,message):
    if tour==1:
        pion='x'
        pion_enemie='o'
    else:
        pion='o'
        pion_enemie='x'
    
    ligne=int(DepMessage[1])-1
    colonne=alphabet.index(DepMessage[0])
    #Deplacement choisi

    if int(message[1])>=2 and alphabet.index(message[0])>=1: # condition pour ne pas sortir de la grille
        if attaque_nord_ouest(grille,message,pion_enemie,pion,ligne,colonne)==True:
            return True
                    
    if int(message[1])>=2 and alphabet.index(message[0])<=len(alphabet)-2:  # condition pour ne pas sortir de la grille     
        if attaque_nord_est(grille,message,pion_enemie,pion,ligne,colonne)==True:
            return True
            
    if int(message[1])>=2:     # condition pour ne pas sortir de la grille  
        if attaque_nord(grille,message,pion_enemie,pion,ligne,colonne)==True:
            return True
            
    if int(message[1])<=len(grille)-2 and alphabet.index(message[0])<=len(alphabet)-2: # condition pour ne pas sortir de la grille   
        if attaque_sud_est(grille,message,pion_enemie,pion,ligne,colonne)==True:
            return True
              
    if int(message[1])<len(grille)-2: # condition pour ne pas sortir de la grille 
        if attaque_sud(grille,message,pion_enemie,pion,ligne,colonne)==True:
            return True        
            
    if int(message[1])<=len(grille)-2 and alphabet.index(message[0])>=2: # condition pour ne pas sortir de la grille     
        if attaque_sud_ouest(grille,message,pion_enemie,pion,ligne,colonne)==True:
            return True              
            
    if alphabet.index(message[0])>2:  # condition pour ne pas sortir de la grille    
        if attaque_ouest(grille,message,pion_enemie,pion,ligne,colonne)==True:
            return True  
            
    if alphabet.index(message[0])<len(LetterList)-2:  # condition pour ne pas sortir de la grille     
        if attaque_est(grille,message,pion_enemie,pion,ligne,colonne)==True:
            return True  
    return False            


def test_attaque_valide():
    assert attaque_valide(grille_fin_test,'C4','E2')==False, 'Erreur attaque valide'
    assert attaque_valide(grille_fin_test,'E4','E6')==False, 'Erreur attaque valide'
    assert attaque_valide(grille_mileu_test,'A5','C5')==False, 'Erreur attaque valide'
    assert attaque_valide(grille_mileu_test,'D3','F3')==False, 'Erreur attaque valide'
    assert attaque_valide(grille_fin_test,'A4','B3')==False,'Erreur attaque valide'
    assert attaque_valide(grille_fin_test,'G7','A1')==False, 'Erreur attaque valide'


#Fonction unitest
def test_func():
    print("Test de fonction \n")
    test_est_dans_grille()
    test_choix_grille()
    test_nb_pion()
    test_pion_choisi()
    test_ordi_capture_sud_ouest()
    test_ordi_capture_sud()
    test_ordi_capture_nord()
    test_ordi_capture_sud_est()
    test_ordi_capture_nord_est()
    test_ordi_capture_nord_ouest()
    test_ordi_capture_ouest()
    test_ordi_capture_est()
    test_attaque_possibles_ordinateur()
    test_mouvements_possibles_ordinateur()
    test_enchainement_possible()
    test_deplacement_valide()
    test_attaque_nord_ouest()
    test_attaque_nord_est()
    test_attaque_nord()
    test_attaque_sud()
    test_attaque_sud_est()
    test_attaque_sud_ouest()
    test_attaque_ouest()
    test_attaque_est()
    test_attaque_valide()
    print("  OK\n")


##Choix de grille:
def choix_grille_depart():
    erreur="Choisir entre 1 et 2 et 3 et 4 ou 0!\n"
    
    print("########################################\n"
         ,"             Menu Principale             \n",
         "1 - Afficher grille de test debut de jeu \n",
         "2 - Afficher grille de test milieu de jeu \n",
         "3 - Afficher grille de test fin de jeu \n",
         "4 - Tester le jeu \n",
         "0 - Quitter \n",
         "########################################")
    grille=(input("Grille: "))
    while not grille in {"0","1","2","3","4"}:
        print(erreur)
        print("Choisir la grille de test /!\ \n")

        grille=(input("Grille: "))  

    if grille=="1":
        grille=grille_debut
    elif grille=="2":
        grille=grille_mileu
    elif grille=="3":
        grille=grille_fin
    elif grille=="4":
        test_func()
        quit()
    else:  
        grille=[]

    return grille




##choisir de jouer contre joueur ou ordinateur
def choix_adversaire():
    erreur="Choisir entre 1 et 2 !"
    print("########################################\n")

    print("        Choisi ton adversaire           ")
    print("1 - Jouer contre un joueur \n")
    print("2 - Jouer contre un ordinateur \n")
    print("0 - Quitter le jeu")

    print("########################################")


    adversaire=input()
    while not adversaire in {'1','2','0'}:
        print(erreur)
        adversaire=input()
    if adversaire=='1':
        return '1'
    elif adversaire=='2':
        return '2'
    else:    
        quit()            




  
######INITIALISATION######

#Grille de début (1)
grille_debut=[
    ["o","o","o","o","o","o","x"],
    ["o","o","o","o","o","x","x"],
    ["o","o","o","o","x","x","x"],
    ["o","o","o"," ","x","x","x"],
    ["o","o","o","x","x","x","x"],
    ["o","o","x","x","x","x","x"],
    ["o","x","x","x","x","x","x"]
    ]

#Grille de mileu (2)
grille_mileu=[
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," ","o"," ","o","x"," "],
    [" "," "," "," ","x"," "," "],
    [" ","o","x"," "," "," "," "],
    [" ","x"," "," "," ","x"," "],
    [" "," "," ","x"," "," "," "]
    ]

#Grille de fin (3)
grille_fin=[
    [" "," "," "," "," "," "," "],
    [" "," "," "," ","x"," "," "],
    [" "," "," ","o"," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," ","o"," "," "],
    [" "," "," "," ","x"," "," "],
    [" "," "," "," ","x"," "," "]
    ]

#Grille de début (1)
grille_debut_test=[
    ["o","o","o","o","o","o","x"],
    ["o","o","o","o","o","x","x"],
    ["o","o","o","o","x","x","x"],
    ["o","o","o"," ","x","x","x"],
    ["o","o","o","x","x","x","x"],
    ["o","o","x","x","x","x","x"],
    ["o","x","x","x","x","x","x"]
    ]

#Grille de mileu (2)
grille_mileu_test=[
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," ","o"," ","o","x"," "],
    [" "," "," "," ","x"," "," "],
    [" ","o","x"," "," "," "," "],
    [" ","x"," "," "," ","x"," "],
    [" "," "," ","x"," "," "," "]
    ]

#Grille de fin (3)
grille_fin_test=[
    [" "," "," "," "," "," "," "],
    [" "," "," "," ","x"," "," "],
    [" "," "," ","o"," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," ","o"," "," "],
    [" "," "," "," ","x"," "," "],
    [" "," "," "," ","x"," "," "]
    ]



NumList=['1','2','3','4','5','6','7'] #Listes de ligne
LetterList=["A","B","C","D","E","F","G"] #Liste de colonne
alphabet=list(LetterList[:7])  
tour=1

 #########Programme principal#########


print(afficher_jeu(grille_debut,grille_mileu,grille_fin))
##Choix de grille:
grille=choix_grille_depart()
taille=len(grille)
if grille!=[]:
    if choix_adversaire()=='1': #Joueur contre Joueur
        while nb_pions(grille)==True: #Condition d'arret du jeu
            choix_grille(grille) #affichage de la grille choisi
            nb_pions(grille) #affichage du nombre de pion a chaque tour
            tour_du_joueur(tour) #affichage du tour du joueur
            message=est_au_bon_format(LetterList,NumList) #fonction d'insertion
            test_est_dans_grille() 
            choix_deplacement(grille,message)

            if tour==1: #tour de joueur
                tour-=1
            else:
                tour+=1
    else: # Joueur contre ordinateur
        while nb_pions(grille)==True: #Condition d'arret du jeu
            choix_grille(grille) #affichage de grille
            tour_du_joueur(tour) #annoncer le tour du joueur
            if tour==1: #tour du joueur x
                message=est_au_bon_format(LetterList,NumList) #input du joueur x
                test_est_dans_grille() 
                grille=choix_deplacement(grille,message)
                tour-=1 #iteration de tour
            else: #tour du joueur o (ordinateur)
                print("L'ordinateur a joué son coup!")
                deplacement_ordinateur_avancée(grille,taille) #applique le tour de l'ordinateur

                tour+=1 #iteration de tour


            

#Fin de partie
choix_grille(grille)
if grille==[]:
    quit()  
elif tour==0:    
    print('Le joueur X gagne la partie')
else:
    print('Le joueur O gagne la partie')




##deplacement:
#north: -1 on numbers
#south: +1 on numbers
#west: -1 in alphabet
#east: +1 in alphabet
#north east: -1 on numbers and +1 in alphabet
#north west: -1 on numbers and -1 in alphabet
#south east: +1 on numbers and +1 on alphabet
#south west: +1 on numbers and -1 on alphabet
