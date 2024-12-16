from langchain_openai.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain

template = ChatPromptTemplate.from_messages([('system', 'You are a helpful assistant and you know about Large Language Models (LLMs)'), ('human', '{question}')])
model = ChatOpenAI()

@chain
def chatbot(values):
    """chain decorator ads the Runnable interface for a function"""
    prompt = template.invoke(values)
    return model.invoke(prompt)

result = chatbot.invoke({"question": "Which model providers offer LLMs"})
print(result)

""" 
$ python impcomp.py
content='Several companies offer Large Language Models (LLMs) that can be used for various natural language processing tasks. Some of the prominent providers of LLMs include:\n\n1. OpenAI: OpenAI offers models like GPT-3 (Generative Pre-trained Transformer 3), which is one of the most well-known and widely used LLMs.\n\n2. Google: Google provides models like BERT (Bidirectional Encoder Representations from Transformers) and T5 (Text-to-Text Transfer Transformer) for natural language understanding and generation tasks.\n\n3. Microsoft: Microsoft offers models like Microsoft Turing, which is a large-scale LLM designed for various language tasks.\n\n4. Facebook: Facebook provides models like RoBERTa (Robustly optimized BERT approach) and XLM (Cross-lingual Language Model) for multilingual and cross-lingual applications.\n\n5. Hugging Face: Hugging Face is a popular platform for accessing and using pre-trained LLMs from various providers, including models like BERT, GPT-2, and many others.\n\nThese are just a few examples of companies that offer LLMs, and there are many other providers in the field of natural language processing.' additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 242, 'prompt_tokens': 34, 'total_tokens': 276, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-c29d9e32-dd05-4860-86dc-ffec23f9370c-0' usage_metadata={'input_tokens': 34, 'output_tokens': 242, 'total_tokens': 276, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
"""

# Just using: "You are a helpful assistant" will give you strange answer:
"""
content="Several universities and institutions around the world offer Master of Laws (LLM) programs. Some well-known institutions that offer LLM programs include:\n\n1. Harvard Law School\n2. Yale Law School\n3. Stanford Law School\n4. University of Oxford\n5. University of Cambridge\n6. London School of Economics and Political Science (LSE)\n7. University of California, Berkeley (Berkeley Law)\n8. New York University (NYU) School of Law\n9. University of Melbourne Law School\n10. University of Toronto Faculty of Law\n\nThese are just a few examples, and there are many other reputable institutions that offer LLM programs. It's important to research and consider factors such as program specialization, faculty expertise, and location when choosing a program that best fits your academic and career goals." additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 164, 'prompt_tokens': 23, 'total_tokens': 187, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None} id='run-2b899738-e6e1-4e56-b15a-70042f7e0f70-0' usage_metadata={'input_tokens': 23, 'output_tokens': 164, 'total_tokens': 187, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
"""
