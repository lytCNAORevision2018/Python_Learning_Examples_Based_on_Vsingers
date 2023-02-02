import unittest
from survey import AnonymousSurvey
class TestAnoymousSurvey(unittest.TestCase):
    """针对AnoymousSurvey类的测试。"""
    def test_store_single_response(self):
        """测试单个的答案会被妥善地存储。"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response("Chinese")
        self.assertIn('Chinese',my_survey.responses)
    def test_store_three_responses(self):
        """测试三个答案会被妥善存储。"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['Chinese','English','Spanish']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses())
if __name__ == '__main__':
    unittest.main()