from os import listdir
import numpy as np
import cv2

def get_images():
    img_list = [ d for d in listdir("original images path")]
    print(img_list)
    for t in range(len(img_list)):
        original_path_p = 'original images path'
        original_path = original_path_p + img_list[t]
        reference_image_0 = cv2.imread(original_path, 1)
        b, g, r = cv2.split(reference_image_0)
        w, h, c = reference_image_0.shape
        x = [b, g, r]
        reference_color = np.empty((w, h, c))
        for i in range(c):
            reference_color[:, :, i] = x[i]
        reference_color = cv2.cvtColor(reference_image_0, cv2.COLOR_BGR2GRAY)
        m, n = reference_color.shape
        reference_fake = np.zeros((m, n, 3))
        for i in range(m):
            for j in range(n):
                if reference_color[i][j] == 255:
                    reference_fake[i][j][0] = 0
                    reference_fake[i][j][1] = 0
                    reference_fake[i][j][2] = 0
                elif reference_color[i][j] == 0:
                    reference_fake[i][j][0] = 0
                    reference_fake[i][j][1] = 255
                    reference_fake[i][j][2] = 255
                else:
                    reference_fake[i][j][0] = 0
                    reference_fake[i][j][1] = 0
                    reference_fake[i][j][2] = 255
        str0 = 'the path that stores the results'
        str1 = str0 + img_list[t]
        cv2.imwrite(str1, reference_fake)

if __name__ == '__main__':
    get_images()