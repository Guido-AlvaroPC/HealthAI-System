import datetime
import cv2
import os


    # Define o nome da pasta onde a foto será armazenada
folder_name = "Images"

    # Cria a pasta se ela não existir
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

    # Inicializa a câmera
cap = cv2.VideoCapture(0)

    # Tira a foto
ret, frame = cap.read()

    # Define o nome do arquivo com base na hora atual
filename = os.path.join(folder_name,"GG.png")

    # Salva a foto na pasta
cv2.imwrite(filename, frame)

    # Libera a câmera
cap.release()
