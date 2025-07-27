# 🧠 Coheron

**Quantum-Guided Symbolic Agent**  
*A hybrid reasoning system that modulates language model outputs via quantum coherence.*

---

## 📘 Overview

**Coheron** is an experimental project that merges classical symbolic inference with quantum computation to explore emergent behavior in intelligent systems. It uses a lightweight transformer model for token generation and IBM Quantum backends to evaluate the *coherence* of potential outputs.

Instead of relying solely on statistical likelihood, Coheron introduces a quantum "intuition layer"—filtering or modulating token paths based on measured quantum interference and harmonic resonance.

---

## ⚙️ Architecture

```

\[ Rust LLM (e.g., GPT-2) ]
↓
\[ Generate token candidates ]
↓
\[ Send embeddings to Python → Qiskit ]
↓
\[ Quantum circuit evaluates resonance ]
↓
\[ Coherence scores returned ]
↓
\[ Final token selected → next loop ]

```

---

## 🔧 Tech Stack

- **Rust** – Orchestration, transformer inference, feedback loop
- **Python** – Quantum logic layer (via Qiskit)
- **Qiskit / IBM Quantum** – Simulated or real quantum backend
- **ONNX / Hugging Face** – Local LLM execution (e.g., GPT-2)
- **IPC or FFI** – Communication between Rust and Python layers

---

## 🚀 Goals

- Investigate symbolic inference guided by quantum resonance
- Prototype a system capable of detecting emergent coherence
- Log, visualize, and analyze coherence-influenced token selection
- Operate entirely on a local developer machine using free-tier IBM Quantum resources

---

## 📂 Project Structure

```

coheron/
├── rust-core/              # Inference engine & orchestration (Rust)
├── quantum-layer/          # Python module for Qiskit-based logic
├── bridge/                 # IPC/FFI glue code
├── data/                   # Logs and captured resonance outputs
├── README.md
└── TRD.md                  # Technical Requirements Document

````

---

## 🔑 Getting Started

### Prerequisites
- Rust (latest stable)
- Python 3.10+
- NumPy (`pip install numpy`)

### Quick Start

1. Clone the repo:
   ```bash
   git clone https://github.com/rileyseaburg/coheron.git
   cd coheron
   ```

2. Install Python dependencies:
   ```bash
   pip install numpy
   ```

3. Run the integrated system:
   ```bash
   cargo run
   ```

4. Run tests to validate functionality:
   ```bash
   python3 integration_test.py
   ```

### Current Implementation Status

✅ **WORKING PROTOTYPE** - See [IMPLEMENTATION.md](IMPLEMENTATION.md) for details.

- Rust inference engine with mock transformer
- Python quantum coherence evaluation layer  
- JSON-based communication bridge
- Comprehensive test suite
- End-to-end text generation with quantum modulation

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🌐 Contact

Built by [Riley Seaburg](https://github.com/RileySeaburg)
Questions or collaborations welcome—open an issue or PR.
