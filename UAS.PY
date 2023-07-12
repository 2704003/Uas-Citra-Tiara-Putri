import cv2
import numpy as np
import math

def median_filter(image, kernel_size):
    result = cv2.medianBlur(image, kernel_size)
    return result

def histogram_equalization(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = cv2.equalizeHist(gray_image)
    return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

def image_stretching(image, alpha, beta):
    result = np.clip(alpha * image + beta, 0, 255).astype(np.uint8)
    return result

def calculate_mse(original_image, processed_image):
    mse = np.mean((original_image - processed_image) ** 2)
    return mse

def calculate_psnr(mse):
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr

# Baca citra
original_image = cv2.imread('C:\\Users\\ACER\\Downloads\\UAS PENGOLAHAN CITRA TIARA PUTRI\\lena.jpg')

# Proses median filter
kernel_size = 3
filtered_image = median_filter(original_image, kernel_size)

# Proses histogram equalization
equalized_image = histogram_equalization(original_image)

# Proses image stretching
alpha = 1.2
beta = 10
stretched_image = image_stretching(original_image, alpha, beta)

# Hitung MSE dan PSNR
mse_filtered = calculate_mse(original_image, filtered_image)
psnr_filtered = calculate_psnr(mse_filtered)

mse_equalized = calculate_mse(original_image, equalized_image)
psnr_equalized = calculate_psnr(mse_equalized)

mse_stretched = calculate_mse(original_image, stretched_image)
psnr_stretched = calculate_psnr(mse_stretched)

# Tampilkan nilai MSE dan PSNR
print("Median Filter:")
print("MSE:", mse_filtered)
print("PSNR:", psnr_filtered)

print("Histogram Equalization:")
print("MSE:", mse_equalized)
print("PSNR:", psnr_equalized)

print("Image Stretching:")
print("MSE:", mse_stretched)
print("PSNR:", psnr_stretched)
