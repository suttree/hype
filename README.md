# Hype!

Just a dumb bot that listens for speech and picks a word it hears to display on a small eink screen. Made for those early WFH-2020 days...

![Image of Hype](https://github.com/suttree/hype/blob/master/hype.jpg?raw=true)

---

## Notes / todo / misc

Install from requirements.txt

Basic python code setup:
https://realpython.com/python-speech-recognition/

Pulseaudio setup (to run for all users, including via cron):
vi /etc/systemd/system/pulseaudio.service:

[Unit]
Description=PulseAudio Daemon

[Install]
WantedBy=multi-user.target

[Service]
Type=simple
PrivateTmp=true
ExecStart=/usr/bin/pulseaudio –system –realtime –disallow-exit –no-cpu-limit

Then ‘systemctl enable pulseaudio’ and ‘systemctl start pulseaudio’ 


Login to https://console.cloud.google.com/ and create creds for Google Speech to text API.
Add those credentials to a file called `google_cloud_speech_credentials.json`
