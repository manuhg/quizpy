from users import Users

def get_int_input(inpstr):
    try:
        inp = int(input(inpstr))
        return inp
    except Exception as _:
        print('Invalid number')
    
class Quiz:
    def __init__(self):
        self.users = Users()
        self.choices = {1:self.new_quiz,2:self.past_results}
        self.questions = [['What is the capital of karnataka','Bengaluru'],   ['Where is India','Asia']]
    def get_user(self):
        username = input('Enter username(No spaces): ')
        user = self.users.add_or_load(username)
        return user
    
    def get_choice(self,user):
        choices = []
        choices.append(['Take a new quiz : ',1])
        if user['quizzes']:
            choices.append(['View past results: ',2])
        self.print_choices(choices)
        return get_int_input('Enter choice:')

    def print_choices(self,choices):
        print('Choose one of the below')
        # _ = list(map(print,choices))
        for c in choices:
            print(' '.join(list(map(str, c))))
    
    def conduct_quiz(self):
        choice = 1
        print('Welome to quiz')
        while choice==1:
            self.quiz()
            choice = get_int_input('Press 1 to continue. Press any other key to exit: ')
        print('Thank you for taking the quiz.')

    def quiz(self):
        user = self.get_user()
        choice = self.get_choice(user)
        choice_func = self.choices.get(choice)
        if choice_func is None:
            print('No such choice')
        else:
            choice_func(user)
    
    def new_quiz(self,user):
        score = 0
        user['quizzes'].append([])
        for q in self.questions:
            answer = input(q[0]+': ')
            marks =0
            if answer == q[1]:
                marks = 1
            score+=marks
            user['quizzes'][-1].append([q[0],marks])
        user['quizzes'][-1].append(['Total score',score])
        
        self.past_results(user,1)
    
    def print_result(self,quiz):
        for q in quiz:
            print(q[0],'marks:',q[1])

    def past_results(self,user,nq=None):
        print('\n=========================================\nResults\n=========================================')
        if nq is None:
             nq = len(user['quizzes'])
             nd = nq
             print('You have previosuly attempted ',nq,'times')
             if nq>1:
                 nd = get_int_input('How many past attempts do you want to see? ')
                 nq = nd
            
        for q in (user['quizzes'][-nq:]):
            print('\n=========================')
            self.print_result(q)
            print('\n=========================')
        print('\n=========================================\nResults\n=========================================')
        
        
def main():
    quiz = Quiz()
    quiz.conduct_quiz()

if __name__=="__main__":
    main()