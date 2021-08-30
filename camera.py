import face_recognition
import cv2
import numpy as np
import os
import glob

class ReconhecimentoFacial():
    
    faces_encoding = []
    faces_name = []

    diretorio = os.getcwd()

    path = os.path.join(diretorio, 'faces/')

    list_of_files = [f for f in glob.glob(path+'*.jpg')]

    num_files = len(list_of_files)

    nomes = list_of_files.copy()

    for i in range(num_files):
        globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
        globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
        faces_encoding.append(globals()['image_encoding_{}'.format(i)])
        
        nomes[i] = nomes[i].replace(diretorio, "")
        faces_name.append(nomes[i])
        
        print(nomes[i])