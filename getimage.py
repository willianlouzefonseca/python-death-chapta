import requests
import shutil

r = requests.get("http://anp.gov.br/preco/prc/imagem.asp".format(**data), stream=True)
if r.status_code == 200:
    with open("images/file.png", 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
