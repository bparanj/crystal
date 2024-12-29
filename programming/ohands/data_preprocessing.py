import re
import string
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
from collections import Counter
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import warnings
warnings.filterwarnings('ignore')

class TextPreprocessor:
    def __init__(self):
        # Download required NLTK data
        try:
            nltk.download('punkt', quiet=True)
            nltk.download('stopwords', quiet=True)
            nltk.download('wordnet', quiet=True)
            nltk.download('averaged_perceptron_tagger', quiet=True)
        except:
            print("NLTK data already downloaded or error in downloading")
        
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
    
    def basic_cleaning(self, text):
        """Basic text cleaning"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Remove extra whitespace
        text = ' '.join(text.split())
        
        return text
    
    def remove_stopwords(self, text):
        """Remove stop words"""
        words = text.split()
        words = [w for w in words if w not in self.stop_words]
        return ' '.join(words)
    
    def lemmatize_text(self, text):
        """Lemmatize text"""
        words = text.split()
        words = [self.lemmatizer.lemmatize(word) for word in words]
        return ' '.join(words)
    
    def stem_text(self, text):
        """Stem text"""
        words = text.split()
        words = [self.stemmer.stem(word) for word in words]
        return ' '.join(words)
    
    def get_text_statistics(self, text):
        """Get basic statistics about the text"""
        sentences = text.split('.')
        sentences = [s.strip() for s in sentences if s.strip()]
        words = text.split()
        
        return {
            'num_sentences': len(sentences),
            'num_words': len(words),
            'num_unique_words': len(set(words)),
            'avg_word_length': np.mean([len(word) for word in words])
        }

class DataPreprocessor:
    def __init__(self):
        self.label_encoders = {}
        self.scaler = StandardScaler()
    
    def handle_missing_values(self, df):
        """Handle missing values in the dataset"""
        # Numeric columns: fill with mean
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df[col].fillna(df[col].mean(), inplace=True)
        
        # Categorical columns: fill with mode
        categorical_cols = df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            df[col].fillna(df[col].mode()[0], inplace=True)
        
        return df
    
    def encode_categorical(self, df, columns):
        """Encode categorical variables"""
        df_encoded = df.copy()
        
        for col in columns:
            if col not in self.label_encoders:
                self.label_encoders[col] = LabelEncoder()
                df_encoded[col] = self.label_encoders[col].fit_transform(df[col])
            else:
                df_encoded[col] = self.label_encoders[col].transform(df[col])
        
        return df_encoded
    
    def scale_numeric(self, df, columns):
        """Scale numeric features"""
        df_scaled = df.copy()
        df_scaled[columns] = self.scaler.fit_transform(df[columns])
        return df_scaled

def demonstrate_preprocessing():
    # 1. Text Preprocessing Example
    print("1. Text Preprocessing Example")
    print("=" * 50)
    
    text_processor = TextPreprocessor()
    
    sample_text = """
    Hello World! This is an example of text preprocessing in Python 3.0. 
    We'll demonstrate various techniques like cleaning, tokenization, and lemmatization.
    The quick brown fox jumps over the lazy dog!!! 
    """
    
    print("Original Text:")
    print(sample_text)
    print("\nBasic Cleaning:")
    cleaned_text = text_processor.basic_cleaning(sample_text)
    print(cleaned_text)
    
    print("\nAfter Removing Stopwords:")
    text_no_stops = text_processor.remove_stopwords(cleaned_text)
    print(text_no_stops)
    
    print("\nAfter Lemmatization:")
    lemmatized_text = text_processor.lemmatize_text(cleaned_text)
    print(lemmatized_text)
    
    print("\nAfter Stemming:")
    stemmed_text = text_processor.stem_text(cleaned_text)
    print(stemmed_text)
    
    print("\nText Statistics:")
    stats = text_processor.get_text_statistics(sample_text)
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # 2. Structured Data Preprocessing Example
    print("\n2. Structured Data Preprocessing Example")
    print("=" * 50)
    
    # Create sample dataset
    data = {
        'age': [25, 30, np.nan, 45, 35],
        'salary': [50000, 60000, 75000, np.nan, 65000],
        'department': ['IT', 'HR', 'IT', None, 'Finance'],
        'experience': [2, 5, 8, 15, 7]
    }
    
    df = pd.DataFrame(data)
    print("\nOriginal Dataset:")
    print(df)
    
    data_processor = DataPreprocessor()
    
    # Handle missing values
    df_clean = data_processor.handle_missing_values(df)
    print("\nAfter Handling Missing Values:")
    print(df_clean)
    
    # Encode categorical variables
    df_encoded = data_processor.encode_categorical(df_clean, ['department'])
    print("\nAfter Encoding Categorical Variables:")
    print(df_encoded)
    
    # Scale numeric features
    numeric_cols = ['age', 'salary', 'experience']
    df_scaled = data_processor.scale_numeric(df_encoded, numeric_cols)
    print("\nAfter Scaling Numeric Features:")
    print(df_scaled)

if __name__ == "__main__":
    demonstrate_preprocessing()