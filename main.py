import cv2
import os
import pickle
import face_recognition
import numpy as np
from teste import get_user_data

webcam = cv2.VideoCapture(0) #Inicia a Webcam
webcam.set(3 , 640) #Largura
webcam.set(4, 480) #Altura
 
imgBackground = cv2.imread('Resources/background.png') #Carrega Imagem de fundo


# IMPORTA IMAGENS MODE E TRANSFORMA EM LISTA
pastaMode = 'Resources/Modes' #Carrega Imagens da pasta MODES
modeLista = os.listdir(pastaMode) #Cria lista das Imagens
imgModeList = []
index = 0
for mode in modeLista:
    imgModeList.append(cv2.imread(os.path.join(pastaMode, mode)))

# CARREGA O ARQUIVO CODIGOID.P
file = open('CodigosID.p', 'rb')
codificadoID = pickle.load(file)
file.close()
codificado, fotoID = codificadoID

while True:
    sucesso, img = webcam.read()
    #img = cv2.resize(img, (640,480))

    #Reduze o tamanho a imagem
    imgS = cv2.resize(img,(0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    #Reconhece rosto
    faceFrame = face_recognition.face_locations(imgS)
    codificaFrame = face_recognition.face_encodings(imgS, faceFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img #Posiciona WebCam
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[index] #Posiciona os Modes

    #verifica se a autenticidade
    for rostoCode , rostoID in zip(codificaFrame,faceFrame):
        match = face_recognition.compare_faces(codificado, rostoCode)
        face = face_recognition.face_distance(codificado, rostoCode)
        #print(match)
        #print(face)
        mathIndex = np.argmin(face)
        print(mathIndex)
        if match[mathIndex]:
            print('Rosto Reconhecido')
            index = 2
        else:
            print('Rosto Desconhecido')
            index = 0
            
    cv2.imshow('back',imgBackground)
    key = cv2.waitKey(1)
    if key == ord('q'):
        get_user_data()
        exec(open('print.py').read())
        exec(open('GeradorCodigo.py').read())
        index = 2
        continue
        