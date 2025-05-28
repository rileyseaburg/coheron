#!/bin/bash
# Run script for Coheron prototype

echo "🧠 Coheron - Quantum-Guided Token Selection Loop"
echo "-----------------------------------------------"

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Error: Python is not installed"
    exit 1
fi

# Check if pip is installed
if ! command -v pip &> /dev/null; then
    echo "❌ Error: pip is not installed"
    exit 1
fi

# Check if Rust is installed
if ! command -v cargo &> /dev/null; then
    echo "❌ Error: Rust/Cargo is not installed"
    exit 1
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r quantum_layer/requirements.txt

# Move to the rust_core directory
cd rust_core

# Build the Rust project
echo "🔨 Building Rust core..."
cargo build

# Run the prototype
echo "🚀 Running Coheron prototype..."
cargo run

echo "✅ Done"