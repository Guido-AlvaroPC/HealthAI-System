import cv2
import face_recognition
import pickle
import os

# IMPORTA FOTOS
pastaFoto = 'Images' #Carrega Imagens da pasta MODES
fotoLista = os.listdir(pastaFoto) #Cria lista das Imagens
imgFotoList = []
fotoID = []
for foto in fotoLista:
    imgFotoList.append(cv2.imread(os.path.join(pastaFoto, foto)))
    fotoID.append(os.path.splitext(foto)[0]) #Pega a ID da imagem e adiciona na lista

# Codifica fotos
def codifica(imgfoto):
    codificaList = []
    for img in imgfoto:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        codifica = face_recognition.face_encodings(img)[0]
        codificaList.append(codifica)
    return codificaList

codificado = codifica(imgFotoList) #Usa a função codifica para codificar as imagens
codificadoID = [codificado, fotoID] #Associa das codificaçoes com as IDS


# Cria arquivo de IDs codificados
file = open("CodigosID.p", 'wb')
pickle.dump(codificadoID, file)
file.close()
