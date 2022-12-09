#!/bin/bash
name="~/DVIoT/src/url.txt"

content=$(cat "$name")
echo "$content"
ffmpeg -re -stream_loop -1 -i ~/DVIoT/src/Animation.mp4 -c copy -f rtsp "$content" &
