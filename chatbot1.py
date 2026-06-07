import datetime

def chatbot():
    print("Chatbot: Hello! i am simple chatbot .")
    print("Chatbot: you can ask about hello,time,name,joke,marks.")
    print("Chatbot: type bye for exit .\n")

    while True:
        user = input("You: ").lower()

        # Greetings
        if "hello" in user or "hi" in user:
            print("Chatbot: Hello! how are u ?")

        # Name
        elif "name" in user:
            print("Chatbot: Mey name is help buddy .")

        # Time
        elif "time" in user:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Chatbot: Current time hai:", current_time)

        # Joke
        elif "joke" in user:
            print("Chatbot: Why do programmers prefer dark mode? Because light attracts bugs ")


        # Python info
        elif "python" in user:
            print("Chatbot: Python ek easy programming language hai.")

        # Marks system (input + logic)
        elif "marks" in user:
            marks = int(input("Apne marks enter karo: "))
            if marks >= 40:
                print("Chatbot: passed .hard work really pays off")
            else:
                print("Chatbot: failed do more practice")

        # Help
        elif "help" in user:
            print("Chatbot: you can ask  -> hello, name, time, joke,  marks")

        # Exit
        elif "bye" in user:
            print("Chatbot: Goodbye! ")
            break

        # Default
        else:
            print("Chatbot: OOPS! try something else!!.")

# Run chatbot
chatbot()