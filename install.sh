#!/usr/bin/bash

## BFM
echo 'Downloading... BFM'

wget --output-document BFM.zip 'https://brpucrs-my.sharepoint.com/:u:/g/personal/vitor_peres_edu_pucrs_br/ERS7-x8YCNlCnNFgmNOycagBKwP0z3CncSxpLF1xrIhqtg?e=45mkbN&download=1' 
unzip 'BFM.zip'
rm -rf BFM.zip

## Models
echo 'Downloading... Models'

wget --output-document model.zip 'https://brpucrs-my.sharepoint.com/:u:/g/personal/vitor_peres_edu_pucrs_br/EcdtDP0hUdxOnr0DqwOuPusBFR19jeRf9BFQ38HwFBJcqQ?e=1CvLhR&download=1'
unzip 'model.zip' 
rm -rf model.zip

## Network
echo 'Downloading... Network'

wget --output-document network.zip 'https://brpucrs-my.sharepoint.com/:u:/g/personal/vitor_peres_edu_pucrs_br/EZN4EEY-ekpGj_xfbvKVNuUBhXfMbhwUtQqet50AN38cQA?e=dtdlkZ&download=1'
unzip 'network.zip' 
rm -rf network.zip
