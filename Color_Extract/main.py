from colorthief import ColorThief
import matplotlib.pyplot as plt 
import colorsys

img = "imgs/img1.jpg"
ct = ColorThief(img)
palette = ct.get_palette(color_count=5)                    # get 5 most dom colors

"""uncomment to get output
for color in palette:
    print(color)                                           # rgb
    print(f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}')  # convert to hex code
    print(colorsys.rgb_to_hsv(*color))                     # hsv
    print(colorsys.rgb_to_hls(*color))                     # hls
"""
hexlist = []

for color in palette:
    hexval = f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'
    hexlist.append(hexval)

plt.imshow([[palette[i] for i in range(5)]])
plt.title(f'Dominant Colors of {img}', fontsize=10)
plt.xticks(range(len(hexlist)), [i for i in hexlist])      # set xticks to a range of len(hexlist) and replace with hexlist vals
plt.yticks([])                                             # this makes yticks empty, basically getting rid of the yaxis
plt.xlabel('Hex Val')

plt.show()

