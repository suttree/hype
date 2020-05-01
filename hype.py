import sys, random, time
from inky import InkyPHAT

from PIL import Image, ImageFont, ImageDraw
from font_source_serif_pro import SourceSerifProSemibold
from font_source_sans_pro import SourceSansProSemibold

# TODO:
# centre and relow text/font to fit screen
# pick interesting words to hype

def main(argv):
	import speech_recognition as sr

	# Load our stop words
	file = open('./stoplist.txt', 'r')
	stoplist = file.read().splitlines()
	file.close()

	r = sr.Recognizer()

	while True:
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source) 

			print("Speak Anything :")
			audio = r.listen(source)

			try:
				text = r.recognize_google(audio)
				print("You said : {}".format(text))

				for stopword in stoplist:
					if stopword in text.split():
						text = text.replace(stopword,'').strip()
				print("We said : {}".format(text))

				words = text.split(' ')
				word = random.choice(words)

				if word:
					hype(word)

			except Exception as e:
				print(e)
			#except sr.UnknownValueError:
			#    print("Google Speech Recognition could not understand audio")
			#except sr.RequestError as e:
			#    print("Could not request results from Google Speech Recognition service; {0}".format(e))

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

		print('Sleepee')
		time.sleep(60)

# Adapted from the Pimoroni inkyWhat examples: https://github.com/pimoroni/inky
def hype(word):
	print(word)

	# Set up the correct display and scaling factors
	inky_display = InkyPHAT('black')
	inky_display.set_border(inky_display.BLACK)
	# inky_display.set_rotation(180)

	w = inky_display.WIDTH
	h = inky_display.HEIGHT

	# Create a new canvas to draw on
	img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
	draw = ImageDraw.Draw(img)

	# Load the fonts
	font_size = 44
	font = ImageFont.truetype(SourceSansProSemibold, font_size)

	padding = 20 
	max_width = w - padding
	max_height = h - padding

	below_max_length = False
	while not below_max_length:
			p_w, p_h = font.getsize(word)  # Width and height of quote
			p_h = p_h * (word.count("\n") + 1)   # Multiply through by number of lines

			if p_h < max_height:
					below_max_length = True              # The quote fits! Break out of the loop.

			else:
					font_size = font_size - 2
					font = ImageFont.truetype(SourceSansProSemibold, font_size)

					continue

	# x- and y-coordinates for the top left of the quote
	#word_x = (w - max_width) / 2
	word_x = (max_width - p_w) / 2
	word_y = (max_height - p_h) / 2

	draw.multiline_text((word_x, word_y), word, fill=inky_display.BLACK, font=font, align="left")

	# Display the completed canvas on Inky wHAT
	inky_display.set_image(img)
	inky_display.show()

if __name__ == "__main__":
  main(sys.argv[1:])
