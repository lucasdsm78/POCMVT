import abjad
from datetime import datetime
from const import *


frequences = [
(440, 0),
(None, 400), 
(220, 1000), 
(440, 1230), 
(440, 1500), 
]
# une fonction
for item in frequences:
	print(item, get_nearest_note(item[0]))


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

to write a respiration, use r + same nb as for any other rythm
ex : "c4 r8 g8"

~ to mark a legato
"""
def generate_score():
	#string = "c'8 f' g' a' d' g' a' b''8 e''4 a' b' c'' f' b' c'' d''4"
	#string = "c'4 c8 c''16 c'''"
	string = "c'8 c' d'4 c' f' e'2 c'8 c' d'4 c' g' f'2"
	voice_1 = abjad.Voice(string, name="Voice_1")
	staff_1 = abjad.Staff([voice_1], name="Staff_1")
	abjad.show(staff_1, output_directory=("/tmp/"))



#generate_score()
#print(get_rythm(.2))

