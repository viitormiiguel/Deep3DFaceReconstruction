
from simple_3dviz import Mesh
from simple_3dviz.window import show
from simple_3dviz.behaviours.movements import CameraTrajectory
from simple_3dviz.behaviours.trajectory import Circle
from simple_3dviz.utils import render
from simple_3dviz.behaviours.io import SaveFrames

import os

# path = 'E:/PythonProjects/DECA/TestSamples/dataset_output/'
# dest = 'E:/PythonProjects/Dataset_Deca/'
path = 'D:/Orgazine Faces/Deep3D/Jennifer/'

lista = os.listdir(path + 'surprise')

for l in lista:
    
    # if '.jpg' not in l:
        
    #     lt = os.listdir(path + '/cgi/jennifer/' + l)
    #     print(l)
        
    #     cond = l + '.obj'
    #     if cond in lt:
            
    #         m = Mesh.from_file(path + '/cgi/jennifer/' + l + '/' + cond, color=(0.8, 0.8, 0.8, 1.0))
    #         m.to_unit_cube()
            
    #         nome = l
    #         render(
    #             [m],
    #             n_frames=200,
    #             size=(256,256),
    #             camera_position=(0.0, 0.15, 1.5),
    #             up_vector=(0, 1, 0),
    #             behaviours=[
    #                 SaveFrames(dest + '/cgi/jennifer/' + nome + '.png')
    #             ]
    #         )        
    
# for im in os.listdir('output/test/' + l):
    
    # if not os.path.exists('imgs/test/' + l):
    #     os.makedirs('imgs/test/' + l)
    
    if '.obj' in l:
        print(path + 'surprise' + '/' + l)
        m = Mesh.from_file(path + 'surprise' + '/' + l, color=(0.8, 0.8, 0.8, 1.0))
        m.to_unit_cube()
        
        nome = l.split('.')            
        print(nome)
        render(
            [m],
            n_frames=200,
            size=(256,256),
            camera_position=(0.0, 0.15, 1.5),
            up_vector=(0, 1, 0),
            behaviours=[
                SaveFrames('D:/Orgazine Faces/DeepImgs/Jennifer/surprise/' + nome[0] + '.png')
            ]
        )
           
    

