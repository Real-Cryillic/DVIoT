#!/bin/bash

$value = cat ../src/url.txt
echo $value
ffmpeg -re -stream_loop -1 -i ../src/sample-mp4-file-small.mp4 -c copy -f rtsp $value &
