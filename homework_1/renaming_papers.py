import os

# Definisci il percorso della cartella
cartella = "C:/Users/hp/progetto_idd/project_idd/homework_1/sources"

# Verifica se la cartella esiste
if os.path.exists(cartella) and os.path.isdir(cartella):
    # Itera su tutti i file nella cartella
    for filename in os.listdir(cartella):
        # Verifica che sia effettivamente un file
        percorso_file = os.path.join(cartella, filename)
        if os.path.isfile(percorso_file):
            # Trova la posizione del primo underscore
            pos_underscore = filename.find('_')
            # Se trova un underscore, rinomina il file
            if pos_underscore != -1:
                nuovo_nome = filename[pos_underscore + 1:]
                nuovo_percorso = os.path.join(cartella, nuovo_nome)
                # Rinomina il file
                os.rename(percorso_file, nuovo_percorso)
                print(f"Rinominato: {filename} -> {nuovo_nome}")
else:
    print("La cartella specificata non esiste o non è una directory.")
