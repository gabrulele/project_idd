import os
import requests
from lxml import html
import lxml.etree as etree
import string
from bs4 import BeautifulSoup
import json


def estrai_con_xpath(file_path, xpath_query):

    # Carica il contenuto come una pagina HTML parsata
    try:
         with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            pagina = html.fromstring(content)
            risultato = pagina.xpath(xpath_query)
            return risultato
    
    except Exception as e:
        print(f"Errore nell'elaborazione del file {file_path}:", e)

def estrai_json(file_path):

    # Dizionario che conterrà i dati finali da convertire in JSON
    json_data = {}

    # Lista di id per accedere ad ogni tables
    xpath_query_id_tables = "//table/@id"  
    
    id_tables = estrai_con_xpath(file_path, xpath_query_id_tables)

    clean_id_tables = [elemento for elemento in id_tables if "T" in elemento]

    if clean_id_tables:

        # Scorriamo la lista id_tables per accedere ad ogni id delle tables
        for id in clean_id_tables:

            # Dati per la tabella corrente
            table_data = {}
            table = estrai_con_xpath(file_path,"//table[@id='" + id + "']")
            html_table = "".join([etree.tostring(elem, pretty_print=True).decode() for elem in table])
            table_data["table"] = html_table

            # Tramite l'id della table i-esima prendiamo la caption associata
            xpath_query_caption = "//table[@id='"+ id + "']/ancestor::figure/figcaption/text() | //table[@id='"+ id + "']/ancestor::figure/figcaption//*/text()"
            caption_list = estrai_con_xpath(file_path,xpath_query_caption)
            caption = " ".join(caption_list)
            table_data["caption"]=caption
            print("\n")

            # Tramite l'id della table i-esima prendiamo tutti i footnotes associati alla table e caption
            xpath_query_href_cite = "//table[@id='"+ id + "']/ancestor::figure//cite//@href"
            href_cites = estrai_con_xpath(file_path, xpath_query_href_cite)

            # Lista unica per i molteplici footnote cada table
            footnote_table_list = []

            # Usiamo il metodo split per dividere la stringa su "...bib.bib..."
            for href in href_cites:
                num_footnote = href.split("bib.bib")[-1]
                xpath_query_footnote = "//li[@id='bib.bib"+ num_footnote + "']/*/text() | //li[@id='bib.bib"+ num_footnote + "']//*/text()"
                footnote_list = estrai_con_xpath(file_path, xpath_query_footnote)
                footnote = " ".join(footnote_list)
                footnote_table_list.append(footnote)
            table_data["footnotes"] = footnote_table_list
            print("\n")

            # Tramite l'id della table recuperiamo l'id della figure ancestor per ottenere i paragraphs
            xpath_query_id_figure = "//table[@id='"+ id + "']/ancestor::figure/@id"
            id_figure = estrai_con_xpath(file_path, xpath_query_id_figure)
            paragraph_list = []
            if(id_figure):
                xpath_query_paragraph = "//*[substring(@href, string-length(@href) - string-length('"+ id_figure[0] +"') + 1) ='"+ id_figure[0] +"']/ancestor::p"
                paragraph_htmls = estrai_con_xpath(file_path,xpath_query_paragraph)

                for html_p in paragraph_htmls:

                    # Usa lxml per trovare l'elemento e ottenere solo il testo
                    text_content = html_p.text_content() 
                    paragraph_list.append(text_content)
                print("\n\n")
            
            table_data["references"] = paragraph_list

            # Aggiungi il risultato al dizionario principale con l'ID della tabella come chiave
            json_data[id] = table_data

    output_dir = "homework_1/extraction"

    json_name = file_path.split("arXiv")[-1]
    json_name = json_name.split(".html")[0]  # prendo solo il numero del paper, togliendo ".html"

    output_file = os.path.join(output_dir, json_name + ".json")

    # Scrivi il risultato in un file JSON
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4)

        
            


