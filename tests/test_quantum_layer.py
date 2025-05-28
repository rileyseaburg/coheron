#!/usr/bin/env python3
"""
Test script for the quantum layer to verify functionality
"""

import sys
import os
import json
import random
from typing import List, Dict, Any

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the quantum processor directly
from quantum_layer.quantum_processor import process_token_embeddings

def generate_test_embeddings(dim: int = 8, num_tokens: int = 3) -> List[Dict[str, Any]]:
    """Generate test token data with random embeddings"""
    tokens = ["revealed", "hidden", "lost"]
    
    result = []
    for i in range(min(num_tokens, len(tokens))):
        # Generate random embedding
        embedding = [random.uniform(-1, 1) for _ in range(dim)]
        
        # Create token info
        token_info = {
            "token": tokens[i],
            "embedding": embedding
        }
        
        result.append(token_info)
    
    return result

def main():
    """Run a test of the quantum processing layer"""
    print("🧪 Testing Quantum Layer")
    print("------------------------")
    
    # Generate test token data
    token_data = generate_test_embeddings()
    
    print(f"Generated {len(token_data)} test tokens with embeddings")
    
    # Process through quantum layer
    print("Processing through quantum layer...")
    result = process_token_embeddings(token_data)
    
    # Display results
    print("\nResults:")
    for token_info in result:
        print(f"  - {token_info['token']}: score = {token_info['score']}")
    
    # Find highest scoring token
    best_token = max(result, key=lambda x: x['score'])
    print(f"\nHighest scoring token: {best_token['token']} (score: {best_token['score']})")
    
    # Format as expected log output
    log_output = {
        "prompt": "The truth is",
        "candidates": result,
        "selected_token": best_token["token"],
        "timestamp": "2025-05-28T23:04:00Z"  # Placeholder timestamp
    }
    
    # Output JSON
    print("\nJSON Output:")
    print(json.dumps(log_output, indent=2))

if __name__ == "__main__":
    main()