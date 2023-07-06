from datetime import datetime

NOW = str(datetime.now().strftime("%Y-%m-%d_%H:%M"))
FILENAME = ("Score_"+NOW)

ARRAY_RYHTM_NB=[(4, 1), (2, 2), (1, 4), (0.5, 8), (0.25, 16)] # first=value calculted, second= notation value for lilypond
TEMPO = 60 # considered as a tempo for a black note


ARRAY_OCTAVA =[(1, 0), (2, 1), (4, 2),  (8, 3), (16, 4), (32, 5),  (64, 6), (128, 7), (256, 8)]

ARRAY_FREQ_NOTE_0=[
(16.35, 'c'),
(17.32, 'cs'),
(18.35, 'd'),
(19.45, 'ds'),
(20.6, 'e'),
(21.83, 'f'),
(23.12, 'fs'),
(24.5, 'g'),
(25.96, 'gs'),
(27.5, 'a'),
(29.14, 'as'),
(30.87, 'b'),
]

def get_nearest_octava(freq):
	value = (freq / ARRAY_FREQ_NOTE_0[len(ARRAY_FREQ_NOTE_0)-1][0])
	for item in ARRAY_OCTAVA:
		if(item[0]>=value):
			return item
	return ARRAY_OCTAVA[len(ARRAY_OCTAVA)-1]

def get_nearest_note(freq):
	if(freq is None):
		return (None, "r")
	octava = get_nearest_octava(freq)
	note = min(ARRAY_FREQ_NOTE_0, key=lambda x:abs(x[0] - (freq/octava[0]) ))
	return (note[0], (note[1]+("'"*octava[1])))


# carefull, here we return only the rythm value, no need of the duration
def get_closest_rythm(duration):
	return min(ARRAY_RYHTM_NB, key=lambda x:abs(x[0]-duration))[1]

def get_rythm(duration):
	time_ratio = duration * TEMPO / 60
	return get_closest_rythm(duration)