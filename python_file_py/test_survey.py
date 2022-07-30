import unittest
from class_survey import Survey


class TestSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = Survey(question)
        self.responses = ['english', 'chinese', 'japanese']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[1])
        self.assertIn('chinese', self.my_survey.response)

    def test_store_three_response(self):
        for i in self.responses:
            self.my_survey.store_response(i)
        for i in self.responses:
            self.assertIn(i, self.responses)

if __name__ == '__main__':
    unittest.main()
