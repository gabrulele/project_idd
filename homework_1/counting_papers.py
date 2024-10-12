import os

def rename_files_in_directory(directory):
    """Conta e rinomina i file nella cartella specificata."""
    
    # Verifica se la cartella esiste
    if not os.path.isdir(directory):
        print(f"La directory '{directory}' non esiste.")
        return
    
    # Conta i file nella cartella
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    file_count = len(files)
    print(f"Numero di file trovati: {file_count}")
    
    # Rinomina ogni file
    for index, filename in enumerate(files, start=1):
        old_path = os.path.join(directory, filename)
        new_filename = f"html_paper_{index}"
        new_path = os.path.join(directory, new_filename)
        
        # Aggiunge estensione solo se il file ne ha già una
        if '.' in filename:
            ext = os.path.splitext(filename)[1]  # Mantiene l'estensione originale
            new_path += ext
        
        os.rename(old_path, new_path)
        #print(f"File rinominato: {old_path} -> {new_path}")

# Esempio di utilizzo
directory = input("Inserisci il percorso della cartella: ")
rename_files_in_directory(directory)
