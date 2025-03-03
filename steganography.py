import cv2
import numpy as np
from PIL import Image

def encode_text("C:\Users\A\Downloads\pic.jpg", text, output_path):
    image = cv2.imread("C:\Users\A\Downloads\pic.jpg")
    binary_text = ''.join(format(ord(i), '08b') for i in text) + '1111111111111110'  
    data_index = 0
    
    for row in image:
        for pixel in row:
            for i in range(3):  
                if data_index < len(binary_text):
                    pixel[i] = pixel[i] & ~1 | int(binary_text[data_index])
                    data_index += 1
                    
    cv2.imwrite(output_path, image)
    print("Text successfully hidden in", output_path)

def decode_text("C:\Users\A\Downloads\pic.jpg"):
    image = cv2.imread("C:\Users\A\Downloads\pic.jpg")
    binary_text = ""
    
    for row in image:
        for pixel in row:
            for i in range(3):
                binary_text += str(pixel[i] & 1)
    
    text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))
    return text.split('1111111111111110')[0]

# Example usage
# encode_text('input.png', 'Secret Message', 'output.png')
# print(decode_text('output.png'))
