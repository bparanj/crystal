**Parametric Knowledge**  
Parametric knowledge is the information stored directly in an AI model’s parameters. In large language models, these parameters capture patterns from the training data. When you ask the model a question, it draws on this “built-in” knowledge encoded during training.

**Non-Parametric Knowledge**  
Non-parametric knowledge is information stored outside the model. It can be in databases, documents, or any external knowledge base. The AI model can query this external knowledge at runtime without relying solely on what it “memorized.”

**RAG AI Application**  
In a Retrieval-Augmented Generation (RAG) setting, a model uses both:  
1. **Parametric Knowledge** for its learned language understanding.  
2. **Non-Parametric Knowledge** by retrieving relevant text from external sources.  

This blend allows for richer and more up-to-date answers without needing to fully retrain the model.