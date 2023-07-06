# region used to import from parent
import os, sys
parent = os.path.abspath('.')
sys.path.insert(1, parent)
#endregion

from const import * 

TEMPO = 60

ARRAY_TEST_RYTHM = [
(4, 1), 
(3.5, 1), 
(3.05, 1), 

(2.8, 2), 
(2, 2), 
(1.6, 2),

(1.2, 4),  
(1, 4), 
(.8, 4), 

(0.7, 8),
(0.5, 8), 
(0.38, 8),

(0.35, 16),
(0.25, 16),
(0.01, 16)
]

def test_rythm():
    for item in ARRAY_TEST_RYTHM:
    	assert get_rythm(item[0]) == item[1]