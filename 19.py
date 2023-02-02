from survey import AnonymousSurvey
#定义一个问题，并创建一个调查。
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

#显示问题并存储答案。
print("Press q to quit this program asking you questions.")
my_survey.show_question()
while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_response(response)
#显示调查结果。

print("\n Thank you for your time!")
my_survey.show_results()