"""This module tests the emotion_detection function."""
# Import unittest library.
from EmotionDetection.emotion_detection import emotion_detector
import unittest

# Create a class to test the test statments.
class TestEmotionDetector(unittest.TestCase):
    """The class is used to call the multiple tests."""

    def test_emotion_detector(self):
        """This is the test case function."""

        # Test case for 'joy' dominant emotion.
        stat_1 = emotion_detector("I am glad this happened.")
        self.assertEqual(stat_1['dominant_emotion'], 'joy')

        # Test case for 'anger' dominant emotion.
        stat_2 = emotion_detector("I really mad about this.")
        self.assertEqual(stat_2['dominant_emotion'], 'anger')

        # Test case for 'disgust' dominant emotion.
        stat_3 = emotion_detector("I feel disgusted just hearing about this.")
        self.assertEqual(stat_3['dominant_emotion'], 'disgust')

        # Test case for 'sadness' dominant emotion.
        stat_4 = emotion_detector("I am so sad about this.")
        self.assertEqual(stat_4['dominant_emotion'], 'sadness')

        # Test case for 'fear' dominant emotion.
        stat_5 = emotion_detector("I am really afraid that this will happen.")
        self.assertEqual(stat_5['dominant_emotion'], 'fear')


# Call the tests.
unittest.main()
