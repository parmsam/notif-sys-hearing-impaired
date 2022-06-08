# Notification System for the Hearing Impaired

## Motivation
Hearing impaired individuals commonly use alerting devices for notification of an event taking place (a doorbell, a telephone, or alarm). [1,2] The landscape of alerting devices to notify hearing impaired individuals is expensive and has had seemingly limited attention from the open source community thus far. [3-5] Here we propose an notification system built around a Raspberry Pi to notify a hearing impaired individual of trigger sounds such as a baby crying or dog barking in their surrounding environment, with setup instructions (see technical approach) made publicly available. This project was created as part of the CS 498 Internet of Things class at University of Illinois Urbana-Champaign in Spring 2022. 

## Materials
* Raspberry Pi 4
* [Raspberry Pi 4 Case](https://www.amazon.com/dp/B07WCKLFLP)
* [USB Conference Microphone](https://www.amazon.com/gp/product/B07PXQCYKV/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
* Mini display for Raspberry Pi 4 

## Acknowledgements
Credit to Fabio Manganiello for building the Micmon library used in this project. [6-7].

## Programs
* train-baby.py, train-dog.py - training scripts to build models for baby crying and dog barking
* send_text.py - program to send text message to phone number via Twilio API
* predict_from_microphone_baby.py, predict_from_microphone_dog.py - prediction programs for baby crying and dog barking audio recognition models
* streamlit-app.py - prototype streamlit app 
* datasets/ - datasets used to train models
* models/ - models built using training programs and datasets

## Technical Approach

In this project, we used a Raspberry Pi 4 Model B 4GB with a $20 conference microphone. The Raspberry Pi used Raspian OS with the Armv7l architecture loaded with Python 3.7.3. We installed Tensorflow 2.5.2 on our Raspberry Pi and PC. The version of Tensorflow 2 was installed on the Raspberry Pi using a virtual environment in Python. [8]

The PC was used for model training the models but training could also have been done directly on the Raspberry Pi. Models were copied over to the Raspberry Pi. It is important to note that we leveraged the prior work of Fabio Manganiello [6,7] who previously built a smart baby monitor on a Raspberry Pi. [7] Fabio authored the Micmon library, a generic library and set of utilities for sound monitoring, which we used for this project. [7] Micmon is used to generate  datasets from raw audio samples. Micmon also uses tensorflow and keras to define and train sound detection models. The example model training script available on the Micmon github repository was used. [6]

## References
1. https://www.nidcd.nih.gov/health/assistive-devices-people-hearing-voice-speech-or-language-disorders
2. https://www.healthyhearing.com/help/assistive-listening-devices/alerting-devices
3. https://mn.gov/deaf-hard-of-hearing/assistive-technology/alerting-devices/
4. https://github.com/search?q=alert+hearing+impaired
5. https://github.com/search?q=alert+deaf
6. https://github.com/BlackLight/micmon
7. https://blog.platypush.tech/article/Create-your-smart-baby-monitor-with-Platypush-and-Tensorflow
8. https://www.youtube.com/watch?v=QLZWQlg-Pk0

## Team Members
* Praveen Pathri
* Sam Parmar
* Jeff Zhan
* Dylan Love


