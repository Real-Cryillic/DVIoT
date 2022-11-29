#!/bin/bash
input="../src/url.txt"
while IFS= read -r line
do
  echo "$line"
  ffmpeg -re -stream_loop -1 -i ../src/sample-mp4-file-small.mp4 -c copy -f rtsp $line &

done < "$input"
