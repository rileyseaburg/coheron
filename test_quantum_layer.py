#!/usr/bin/env python3
"""
Tests for the quantum coherence evaluation module.
"""

import json
import unittest
import sys
import os

# Add the current directory to the path so we can import quantum_layer
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import quantum_layer

class TestQuantumLayer(unittest.TestCase):
    
    def test_embedding_to_quantum_params(self):
        """Test embedding conversion to quantum parameters."""
        embedding = [0.1, 0.2, 0.3, 0.4]
        params = quantum_layer.embedding_to_quantum_params(embedding)
        
        self.assertEqual(len(params), 4)
        import math
        self.assertTrue(all(0 <= p <= 2 * math.pi + 0.001 for p in params))
    
    def test_embedding_to_quantum_params_empty(self):
        """Test handling of empty embeddings."""
        params = quantum_layer.embedding_to_quantum_params([])
        self.assertEqual(params, [0.0])
    
    def test_embedding_to_quantum_params_short(self):
        """Test handling of short embeddings."""
        embedding = [0.5, 0.8]
        params = quantum_layer.embedding_to_quantum_params(embedding)
        self.assertEqual(len(params), 4)  # Should be padded to 4
    
    def test_create_coherence_circuit(self):
        """Test quantum circuit creation."""
        embedding = [0.1, 0.2, 0.3]
        circuit = quantum_layer.create_coherence_circuit(embedding)
        
        self.assertIsInstance(circuit, quantum_layer.MockQuantumCircuit)
        self.assertGreaterEqual(circuit.num_qubits, 2)
        self.assertLessEqual(circuit.num_qubits, 4)
        self.assertGreater(len(circuit.operations), 0)
    
    def test_calculate_coherence_score(self):
        """Test coherence score calculation."""
        # Test with uniform distribution (high entropy)
        uniform_results = {"00": 250, "01": 250, "10": 250, "11": 250}
        uniform_score = quantum_layer.calculate_coherence_score(uniform_results)
        
        # Test with concentrated distribution (low entropy)
        concentrated_results = {"00": 1000, "01": 1, "10": 1, "11": 1}
        concentrated_score = quantum_layer.calculate_coherence_score(concentrated_results)
        
        # Uniform distribution should have higher coherence score
        self.assertGreater(uniform_score, concentrated_score)
        self.assertGreaterEqual(uniform_score, 0.0)
        self.assertLessEqual(uniform_score, 1.0)
        self.assertGreaterEqual(concentrated_score, 0.0)
        self.assertLessEqual(concentrated_score, 1.0)
    
    def test_calculate_coherence_score_empty(self):
        """Test coherence score with empty results."""
        score = quantum_layer.calculate_coherence_score({})
        self.assertEqual(score, 0.0)
    
    def test_evaluate_token_coherence(self):
        """Test token coherence evaluation."""
        token_data = {
            "token": "quantum",
            "embedding": [0.1, 0.2, 0.3, 0.4],
            "probability": 0.5
        }
        
        result = quantum_layer.evaluate_token_coherence(token_data)
        
        self.assertIn("score", result)
        self.assertIn("quantum_state", result)
        self.assertIsInstance(result["score"], float)
        self.assertIsInstance(result["quantum_state"], str)
        self.assertGreaterEqual(result["score"], 0.0)
        self.assertLessEqual(result["score"], 1.0)
    
    def test_main_function_integration(self):
        """Test the main function with mock input."""
        test_input = [
            {
                "token": "test1",
                "embedding": [0.1, 0.2],
                "probability": 0.4
            },
            {
                "token": "test2", 
                "embedding": [0.3, 0.4],
                "probability": 0.6
            }
        ]
        
        # Mock sys.argv for testing
        original_argv = sys.argv
        sys.argv = ["quantum_layer.py", json.dumps(test_input)]
        
        try:
            # Capture stdout
            from io import StringIO
            import contextlib
            
            f = StringIO()
            with contextlib.redirect_stdout(f):
                quantum_layer.main()
            
            output = f.getvalue()
            results = json.loads(output)
            
            self.assertEqual(len(results), 2)
            for result in results:
                self.assertIn("score", result)
                self.assertIn("quantum_state", result)
                self.assertIsInstance(result["score"], float)
        
        finally:
            sys.argv = original_argv

if __name__ == "__main__":
    unittest.main()