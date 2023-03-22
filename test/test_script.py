# Import necessary modules

import os
import sys
from pathlib import Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Import the function to test
from script import action

# Define the test function
def test_action():

    # Call the function with test inputs
    o = 'test/test_outputs/'
    oh = 'test/test_outputs/test_header/'
    wcf = 'test/test_wordClouds'
    lolf = 'test/test_listOfLinks'
    fpaf = 'test/test_figuresperArticle'

    action(oh,o,wcf, lolf, fpaf)

    # Check that the expected files were created
    assert os.path.exists(wcf)
    assert os.path.exists(lolf)
    assert os.path.exists(fpaf)
    assert os.path.exists(os.path.join(fpaf, 'figure.png'))
    assert os.path.exists(os.path.join(wcf, 'test_file.png'))
    assert os.path.exists(os.path.join(lolf, 'test_file.txt'))

    # Clean up the test files
    os.remove(os.path.join(wcf, 'test_file.png'))
    os.remove(os.path.join(lolf, 'test_file.txt'))
    os.remove(os.path.join(fpaf, 'figure.png'))
