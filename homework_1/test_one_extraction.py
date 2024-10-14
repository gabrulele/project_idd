import requests
from lxml import html
import lxml.etree as etree

def estrai_con_xpath(url, xpath_query):
    try:
        # Ottiene il contenuto HTML dalla pagina
        response = requests.get(url)
        response.raise_for_status()  # Controlla che la richiesta sia andata a buon fine
        pagina = html.fromstring(response.content)

        # Applica la query XPath
        risultato = pagina.xpath(xpath_query)
        
        return risultato
    
    except requests.exceptions.RequestException as e:
        print("Errore nella richiesta:", e)
        return None
    except Exception as e:
        print("Errore nell'elaborazione:", e)
        return None

url = "https://arxiv.org/html/2410.08946"

# Lista di id per accedere poi ad ogni tables

xpath_query_id_tables = "//table/@id"  
   
id_tables = estrai_con_xpath(url, xpath_query_id_tables)

if id_tables:
    for id in id_tables:
        table = estrai_con_xpath(url,"//table[@id='" + id + "']")
        for elem in table:
            print(etree.tostring(elem, pretty_print=True).decode())
        xpath_query_caption = "//table[@id='"+ id + "']/ancestor::figure/figcaption/text()"
        caption = estrai_con_xpath(url,xpath_query_caption)
        print(caption)
        xpath_query_footnote = "//table[@id='"+ id + "']//cite/*/text()"
        footnote = estrai_con_xpath(url,xpath_query_footnote)
        print(footnote)
        print("\n\n")

        


