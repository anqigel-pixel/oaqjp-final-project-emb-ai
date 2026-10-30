import unittest
from EmotionDetection.emotion_detection import emotion_detector 

class Test_emotiondetection(unittest.TestCase):
    def test_emotion_detection(self):
        test1 = 'I am glad this happened'
        self.assertEqual(test1['dominant_emotion'], 'joy')
        test2 = 'I am really mad about this'
        self.assertEqual(test2['dominant_emotion'], 'anger')
        test3 = 'I feel disgusted just hearing about this'
        self.assertEqual(test3['dominant_emotion'], 'disgust')
        test4 = 'I am glad this happened'
        self.assertEqual(test4['dominant_emotion'], 'joy')
        test5 = 'I am so sad about this'
        self.assertEqual(test5['dominant_emotion'], 'sadness')
        test6 = 'I am really afraid that this will happen'
        self.assertEqual(test6['dominant_emotion'], 'fear')

unittest(main)        