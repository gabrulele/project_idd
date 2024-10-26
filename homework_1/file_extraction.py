import os
from lxml import html
import lxml.etree as etree
from json_extraction import estrai_json

# myenv -> source myenv/bin/activate

def processa_file_html():

    # Cartella contenente i file HTML locali
    directory_path = "homework_1/sources"

    # Itera su ogni file .html nella cartella e applica le operazioni di estrazione
    for filename in os.listdir(directory_path):

        # Costruisce il percorso completo del file
        file_path = os.path.join(directory_path, filename)
        
        # Processa solo i file HTML
        if os.path.isfile(file_path):
            estrai_json(file_path)


processa_file_html()
