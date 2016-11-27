#!/bin/bash
MBTILES=$1

cp $MBTILES work-$MBTILES
sqlite3 work-$MBTILES < add_logs.sql
python tile_size.py work-$MBTILES
rm work-$MBTILES

