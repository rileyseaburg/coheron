# Coheron Rust Core

This directory contains the Rust implementation of the inference engine and orchestration layer for Coheron.

## Components

- `main.rs`: Entry point and orchestration logic
- `model.rs`: Transformer model interface for token generation
- `bridge.rs`: Communication with Python quantum layer
- `logger.rs`: Logging functionality for inference results

## Building and Running

Make sure you have Rust installed, then run:

```bash
cargo build
cargo run
```

## Dependencies

- rust-bert: Hugging Face Transformers bindings for Rust
- serde/serde_json: Serialization/deserialization
- chrono: Date and time utilities
- anyhow/thiserror: Error handling

## Configuration

The default model is `distilgpt2`. To use a different model, modify the `MODEL_NAME` constant in `model.rs`.