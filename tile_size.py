import sqlite3
import sys
import itertools
import matplotlib.pyplot as plt

file = sys.argv[1]

conn = sqlite3.connect(file)
c = conn.cursor()

c.execute('SELECT MAX(zoom_level) FROM map')
max_zoom = list(c)[0][0]

size = [[]]*(max_zoom+1)
for zoom in range(0,max_zoom+1):
	c.execute('SELECT length(tile_data) FROM map INNER JOIN images on map.tile_id = images.tile_id AND map.zoom_level = "'+str(zoom)+'"')  # Get tiles based on tile_id matching in inner join, that way the zoom_level can be accessed from the images tables
	size[zoom] = list(itertools.chain.from_iterable(list(c)))

plt.boxplot(size)
plt.title('Tile size')
plt.xlabel('Zoom')
plt.ylabel('Size (bytes)')
plt.xticks(range(1,max_zoom+2), range(0,max_zoom+1))
plt.show()
