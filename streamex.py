chatbot = template | model
for part in chatbot.stream({"question": "Which model providers offer LLMs?"}):
    print(part)

chatbot = template | model
result = await chatbot.ainvoke({"question": "Which model providers offer LLMs?"})

