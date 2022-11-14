# Download video from youtube using youtube-dl
youtube-dl  https://youtu.be/sf6JLgKbhSU

#convert video to mp4 
ffmpeg -i *.mkv video.mp4 

#remove old file
rm *.mkv

# split the video insto images using ffmpeg
ffmpeg -r 1 -i video.mp4 -r 1 "images/%03d.png" 


#open the images directory wit the default program(file explorer)
xdg-open images
