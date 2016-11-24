import sqlite3
import sys
import itertools
import matplotlib.pyplot as plt

file = sys.argv[1]

conn = sqlite3.connect(file)
c = conn.cursor()

max_zoom = 14
size = [[]]*(max_zoom+1)
for zoom in xrange(0,max_zoom+1):
	c.execute('SELECT tile_data FROM map INNER JOIN images on map.tile_id = images.tile_id AND map.zoom_level = "'+str(zoom)+'"')  # Get tiles based on tile_id matching in inner join, that way the zoom_level can be accessed from the images tables
	tiles=list(itertools.chain.from_iterable(list(c)))	# Flatten results to a single list
	size[zoom]=[len(tile) for tile in tiles]		# Get the size

plt.boxplot(size)
plt.title('Tile size')
plt.xlabel('Zoom')
plt.ylabel('Size (bytes)')
plt.xticks(xrange(1,max_zoom+2), xrange(0,max_zoom+1))
plt.show()
