import csv

class ChatBot:
    def __init__(self, name, replies):
        self.name = name 
        self.replies = {}

        if type(replies) == dict :
            self.replies = replies
        elif type(replies) == str:
             with open(replies) as csv_file:
                data = csv.reader(csv_file, delimiter="#")
                self.replies = {row[0]:row[1] for row in data}
             
    
    def replyTo (self, message):
        if message in self.replies:
            return self.replies[message]
        else:
            return "I don't understand, please retry"    
