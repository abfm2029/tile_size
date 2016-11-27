# tile_size
Calculate the size of PBF tiles in an mbtiles and plot with matplotlib

This uses logs of OpenStreetMap tileservers in order to better determine what the tile sizes are for tiles that actually matter.

## Installation

Make sure you have the sqlite3 and matplotlib libraries installed for Ubuntu

## Usage

Simply run "bash tile_size.sh tile.mbtiles" when tile.mbtiles is in this directory. The final output will be a boxplot, split into zooms with the size in bytes and the bottom axis the zoom.
