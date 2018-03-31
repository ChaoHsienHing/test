import numpy as np
import pywt

#data = np.ones((4,4), dtype=np.float64)
data = [[ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.]]

DWT = pywt.dwt2(data, 'haar')
cA, (cH, cV, cD) = DWT
print('DWT----------------------')
print('LL： \n', cA)
print('LH： \n', cH)
print('HL： \n', cV)
print('HH： \n', cD)

IDWT = pywt.idwt2(DWT, 'haar')
print('IDWT---------------------- \n', IDWT)
