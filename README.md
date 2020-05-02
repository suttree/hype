Python setup:
https://realpython.com/python-speech-recognition/

Pulseaudio setup:
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
