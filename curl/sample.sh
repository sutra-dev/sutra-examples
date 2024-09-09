# sutra-light, sutra-pro

curl -X POST "https://api.two.ai/v2/chat/completions" \
  -H "authorization: Bearer $SUTRA_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Accept text/event-stream" \
  -d '{
  "model": "sutra-light",
  "messages": [
    {"role": "user", "content": "मुझे मंगल ग्रह के बारे में 5 पैराग्राफ दीजिए"}
  ]
}'
