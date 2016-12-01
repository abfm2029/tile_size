import sqlite3
import sys
import math
import itertools
import matplotlib.pyplot as plt

file = sys.argv[1]

conn = sqlite3.connect(file)
c = conn.cursor()

c.execute('SELECT MAX(zoom_level) FROM map')
max_zoom = list(c)[0][0]

size = [None]*(max_zoom+1)
top_decile = [None]*(max_zoom+1)
for zoom in range(0,max_zoom+1):
	c.execute('SELECT LENGTH(tile_data) FROM tiles WHERE zoom_level = "'+str(zoom)+'"')	# Get size of tiles based on the zoom_level
	size[zoom] = sorted(list(itertools.chain.from_iterable(list(c))))
	leng = len(size[zoom])
	top_decile[zoom] = size[zoom][int(math.floor(leng*0.9)):]				# Take the approximate top 10% of the tile sizes

plt.boxplot(size)
plt.title('Tile size')
plt.xlabel('Zoom')
plt.ylabel('Size (bytes)')
plt.xticks(range(1,max_zoom+2), range(0,max_zoom+1))
plt.show()

plt.boxplot(top_decile)
plt.title('Tile size')
plt.xlabel('Zoom')
plt.ylabel('Size (bytes)')
plt.xticks(range(1,max_zoom+2), range(0,max_zoom+1))
plt.show()

