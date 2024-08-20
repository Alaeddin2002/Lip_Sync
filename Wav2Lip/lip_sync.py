import os
from flask import Flask, request, jsonify, send_file
import cv2
from PIL import Image



app = Flask(__name__)

@app.route('/upload/<video>/<audio>')
# Run a command

def lip_sync(video,audio):
    #once /upload/<video>/<audio> is run the command to create a video with the input audio will run, creating the video with inference and saving it 
    #in results file in Wav2Lip file
    #instead of video it should be the video file name example input_vid.mp4
    #instead of audio it should be the video file name example input_audio.mp3
    cmd = "python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face assets/{0} --audio assets/{1}".format(video,audio)
    returned_value = os.system(cmd)  # returns the exit code in unix
    return("file is saved in results file",returned_value)


def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    #This function seperates the video into frames and saves it into a file, so that it can be used in the enhance frame functions
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        #capturing each frame and naming them
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return

@app.route('/frames')
#Once /frames is run it takes the video (saved in results) to and runs the previous functions to capture all the frames in them and save it 
def get_frames():
    #copying the results video into the GFPGAN file
    cmd = "cp  results/result_voice.mp4 GFPGAN"
    returned_value = os.system(cmd)    
    
    #running the frames function
    save_all_frames('GFPGAN/result_voice.mp4', 'Testing', 'sample_video_img')
    os.system("pip ")
    
    #Runningthe command for enhancing framess, new frames are saved in the Testing files
    enhance = "python GFPGAN/inference_gfpgan.py -i Testing -o results -v 1.3 -s 2 --bg_upsampler a"
    enhanced_value = os.system(enhance) 
    return "Frames are Enhanced"  

@app.route('/enhanced_vid/<audio>')
def enhanced_vid(audio):
    #instead of audio it should be the video file name example input_audio.mp3
    #command is run to save all frames into a video and syncing the audio into them
    final = "ffmpeg -y -i results/restored_imgs/sample_video_img_%03d.jpg -i assets/{0} -map 0 -map 1:a -c:v libx264 -pix_fmt yuv420p -c:a aac -strict experimental -shortest output.mp4".format(audio)
    enhanced_mp4= os.system(final)
    #new file will be saved in the Wav2Lip Folder named Output.mp4
    return ("Final Video is saved in the Wav2Lip Folder named Output.mp4")


if __name__ == "__main__":
    app.run(debug=True)
