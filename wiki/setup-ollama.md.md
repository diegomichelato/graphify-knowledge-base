# setup-ollama.md

> Statically indexed from `docs/setup-ollama.md` (no AI). Node id: `doc:docs/setup-ollama.md`

## Sections

- Using graphify-dotnet with Ollama (Local Models)
  - Quick Start
  - Why Use Ollama?
  - Prerequisites
  - Step 1: Install Ollama
- Download and run the installer from https://ollama.com
- Or use Homebrew:
- Start the server (runs in background)
- Official installation script
- Start the server
  - Step 2: Pull a Model
- llama3.2 - Excellent for general coding tasks, 8B/70B
- Or pull the larger 70B version for better analysis
- CodeLlama - Specialized for code, faster
- Deepseek Coder - Excellent code understanding
  - Step 3: Verify Ollama is Running
- Check if Ollama is serving (any response = success)
- Expected response:
- {"models":[{"name":"llama3.2:latest","modified_at":"..."}]}
- On Windows with PowerShell:
- Kill existing process
- Start fresh
  - Step 4: Configure graphify-dotnet
- Run with default Ollama settings (localhost:11434, llama3.2)
- Specify a custom model

## Outgoing references

- `../README.md`
- `../src/Graphify.Sdk/OllamaClientFactory.cs`
- `./setup-azure-openai.md`
- `./setup-copilot-sdk.md`
