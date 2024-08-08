# Lip_Sync

To Initialize the colab you need to ucreate two files in google drive, one named Wav2Lip and another called Wav2lip.

Store your videos and audio inputs in Wav2Lip

Store the Gan model in the Wav2lip, you can get it from this  [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA?e=n9ljGW)

Now you are ready to access and produce the videos.

Access from this [Colab](https://colab.research.google.com/drive/1UbasjqtuYGs7iLSDWekHZsTa8NK5HjUn?usp=sharing)

# Running Locally the API

Download the Lip_Sync File Locally

Activate the virtual environment in the Lip_Sync file as the requirment.txt folder is not compatible with teh new versions of python

```source env/bin/activate```

Then 

```pip install -r Wav2Lip/requirements.txt```

```wget "https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth" -O "Wav2Lip/face_detection/detection/sfd/s3fd.pth"```

```cd Wav2Lip```

```python lip_sync.py```

Make sure the video and auio files you want to run are saved in the assets file
Flask will run, in which its format is 
http://127.0.0.1:5000/upload/Vid_name/Audio_name

Example:
http://127.0.0.1:5000/upload/input_vid.mpg/input_audio.mp3
