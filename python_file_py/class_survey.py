class Survey:
    def __init__(self, question):
        self.question = question
        self.response = []

    def show_question(self):
        print(self.question.rstrip().title())

    def store_response(self, response):
        self.response.append(response)

    def show_result(self):
        print("Survey result: ")
        for i in self.response:
            print(f"\t -- {i.title()}")
