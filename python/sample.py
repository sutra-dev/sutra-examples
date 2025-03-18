# ---
# sutra-v2

import os
from openai import OpenAI

url = 'https://api.two.ai/v2'

client = OpenAI(base_url=url,
                api_key=os.environ.get("SUTRA_API_KEY"))

stream = client.chat.completions.create(model='sutra-v2',
                                        messages = [{"role": "user", "content": "मुझे मंगल ग्रह के बारे में 5 पैराग्राफ दीजिए"}],
                                        max_tokens=1024,
                                        temperature=0,
                                        stream=True)

for chunk in stream:
    if len(chunk.choices) > 0:
        content = chunk.choices[0].delta.content
        finish_reason = chunk.choices[0].finish_reason
        if content and finish_reason is None:
            print(content, end='', flush=True)
