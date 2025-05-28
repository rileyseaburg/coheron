mod bridge;
mod logger;
mod model;

use anyhow::{Result, Context};
use chrono::Utc;
use logger::{LogOutput, TokenCandidate};
use model::TransformerModel;
use bridge::QuantumBridge;

fn main() -> Result<()> {
    // Set up logging
    env_logger::init();
    
    println!("🧠 Coheron - Quantum-Guided Token Selection Loop");
    println!("------------------------------------------------");
    
    // Sample prompt
    let prompt = "The truth is";
    println!("Input prompt: {}", prompt);
    
    // Initialize transformer model
    let model = TransformerModel::new()?;
    
    // Generate token candidates
    let num_candidates = 5;
    println!("Generating {} token candidates...", num_candidates);
    let candidates = model.generate_candidates(prompt, num_candidates)
        .context("Failed to generate token candidates")?;
    
    // Display generated candidates
    println!("Token candidates generated:");
    for candidate in &candidates {
        println!("  - {}", candidate.token);
    }
    
    // Send candidates to quantum layer for evaluation
    println!("Evaluating quantum coherence...");
    let scored_candidates = QuantumBridge::evaluate_coherence(&candidates)
        .context("Failed to evaluate coherence")?;
    
    // Display scored candidates
    println!("Coherence scores:");
    for candidate in &scored_candidates {
        println!("  - {} (score: {:.2})", candidate.token, candidate.score);
    }
    
    // Select the token with highest coherence score
    let selected_token = scored_candidates.iter()
        .max_by(|a, b| a.score.partial_cmp(&b.score).unwrap_or(std::cmp::Ordering::Equal))
        .map(|c| c.token.clone())
        .unwrap_or_else(|| "".to_string());
    
    println!("Selected token: {}", selected_token);
    
    // Prepare log output
    let log_output = LogOutput {
        prompt: prompt.to_string(),
        candidates: scored_candidates.clone(),
        selected_token: selected_token.clone(),
        timestamp: Utc::now(),
    };
    
    // Log the results
    let log_file = logger::log_results(&log_output)
        .context("Failed to log results")?;
    
    println!("Results logged to: {}", log_file);
    
    Ok(())
}
