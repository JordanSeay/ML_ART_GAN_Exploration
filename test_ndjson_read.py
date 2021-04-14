import numpy as np
from PIL import Image, ImageDraw
import ndjson



# data = np.load("full_numpy_bitmap_cat.npy")

# A = np.reshape(data[0], (28,28))
# im = Image.fromarray(A)
# im.show()

# for A in data:
#     A = np.reshape(A, (25,25))
#     im = Image.fromarray(A)
#     im.save("your_file.jpeg")


with open('full_simplified_The Eiffel Tower.ndjson') as f:
    data = ndjson.load(f)
#print(data[0])
#print(data[0]['drawing'])

stroke_list  = data[0]['drawing']
print(stroke_list)




# print(stroke_list)
# new_stroke_list = []
# for stroke in stroke_list:
#     new_stroke = []
#     for i in stroke:
#         new_stroke.append(np.array(i))
#     new_stroke = np.array(new_stroke)
#     new_stroke_list.append(new_stroke)

# print(new_stroke_list)
# print(type(new_stroke_list))
#new_stroke_list = np.array(new_stroke_list)

# def list_helper(l):
    
#     #if l is a list of ints
#     if not (type(l[0]) == list):
#         return np.asarray(l)
#     else:
#         np.asarray([list_helper(i) for i in l])



# print(stroke_list)
# print('\n')
# print(np.asarray([ list_helper(i) for i in stroke_list]))
    











def draw_it(raw_strokes):
    image = Image.new("P", (255,255), color=255)
    image_draw = ImageDraw.Draw(image)
    

    for stroke in eval(raw_strokes):
       


        for i in range(len(stroke[0])-1):

            image_draw.line([stroke[0][i], 
                             stroke[1][i],
                             stroke[0][i+1], 
                             stroke[1][i+1]],
                            fill=0, width=6)
    image.show()
    print(np.array(image))
    return np.array(image)

#draw_it(new_stroke_list)

# load from file-like objects
# with open('full-raw-The Eiffel Tower.ndjson') as f:
#     data = ndjson.load(f)
# print(data[0]['drawing'])
# drawing  = np.array(data[0]['drawing'])
# print()


# im = Image.fromarray(drawing)
# im.show()
