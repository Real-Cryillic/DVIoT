#!/bin/bash
input="../src/sample-mp4-file-small.mp4"
while IFS= read -r line
do
  echo "$line"
  ffmpeg -re -stream_loop -1 -i file.ts -c copy -f rtsp $line

done < "$input"
