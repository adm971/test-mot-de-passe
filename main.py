# main.py
import PySimpleGUI4 as sg, random
from gui import main_layout
from modules import generate_password, hash_pswd, brute_force

# Création de la fenêtre
win = sg.Window("Générateur de mot de passe sécurisé", main_layout)


# Boucle événementielle
while True:
    event, values = win.read()
    
    if event == sg.WIN_CLOSED:
        break    


        # MOT DE PASSE 
    if event == "-GEN-" : 
        # GENERER MDP
        passwd = generate_password(random.randint(2,6))
        sg.Popup(passwd, title="Mot de passe", custom_text="Fermer")
    if event == "-OK-" : 
        # INPUT MDP
        passwd = values["-INPUT-"]
        print(f"mot de passe séléctionné : {passwd}")



        # BRUTEFORCE
    if event == "-BRUTE-":
        print("BRUTE FORCE")

        # BRUTE FORCE AVEC PYTHON
        if values["-PY-"]:  
            print("BRUTE FORCE PYTHON")
            brute = brute_force(passwd)
            if brute[1] > 31536000 :
                crack = hash_pswd(passwd, "md5", True, 10)
                print(f"Return de la fonction hash_pswd ====> {crack}")
                sg.Popup(f"Mot de passe : {crack} trouvé avec Hashcat \n Bruteforce Python trop lent \n Durée estimée avec Python : {round(brute[1])} an(s) \n Veuillez utiliser hashcat en sélectionnant une méthode de hachage pour ce type de mot de passe", title="Echec de Bruteforce avec Python")
            else : 
                print(f"return de la fonction brute_force ====> {brute}")
                sg.Popup(f"{brute[0]} trouvé en moins de {brute[1]} secondes", title="Mot de passe trouvé")
        # BRUTE FORCE AVEC HASHCAT
        else : 
            # SELECTION DE LA METHODE DE HACHAGE
            selected_key = next((key for key in values if key in ["-MD5-", "-SHA1-", "-SHA256-", "-SHA512-", "-BCRYPT-"] 
                                 and values[key]),None)
            k = selected_key.strip("-").lower() 
            print(f"BRUTE FORCE AVEC HASCAT MODE : {k}")
            # DUREE DU BRUTE FORCE INFINIE
            if values["-INFINI-"] : 
                print("durée de brute force infinie")
                runtime = None
                crack = hash_pswd(passwd, k, True)
            # DUREE DU BRUTE FORCE FINIE
            elif values["-FINI-"] : 
                if not values["-TIME-"].isdigit():
                    sg.Popup("Veuillez sélectionner un nombre")
                else :
                    runtime = int(values["-TIME-"])
                    print(f"durée max de brute force : {runtime} secondes")
                    crack = hash_pswd(passwd, k, True, runtime)
            # DUREE DE BRUTEFORCE PAS INDIQUEE
            else :                  
                runtime = 60
                crack = hash_pswd(passwd, k, True, runtime)
                print(f"durée max de brute de force : 60 secondes")


            print(f"Return de la fonction hash_pswd ====> {crack}")
            if crack != None :
                sg.Popup(f"Mot de passe : {crack} trouvé", title="Mot de passe trouvé")
            else : 
                sg.Popup(f"Mot de passe trop solide pour etre cracké \n", title="Runtime limit reached, aborting")



        # CHIFFREMENT
    if event == "-CRYPT-":
        print("Chiffrement")

win.close()