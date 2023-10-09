from pygpt4all import GPT4All_J
model = GPT4All_J('ggml-gpt4all-j-v1.3-groovy.bin')

while True:
    print("\n")
    user_input = input("You: ")
    if user_input.lower() in ["quit","exit","bye"]:
        break    
    print("Chatbot: ")
    for token in model.generate(user_input + "\n"):
        print(token, end='', flush=True)

