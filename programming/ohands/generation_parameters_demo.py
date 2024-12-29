from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import pandas as pd
from typing import Dict, List
import time
from dataclasses import dataclass
import json

@dataclass
class GenerationConfig:
    """Configuration for text generation"""
    temperature: float
    top_k: int
    top_p: float
    num_beams: int
    max_length: int
    no_repeat_ngram_size: int
    
    def to_dict(self) -> Dict:
        return {
            'temperature': self.temperature,
            'top_k': self.top_k,
            'top_p': self.top_p,
            'num_beams': self.num_beams,
            'max_length': self.max_length,
            'no_repeat_ngram_size': self.no_repeat_ngram_size
        }

class GenerationExplorer:
    def __init__(self, model_name: str):
        """Initialize with a specific model"""
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True
        )
        self.results = []
    
    def generate_text(self, 
                     prompt: str,
                     config: GenerationConfig) -> Dict:
        """Generate text with specific parameters"""
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        
        start_time = time.time()
        output = self.model.generate(
            input_ids,
            do_sample=True,
            **config.to_dict()
        )
        generation_time = time.time() - start_time
        
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        
        result = {
            'prompt': prompt,
            'generated_text': generated_text,
            'generation_time': generation_time,
            **config.to_dict()
        }
        
        self.results.append(result)
        return result
    
    def explore_temperature(self, 
                          prompt: str,
                          temperatures: List[float]) -> List[Dict]:
        """Explore different temperature values"""
        results = []
        base_config = GenerationConfig(
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            num_beams=1,
            max_length=100,
            no_repeat_ngram_size=2
        )
        
        for temp in temperatures:
            config = GenerationConfig(**base_config.to_dict())
            config.temperature = temp
            result = self.generate_text(prompt, config)
            results.append(result)
        
        return results
    
    def explore_top_k_p(self,
                       prompt: str,
                       top_k_values: List[int],
                       top_p_values: List[float]) -> List[Dict]:
        """Explore different top-k and top-p combinations"""
        results = []
        base_config = GenerationConfig(
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            num_beams=1,
            max_length=100,
            no_repeat_ngram_size=2
        )
        
        for k in top_k_values:
            for p in top_p_values:
                config = GenerationConfig(**base_config.to_dict())
                config.top_k = k
                config.top_p = p
                result = self.generate_text(prompt, config)
                results.append(result)
        
        return results
    
    def explore_beam_search(self,
                          prompt: str,
                          beam_values: List[int]) -> List[Dict]:
        """Explore different beam search settings"""
        results = []
        base_config = GenerationConfig(
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            num_beams=1,
            max_length=100,
            no_repeat_ngram_size=2
        )
        
        for num_beams in beam_values:
            config = GenerationConfig(**base_config.to_dict())
            config.num_beams = num_beams
            result = self.generate_text(prompt, config)
            results.append(result)
        
        return results
    
    def save_results(self, filename: str):
        """Save all results to file"""
        df = pd.DataFrame(self.results)
        df.to_csv(filename, index=False)
        
        # Also save as JSON for better readability
        with open(filename.replace('.csv', '.json'), 'w') as f:
            json.dump(self.results, f, indent=2)

def demonstrate_generation_parameters():
    # Initialize explorer with a small model
    explorer = GenerationExplorer('distilgpt2')
    
    # Test prompts
    prompts = [
        "The future of artificial intelligence will",
        "Once upon a time in a digital world",
        "The solution to climate change requires"
    ]
    
    print("\nExploring Temperature Values...")
    temperatures = [0.2, 0.5, 0.8, 1.0]
    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        results = explorer.explore_temperature(prompt, temperatures)
        for result in results:
            print(f"\nTemperature: {result['temperature']}")
            print(f"Generated text: {result['generated_text'][:100]}...")
    
    print("\nExploring Top-K and Top-P Values...")
    top_k_values = [10, 50]
    top_p_values = [0.5, 0.9]
    for prompt in prompts[:1]:  # Use first prompt only for brevity
        results = explorer.explore_top_k_p(prompt, top_k_values, top_p_values)
        for result in results:
            print(f"\nTop-K: {result['top_k']}, Top-P: {result['top_p']}")
            print(f"Generated text: {result['generated_text'][:100]}...")
    
    print("\nExploring Beam Search...")
    beam_values = [1, 3, 5]
    for prompt in prompts[:1]:  # Use first prompt only for brevity
        results = explorer.explore_beam_search(prompt, beam_values)
        for result in results:
            print(f"\nNum Beams: {result['num_beams']}")
            print(f"Generated text: {result['generated_text'][:100]}...")
    
    # Save all results
    explorer.save_results('generation_parameters_results.csv')
    print("\nResults saved to generation_parameters_results.csv and .json")

if __name__ == "__main__":
    print("Generation Parameters Demo")
    print("=" * 50)
    demonstrate_generation_parameters()