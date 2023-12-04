
from simple_3dviz import Mesh
from simple_3dviz.window import show
from simple_3dviz.behaviours.movements import CameraTrajectory
from simple_3dviz.behaviours.trajectory import Circle
from simple_3dviz.utils import render
from simple_3dviz.behaviours.io import SaveFrames

import os

path = 'D:/PythonProjects/NextFace/output/'
dest = 'E:/PythonProjects/Dataset_NextFace/'

lista = os.listdir(path + 'dataset_cg/cgi/will')

for l in lista:
    
    if '.obj' in l:
        
        print(l)       
            
        m = Mesh.from_file(path + 'dataset_cg/cgi/will/' + l, color=(0.8, 0.8, 0.8, 1.0))
        m.to_unit_cube()
        
        nome = l.split('.')
        render(
            [m],
            n_frames=200,
            size=(256,256),
            camera_position=(-0.04, -0.3, -1.4),
            # camera_target=(0.0, 0.5, 0.0),
            # up_vector=(0.0, 0.22, 0.73),
            behaviours=[
                SaveFrames(dest + '/cgi/will/' + nome[0] + '.png')
            ]
        )
        
        # break
    
    # for im in os.listdir('output/paper/spontaneous/men/' + l):
    
    # if not os.path.exists('imgs/paper/spontaneous/men/' + l):
    #     os.makedirs('imgs/paper/spontaneous/men/' + l)
    
    # if '.obj' in l:
    #     print("output/paper/spontaneous/men/" + l)
    #     m = Mesh.from_file("output/paper/spontaneous/men/" + l, color=(0.8, 0.8, 0.8, 1.0))
    #     m.to_unit_cube()
        
    #     nome = l.split('.')            
    #     print(nome)
    #     render(
    #         [m],
    #         n_frames=200,
    #         size=(256,256),
    #         camera_position=(0.0, 0.15, 1.5),
    #         up_vector=(0, 1, 0),
    #         behaviours=[
    #             SaveFrames('imgs/paper/spontaneous/men/' + nome[0] + '.png')
    #         ]
    #     )
           
    

