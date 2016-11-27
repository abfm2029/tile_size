.mode csv
.import logs.csv logs
create index logs_zoom_idx on logs(zoom);
create index logs_x_idx on logs(x);
create index logs_y_idx on logs(y);
