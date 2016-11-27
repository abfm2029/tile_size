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
	c.execute('SELECT length(tile_data) FROM tiles INNER JOIN logs WHERE logs.zoom = "'+str(zoom)+'" AND tiles.tile_column = logs.x AND tiles.tile_row = logs.y AND tiles.zoom_level = logs.zoom;')
	size[zoom] = list(itertools.chain.from_iterable(list(c)))

plt.boxplot(size)
plt.title('Tile size')
plt.xlabel('Zoom')
plt.ylabel('Size (bytes)')
plt.xticks(range(1,max_zoom+2), range(0,max_zoom+1))
plt.show()
