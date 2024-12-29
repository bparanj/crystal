from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

def demonstrate_sequence_and_summary():
    # Initialize tokenizer and model (using BART, which is good for summarization)
    model_name = "facebook/bart-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    
    # Sample text (a longer sequence to summarize)
    text = """
    Artificial Intelligence has transformed the way we live and work. Machine learning algorithms 
    now power everything from recommendation systems to autonomous vehicles. Deep learning, 
    a subset of AI, has made significant breakthroughs in image recognition, natural language 
    processing, and speech synthesis. Companies worldwide are investing heavily in AI research 
    and development, leading to innovations in healthcare, finance, and education. However, 
    the rapid advancement of AI also raises important ethical considerations about privacy, 
    bias, and the future of human work. Researchers and policymakers are working to address 
    these challenges while continuing to push the boundaries of what AI can achieve.
    """
    
    # 1. Basic Tokenization
    print("\n1. Tokenization Process:")
    print("Original text length:", len(text))
    
    # Tokenize the text
    tokens = tokenizer.tokenize(text)
    print("Number of tokens:", len(tokens))
    print("\nFirst 20 tokens:", tokens[:20])
    
    # 2. Convert to token IDs
    input_ids = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
    print("\n2. Token IDs:")
    print("Shape of input_ids:", input_ids.shape)
    print("First few token IDs:", input_ids[0][:10].tolist())
    
    # 3. Generate Summary
    print("\n3. Generating Summary:")
    
    # Generate with beam search
    summary_ids = model.generate(
        input_ids,
        max_length=150,
        min_length=40,
        num_beams=4,
        length_penalty=2.0,
        early_stopping=True,
        no_repeat_ngram_size=3
    )
    
    # Decode the generated summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    
    print("\nOriginal Text:")
    print(text.strip())
    print("\nGenerated Summary:")
    print(summary)
    
    # 4. Token Analysis
    print("\n4. Token Analysis:")
    
    # Show special tokens
    print("Special Tokens:")
    for token_name, token_id in tokenizer.special_tokens_map.items():
        print(f"{token_name}: {token_id} (ID: {tokenizer.convert_tokens_to_ids(token_id)})")
    
    # Show vocabulary size
    print(f"\nVocabulary size: {tokenizer.vocab_size}")
    
    # 5. Attention Visualization (simplified)
    print("\n5. Input Structure:")
    attention_mask = torch.ones_like(input_ids)
    print("Attention mask shape:", attention_mask.shape)
    print("This shows which tokens the model will pay attention to")

def main():
    print("Sequence and Summarization Demo")
    print("=" * 50)
    
    try:
        demonstrate_sequence_and_summary()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("\nTroubleshooting tips:")
        print("1. Make sure you have enough memory")
        print("2. Check your internet connection for model download")
        print("3. Verify that all required packages are installed")

if __name__ == "__main__":
    main()