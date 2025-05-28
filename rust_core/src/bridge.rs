use anyhow::{Result, Context};
use serde_json;
use std::io::{Read, Write};
use std::process::{Command, Stdio};
use crate::logger::TokenCandidate;

/// Handles communication with the Python quantum layer
pub struct QuantumBridge;

impl QuantumBridge {
    /// Send token candidates to the quantum layer and get back coherence scores
    pub fn evaluate_coherence(candidates: &[TokenCandidate]) -> Result<Vec<TokenCandidate>> {
        // Prepare serializable candidates (include token and embedding)
        let serializable_candidates: Vec<serde_json::Value> = candidates
            .iter()
            .map(|candidate| {
                serde_json::json!({
                    "token": candidate.token,
                    "embedding": candidate.embedding.clone().unwrap_or_default()
                })
            })
            .collect();

        // Serialize to JSON
        let input_json = serde_json::to_string(&serializable_candidates)?;

        // Start the Python bridge script
        let mut child = Command::new("python")
            .arg("bridge/bridge.py")
            .stdin(Stdio::piped())
            .stdout(Stdio::piped())
            .stderr(Stdio::piped())
            .spawn()
            .context("Failed to start bridge process")?;

        // Write the JSON to the process's stdin
        if let Some(mut stdin) = child.stdin.take() {
            stdin.write_all(input_json.as_bytes())?;
            // stdin is closed automatically when dropped
        }

        // Read the output
        let mut output = String::new();
        if let Some(mut stdout) = child.stdout.take() {
            stdout.read_to_string(&mut output)?;
        }

        // Read any errors
        let mut errors = String::new();
        if let Some(mut stderr) = child.stderr.take() {
            stderr.read_to_string(&mut errors)?;
        }

        // Wait for the process to exit
        let status = child.wait()?;
        if !status.success() {
            anyhow::bail!("Bridge process failed: {}", errors);
        }

        // Parse the output JSON
        let scored_candidates: Vec<TokenCandidate> = serde_json::from_str(&output)
            .context("Failed to parse bridge output")?;

        Ok(scored_candidates)
    }
}