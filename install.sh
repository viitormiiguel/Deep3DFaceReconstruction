#!/usr/bin/bash

## BFM
echo -p 'Downloading... BFM'

wget 'https://brpucrs-my.sharepoint.com/:u:/g/personal/vitor_peres_edu_pucrs_br/ERS7-x8YCNlCnNFgmNOycagBKwP0z3CncSxpLF1xrIhqtg?e=muM4yg&download=1' 

unzip '*.zip'

zip -d 'BFM.zip'

## Models
echo -p 'Downloading... Models'

wget 'https://brpucrs-my.sharepoint.com/:u:/g/personal/vitor_peres_edu_pucrs_br/EcdtDP0hUdxOnr0DqwOuPusBFR19jeRf9BFQ38HwFBJcqQ?e=1CvLhR&download=1'

unzip '*.zip'

zip -d 'model.zip'

## Network
echo -p 'Downloading... Network'

wget 'https://brpucrs-my.sharepoint.com/:u:/g/personal/vitor_peres_edu_pucrs_br/EZN4EEY-ekpGj_xfbvKVNuUBhXfMbhwUtQqet50AN38cQA?e=dtdlkZ&download=1'

unzip '*.zip'

zip -d 'network.zip'

