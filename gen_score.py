import abjad
from datetime import datetime


NOW = str(datetime.now().strftime("%Y-%m-%d_%H:%M"))
FILENAME = ("Score_"+NOW)

MAP_RYHTM_NB=[[4, 1], [2, 2], [1, 4], [0.5, 8], [0.25, 16]] # first=value calculted, second= notation value for lilypond
TEMPO = 60 # considered as a tempo for a black note


def get_closest_rythm(duration):
	return min(MAP_RYHTM_NB, key=lambda x:abs(x[0]-duration))

def get_rythm(duration):
	time_ratio = duration * TEMPO / 60
	return get_closest_rythm(duration)[1]


"""
notes:
cs = do #
cf = do b

c =  do 2
c' = do 3 (1 row under the score)
c'' = do 4 ( 2nd interline from top)
c''' = do 5 (2 row over the score)


Rythme:
if don't want rythme, we can juste place the letter corresponding to note
ex : "c f g"

if we want to add rythme, we have to place the number next to the note
ex : "c4 f8 g8"

until the next number change, the rythm is guessed staying put
ex : "c4 f8 g a b c" 

"""
def generate_score():
	#string = "c'16 f' g' a' d' g' a' b' e' a' b' c'' f' b' c'' d''16"
	#string = "c'8 f' g' a' d' g' a' b''8 e''4 a' b' c'' f' b' c'' d''4"
	string = "c'4 c8 c''16 c'''"
	voice_1 = abjad.Voice(string, name="Voice_1")
	staff_1 = abjad.Staff([voice_1], name="Staff_1")
	abjad.show(staff_1, output_directory=("/tmp/"))


generate_score()
print(get_rythm(.2))

