data = [[531, 408, 'A'], [225, 52, 'B'], [594, 242, 'C'], [351, 102, 'D'], [371, 15, 'E'], [569, 353, 'F'], [342, 39, 'G'], [218, 304, 'H'], [428, 260, 'I'], [329, 158, 'J'], [585, 530, 'K'], [71, 114, 'L'], [587, 88, 'M'], [347, 180, 'N'], [180, 332, 'O'], [250, 522, 'P'], [88, 475, 'Q'], [260, 128, 'R'], [328, 505, 'S'], [381, 201, 'T'], [360, 192, 'U'], [414, 313, 'V'], [525, 293, 'W'], [240, 563, 'X'], [117, 546, 'Y'], [507, 127, 'Z']]

square_size = 600

style="""
<style>
    #box{
        background:blue;
        position:relative;
    }
    #box span{
        color:white;
        position:absolute;
    }
</style>
"""

box_template = '<div id="box" style="width:%dpx;height:%dpx;">\n%s\n</div>\n'
letter_template = '<span style="left:%dpx;top:%dpx;">%s</span>\n'
output = []

for p in data:
    output.append( letter_template % (p[0],p[1],p[2]))
print(output)
merged = "".join(output)

print(merged)

f = open("positions.html","w")
f.write(style)
f.write( box_template % (square_size, square_size, merged))
f.close()
