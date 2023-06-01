# Camera Setup Notes
- `raspi-config`: enable legacy camera and reboot
- in `/boot/config.txt` change to `dtoverlay=ov5647`
- `vcgencmd get_camera` to check supported / detected / libcamera interface
- `libcamera-hello --qt-preview` based on forums.raspberrypi.com/viewtopic.php?t=338799, somehow enabled X forwarding (maybe on VNC) and need to use this option otherwise get an error with `fd 19`

```
libcamera-hello --qt-preview		# live feed for 5 sec
libcamera-still -t 30000 --timelapse 2000 -o image%04d.jpg --qt-preview
ffmpeg -r 10 -f image2 -pattern_type glob -i 'image*.jpg' -s 1280x720 -vcodec libx264 timelapse.mp4
``` 
