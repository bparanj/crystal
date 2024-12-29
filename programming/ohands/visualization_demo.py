import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class ModelVisualizer:
    def __init__(self, model_names: List[str]):
        """Initialize visualizer with multiple models"""
        self.model_names = model_names
        self.models = {}
        self.tokenizers = {}
        
        for name in model_names:
            self.tokenizers[name] = AutoTokenizer.from_pretrained(name)
            self.models[name] = AutoModelForCausalLM.from_pretrained(
                name,
                torch_dtype=torch.float16,
                low_cpu_mem_usage=True
            )
    
    def visualize_model_architectures(self) -> None:
        """Create visualization of model architectures"""
        architecture_data = []
        
        for name in self.model_names:
            model = self.models[name]
            architecture_data.append({
                'model': name,
                'parameters': sum(p.numel() for p in model.parameters()),
                'layers': len(list(model.modules())),
                'hidden_size': model.config.hidden_size,
                'attention_heads': model.config.num_attention_heads
            })
        
        df = pd.DataFrame(architecture_data)
        
        # Create subplot figure
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Model Parameters', 'Number of Layers',
                          'Hidden Size', 'Attention Heads')
        )
        
        # Add bars for each metric
        fig.add_trace(
            go.Bar(x=df['model'], y=df['parameters'], name='Parameters'),
            row=1, col=1
        )
        fig.add_trace(
            go.Bar(x=df['model'], y=df['layers'], name='Layers'),
            row=1, col=2
        )
        fig.add_trace(
            go.Bar(x=df['model'], y=df['hidden_size'], name='Hidden Size'),
            row=2, col=1
        )
        fig.add_trace(
            go.Bar(x=df['model'], y=df['attention_heads'], name='Attention Heads'),
            row=2, col=2
        )
        
        fig.update_layout(height=800, title_text="Model Architecture Comparison")
        fig.write_html('model_architecture_comparison.html')
    
    def visualize_attention_patterns(self, text: str) -> None:
        """Visualize attention patterns for each model"""
        for name in self.model_names:
            tokenizer = self.tokenizers[name]
            model = self.models[name]
            
            # Tokenize input
            inputs = tokenizer(text, return_tensors="pt")
            
            # Get attention weights
            with torch.no_grad():
                outputs = model(**inputs, output_attentions=True)
            
            attention = outputs.attentions[-1].mean(dim=1).squeeze()
            tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
            
            # Create heatmap
            fig = go.Figure(data=go.Heatmap(
                z=attention.numpy(),
                x=tokens,
                y=tokens,
                colorscale='Viridis'
            ))
            
            fig.update_layout(
                title=f'Attention Pattern - {name}',
                xaxis_title='Target Tokens',
                yaxis_title='Source Tokens'
            )
            
            fig.write_html(f'attention_pattern_{name}.html')
    
    def visualize_token_distributions(self, text: str) -> None:
        """Visualize token distribution patterns"""
        distribution_data = []
        
        for name in self.model_names:
            tokenizer = self.tokenizers[name]
            tokens = tokenizer.tokenize(text)
            
            # Get token distribution
            token_counts = pd.Series(tokens).value_counts()
            
            for token, count in token_counts.items():
                distribution_data.append({
                    'model': name,
                    'token': token,
                    'count': count
                })
        
        df = pd.DataFrame(distribution_data)
        
        # Create token distribution plot
        fig = px.bar(df, x='token', y='count', color='model',
                    barmode='group',
                    title='Token Distribution Comparison')
        
        fig.update_layout(
            xaxis_tickangle=-45,
            xaxis_title='Tokens',
            yaxis_title='Count'
        )
        
        fig.write_html('token_distribution.html')
    
    def visualize_generation_metrics(self, 
                                  prompts: List[str],
                                  num_generations: int = 5) -> None:
        """Visualize various generation metrics"""
        generation_data = []
        
        for name in self.model_names:
            model = self.models[name]
            tokenizer = self.tokenizers[name]
            
            for prompt in prompts:
                for _ in range(num_generations):
                    inputs = tokenizer(prompt, return_tensors="pt")
                    
                    # Generate text
                    start_time = time.time()
                    outputs = model.generate(
                        inputs['input_ids'],
                        max_length=50,
                        do_sample=True,
                        temperature=0.7
                    )
                    generation_time = time.time() - start_time
                    
                    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
                    
                    generation_data.append({
                        'model': name,
                        'prompt': prompt,
                        'generation_time': generation_time,
                        'output_length': len(generated_text.split()),
                        'unique_tokens': len(set(tokenizer.tokenize(generated_text)))
                    })
        
        df = pd.DataFrame(generation_data)
        
        # Create subplot figure for metrics
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Generation Time', 'Output Length',
                          'Unique Tokens', 'Time vs Length')
        )
        
        # Add box plots for metrics
        fig.add_trace(
            go.Box(x=df['model'], y=df['generation_time'], name='Generation Time'),
            row=1, col=1
        )
        fig.add_trace(
            go.Box(x=df['model'], y=df['output_length'], name='Output Length'),
            row=1, col=2
        )
        fig.add_trace(
            go.Box(x=df['model'], y=df['unique_tokens'], name='Unique Tokens'),
            row=2, col=1
        )
        
        # Add scatter plot for time vs length
        for name in self.model_names:
            model_df = df[df['model'] == name]
            fig.add_trace(
                go.Scatter(
                    x=model_df['output_length'],
                    y=model_df['generation_time'],
                    mode='markers',
                    name=f'{name} - Time vs Length'
                ),
                row=2, col=2
            )
        
        fig.update_layout(height=1000, title_text="Generation Metrics Comparison")
        fig.write_html('generation_metrics.html')

def demonstrate_visualizations():
    # Initialize visualizer with models
    models = ['distilgpt2', 'gpt2']
    visualizer = ModelVisualizer(models)
    
    # Sample text for analysis
    text = """
    Artificial Intelligence has transformed modern technology.
    It powers everything from search engines to autonomous vehicles.
    The future of AI holds both promise and challenges.
    """
    
    # Sample prompts for generation
    prompts = [
        "The future of AI will",
        "Once upon a time",
        "The solution requires"
    ]
    
    print("Creating visualizations...")
    
    # Create various visualizations
    print("1. Visualizing model architectures...")
    visualizer.visualize_model_architectures()
    
    print("2. Visualizing attention patterns...")
    visualizer.visualize_attention_patterns(text)
    
    print("3. Visualizing token distributions...")
    visualizer.visualize_token_distributions(text)
    
    print("4. Visualizing generation metrics...")
    visualizer.visualize_generation_metrics(prompts)
    
    print("\nVisualization files created:")
    print("- model_architecture_comparison.html")
    print("- attention_pattern_*.html")
    print("- token_distribution.html")
    print("- generation_metrics.html")

if __name__ == "__main__":
    print("Model Visualization Demo")
    print("=" * 50)
    demonstrate_visualizations()