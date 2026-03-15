import PySimpleGUI4 as sg

main_layout = [
    # Ligne Titre
    [sg.Text("Mot de passe :\nAu dessus de 8 caractères il sera impossible de le cracker")],

    # Ligne Mot de passe
    [   sg.Input(key="-INPUT-", size=(25, 1)),
        sg.Button("OK", key="-OK-"),
        sg.Button("Générer mot de passe(6 caractères)", key="-GEN-"), 
    ],

    # Ligne Bruteforce 
    [
        sg.Button(
            button_text="Bruteforce",
            key="-BRUTE-",
            button_color="green",
            disabled_button_color="red",
            auto_size_button=True,
            mouseover_colors="blue"
        )
    ],

    # Ligne Radio 
    [
        sg.Radio("Bruteforce Python(aucun hachage)", "HASH_GROUP", key="-PY-", default=True),
    ],
    [
        sg.Text("Bruteforce + hachage"),
        sg.Radio("MD5", "HASH_GROUP", key="-MD5-"),
        sg.Radio("SHA1", "HASH_GROUP", key="-SHA1-"),
        sg.Radio("SHA256", "HASH_GROUP", key="-SHA256-"),
        sg.Radio("SHA512", "HASH_GROUP", key="-SHA512-"),
        sg.Radio("BCRYPT(solide)", "HASH_GROUP", key="-BCRYPT-")
    ],

    # Ligne Durée du Bruteforce
    [
        sg.Text("Durée de Bruteforce max(Hashcat uniquement) :"),
        sg.Radio("Illimitée","TIME_GROUP", key="-INFINI-", default=True),
        sg.Radio("Limitée ==>","TIME_GROUP", key="-FINI-"),
        sg.Input(key="-TIME-", size=(5,1)), sg.Text("secondes"),
    ],
    

    # Ligne Chiffrement
    [
        sg.Button(
            button_text="Chiffrement",
            key="-CRYPT-",
            button_color="green",
            disabled_button_color="red",
            auto_size_button=True,
            mouseover_colors="blue"
        )
    ],

    # Affichage mot de passe
    [sg.Text("", key="-PASSWD-")]
]