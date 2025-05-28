#!/usr/bin/env python3
"""
Bridge Layer for Coheron

This module serves as the IPC bridge between Rust and Python components,
reading token data and returning coherence scores.
"""

import json
import sys
import subprocess
import os
from typing import List, Dict, Any

def process_via_quantum_layer(token_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Send token data to quantum processor and get back coherence scores.
    
    Args:
        token_data: List of dictionaries containing token info and embeddings
        
    Returns:
        The same list with added coherence scores
    """
    # Path to the quantum processor script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    quantum_processor = os.path.join(os.path.dirname(script_dir), 'quantum-layer', 'quantum_processor.py')
    
    # Run the quantum processor script as a subprocess
    process = subprocess.Popen(
        ['python', quantum_processor],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Send token data to the subprocess
    stdout, stderr = process.communicate(input=json.dumps(token_data))
    
    if process.returncode != 0:
        print(f"Error in quantum processing: {stderr}", file=sys.stderr)
        return token_data
    
    try:
        # Parse the output JSON
        return json.loads(stdout)
    except json.JSONDecodeError:
        print(f"Error parsing quantum processor output: {stdout}", file=sys.stderr)
        return token_data

def main():
    """
    Main function that reads token data from stdin and outputs scores to stdout.
    """
    # Read JSON input from stdin
    input_data = json.load(sys.stdin)
    
    # Process via quantum layer
    result = process_via_quantum_layer(input_data)
    
    # Output results as JSON to stdout
    json.dump(result, sys.stdout)

if __name__ == "__main__":
    main()