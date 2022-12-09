#!/bin/bash
name="../src/url.txt"

content=$(cat "$name")
echo "$content"
ffmpeg -re -stream_loop -1 -i ../src/Animation.mp4 -c copy -f rtsp "$content" &
