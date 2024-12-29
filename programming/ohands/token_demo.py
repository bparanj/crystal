from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def demonstrate_tokenization():
    # Initialize tokenizer (using BERT as an example)
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    
    # Example text
    text = "Hello, I love working with transformers! 🤗"
    print("\n1. Basic Tokenization Example:")
    print(f"Original text: {text}")
    
    # Tokenize the text
    tokens = tokenizer.tokenize(text)
    print(f"Tokens: {tokens}")
    
    # Convert tokens to IDs
    token_ids = tokenizer.encode(text)
    print(f"Token IDs: {token_ids}")
    
    # Decode back to text
    decoded_text = tokenizer.decode(token_ids)
    print(f"Decoded text: {decoded_text}")
    
    # Show token-to-id mapping
    print("\n2. Token to ID Mapping:")
    for token in tokens:
        token_id = tokenizer.convert_tokens_to_ids(token)
        print(f"Token: {token:15} ID: {token_id}")
    
    # Demonstrate batch tokenization
    print("\n3. Batch Tokenization Example:")
    sentences = [
        "I love programming.",
        "Natural Language Processing is fascinating!",
        "Transformers are powerful."
    ]
    
    # Tokenize with padding and truncation
    batch_tokens = tokenizer(
        sentences,
        padding=True,
        truncation=True,
        max_length=12,
        return_tensors="pt"
    )
    
    print("Input IDs shape:", batch_tokens["input_ids"].shape)
    print("Attention mask shape:", batch_tokens["attention_mask"].shape)
    
    # Show each sentence's tokens
    print("\nTokenized sentences:")
    for i, sentence in enumerate(sentences):
        decoded = tokenizer.decode(batch_tokens["input_ids"][i])
        print(f"\nOriginal: {sentence}")
        print(f"Tokenized: {decoded}")
    
    # Demonstrate special tokens
    print("\n4. Special Tokens Example:")
    print(f"CLS token ID: {tokenizer.cls_token_id}")
    print(f"SEP token ID: {tokenizer.sep_token_id}")
    print(f"PAD token ID: {tokenizer.pad_token_id}")
    print(f"UNK token ID: {tokenizer.unk_token_id}")
    
    # Demonstrate vocabulary access
    print("\n5. Vocabulary Example:")
    print(f"Vocabulary size: {tokenizer.vocab_size}")
    print("First 10 tokens in vocabulary:")
    for i, (token, id) in enumerate(list(tokenizer.vocab.items())[:10]):
        print(f"{token}: {id}")

if __name__ == "__main__":
    print("Token Operations Demo using Hugging Face Transformers")
    print("=" * 50)
    demonstrate_tokenization()
    