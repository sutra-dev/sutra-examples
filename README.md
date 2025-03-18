# SUTRA API Samples Repository

SUTRA is a series of ultrafast, multilingual, online Generative AI models. It supports over 50 languages with conversation, search, and visual capabilities.

This repository is a resource designed to provide straightforward examples on how to implement API testing in both Python and TypeScript,
aimed at developers, QA engineers, and anyone interested in using our models.

## SUTRA models comes in multiple flavors.
- **SUTRA-V2**: Designed for conversation, summarization, and other tasks in 50+ languages. Highly efficient and optimized for ultra-low latency applications.

## Repository Structure

This repository is organized into subdirectories:

- **[python](python/README.md)**
- **[typeScript](typescript/README.md)**
- **[curl](curl/README.md)**

Each subdirectory contains sample code and instructions specific to the respective programming language.

## Getting Started

To get started with these examples, you will need to clone this repository to your local machine.
Depending on your environment setup, you may need to install additional software or libraries.
For obtaining an API key contact: `support@two.ai`. The documentation can be accessed [here](https://docs.two.ai/).

### Prerequisites

- Get a SUTRA API key and set as an environment variable named SUTRA_API_KEY.
- Git (for cloning this repository)
- Python (for running Python samples)
- Node.js and npm/yarn (for running TypeScript samples)

### How to Use This Repository

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/TwoResearch/sutra-examples.git
   cd sutra-examples
   ```

2. **Navigate to a Subdirectory:**
   ```bash
   cd python   # For Python samples
   ```
   or
   ```bash
   cd typescript   # For TypeScript samples
   ```
   or
   ```bash
   cd curl   # For Curl examples
   ```

3. **Follow the README in the Subdirectory:**
   Each subdirectory has its own README file with detailed instructions on how to run the samples.

4. List of available endpoints and models: 

| endpoint url                             | model       |
|------------------------------------------|-------------|
| `https://api.two.ai/v2/chat/completions` | SUTRA-V2	 |
| `https://api.two.ai/v2/chat/completions` | SUTRA-LIGHT | # now deprecated
| `https://api.two.ai/v2/chat/completions` | SUTRA-PRO   | # now deprecated


## Contributions and Feedback

Contributions to this repository are welcome. To contribute, please follow the standard fork-and-pull request workflow. Ensure you update or provide a README file in your pull requests if necessary.

For feedback and questions, please open an issue in this repository.

## License

This repository is released under the MIT License. See the `LICENSE` file for more details.
