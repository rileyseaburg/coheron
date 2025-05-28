use anyhow::Result;
use chrono::{DateTime, Utc};
use serde::{Deserialize, Serialize};
use std::fs;
use std::path::Path;

/// Represents a token candidate with its score
#[derive(Debug, Serialize, Deserialize, Clone)]
pub struct TokenCandidate {
    pub token: String,
    pub score: f32,
    #[serde(skip_serializing)]
    pub embedding: Option<Vec<f32>>,
}

/// Structure for the log output
#[derive(Debug, Serialize, Deserialize)]
pub struct LogOutput {
    pub prompt: String,
    pub candidates: Vec<TokenCandidate>,
    pub selected_token: String,
    pub timestamp: DateTime<Utc>,
}

/// Logs the inference results to a JSON file
pub fn log_results(log_output: &LogOutput) -> Result<String> {
    // Create logs directory if it doesn't exist
    let log_dir = Path::new("data/logs");
    fs::create_dir_all(log_dir)?;

    // Generate timestamp-based filename
    let timestamp = Utc::now().format("%Y%m%d_%H%M%S");
    let filename = format!("data/logs/{}.json", timestamp);

    // Serialize the log output to JSON
    let json = serde_json::to_string_pretty(log_output)?;

    // Write to file
    fs::write(&filename, json)?;

    Ok(filename)
}