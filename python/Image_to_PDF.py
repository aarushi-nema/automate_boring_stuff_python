from PIL import Image

image1 = Image.open(r'Financial_Express_coverage.jpeg')
im1 = image1.convert('RGB')
im1.save('Financial_Express_coverage.pdf')
