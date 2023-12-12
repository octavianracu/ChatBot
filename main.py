from bot import ChatBot


faqBot = ChatBot("support", 'data.csv')


while True:
    message = input("You: ")
    reply = faqBot.replyTo(message)
    print('Support:', reply)
    if message == "x":
        break
