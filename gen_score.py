import abjad

from datetime import datetime
from const import *
import traceback

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
def generate_score_from_lilypond_str(score_str = "c'8"):
	generate_score_midi(score_str)
	generate_score_pdf(score_str)


def generate_score_pdf(score_str):
	# old fashion way, but not that much customisable
	#voice_1 = abjad.Voice(score_str, name="Voice_1")
	#staff_1 = abjad.Staff([voice_1], name="Staff_1")
	#abjad.show(staff_1, output_directory=("/tmp/"))

	lilypond_file = abjad.LilyPondFile(["""\\version "2.14.2"
	\\book{
		\\header{
			title = "%s"
		}

		\\score{
			{
				\\tempo 4=%d

				%s
			}
		}
	}""" % (FILENAME, TEMPO, score_str)])
	abjad.show(lilypond_file, output_directory=("/tmp/"))

def generate_score_midi(score_str):
	lilypond_file = abjad.LilyPondFile(["""\\version "2.14.2"
	\\score{
		{
			\\tempo 4=%d
			%s
		}
		\\midi{ 
		}
	}""" % (TEMPO, score_str)])
	abjad.show(lilypond_file, output_directory=("/tmp/"))


def generate_score(freq_arr):
	generate_score_from_lilypond_str(translate_frequences_to_lilypond_string(freq_arr))


def translate_frequences_to_lilypond_string(frequences_arr):
	i = 0
	score_str = ""
	while i < len(frequences_arr):
		try:
			current_freq = frequences_arr[i]
			note = get_nearest_note(current_freq[0])
			if(i+1>= len(frequences_arr)):
				score_str += " {note}{rythm}".format(**{"note":note[1], "rythm":"4"})
			else:
				rythm = get_rythm((frequences_arr[i+1][1] - current_freq[1])/1000)
				score_str += " {note}{rythm}".format(**{"note":note[1], "rythm":rythm})

		except Exception as err:
			print("Error: ", err, traceback.format_exc())
		i+=1
	return score_str





if( __name__ == "__main__" ):
	fake_freq_arr = [
	(260, 0),
	(None, 270), 
	(260, 500), 
	(290, 1000), 
	(260, 2000), 
	(350, 3000), 
	(330, 5000), 
	]

	generate_score(fake_freq_arr)
	#generate_score()
