from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import numpy as np
from typing import Dict, List
import pandas as pd
from nltk.translate.bleu_score import sentence_bleu
from nltk.tokenize import word_tokenize
import time
import nltk
from collections import Counter
import math

class ModelAnalyzer:
    def __init__(self, model_name: str):
        """Initialize the analyzer with a specific model"""
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True
        )
        self.metrics = {}
        
        # Download required NLTK data
        try:
            nltk.download('punkt', quiet=True)
        except:
            pass
    
    def analyze_model_architecture(self) -> Dict:
        """Analyze model architecture metrics"""
        return {
            'parameters': sum(p.numel() for p in self.model.parameters()),
            'layers': len(list(self.model.modules())),
            'vocab_size': self.tokenizer.vocab_size,
            'hidden_size': self.model.config.hidden_size,
            'num_attention_heads': self.model.config.num_attention_heads
        }
    
    def measure_inference_speed(self, text: str, num_runs: int = 3) -> Dict:
        """Measure inference speed metrics"""
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        
        # Warm-up run
        _ = self.model.generate(input_ids, max_length=50)
        
        times = []
        token_counts = []
        
        for _ in range(num_runs):
            start_time = time.time()
            output = self.model.generate(
                input_ids,
                max_length=50,
                do_sample=True,
                temperature=0.7
            )
            end_time = time.time()
            
            times.append(end_time - start_time)
            token_counts.append(len(output[0]))
        
        return {
            'avg_inference_time': np.mean(times),
            'tokens_per_second': np.mean(token_counts) / np.mean(times),
            'std_inference_time': np.std(times)
        }
    
    def analyze_text_quality(self, prompt: str, num_samples: int = 3) -> Dict:
        """Analyze the quality of generated text"""
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        
        generated_texts = []
        for _ in range(num_samples):
            output = self.model.generate(
                input_ids,
                max_length=100,
                do_sample=True,
                temperature=0.7,
                top_p=0.9
            )
            generated_texts.append(
                self.tokenizer.decode(output[0], skip_special_tokens=True)
            )
        
        # Calculate lexical diversity
        all_words = []
        for text in generated_texts:
            all_words.extend(word_tokenize(text.lower()))
        
        unique_words = len(set(all_words))
        total_words = len(all_words)
        
        # Calculate repetition rate
        word_counts = Counter(all_words)
        repeated_words = sum(1 for count in word_counts.values() if count > 1)
        
        return {
            'lexical_diversity': unique_words / total_words if total_words > 0 else 0,
            'avg_length': np.mean([len(text.split()) for text in generated_texts]),
            'repetition_rate': repeated_words / len(word_counts) if word_counts else 0,
            'samples': generated_texts
        }
    
    def analyze_memory_usage(self) -> Dict:
        """Analyze model memory usage"""
        memory_stats = {
            'model_size_mb': sum(p.nelement() * p.element_size() 
                               for p in self.model.parameters()) / (1024 * 1024),
            'vocab_size_mb': self.tokenizer.vocab_size * 2 / (1024 * 1024)  # Approximate
        }
        
        if torch.cuda.is_available():
            memory_stats.update({
                'gpu_allocated_mb': torch.cuda.memory_allocated() / (1024 * 1024),
                'gpu_cached_mb': torch.cuda.memory_reserved() / (1024 * 1024)
            })
        
        return memory_stats
    
    def run_comprehensive_analysis(self, test_text: str) -> Dict:
        """Run all analyses and compile results"""
        print(f"\nAnalyzing {self.model_name}...")
        
        self.metrics['architecture'] = self.analyze_model_architecture()
        print("Architecture analysis complete")
        
        self.metrics['inference_speed'] = self.measure_inference_speed(test_text)
        print("Inference speed analysis complete")
        
        self.metrics['text_quality'] = self.analyze_text_quality(test_text)
        print("Text quality analysis complete")
        
        self.metrics['memory_usage'] = self.analyze_memory_usage()
        print("Memory usage analysis complete")
        
        return self.metrics

def demonstrate_model_analysis():
    # Test text for analysis
    test_text = """
    Artificial Intelligence has transformed modern technology.
    It powers everything from search engines to autonomous vehicles.
    The future of AI holds both promise and challenges.
    """
    
    # Models to analyze
    models = ['distilgpt2', 'gpt2']
    results = {}
    
    for model_name in models:
        try:
            analyzer = ModelAnalyzer(model_name)
            results[model_name] = analyzer.run_comprehensive_analysis(test_text)
        except Exception as e:
            print(f"Error analyzing {model_name}: {str(e)}")
    
    # Create comparison report
    print("\nModel Comparison Report")
    print("=" * 50)
    
    # Architecture comparison
    print("\nArchitecture Comparison:")
    arch_df = pd.DataFrame({
        model: data['architecture'] 
        for model, data in results.items()
    }).round(2)
    print(arch_df)
    
    # Speed comparison
    print("\nInference Speed Comparison:")
    speed_df = pd.DataFrame({
        model: data['inference_speed']
        for model, data in results.items()
    }).round(3)
    print(speed_df)
    
    # Text quality comparison
    print("\nText Quality Metrics:")
    quality_df = pd.DataFrame({
        model: {
            k: v for k, v in data['text_quality'].items() 
            if k != 'samples'
        }
        for model, data in results.items()
    }).round(3)
    print(quality_df)
    
    # Memory usage comparison
    print("\nMemory Usage (MB):")
    memory_df = pd.DataFrame({
        model: data['memory_usage']
        for model, data in results.items()
    }).round(2)
    print(memory_df)
    
    # Save detailed results
    with pd.ExcelWriter('model_analysis_results.xlsx') as writer:
        arch_df.to_excel(writer, sheet_name='Architecture')
        speed_df.to_excel(writer, sheet_name='Speed')
        quality_df.to_excel(writer, sheet_name='Quality')
        memory_df.to_excel(writer, sheet_name='Memory')
    
    print("\nDetailed results saved to model_analysis_results.xlsx")

if __name__ == "__main__":
    print("Model Analysis Metrics Demo")
    print("=" * 50)
    demonstrate_model_analysis()