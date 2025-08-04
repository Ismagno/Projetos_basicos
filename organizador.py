
import os
import shutil

#coloca o caminho do diretorio entre as aspas abaixo e so funfar o codigo
pasta_origem = r"C:\\" 

extensao_para_pasta = {
    "Executáveis" : [".exe"],
    "Imagens": [".png", ".jpeg", "jpng", ".jpg"],
    "PDFs": [".pdf"],
    "Word": [".docx",".doc"],
    "Planilhas" : [".xlsx", ".csv", ".xls", ".xltx"],
    "PowerPoint" : [".pptx", ".ppt"],
    "Winrar" : [".zip",".rar",".7z",".tar"],
    "Musicas": [".mp3"],
    "Vídeos": [".mp4"],
    "Notepads": [".txt"]
}

os.chdir(pasta_origem)

for arquivos in os.listdir():
    if os.path.isdir(arquivos):
        continue
    for pasta, extensoes in extensao_para_pasta.items():
        if arquivos.lower().endswith(tuple(extensoes)):
            os.makedirs(pasta,exist_ok=True)
            destino = os.path.join(pasta, os.path.basename(arquivos))
            shutil.move(arquivos, destino)
            print('='*30)
            print(f"O arquivo, {arquivos}, foi movido com sucesso para {pasta}!")
            break

os.startfile(pasta_origem)