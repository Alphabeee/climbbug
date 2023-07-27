import ddddocr
from PIL import Image
ocr = ddddocr.DdddOcr()
for i in range(0, 100):
    with open(f'picture/{i}.png', 'rb') as f:
        img = f.read()
    text = ocr.classification(img)
    text += '\n'
    with open('test.txt', 'a', encoding='UTF-8') as f:
        f.write(text)
