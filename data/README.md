# Coheron Data Directory

This directory stores logs and outputs from the Coheron system.

## Structure

- `logs/`: Contains JSON logs of inference runs with the following format:

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

Each log file is named with a timestamp in the format `YYYYMMDD_HHMMSS.json`.