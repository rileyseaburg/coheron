# 🧠 Coheron: Quantum-Guided Token Selection Loop (Prototype)

A hybrid reasoning system that modulates language model outputs via quantum coherence.

## 📘 Overview

**Coheron** is an experimental project that merges classical symbolic inference with quantum computation to explore emergent behavior in intelligent systems. It uses a lightweight transformer model for token generation and IBM Quantum backends to evaluate the *coherence* of potential outputs.

Instead of relying solely on statistical likelihood, Coheron introduces a quantum "intuition layer"—filtering or modulating token paths based on measured quantum interference and harmonic resonance.

## 📂 Project Structure

```
coheron/
├── rust_core/              # Inference engine & orchestration (Rust)
├── quantum_layer/          # Python module for Qiskit-based logic
├── bridge/                 # IPC/FFI glue code
├── data/                   # Logs and captured resonance outputs
├── tests/                  # Test scripts
├── README.md
└── docs/trd/index.md       # Technical Requirements Document
```

## ⚙️ Architecture

```
[ Rust LLM (e.g., GPT-2) ]
↓
[ Generate token candidates ]
↓
[ Send embeddings to Python → Qiskit ]
↓
[ Quantum circuit evaluates resonance ]
↓
[ Coherence scores returned ]
↓
[ Final token selected → next loop ]
```

## 🚀 Getting Started

### Prerequisites

- Rust (latest stable)
- Python 3.8+
- Qiskit (`pip install qiskit`)
- IBM Quantum account (free tier)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rileyseaburg/coheron.git
   cd coheron
   ```

2. Install Python dependencies:
   ```bash
   pip install -r quantum_layer/requirements.txt
   ```

3. Build the Rust project:
   ```bash
   cd rust_core
   cargo build
   ```

### Running the Prototype

You can run the prototype with:

```bash
./run.sh
```

Or manually:

```bash
cd rust-core
cargo run
```

### Testing

Test the quantum layer:
```bash
./tests/test_quantum_layer.py
```

Test the bridge:
```bash
./tests/test_bridge.py
```

## 📊 Output

The system generates logs in `data/logs/` with the following format:

```json
{
  "prompt": "The truth is",
  "candidates": [
    { "token": "revealed", "score": 0.94 },
    { "token": "hidden", "score": 0.67 },
    { "token": "lost", "score": 0.31 }
  ],
  "selected_token": "revealed",
  "timestamp": "2025-05-28T23:04:00Z"
}
```

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.

## 🌐 Contact

Built by [Riley Seaburg](https://github.com/RileySeaburg)
Questions or collaborations welcome—open an issue or PR.