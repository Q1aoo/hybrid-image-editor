# 02_PROMPT_LOG.md

Use this file if you ask an AI assistant to help with the project. Name the tool, record the request or command, summarise what came back and explain what you kept, changed or rejected. If you did not use an assistant, you do not need to submit this file.

## Test A: Standard Input (Normal Prompt) <16:20>
**Tool used**: Gemini Pro (via API or Web Interface)

**Request or command (System Prompt + User Input)**:
I am building an intent parser for an image editing tool. You will receive a user's text prompt. You must output ONLY a valid JSON object with the following keys:
- "operation" (e.g., add, remove, modify)
- "target_object" (what the user wants to affect)
- "attributes" (any specific details like color, size, etc.)
If the prompt is ambiguous or asks for global changes (like changing the whole style), output a JSON with a single key "error" explaining the issue.

User Prompt: "Add a bright red winter hat onto the head."

**What came back (LLM Output)**:
{
  "operation": "add",
  "target_object": "winter hat",
  "attributes": "bright red"
}

**What I decided to keep, change or reject, and why**:
**Kept:** I kept the system prompt as is for this test because the LLM successfully followed instructions. It extracted the correct operation, target, and attributes perfectly, and output strictly valid JSON without any conversational filler text. This verifies the normal system path works.

## Test B: Problem Input (Ambiguous/Global Request) <16:45>
**Tool used**: Gemini Pro (via API or Web Interface)

**Request or command (System Prompt + User Input)**:
I am building an intent parser for an image editing tool. You will receive a user's text prompt. You must output ONLY a valid JSON object with the following keys:
- "operation" (e.g., add, remove, modify)
- "target_object" (what the user wants to affect)
- "attributes" (any specific details like color, size, etc.)
If the prompt is ambiguous or asks for global changes (like changing the whole style), output a JSON with a single key "error" explaining the issue.

User Prompt: "Change the whole image into a cyberpunk style and make it night time."

**What came back (LLM Output)**:
{
  "error": "The prompt requests a global style change (cyberpunk, night time) rather than a localized object edit. This tool is for specific regional edits only."
}

**What I decided to keep, change or reject, and why**:
**Kept:** I kept this result because the LLM successfully executed the fallback strategy. Instead of trying to force a global style change into the "operation" and "target_object" keys (which would cause the brush mask to fail), it correctly identified the out-of-scope request and returned a structured JSON error. This proves the system can safely trigger a repair turn.