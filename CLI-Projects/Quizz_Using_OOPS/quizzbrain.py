class  brain:
    def __init__(self,q_list):
        self.q_list = q_list
        self.q_number = 0
        self.score = 0
        
    def still_has_question(self):
        return self.q_number < len(self.q_list) # check if we took all question in quizz
            
       
    def next_question(self):
        current = self.q_list[self.q_number]
        print(f"{self.q_number} : {current.text}")
        self.q_number += 1
        choice = input("True/Fale : ").capitalize()
        self.check_answer(choice, current.answer) # we dont need to write in main program because we call it in next
                                                    # question method
        
    def check_answer(self, ch, ans):
        if ch == ans:
            print("correct !!")
            self.score += 1
        else:
            print("Wrong.")
        
        
    def score_report(self):
        print("--------------------------------------------")
        print(f"Total Score: {self.score}/{len(self.q_list)}")
        print("--------------------------------------------")

            
    