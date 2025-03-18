// ---
// sutra-v2

import { OpenAI } from 'openai';

async function testSutra() {

    const url = 'https://api.two.ai/v2';
    
    const client = new OpenAI({
        apiKey: process.env.SUTRA_API_KEY,
        baseURL: url,
    })

    const stream = await client.beta.chat.completions.stream(
        {
            model: 'sutra-v2',
            messages: [ { role: 'user', content: 'मुझे मंगल ग्रह के बारे में 5 पैराग्राफ दीजिए' } ],
        }
    );

    for await (const event of stream) {
        console.log(event);
    }
}

(async (): Promise<void> => {
    await testSutra();
    process.exit(0);
})();
