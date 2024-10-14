import os
from lxml import html
import lxml.etree as etree

def estrai_con_xpath(pagina, xpath_query):
    """Applica una query XPath a una pagina HTML e restituisce il risultato."""
    try:
        risultato = pagina.xpath(xpath_query)
        return risultato
    except Exception as e:
        print("Errore nell'elaborazione:", e)
        return None

def processa_file_html(file_path):
    """Processa un file HTML locale per estrarre le tabelle e relative informazioni."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Carica il contenuto come una pagina HTML parsata
        pagina = html.fromstring(content)

        # Estrae gli ID di tutte le tabelle
        xpath_query_id_tables = "//table/@id"  
        id_tables = estrai_con_xpath(pagina, xpath_query_id_tables)

        if id_tables:
            for id in id_tables:

                # Estrazione della tabella specifica con l'ID corrente
                table = estrai_con_xpath(pagina, f"//table[@id='{id}']")
                for elem in table:
                    print("\nTable:\n")
                    print(etree.tostring(elem, pretty_print=True).decode())

                # Estrazione della caption associata alla tabella
                xpath_query_caption = f"//table[@id='{id}']/ancestor::figure/figcaption/text()"
                caption = estrai_con_xpath(pagina, xpath_query_caption)
                print("\nDidascalia: ", caption)

                # Estrae eventuali footnotes o nella table o nella caption
                # xpath_query_footnote = f"//table[@id='{id}']//cite/*/text()"
                # footnote = estrai_con_xpath(pagina, xpath_query_footnote)
                # print("Footnotes:", footnote)

    except Exception as e:
        print(f"Errore nell'elaborazione del file {file_path}:", e)

# Cartella contenente i file HTML locali
directory_path = "sources"

# Itera su ogni file .html nella cartella e applica le operazioni di estrazione
for filename in os.listdir(directory_path):
    # Costruisce il percorso completo del file
    file_path = os.path.join(directory_path, filename)
    # Processa solo i file HTML
    if os.path.isfile(file_path):
        processa_file_html(file_path)
