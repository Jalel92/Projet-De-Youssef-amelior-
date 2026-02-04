import calendar # Bibliothèque externe 1 : pour générer les matrices de mois
import datetime # Bibliothèque externe 2 : pour manipuler les dates système

def menu(): # Fonction pour afficher les choix possibles
    print("--- MENU ---") # Simple séparateur de texte
    print("1. Voir un mois") # Option pour l'affichage calendrier
    print("2. Date du jour") # Option pour voir aujourd'hui
    print("3. Stop") # Option pour fermer le script

while True: # Boucle infinie pour faire tourner le menu
    menu() # Appel de la fonction d'affichage
    user_input = input("> ")   # Récupération de la saisie utilisateur
    
    if user_input == "1": # Test si l'utilisateur veut le calendrier
        m = int(input("Mois (1-12): ")) # Conversion de l'entrée en entier pour le mois
        a = int(input("Année: ")) # Conversion de l'entrée en entier pour l'année
        print(calendar.month(a, m))    # Utilisation de calendar pour afficher le bloc du mois
        
    elif user_input == "2": # Test pour la date actuelle
        maintenant = datetime.datetime.now() # Récupération de l'objet date complet
        print(f"Date : {maintenant.strftime('%d/%m/%Y')}") # Formatage propre en jour/mois/année
        
    elif user_input == "3": # Test pour quitter
        print("Bye!") # Petit message de sortie
        break # Sortie brutale de la boucle (plus naturel pour un humain)
        
    else: # Si l'utilisateur tape n'importe quoi
        print("Erreur de saisie") # Message de sécurité
