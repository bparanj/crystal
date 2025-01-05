- Ask for positives
- Bolster command with a reason
- Avoid absolutes

- How to use few shot prompting?
- How to teach the LLM the format and style to use in the answer?

Introduction
Examples
Main Question

Few shot prompting is suited to demonstrate the expected output format

Include all major classes of examples in few short prompt whenever possible.

Use few-shot prompting if you have relevant examples that illustrate an aspect of what you want the model to do that is otherwise unobvious. But, if the problem at hand is already clear to the model, don’t feel that you have to use few-shot prompting. 

- Include the objective of the task: write, summarize ...
- Include the format of the output: use bullet points, JSON ...

This is conflicting:

The constraints: Do not ...

with another book's suggestion to provide only positive commands.

- Include a role: You are an <role-name>

Split complex tasks into subtasks

Summarization:

- Extract keywords or main points
- Rewrite 
- Trim

Provide a clear justification of your answer and the reasoning behind it

Prompt the model to generate multiple responses
Pick the one which is most suitable for the user's query

You are an ...
Given a ... generate three answers
For each answer, be specific about the reasoning you made
Then, among the three answers, select the one which is most plausible given the ...

Use delimiters:

>>>>
====
----
####
````

You are a Python expert that produces Python code as per user's request.
====>START EXAMPLE
----User Query----
Give me a function to print a string of text
----User Output---
Below you can find the described function:
```
def my_print(text):
  print(text)
```
<===END EXAMPLE

Generate a Python function to calculate ...

ReAct Metaprompt

Answer the following questions as best you can.

Use the following format:

Question: the input question you must answer

Thought: you should always think about what to do

Action: the action to take

Action Input: the input to the action

Observation: the result of the action

... (this Thought/Action/Action Input/Observation can repeat N times)

Thought: I now know the final answer

Final Answer: the final answer to the original input quest

