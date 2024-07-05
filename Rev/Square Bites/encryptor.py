import sys

# 0CTF{A_S1mpl3_Gr1d_enc__}
flag = sys.argv[1]
# print(flag)

width = int(len(flag) ** (0.5))

grid = [[0 for i in range(width)] for _ in range(width)]

for row, rowVals in enumerate(grid):
    for col, val in enumerate(rowVals):
        grid[row][col] = ord(flag[row*width + col]) ^ (row + col)

enc = b""
for row in grid:
    for val in row:
        enc += chr(val).encode()

with open("encrypted", "wb") as f:
    f.write(enc)