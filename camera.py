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