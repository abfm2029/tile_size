import sqlite3
import sys
import matplotlib.pyplot as plt

file = sys.argv[1]
conn = sqlite3.connect(file)
c = conn.cursor()
c.execute('SELECT zoom_level,tile_row,tile_column,tile_id FROM map')
tiles = c.fetchall()
print len(tiles)
size = [[]]*(14+1)
for tile in tiles:
	tile_id = tile[3]
	zoom = tile[0]
	c.execute('SELECT tile_data FROM images WHERE tile_id = "'+tile_id+'"')
	tile_size = len(c.fetchall()[0][0])
	size[zoom]=size[zoom]+[tile_size]

plt.boxplot(size)
plt.show()
