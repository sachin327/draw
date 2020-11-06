import base64
from PIL import Image
import io
import numpy as np
def toImage(s):
    imgstring = s[22:]
    imgdata = base64.b64decode(imgstring)
    im = Image.open(io.BytesIO(imgdata))
    im = im.resize((28,28))
    im = im.convert('L')
    im = np.array(im)/255
    im=im.reshape(1,28,28,1)
    return im

