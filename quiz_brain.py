class Brain:
    def __init__(self, question_list, qs):
        self.question_no = 0
        self.question_list = question_list
        self.score = 0
        self.qs = qs

    def still_has_qs(self):
        if self.question_no < self.qs:
            return True
        else:
            
            return False

    def next_question(self):
        qs = self.question_list[self.question_no].text
        ans = self.question_list[self.question_no].answer
        u_answer = input(f"Qs.{self.question_no + 1}: {qs} (True or False): ")
        self.question_no += 1
        self.check_answer(u_answer, ans)


    def check_answer(self,user_ans, ans):
        if user_ans.lower() == ans.lower():
            self.score += 1
            print("You got it right")
        else:
            print(f"\tYou got it wrong, the correct answer is {ans}")
        print(f"\tYour current score is {self.score}/{self.question_no}")
        print("\n")
