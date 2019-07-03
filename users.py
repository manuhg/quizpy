import json

class Users:
    def __init__(self,data_file=None):
        self.data_file = 'users.json' if data_file is None else data_file
        self.data = {}
    
    def get(self,username):
        return self.data.get(username)
    
    def add_or_load(self,username):
        data = self.get(username)
        if data is None:
            self.data[username] = {'name':username,'quizzes':[]}
        
        return self.get(username)

    def load(self):
        self.data={}
        #self.data = self.load_user_data(self.data_file)

    
    def save(self):
        return True
        #return self.save_user_data(self.data_file)
        
    
    def load_user_data(self,data_file):
        try:
            with open(data_file) as f:
                return json.load(f)
        except Exception as _:
            print('Unable to load user data from',data_file)

    def save_user_data(self,data_file):
        try:
            with open(data_file,'w') as f:
                return json.dump(self.data,f)
        except Exception as _:
            print('Unable to write user data to',data_file)
        
        
