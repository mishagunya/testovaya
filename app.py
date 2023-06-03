from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Пробная строка для проверки деплоя на render.com!'



from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def draw_cross(image_path, color, is_horizontal):
    img = Image.open(image_path).convert('RGB')
    pixels = img.load()
    width, height = img.size

    if is_horizontal:
        for i in range(width):
            pixels[i, height // 2] = color
    else:
        for j in range(height):
            pixels[width // 2, j] = color

    img.save('output.png')

   
    # Plot color distribution of output image
    img_output = Image.open('output.png')
    r, g, b = img_output.split()
    colors = ('r', 'g', 'b')
    for channel, color in zip((r, g, b), colors):
        plt.hist(np.array(channel).ravel(), bins=256, color=color, alpha=0.5)

    img1 = Image.open(image_path)
# Show original and output images
    fig, axs = plt.subplots(1)
    
    axs.imshow(img_output)
    axs.set_title('Output Image')

    plt.show()

# Example usage:
draw_cross('/mntDrive/MyDrive/python/dataf/1.jpg', (255, 0, 0), is_horizontal=False)
