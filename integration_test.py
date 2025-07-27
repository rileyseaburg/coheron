#!/usr/bin/env python3
"""
Integration test for the full Coheron system.
Tests the end-to-end workflow from Rust to Python and back.
"""

import subprocess
import json
import sys
import os

def test_quantum_layer_standalone():
    """Test the quantum layer with various inputs."""
    print("Testing quantum layer standalone...")
    
    test_cases = [
        {
            "name": "Single token",
            "input": [{"token": "quantum", "embedding": [0.1, 0.2, 0.3], "probability": 0.5}],
            "expected_count": 1
        },
        {
            "name": "Multiple tokens",
            "input": [
                {"token": "quantum", "embedding": [0.1, 0.2, 0.3], "probability": 0.4},
                {"token": "coherence", "embedding": [0.4, 0.5, 0.6], "probability": 0.3},
                {"token": "resonance", "embedding": [0.7, 0.8, 0.9], "probability": 0.3}
            ],
            "expected_count": 3
        },
        {
            "name": "Empty embedding",
            "input": [{"token": "empty", "embedding": [], "probability": 0.5}],
            "expected_count": 1
        }
    ]
    
    for test_case in test_cases:
        print(f"  - {test_case['name']}")
        result = subprocess.run(
            ["python3", "quantum_layer.py", json.dumps(test_case["input"])],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"    FAILED: {result.stderr}")
            return False
        
        try:
            scores = json.loads(result.stdout)
            if len(scores) != test_case["expected_count"]:
                print(f"    FAILED: Expected {test_case['expected_count']} scores, got {len(scores)}")
                return False
            
            for score in scores:
                if not isinstance(score.get("score"), (int, float)):
                    print(f"    FAILED: Invalid score type: {type(score.get('score'))}")
                    return False
                if not 0 <= score["score"] <= 1:
                    print(f"    FAILED: Score out of range: {score['score']}")
                    return False
            
            print(f"    PASSED: Got {len(scores)} valid coherence scores")
            
        except json.JSONDecodeError as e:
            print(f"    FAILED: Invalid JSON output: {e}")
            return False
    
    return True

def test_rust_unit_tests():
    """Run Rust unit tests."""
    print("Testing Rust components...")
    
    result = subprocess.run(
        ["cargo", "test", "--quiet"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"  FAILED: Rust tests failed: {result.stderr}")
        return False
    
    print("  PASSED: All Rust unit tests passed")
    return True

def test_python_unit_tests():
    """Run Python unit tests."""
    print("Testing Python components...")
    
    result = subprocess.run(
        ["python3", "-m", "unittest", "test_quantum_layer.py", "-q"],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"  FAILED: Python tests failed: {result.stderr}")
        return False
    
    print("  PASSED: All Python unit tests passed")
    return True

def test_end_to_end():
    """Test the complete Coheron system end-to-end."""
    print("Testing end-to-end integration...")
    
    result = subprocess.run(
        ["cargo", "run", "--quiet"],
        capture_output=True,
        text=True,
        timeout=30
    )
    
    if result.returncode != 0:
        print(f"  FAILED: End-to-end test failed: {result.stderr}")
        return False
    
    output = result.stdout
    if "Generated text:" not in output:
        print(f"  FAILED: No generated text found in output")
        return False
    
    if "coherence modulated" not in output:
        print(f"  FAILED: No coherence modulation evidence found")
        return False
    
    print("  PASSED: End-to-end generation with quantum coherence modulation")
    return True

def main():
    """Run all integration tests."""
    print("=== Coheron Integration Test Suite ===\n")
    
    tests = [
        ("Python unit tests", test_python_unit_tests),
        ("Rust unit tests", test_rust_unit_tests),
        ("Quantum layer standalone", test_quantum_layer_standalone),
        ("End-to-end integration", test_end_to_end),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"Running {test_name}...")
        try:
            if test_func():
                passed += 1
            print()
        except Exception as e:
            print(f"  ERROR: {e}\n")
    
    print(f"=== Results: {passed}/{total} tests passed ===")
    
    if passed == total:
        print("🎉 All tests passed! Coheron is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())