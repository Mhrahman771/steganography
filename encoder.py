import numpy as np
from PIL import Image

#convert source image to NUMPY & store size
#image mode RGB  --> n = 3
#image mode RGBA --> n = 4
#not any mode --> n = 0
#calculate total pixel

def encode(src, message, dest):
    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata())) #content of image as a sequence object containing pixel values
    print(array)
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    else:
        n =0
    print(n)
    total_pixels = array.size//n

#add delimiter (“$t3g0") end of secret message
#helps to know when to stop

    if message != None:
        message += "$t3g0"
    else:
        message = ""
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

#checking if total pixel available sufficient for
#secret message or not

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1
#updated pixels array
#create and save as destinationa output message

        array = array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Image Encoded Successfully")

encode("C:\\Users\\RayMan\\Downloads\\image.png", "GOOD_BOY_RAHMAN", "C:\\Users\\RayMan\\Downloads\\image1.png")