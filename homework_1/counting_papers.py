import os

def conta_file(cartella):
    
    try:
        return len([f for f in os.listdir(cartella) if os.path.isfile(os.path.join(cartella, f))])
    except FileNotFoundError:
        return "La cartella non esiste."

percorso_cartella = "C:/Users/hp/progetto_idd/project_idd/homework_1/sources"
print(f"Numero di file nella cartella: {conta_file(percorso_cartella)}")
