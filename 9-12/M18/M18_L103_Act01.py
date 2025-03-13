from nltk.chat.util import Chat, reflections


reflections = {
  "I am"       : "you are",
  "I was"      : "you were",
  "I"          : "you",
  "I'm"        : "you are",
  "I'd"        : "you would",
  "I've"       : "you have",
  "I'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name ?",
        ["I am a chat robot. You can call me Jarvis!"]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "It's OK, never mind"]
    ],
    [
        r"I am fine",
        ["Glad to hear that. How can I help you?"]
    ],
    [
        r"I'm (.*) doing good",
        ["Nice to hear that. How can I help you? :)"]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, not a human. Are you seriously asking me this?"]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse"]
    ],
    [
        r"(.*) created ?",
        ["I was created using Python's NLTK library", "Top secret ;)"]
    ],
    
    [
        r"how is the weather in (.*)?",
        ["The weather in %1 is awesome like always", "Too hot here in %1", "Too cold here in %1", "Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an amazing company, though I've heard they are facing some challenges lately."]
    ],
    [
        r"(.*) raining in (.*)",
        ["No rain since last week here in %2", "Damn, it's raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy"]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of brain game."]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Ragnar Oratmangoen", "Justin Hubner", "Jay Idzes", "Marten Paes"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["I don't like watching movies, so I know no one"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Jarvis_Tech has many great articles with detailed step-by-step explanations and code. You should definitely check it out."]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
]



def mychat():
    print("Hi! I am a chatbot for your service.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

# Initiate the conversation
if __name__ == "__main__":
    mychat()