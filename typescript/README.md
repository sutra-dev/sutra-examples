# TypeScript

This directory contains TypeScript samples for API testing.

## Environment Setup
1. Install Node.js and npm.
2. Install TypeScript and any necessary typings:
   ```bash
   npm ci
   ```

## Running the Samples

Compile and run a TypeScript sample:
  ```bash
  npx ts-node sample.ts
  ```

Which contains the following sample:
  ```typescript
  import { OpenAI } from 'openai';

  async function testSutra() {

      const url = 'https://api.two.ai/v2';

      const client = new OpenAI({
          apiKey: process.env.SUTRA_API_KEY,
          baseURL: url,
      })

      const stream = await client.beta.chat.completions.stream(
          {
              model: 'sutra-light',
              messages: [ { role: 'user', content: 'मुझे मंगल ग्रह के बारे में 5 पैराग्राफ दीजिए' } ],
          }
      ); 

      for await (const chunk of stream) {
          if (chunk.choices.length > 0) {
              const content = chunk.choices[0].delta?.content;
              const finishReason = chunk.choices[0].finish_reason;
              if (content && finishReason === null) {
                  process.stdout.write(content);
              }
          }
      }
  }

  (async (): Promise<void> => {
      await testSutra();
      process.exit(0);
  })();
  ```
