from PIL import Image
from time import sleep, time

ascii_chars1 = "@%#*+=-:. "
ascii_chars2 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
len_ac = len(ascii_chars1)
# image = Image.open(input("Path to the image to convert: ")).convert("L")
image = Image.open("/users/keke/Desktop/mdr.png").convert("L")
pixels = image.load()
size = image.size
print(size)
i = 0
d = 2
y_ = x_ = 0

start = time()
for y in range(0, size[1], d*2):
    for x in range(0, size[0], d):
        i += 1
        pixel = pixels[x, y]
        print(ascii_chars1[int(len_ac * (pixel / 256))], end="")
    print()
end = time()

print(f"Total characters: {i}\nTime to execute: {end-start}\nx: {int(size[0] / d)} | y: {int(size[1]/(d*2))}")
