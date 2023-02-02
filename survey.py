class AnonymousSurvey:
    """收集匿名调查问卷的答案"""
    def __init__(self,question):
        """存储一个问题，并为存储答案做准备。"""
        self.question = question
        self.questions = []
    def show_question(self):
        """显示调查问卷。"""
        print(self.question)
    def store_response(self,new_response):
        """存储单份调查问卷。"""
        self.responses.append(new_response)
    def show_results(self):
        """显示收到的所有答卷。"""
        print("Survey Results:")
        for response in self.response():
            print(f"-{response}")