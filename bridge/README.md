# Coheron Bridge Layer

This directory contains the bridge implementation for inter-process communication between the Rust inference engine and Python quantum layer.

## Components

- `bridge.py`: Python script that handles IPC between Rust and the quantum layer

## Usage

The bridge is typically called from the Rust core, but it can also be used directly:

```bash
echo '[{"token": "example", "embedding": [0.1, 0.2, 0.3, 0.4]}]' | python bridge.py
```

## Operation

1. The bridge receives token data from stdin (JSON format)
2. It passes this data to the quantum layer for processing
3. It receives coherence scores from the quantum layer
4. It returns the scored tokens to stdout (JSON format)

## Dependencies

- Python 3.8+
- JSON for serialization
- subprocess for calling the quantum layer