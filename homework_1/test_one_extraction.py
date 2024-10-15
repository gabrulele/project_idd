import requests
from lxml import html
import lxml.etree as etree
import string


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
    

file_path = "project_idd/homework_1/sources/arXiv2409.07793.html"

# Lista di id per accedere poi ad ogni tables

xpath_query_id_tables = "//table/@id"  
   
id_tables = estrai_con_xpath(file_path, xpath_query_id_tables)

if id_tables:
    for id in id_tables:
        table = estrai_con_xpath(file_path,"//table[@id='" + id + "']")
        for elem in table:
            print(etree.tostring(elem, pretty_print=True).decode())
        xpath_query_caption = "//table[@id='"+ id + "']/ancestor::figure/figcaption/text() | //table[@id='"+ id + "']/ancestor::figure/figcaption//*/text()"
        caption = estrai_con_xpath(file_path,xpath_query_caption)
        print(caption)
        xpath_query_footnote = "//table[@id='"+ id + "']/ancestor::figure//cite/*/text()"
        footnote = estrai_con_xpath(file_path,xpath_query_footnote)
        print(footnote)
        xpath_query_id_figure = "//table[@id='"+ id + "']/ancestor::figure/@id"
        id_figure = estrai_con_xpath(file_path, xpath_query_id_figure)
        if(id_figure):
            xpath_query_paragraph = "//*[substring(@href, string-length(@href) - string-length('"+ id_figure[0] +"') + 1) ='"+ id_figure[0] +"']/ancestor::p/text()"
            paragraph = estrai_con_xpath(file_path,xpath_query_paragraph)
            print(paragraph)
            print("\n\n")
    
        


