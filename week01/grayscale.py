import numpy as np
import cv2
import matplotlib.pyplot as plt


print(
    """welcome to grayscale conversion. Choose your number:
    1. Lightness 
    2. Average
    3. Luminorsity
    """)
answer = int(input('your choice: '))

#---------------------------------#
# data processing

# data sample
img = cv2.imread('./image/dog.jpeg', 1)

# BGR --> RGB
img = img[:, :, [2, 1, 0]]
# --------------------------------#

# vectorization function - answer == 1.
def mean_compute(vector):
    result = vector.mean()

    # scale uint8.
    result = result.astype(np.uint8)
    return result


# lightness solution - answer == 2.
def lightness(vector):
    # convert from uint8 to float.
    # avoid result > 255.
    vector = vector.astype(float)
    result = (vector.max() + vector.min()) / 2

    # back uint8
    result = result.astype(np.uint8)
    return result


# Luminorsity solution - answer == 3.
def luminosity(vector):
    # convert to float
    vector = vector.astype(float)
    result = vector[0]*0.21 + vector[1]*0.72 + vector[2]*0.07

    # back uint8
    result = result.astype(np.uint8)
    return result
# ---------------------------------#


# main
if answer == 1:
    # average_solution
    result = np.apply_along_axis(mean_compute,
                                 axis=2,
                                 arr=img)

    # export
    cv2.imwrite('./image/output_average.jpeg', result)


elif answer == 2:
    # lightness function
    result = np.apply_along_axis(lightness,
                                 axis=2,
                                 arr=img)

    # export
    cv2.imwrite('./image/output_lightness.jpeg', result)


elif answer == 3:
    # luminorsity function
    result = np.apply_along_axis(luminosity,
                                 axis=2,
                                 arr=img)
    cv2.imwrite('./image/output_luminorsity.jpeg', result)
