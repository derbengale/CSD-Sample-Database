import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import skimage.io as io
import os
import colorsys

def get_pixel_colors(img, x, y):
    # Get the RGB values of the pixel
    r, g, b = img[y, x, 0], img[y, x, 1], img[y, x, 2]

    # Convert RGB to HSV
    h, s, v = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)

    # Scale the values to the range [0, 255]
    h *= 255.0 / 360.0
    s *= 255.0
    v *= 255.0

    return r, g, b, h, s, v


# img = Image.open(r'C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Haarcascade\All images\YRY1a1_overview.tif')
# img.show()

# img = cv2.imread(r'C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Haarcascade\All images\good.jpg')
 
# filess = [r'C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Haarcascade\All images\1.jpg', r'C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Haarcascade\All images\2.jpg', r'C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Haarcascade\All images\3.jpg', r'C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Haarcascade\All images\4.jpg' ]
# filess = [r'C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Haarcascade\All images\3.jpg' ]
facecols = ["green", "red", "blue", "orange" ]
filess = [r"C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Dokumente\Messdaten\Keyencejpg\YRY3n1_overview.jpg",r"C:\Users\yassi\OneDrive\Dokumente\GitHub\Masterarbeit\Dokumente\Messdaten\Keyencejpg\YRY1a1_overview.jpg"]

def analyze_colors(files,resize_to_percent = 2.5,  show_image=False, add_color = True, face_colors = None):
    more_than_one = len(files) > 1
    # add_color = True if len(files) == 1 else False
    fig = plt.figure(figsize=plt.figaspect(0.5))
    fig.canvas.manager.set_window_title('Color Analyzer')
    axis = fig.add_subplot(2, 2, 1, projection="3d")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    axis.view_init(elev=90, azim=0)
    axis2 = fig.add_subplot(2, 2, 2, projection="3d")
    axis2.set_xlabel("Hue")
    axis2.set_ylabel("Saturation")
    axis2.set_zlabel("Value")
    axis2.view_init(elev=90, azim=0)
    axis3 = fig.add_subplot(2, 2, 3)
    axis3.set_xlabel("R/G/B")
    axis3.set_ylabel("Frequency")
    axis4 = fig.add_subplot(2, 2, 4)
    axis4.set_xlabel("Hue")
    axis4.set_ylabel("Frequency")


    markersize = 100
    i=0
    n_hsv =[]
    n_rgb = []
    markers = ["solid","dotted","dashed","dashdot"]

    


    for file in files:
        name = os.path.basename(file)
        name = name.split(".")[0]
        img = io.imread(file, as_gray=False, plugin='pil', pilmode='CMYK')
        scale_percent = resize_to_percent # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim)
        if show_image:
            plt.imshow(img)
            # plt.show()

        r, g, b = cv2.split(img)
        
        rvals = np.zeros(256)
        gvals = np.zeros(256)
        bvals = np.zeros(256)

        for y in range(len(r)):
            for x in range(len(r[0])):
                rvals[r[y][x]] += 1
                gvals[g[y][x]] += 1
                bvals[b[y][x]] += 1   

        n_rgb.append([rvals, gvals, bvals]) 

        if more_than_one: 
            axis3.plot(rvals, color="red", label = f"R ({name})", linestyle = markers[i])                   
            axis3.plot(gvals, color="green", label = f"G ({name})", linestyle = markers[i])                   
            axis3.plot(bvals, color="blue", label= f"B ({name})", linestyle = markers[i])  
            if i == len(files) - 1:
                axis3.legend()     
        else:
            axis3.plot(rvals, color="red", label = "Red")                   
            axis3.plot(gvals, color="green", label = "Green")                   
            axis3.plot(bvals, color="blue", label= "Blue")  
            axis3.legend()     


            


        if add_color:
            pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
            norm = colors.Normalize(vmin=-1.,vmax=1.)
            norm.autoscale(pixel_colors)
            pixel_colors = norm(pixel_colors).tolist()

        if more_than_one: 
            if face_colors ==  None:
                axis.scatter(r.flatten(), g.flatten(), b.flatten(), marker="o", label = name)
            else:
                axis.scatter(r.flatten(), g.flatten(), b.flatten(), marker="o", facecolors=face_colors[i], label = name)
        else:
            if add_color:
                axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker="o", s=markersize, label = name) 
        



        hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

        h, s, v = cv2.split(hsv_img)

        if more_than_one: 
            if face_colors ==  None:
                axis2.scatter(h.flatten(), s.flatten(), v.flatten(), marker="o", label = name)
            else:
                axis2.scatter(h.flatten(), s.flatten(), v.flatten(), marker="o", facecolors=face_colors[i], label = name)
        else:
            if add_color:
                axis2.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker="o", s=markersize, label = name) 
        
        hue_sum = 0
        q=0
        hvals = np.zeros(256)

        for y in range(len(h)):
            for x in range(len(h[0])):
                hue = h[y][x]
                hvals[hue] += 1
                hue_sum += hue
                q += 1
        mean_hue=hue_sum/q

        n_hsv.append(hvals)
        axis4.plot(hvals)
        if more_than_one:
            axis.legend()
            axis2.legend()

        sum_red = 0
        sum_green = 0
        sum_blue = 0

        for n in range(len(n_rgb[i][0])):
            sum_red += n_rgb[i][0][n]*n
            sum_green += n_rgb[i][1][n]*n
            sum_blue += n_rgb[i][2][n]*n
            
        # print(sum_red)
        sum = sum_red + sum_green + sum_blue
        # print(f"{name} R:G:B= {100*sum_red/sum:.2f}%:{100*sum_green/sum:.2f}%:{100*sum_blue/sum:.2f}%")
        # print(f"R:G:B {name} = {100*sum_red:.0f}:{100*sum_green:.0f}:{100*sum_blue:.0f}")

        # print(f"{name} Mean Hue: {mean_hue:.2f}")

            
        i+=1
    plt.show()
    return mean_hue, 100*sum_red/sum, 100*sum_green/sum, 100*sum_blue/sum, n_rgb, n_hsv

if __name__ == "__main__":
    analyze_colors(filess)