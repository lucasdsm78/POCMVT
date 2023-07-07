# region used to import from parent
import os, sys
parent = os.path.abspath('.')
sys.path.insert(1, parent)
#endregion

from const import * 


#region init arrays to check
ARRAY_FREQ_NOTE_1=[
(32.7, "c'"),
(34.65, "cs'"),
(36.71, "d'"),
(38.89, "ds'"),
(41.2, "e'"),
(43.65, "f'"),
(46.25, "fs'"),
(49, "g'"),
(51.91, "gs'"),
(55, "a'"),
(58.27, "as'"),
(61.74, "b'"),
]

ARRAY_FREQ_NOTE_2=[
(65.41, "c''"),
(69.3, "cs''"),
(73.42, "d''"),
(77.78, "ds''"),
(82.41, "e''"),
(87.31, "f''"),
(92.5, "fs''"),
(98, "g''"),
(103.83, "gs''"),
(110, "a''"),
(116.54, "as''"),
(123.47, "b''"),
]

ARRAY_FREQ_NOTE_3=[
(130.81, "c'''"),
(138.59, "cs'''"),
(146.83, "d'''"),
(155.56, "ds'''"),
(164.81, "e'''"),
(174.61, "f'''"),
(185, "fs'''"),
(196, "g'''"),
(207.65, "gs'''"),
(220, "a'''"),
(233.08, "as'''"),
(246.94, "b'''"),
]

ARRAY_FREQ_NOTE_4=[
(261.63, "c''''"),
(277.18, "cs''''"),
(293.66, "d''''"),
(311.13, "ds''''"),
(329.63, "e''''"),
(349.23, "f''''"),
(369.99, "fs''''"),
(392, "g''''"),
(415.3, "gs''''"),
(440, "a''''"),
(466.16, "as''''"),
(493.88, "b''''"),
]

ARRAY_FREQ_NOTE_5=[
(523.25, "c'''''"),
(554.37, "cs'''''"),
(587.33, "d'''''"),
(622.25, "ds'''''"),
(659.25, "e'''''"),
(698.46, "f'''''"),
(739.99, "fs'''''"),
(783.99, "g'''''"),
(830.61, "gs'''''"),
(880, "a'''''"),
(932.33, "as'''''"),
(987.77, "b'''''"),
]

ARRAY_FREQ_NOTE_6=[
(1046.5, "c''''''"),
(1108.73, "cs''''''"),
(1174.66, "d''''''"),
(1244.51, "ds''''''"),
(1318.51, "e''''''"),
(1396.91, "f''''''"),
(1479.98, "fs''''''"),
(1567.98, "g''''''"),
(1661.22, "gs''''''"),
(1760, "a''''''"),
(1864.66, "as''''''"),
(1975.53, "b''''''"),
]

ARRAY_FREQ_NOTE_7=[
(2093, "c'''''''"),
(2217.46, "cs'''''''"),
(2349.32, "d'''''''"),
(2489.02, "ds'''''''"),
(2637.02, "e'''''''"),
(2793.83, "f'''''''"),
(2959.96, "fs'''''''"),
(3135.96, "g'''''''"),
(3322.44, "gs'''''''"),
(3520, "a'''''''"),
(3729.31, "as'''''''"),
(3951.07, "b'''''''"),
]

ARRAY_FREQ_NOTE_8=[
(4186.01, "c''''''''"),
(4434.92, "cs''''''''"),
(4698.63, "d''''''''"),
(4978.03, "ds''''''''"),
(5274.04, "e''''''''"),
(5587.65, "f''''''''"),
(5919.91, "fs''''''''"),
(6271.93, "g''''''''"),
(6644.88, "gs''''''''"),
(7040, "a''''''''"),
(7458.62, "as''''''''"),
(7902.13, "b''''''''")
]
#endregion

def test_note_octava_0():
    for item in ARRAY_FREQ_NOTE_0:
    	assert get_nearest_note(item[0])[1] == item[1]

def test_note_octava_1():
    for item in ARRAY_FREQ_NOTE_1:
    	assert get_nearest_note(item[0])[1] == item[1]

def test_note_octava_2():
    for item in ARRAY_FREQ_NOTE_2:
    	assert get_nearest_note(item[0])[1] == item[1]

def test_note_octava_3():
    for item in ARRAY_FREQ_NOTE_3:
    	assert get_nearest_note(item[0])[1] == item[1]

def test_note_octava_4():
    for item in ARRAY_FREQ_NOTE_4:
    	assert get_nearest_note(item[0])[1] == item[1]

def test_note_octava_5():
    for item in ARRAY_FREQ_NOTE_5:
    	assert get_nearest_note(item[0])[1] == item[1]

def test_note_octava_6():
    for item in ARRAY_FREQ_NOTE_6:
    	assert get_nearest_note(item[0])[1] == item[1]

def test_note_octava_7():
    for item in ARRAY_FREQ_NOTE_7:
    	assert get_nearest_note(item[0])[1] == item[1]

def test_note_octava_8():
    for item in ARRAY_FREQ_NOTE_8:
    	assert get_nearest_note(item[0])[1] == item[1]

def test_inaccuracy_la_440():
	array = [428, 430, 435, 440, 445, 450, 453]
	for item in array:
		assert get_nearest_note(item)[1] == "a''''"

def test_no_frequency():
	assert get_nearest_note(None) == (None, "r")