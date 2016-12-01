# tile_size
Calculate the size of PBF tiles in an mbtiles and plot with matplotlib

## Installation

Make sure you have the sqlite3 and matplotlib libraries installed for Ubuntu

## Usage

Simply run "python tile_size.py tile.mbtiles" The final output will be two boxplots, split into zooms with the size in bytes and the bottom axis the zoom. The first boxplot is all the tiles, the second boxplot is the rough top 10% of the tile sizes
