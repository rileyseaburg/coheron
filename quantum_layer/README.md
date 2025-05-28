# Coheron Quantum Layer

This directory contains the Python implementation of the quantum processing layer for Coheron.

## Components

- `quantum_processor.py`: Main module for quantum coherence evaluation
- `requirements.txt`: Python dependencies

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

The quantum processor is typically called by the bridge layer, but it can also be used directly:

```bash
echo '[{"token": "example", "embedding": [0.1, 0.2, 0.3, 0.4]}]' | python quantum_processor.py
```

## Dependencies

- Qiskit: Quantum computing framework
- NumPy: Numerical operations
- SciPy: Scientific computing utilities
- Matplotlib: Visualization tools (optional)

## Configuration

The quantum circuit uses 3 qubits by default. To modify this, change the `num_qubits` parameter in the `embed_to_quantum_state` function.