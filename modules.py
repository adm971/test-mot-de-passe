import string, secrets, itertools, string, time, hashlib, subprocess, os, bcrypt, random, datetime
import sys



if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HASHCAT_PATH = os.path.join(BASE_DIR, "hashcat", "hashcat.exe")

if not os.path.exists(HASHCAT_PATH):
    print("Hashcat introuvable dans le dossier hashcat/")
else : 
    print("hashcat trouvé")





def generate_password(length=random.randint(4,12)):
    """
    Générer un mot de passe aléatoirement.
    
    Args:
        length (int): longueur souhaitée du mot de passe.
    
    Returns:
        str: mot de passe.
    """
    if length < 12:
        print("Il est recommandé d'avoir un mot de passe supérieur à 12 caractères")
    
    # caractères 
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # création du mot de passe
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password



def brute_force(password):
    """
    Tentative de brute force sur un mot de passe.
    
    Args:
        password (str): mot de passe à tester.
    
    Returns:
        mot de passe(str), temsp(float)
        
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    start_time = time.time()
    temps_ecoul = 5

    combi_total = len(chars) ** len(password) # nombre total de combinaison estimée
    print(f"Nombre de combinaison estimé : {combi_total}")
    
    r = len(password)+1 # mesurer la longueur du mot de passe

    # Générer les combinaisons
    for length in range(1, r):  
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            progress = (attempts/combi_total) * 100 # progression du bruteforce
            temps_estim = temps_ecoul / (progress/100) # calcul du temps estimé pour bruteforce

            if temps_estim < 31536000 : # Si le temps estimé est inférieure à 1 an


                if time.time() - start_time > temps_ecoul:
                    temps_rest = temps_estim - temps_ecoul # temps restant pour bruteforce

                    print(f"Brute force en cours depuis plus de {temps_ecoul} secondes... \n Progression : {round(progress)}% \n Temps restant : {temps_rest} secondes")
                    temps_ecoul +=5


                if ''.join(guess) == password:
                    end_time = time.time()

                    print(f"Mot de passe trouvé : {password}")
                    print(f"Nombre d'essais : {attempts}")
                    print(f"Temps nécessaire : {end_time - start_time:.2f} secondes")

                    return password, end_time - start_time
            
            else : 
                print(f"Durée nécessaire de bruteforce supérieure à 1 an : {((((temps_estim/60)/60)/24)/365)} ans")
                return password, temps_estim
            





def hash_pswd(password, mode="md5", hashcat=False, runtime=10**10): 
    """
    Hasher un mot de passe pour le cracker avec hashcat

    Args:
        password (str): mot de passe à hasher
        mode (str): methode de hash(md5, sha1, sha256, sha512, bcrypt)
        hashcat (bool) : True pour brute force avec hashcat, False pour simplement hash
        runtime (int) : durée d'attente max pour le crack
    
    Returns:
        mot de passe(str)

    """            

    # LISTE DES MODES DE HACHAGE 
    HASHCAT_MODES_MAP = {
    "md5": 0,
    "sha1": 100,
    "sha256": 1400,
    "sha512": 1700,
    "bcrypt": 3200
}

    # HASH LE MOT DE PASSE
    if mode == "bcrypt":
        salt = bcrypt.gensalt(rounds=12)
        hash_value = bcrypt.hashpw(password.encode(), salt).decode()

    elif mode in hashlib.algorithms_available:
        hash_function = getattr(hashlib, mode)
        hash_value = hash_function(password.encode()).hexdigest()

    else:
        raise ValueError(f"Méthode de hash non disponible: {mode}")
    print("Hash :", hash_value)

    # LONGUEUR DU MDP
    length = len(password)
    mask = "?a" * length

    # ENREGISTRER LE HASH DANS UN FICHIER POUR UTILISER HASHCAT
    hash_file = os.path.join(BASE_DIR, "hash.txt") # Chemin absolu du hash

    with open(hash_file, "w") as f:
        f.write(hash_value)

        if hashcat == False :
            return hash_value



# UTILISER HASHCAT
    result_file = os.path.join(BASE_DIR, "password.txt") 

    if hashcat == True :
        # SI MOT DE PASSE > 8 ==> IMPOSSIBLE DE BRUTE FORCE
        cracked_password = "aucun mot de passe"
        if len(password) > 8 : 
            cracked_password = "aucun mot de passe"
            print(cracked_password)
            if os.path.exists(result_file):
                with open(result_file, "w") as f:
                    f.write(cracked_password)
            return cracked_password
        
        else :
            if os.path.exists(result_file):
                os.remove(result_file)


            command = [
                HASHCAT_PATH,
                "-m", str(HASHCAT_MODES_MAP[mode]),
                "-a", "3",
                hash_file,
                mask,
                "--potfile-disable",
                "--runtime", str(runtime),
                "--status",
                "--status-timer", "2",
                "-w", "2",
                "--force",
                "--outfile", result_file,
                "--outfile-format", "2"
            ]
            # CREER UN LOG

            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = os.path.join(BASE_DIR, f"hashcat_log_{timestamp}.log")

            process = subprocess.Popen(
            command,
            cwd=os.path.join(BASE_DIR, "hashcat"),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
            with open(log_file, "w", encoding="utf-8") as log:
                for line in process.stdout:
                    print(line.strip())          # Affichage console
                    log.write(line)              # Écriture dans le log

            show_command = [
            HASHCAT_PATH,
            "-m", str(HASHCAT_MODES_MAP[mode]),
            hash_file,
            "--show"
            ]
            subprocess.run(show_command, cwd=os.path.join(BASE_DIR, "hashcat"))

                    # Recup mdp cracké
            if os.path.exists(result_file):
                with open(result_file, "r") as f:
                    cracked_password = f.read().strip()

                    if cracked_password:
                        print("MOT DE PASSE ==>", cracked_password)
                    else:
                        print("aucun mot de passe trouvé dans le temps imparti.")
                return cracked_password