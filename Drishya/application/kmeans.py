import numpy as np
import cv2

def kmeansImage(imageFile):
    img = cv2.imread(imageFile)
    Z = img.reshape((-1, 3))

    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 5.0)
    K = 3
    ret,label,center=cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_PP_CENTERS, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    return center

    #res = center[label.flatten()]
    #res2 = res.reshape(img.shape)
    #print(center)
    #cv2.imshow('res2',res2)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
