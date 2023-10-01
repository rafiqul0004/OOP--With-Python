with open('message.txt','a') as file:
    file.write('I Love Myself')
with open('message.txt','r') as file:
    text=file.read()
    print(text)