from playsound import playsound
import moviepy.editor
print(
    "please make sure you make the name of the file ['sample.mp4'].. ".upper())
ans = "y"
while ans == "y":
    fm = "sample.mp4"
    videotape = str(input("enter file name:"))
    if videotape != fm:
        print("please use mp4 format..".upper())
    else:
        video = moviepy.editor.VideoFileClip(
            "D:\\convert videos to audio\\sample.mp4")
        audio = video.audio
        audio.write_audiofile("D:\\convert videos to audio\\note.mp3")
        playsound('D://convert videos to audio//note.mp3')
        print('your sound now is extracting and running enjoy baby...'.upper())
        ans = input(
            "do you want to again this process you can press (y or n): ")
        if ans == "n":
            print("THANKS MAN..")
