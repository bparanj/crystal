from langchain_openai.llms import OpenAI

model = OpenAI()
completion = model.invoke('Hi there!')

print('----')
print(completion)
print('----')

completions = model.batch(['Hi there!', 'Bye!'])

print('----')
print(completions)
print('----')

for token in model.stream('Bye!'):
    print(token)
