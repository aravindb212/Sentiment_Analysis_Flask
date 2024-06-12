from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyser(unittest.TestCase):
    def test_sentiment_analyser(self):
        res1 = sentiment_analyzer('i love cognitive')
        self.assertEqual(res1['label'], 'SENT_POSITIVE')
        res2 = sentiment_analyzer('i hate cognitive')
        self.assertEqual(res2['label'], 'SENT_NEGATIVE')
        res3 = sentiment_analyzer('i am neutral in cognitive')
        self.assertEqual(res3['label'], 'SENT_NEUTRAL')


unittest.main()
        