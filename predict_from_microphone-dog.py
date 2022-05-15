import os
import time

from micmon.audio import AudioDevice
from micmon.model import Model
from send_text.py import send_text

# Path to a previously saved sound detection Tensorflow model
model_dir = os.path.expanduser('~/models/sound-detect-dog')
model = Model.load(model_dir)

audio_system = 'alsa'        # Supported: alsa and pulse
audio_device = 'plughw:1,0'  # Get list of recognized input devices with arecord -l

last_positive_prediction = None

with AudioDevice(audio_system, device=audio_device) as source:
    for sample in source:
        source.pause()  # Pause recording while we process the frame
        prediction = model.predict(sample)
        #Checks for a positive prediction, waits 5 mintues between sending notifications
        if prediction == "positive":
            if (last_positive_prediction == None) or (time.time() - last_positive_prediction > 300):
                last_positive_prediction = time.time()
                send_text("Dog barking has been detected")
        print(prediction)
        source.resume() # Resume recording
