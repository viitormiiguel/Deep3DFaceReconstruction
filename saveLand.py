from mtcnn import MTCNN
import os
import cv2
import argparse

parser = argparse.ArgumentParser(description='Get landmarks from images.')
parser.add_argument('--input_dir', type=str, default="./input/will2",
                    help='directory with the input images')

args = parser.parse_args()
input_dir = args.input_dir

detector = MTCNN()
for filename in os.listdir(input_dir):
    basename = os.path.splitext(filename)[0]

    image_path = f"{input_dir}/{filename}"
    text_path = f"{input_dir}/{basename}.txt"

    img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    result = detector.detect_faces(img)
    keypoints = result[0]['keypoints']
    text_file = open(text_path, "a")
    for value in keypoints.values():
        text_file.write(f"{value[0]}\t{value[1]}\n")
    print(f"File successfully written: {text_path}")
    text_file.close()