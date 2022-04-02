#Importing modules
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

BankBot = ChatBot(name='BankBot',
                  read_only=False,
                  logic_adapters=["chatterbot.logic.BestMatch"],
                  storage_adapter="chatterbot.storage.SQLStorageAdapter")

corpus_trainer = ChatterBotCorpusTrainer(BankBot)
corpus_trainer.train("chatterbot.corpus.english")

greet_conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

open_timings_conversation = [
    "What time does the Bank open?",
    "The Bank opens at 9AM",
]

close_timings_conversation = [
    "What time does the Bank close?",
    "The Bank closes at 5PM",
]

# Initializing Trainer Object
trainer = ListTrainer(BankBot)

# Training BankBot
trainer.train(greet_conversation)
trainer.train(open_timings_conversation)
trainer.train(close_timings_conversation)

while True:
    user_input = input()
    if user_input == 'quit':
        break
    response = BankBot.get_response(user_input)
    print(response)
