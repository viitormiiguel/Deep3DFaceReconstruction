#!/usr/bin/bash

source C:/Users/vitor/anaconda3/etc/profile.d/conda.sh

conda activate deep3d

python demo.py -i https://faces-app.nyc3.cdn.digitaloceanspaces.com/input/id3/footage3.jpg -s E:/PythonProjects/tesis-app/test/output/models/3d/deep3d/id1

sleep 1m

conda deactivate