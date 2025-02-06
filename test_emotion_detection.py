import unittest
from EmotionDetection.emotion_detection import emotion_detector  # Replace 'your_module' with the actual module name

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        emotions, dominant_emotion = emotion_detector("I am glad this happened")
        self.assertEqual(dominant_emotion, "joy")

    def test_anger(self):
        emotions, dominant_emotion = emotion_detector("I am really mad about this")
        self.assertEqual(dominant_emotion, "anger")

    def test_disgust(self):
        emotions, dominant_emotion = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(dominant_emotion, "disgust")

    def test_sadness(self):
        emotions, dominant_emotion = emotion_detector("I am so sad about this")
        self.assertEqual(dominant_emotion, "sadness")

    def test_fear(self):
        emotions, dominant_emotion = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(dominant_emotion, "fear")

# Run the tests
if __name__ == '__main__':
    unittest.main()