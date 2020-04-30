from inky import InkyPHAT

from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold

def main(argv):
	hype('Ready...')

	import speech_recognition as sr

	r = sr.Recognizer()
	with sr.Microphone(device_index = 2) as source:
		r.adjust_for_ambient_noise(source) 

		print("Speak Anything :")
		audio = r.listen(source)

		try:
			text = r.recognize_google(audio)
			print("You said : {}".format(text))
			#words = text.split(' ')
			#word = random.choice(words)
			#hype(word)
			#print(word)

	# to record the audio for debugging
	#with open("audio_file.wav", "wb") as file:
	#    file.write(audio.get_wav_data())
	# recognize speech using Sphinx
	#try:
	#    print("Sphinx thinks you said " + r.recognize_sphinx(audio, language='en-GB'))
	#except sr.UnknownValueError:
	#    print("Sphinx could not understand audio")
	#except sr.RequestError as e:
	#    print("Sphinx error; {0}".format(e))

def hype(word):
	# Set up the correct display and scaling factors
	inky_display = InkyPHAT('black')
	inky_display.set_border(inky_display.WHITE)
	# inky_display.set_rotation(180)

	w = inky_display.WIDTH
	h = inky_display.HEIGHT

	# Create a new canvas to draw on
	img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
	draw = ImageDraw.Draw(img)

	# Load the fonts
	font_size = 24

	font = ImageFont.truetype(SourceSansProSemibold, font_size)
	draw.multiline_text((10, 10), word, fill=inky_display.BLACK, font=font, align="left")

	# Display the completed canvas on Inky wHAT
	inky_display.set_image(img)
	inky_display.show()

if __name__ == "__main__":
  main(sys.argv[1:])
