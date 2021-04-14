import numpy as np
from PIL import Image, ImageDraw
from tqdm import tqdm
import ndjson

with open('full_simplified_bicycle.ndjson') as f:
    data = ndjson.load(f)


def draw_it(raw_strokes, image_name, dataset_name):
    image = Image.new("RGB", (255,255), color="white")
    image_draw = ImageDraw.Draw(image)
    
    for stroke in raw_strokes:
        for i in range(len(stroke[0])-1):

            image_draw.line([stroke[0][i], 
                             stroke[1][i],
                             stroke[0][i+1], 
                             stroke[1][i+1]],
                            fill=0, width=6)
    image.save(f"./images_{dataset_name}/{image_name}.jpg")
    
    
for i in tqdm(range(len(data))):
    strokes = np.array(data[i]['drawing'])
    draw_it(strokes, i, "bike")

