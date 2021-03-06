import csv
import time
import requests
from PIL import Image, ImageDraw
from io import BytesIO


if __name__ == '__main__':
    link_csv = str(r'Lista Link Imagens3 22-01-2019.csv')
    link_txt = str(r'Resultado3.txt')
    try:
        with open(link_csv,'r', encoding='utf-8', errors='ignore') as lb:
            reader = csv.reader(lb)
            i = 0
            code_padrao = str("200")
            for r in reader:
                if 0 <= i < 194000: #alterado aqui
                    idimagem = r[0]
                    link = r[1]
                    req = None
                    status = None
                    status_link = None
                    image = None
                    try:
                        time.sleep(0.2)
                        req = requests.get(link)
                        status_link = str(req.status_code)
                        image = Image.open(BytesIO(req.content))
						# São vários tamanhos de imagens, verifica todos os demais tamanhos
                        if status_link == code_padrao:
                            link2 = link.replace("/full/", "/g/")
                            req = requests.get(link2)
                            status_link = str(req.status_code)
                        if status_link == code_padrao:
                            link2 = link.replace("/full/", "/p/")
                            req = requests.get(link2)
                            status_link = str(req.status_code)
                        if status_link == code_padrao:
                            link2 = link.replace("/full/", "/m/")
                            req = requests.get(link2)
                            status_link = str(req.status_code)
                        if status_link == code_padrao:
                            link2 = link.replace("/full/", "/gg/")
                            req = requests.get(link2)
                            status_link = str(req.status_code)
                        if status_link == code_padrao:
                            link2 = link.replace("/full/", "/pp/")
                            req = requests.get(link2)
                            status_link = str(req.status_code)
                        status = str('Ok')
                    except Exception as e:
                        status = str('Imagem Quebrada')
                        pass
                    with open(link_txt, 'a') as txtfile:
                        texto_write = str('\"' + str(idimagem) + "\";\"" + str(status) + "\";\"" + str(status_link) + '\"')
                        print(texto_write + "i: " + str(i))
                        txtfile.write(texto_write  + "\n")
                        txtfile.close()
                i += 1
    except IOError:
        print('Erro de IO')
