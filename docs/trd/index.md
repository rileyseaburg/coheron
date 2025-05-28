# 🧾 Technical Requirements Document (TRD)

**Project Title**: Quantum-Guided Symbolic Agent  
**Owner**: Riley Seaburg  
**Languages**: Rust (inference/orchestration), Python (quantum logic)  
**Date**: 2025-05-28  
**Version**: 1.0

---

## 1. Purpose

The purpose of this project is to develop a hybrid inference system that combines a small-scale language model executed locally with a quantum computing backend. The quantum layer acts as a coherence evaluator for symbolic token paths, enabling an exploratory architecture where emergent reasoning is modulated through quantum interference and resonance patterns.

---

## 2. Scope

This system will:
- Run locally on a single developer machine.
- Use Rust for language model inference and orchestration.
- Use Python and Qiskit to interface with IBM Quantum simulators or real backends.
- Operate under a free-tier compute model (e.g., IBM Quantum free access).
- Not require distributed infrastructure or paid services at this stage.

---

## 3. System Overview

The system comprises:
- A Rust-based small transformer model (e.g., GPT-2 via ONNX or HF bindings).
- A Python-based quantum logic module using Qiskit.
- A bridge layer (via FFI or IPC) to exchange token data between Rust and Python.
- A coherence scoring algorithm that feeds quantum measurements back to Rust to influence inference.

---

## 4. Functional Requirements

| ID    | Description                                                                 | Priority |
|-------|-----------------------------------------------------------------------------|----------|
| FR-01 | The system SHALL generate next-token candidates using a local transformer. | High     |
| FR-02 | The system SHALL extract token embeddings from the inference process.       | High     |
| FR-03 | The system SHALL pass token and embedding data to a Python quantum module. | High     |
| FR-04 | The quantum module SHALL evaluate coherence via Qiskit circuits.            | High     |
| FR-05 | The coherence score SHALL be returned to the Rust inference engine.         | High     |
| FR-06 | The inference engine SHALL use this score to influence token selection.     | High     |
| FR-07 | The system SHALL log coherence scores and final token choices.              | Medium   |

---

## 5. Non-Functional Requirements

| ID    | Description                                                                 |
|-------|-----------------------------------------------------------------------------|
| NFR-01 | The system SHALL run entirely on a single local machine (no cloud infra). |
| NFR-02 | The system SHALL not exceed 2GB of RAM during normal operation.           |
| NFR-03 | The system SHALL run in less than 10 seconds per inference cycle.         |
| NFR-04 | The system SHALL use free-tier IBM Quantum resources.                     |
| NFR-05 | The system SHOULD allow token ranking and branching to be configurable.   |

---

## 6. Interfaces

| Component             | Protocol     | Data Format         |
|----------------------|--------------|---------------------|
| Rust → Python Bridge | FFI or IPC   | JSON or Flatbuffers |
| Python → Qiskit      | Native       | Internal Structures |
| Qiskit → Python      | Native       | Qiskit Result Object|
| Python → Rust        | FFI or IPC   | Coherence Score     |

---

## 7. Assumptions

- IBM Quantum account and API key are already registered and available.
- User has local access to CPU and memory sufficient to run ONNX-based GPT-2 or equivalent.
- No hardware GPU acceleration is assumed.

---

## 8. Constraints

- Quantum coherence modeling is limited to what can be simulated or run on IBM’s free quantum backends.
- Output will not initially be real-time or production-grade in terms of speed.

---

## 9. Success Criteria

- System compiles and runs end-to-end on a local machine.
- Token outputs vary based on quantum coherence scores, not just softmax probability.
- Results are logged in a reproducible way showing coherent modulation.
