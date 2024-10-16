import requests
from lxml import html
import lxml.etree as etree
import string
from bs4 import BeautifulSoup


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
    

file_path = "project_idd/homework_1/sources/arXiv2409.13535.html"

# Lista di id per accedere poi ad ogni tables

xpath_query_id_tables = "//table/@id"  
   
id_tables = estrai_con_xpath(file_path, xpath_query_id_tables)

if id_tables:

    #Scorriamo la lista id_tables per accedere ad ogni id delle tables
    for id in id_tables:
        table = estrai_con_xpath(file_path,"//table[@id='" + id + "']")
        for elem in table:
            print(etree.tostring(elem, pretty_print=True).decode())

        # Tramite l'id della table i-esima prendiamo la caption associata
        xpath_query_caption = "//table[@id='"+ id + "']/ancestor::figure/figcaption/text() | //table[@id='"+ id + "']/ancestor::figure/figcaption//*/text()"
        caption_list = estrai_con_xpath(file_path,xpath_query_caption)
        caption = " ".join(caption_list)
        print(caption)
        print("\n")

        # Tramite l'id della table i-esima prendiamo tutti i footnotes associati alla table e caption
        xpath_query_href_cite = "//table[@id='"+ id + "']/ancestor::figure//cite//@href"
        href_cites = estrai_con_xpath(file_path,xpath_query_href_cite)

        footnote_table_list = [] # Lista unica per i molteplici footnote cada table

        # Usiamo il metodo split per dividere la stringa su "...bib.bib..."
        for href in href_cites:
            num_footnote = href.split("bib.bib")[-1]  # Prendiamo il numero del footnote
            xpath_query_footnote = "//li[@id='bib.bib"+ num_footnote + "']/*/text()"
            footnote_list = estrai_con_xpath(file_path,xpath_query_footnote)
            footnote = " ".join(footnote_list)
            footnote_table_list.append(footnote)
        print(footnote_table_list)
        print("\n")

        # Tramite l'id della table recuperiamo l'id della figure ancestor per ottenere i paragraphs
        xpath_query_id_figure = "//table[@id='"+ id + "']/ancestor::figure/@id"
        id_figure = estrai_con_xpath(file_path, xpath_query_id_figure)
        if(id_figure):
            xpath_query_paragraph = "//*[substring(@href, string-length(@href) - string-length('"+ id_figure[0] +"') + 1) ='"+ id_figure[0] +"']/ancestor::p"
            paragraph_htmls = estrai_con_xpath(file_path,xpath_query_paragraph)

            paragraph_list = []

            for html_p in paragraph_htmls:
                # Usa lxml per trovare l'elemento e ottenere solo il testo
                text_content = html_p.text_content() 

                paragraph_list.append(text_content)

            print(paragraph_list)
            print("\n\n")

    
        


