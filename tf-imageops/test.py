import tensorflow
import PIL
from PIL import Image, ImageFilter
import cv2
import sklearn
import skimage
import numpy

# Print library versions

for library in ("tensorflow", "PIL", "cv2", "sklearn", "skimage", "numpy"):
    print(library, locals()[library].__version__)

# Test skimage

chelsea_array = skimage.data.chelsea()  # Load example cat
assert skimage.filters.gaussian(chelsea_array, 5, multichannel=True).any()  # Blur it

# Test PIL

chelsea_image = Image.fromarray(chelsea_array)  # Convert cat to PIL
assert chelsea_array.shape[:2] == chelsea_image.size[::-1]  # Transposed, but correct size?
assert chelsea_image.filter(ImageFilter.GaussianBlur(5))  # Blur PIL cat

# Test OpenCV

chelsea_cv = skimage.img_as_ubyte(chelsea_array)  # Convert cat to CV2
assert chelsea_array.shape == chelsea_cv.shape  # Size correct?
assert cv2.blur(chelsea_cv, (5, 5)).any()  # Blur CV2 cat

# Test Tensorflow

x = tensorflow.constant(chelsea_array)
rs = tensorflow.reduce_sum(x)

with tensorflow.Session() as sess:
    assert float(sess.run(rs))
