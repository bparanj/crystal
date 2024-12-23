from typing import Annotated, Literal, TypedDict
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.vectorstores.in_memory import InMemoryVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
embeddings = OpenAIEmbeddings()
# useful to generate SQL query
model_low_temp = ChatOpenAI(temperature=0.1)
# useful to generate natural language outputs
model_high_temp = ChatOpenAI(temperature=0.7)
class State(TypedDict):
    # to track conversation history
    messages: Annotated[list, add_messages]
    # input
    user_query: str
    # output
    domain: Literal["records", "insurance"]
    documents: list[Document]
    answer: str
class Input(TypedDict):
    user_query: str
class Output(TypedDict):
    documents: list[Document]
    answer: str
# refer to chapter 2 on how to fill a vector store with documents
medical_records_store = InMemoryVectorStore.from_documents([], embeddings)
medical_records_retriever = medical_records_store.as_retriever()
insurance_faqs_store = InMemoryVectorStore.from_documents([], embeddings)
insurance_faqs_retriever = insurance_faqs_store.as_retriever()
router_prompt = SystemMessage(
    """You need to decide which domain to route the user query to. You have two domains to choose from:
- records: contains medical records of the patient, such as diagnosis, treatment, and prescriptions.
- insurance: contains frequently asked questions about insurance policies, claims, and coverage.
Output only the domain name."""
)
def router_node(state: State) -> State:
    user_message = HumanMessage(state["user_query"])
    messages = [router_prompt, *state["messages"], user_message]
    res = model_low_temp.invoke(messages)
    return {
        "domain": res.content,
        # update conversation history
        "messages": [user_message, res],
    }
def pick_retriever(
    state: State,
) -> Literal["retrieve_medical_records", "retrieve_insurance_faqs"]:
    if state["domain"] == "records":
        return "retrieve_medical_records"
    else:
        return "retrieve_insurance_faqs"
def retrieve_medical_records(state: State) -> State:
    documents = medical_records_retriever.invoke(state["user_query"])
    return {
        "documents": documents,
    }
def retrieve_insurance_faqs(state: State) -> State:
    documents = insurance_faqs_retriever.invoke(state["user_query"])
    return {
        "documents": documents,
    }
medical_records_prompt = SystemMessage(
    "You are a helpful medical chatbot, who answers questions based on the patient's medical records, such as diagnosis, treatment, and prescriptions."
)
insurance_faqs_prompt = SystemMessage(
    "You are a helpful medical insurance chatbot, who answers frequently asked questions about insurance policies, claims, and coverage."
)
def generate_answer(state: State) -> State:
    if state["domain"] == "records":
        prompt = medical_records_prompt
    else:
        prompt = insurance_faqs_prompt
    messages = [
        prompt,
        *state["messages"],
        HumanMessage(f"Documents: {state["documents"]}"),
    ]
    res = model_high_temp.invoke(messages)
    return {
        "answer": res.content,
        # update conversation history
        "messages": res,
    }
builder = StateGraph(State, input=Input, output=Output)
builder.add_node("router", router_node)
builder.add_node("retrieve_medical_records", retrieve_medical_records)
builder.add_node("retrieve_insurance_faqs", retrieve_insurance_faqs)
builder.add_node("generate_answer", generate_answer)
builder.add_edge(START, "router")
builder.add_conditional_edges("router", pick_retriever)
builder.add_edge("retrieve_medical_records", "generate_answer")
builder.add_edge("retrieve_insurance_faqs", "generate_answer")
builder.add_edge("generate_answer", END)
graph = builder.compile()

input = {
  "user_query": "Am I covered for COVID-19 treatment?"
}

for chunk in graph.stream(input):
    for key, value in dict(chunk).items():
        print(f"\nStep: {key}")
        if isinstance(value, dict):
            for k, v in value.items():
                print(f"  {k}: {v}")

# for chunk in graph.stream(input):
#     for key, value in dict(chunk).items():
#         print(f"\nStep: {key}")
#         if isinstance(value, dict):
#             for k, v in value.items():
#                 if k == 'domain':
#                     print(f"  Domain: {v}")
#                 elif k == 'documents':
#                     print(f"  Documents: {v}")
#                 elif k == 'answer':
#                     print(f"  Answer: {v}")
#                 elif k == 'messages':
#                     # Extract content from messages if it exists
#                     if hasattr(v, 'content'):
#                         print(f"  Content: {v.content}")
#                     elif isinstance(v, list):
#                         for msg in v:
#                             if hasattr(msg, 'content'):
#                                 print(f"  Content: {msg.content}")
