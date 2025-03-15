# Curl

This directory contains sample scripts demonstrating how to test APIs using Curl

## Running the Samples

To run a sample bash script:
  ```bash
  bash sample.sh
  ```
  
Which contains the following sample for `sutra-light`:
  ```bash
  curl -X POST "https://api.two.ai/v2/chat/completions" \
    -H "Authorization: Bearer $SUTRA_API_KEY" \
    -H "Content-Type: application/json" \
    -H "Accept text/event-stream" \
    -d '{
    "model": "sutra-light",
    "messages": [
      {"role": "user", "content": "मुझे मंगल ग्रह के बारे में 5 पैराग्राफ दीजिए"}
    ]
  }'
  ```
  
