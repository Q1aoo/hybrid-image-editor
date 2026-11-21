# Hybrid Interaction for Precise AI Image Editing

**Prose word count:** ~640 words

## Project Status
- **What I made:** A standalone interactive web prototype (`index.html`) and accompanying design documentation for a hybrid human-AI image editing workflow combining a direct-manipulation spatial brush mask with natural language prompts.
- **What works (Implemented in `index.html`):** HTML5 Canvas brush masking with live bounding-box coordinate extraction, pulsing visual feedback (`"Generating inside mask..."`), rule-based validation guardrails (rejecting missing masks, global style conflicts, multi-object prompts, and undersized masks), explainable G11 repair alerts, and G9/G12 Undo/Redo that preserves the active mask and prompt.
- **What is simulated (Placeholders):** LLM intent parsing (simulated locally in `index.html` via rule-based JSON parsing matching the prompt tests in `02_PROMPT_LOG.md`) and diffusion pixel rendering (simulated via constrained vector rendering clipped strictly inside the mask bounds).
- **What remains unfinished (Planned):** Connecting the validation harness to a live multimodal LLM API, integrating a real masked image-diffusion/inpainting backend, and supporting custom user image uploads.

## Technology Stack
- **Implemented prototype:** HTML5 Canvas API, CSS, and Vanilla JavaScript (zero-dependency single-file prototype in `index.html`).
- **AI tools used for prompt simulation:** Google Gemini (used to test structured JSON intent-parsing prompts and fallback behavior in `02_PROMPT_LOG.md`).
- **Planned backend stack:** Python (Flask) to host the validation harness and live API calls.
- **Undecided choices:** Whether the production image-rendering engine will use a local open-source inpainting model (e.g., Stable Diffusion Inpainting) or a hosted multimodal image API.

## Running or Inspecting the Work
- **Running the interactive prototype:** Open `index.html` directly in any modern web browser (double-click the file; no local server, build step, dependencies, or API key required). Paint a brush mask on the cat, select a quick test case (e.g., *Test A: Red Hat* or *Test B: Global Conflict*), click **Generate Edit**, and click **Undo** to verify active mask retention.
- **Inspecting supporting design work:** Open `01_SPEC.md` for system specifications, `02_PROMPT_LOG.md` for LLM prompt test logs, and the `.png` files for the architecture diagram and early storyboards.
- **API keys:** No API keys are committed to this repository, and none are required to run `index.html`. If a reviewer connects the prompt logic to a live Gemini API later, supply your own key via the `GEMINI_API_KEY` environment variable.

## Development Record
- **Initial framing & storyboards (Weeks 1–2):** Defined the spatial-control problem and created normal and failure-recovery storyboards. *Checked:* Reviewed from a secondary-user perspective, revealing that a plain loading spinner hid mask recognition; revised Frame 3 to add a glowing mask boundary (`"Generating inside mask..."`).
- **Intent parser & fallback design (Weeks 3–4):** Configured the LLM role as a strict JSON intent parser (`operation`, `target_object`, `attributes`). *Checked:* Tested standard prompts (Test A) and conflicting global requests (Test B) to confirm repair turns trigger without hallucination, and added a single-object constraint after identifying multi-object conflicts.
- **Guideline audit & prototype implementation (Weeks 7–8):** Evaluated the workflow against Amershi et al. (2019) and built the standalone `index.html` prototype. *Checked:* Verified all four guardrails, pulsing mask visibility, G11 red-outline error feedback, and G9/G12 Undo state preservation directly in browser testing.

## AI Assistance
- **Tools used:** Gemini (LLM).
- **What I asked for help with:** Structuring the A2 report and README, refining academic English phrasing, drafting the single-file `index.html` prototype from my Lab 1–7 specifications, and generating the visual layout of the system architecture diagram.
- **How I used and changed suggestions:** I supplied my own design specs, storyboard scenarios, and prompt logs, then audited the generated report and README to remove contradictions and clearly separate implemented UI behavior from simulated AI placeholders.
- **How I checked the result:** Manually tested every interaction path and edge case (normal edit, global conflict, multi-object prompt, Undo/Redo) in `index.html` via the browser, and cross-checked all Amershi et al. (2019) guideline mappings against course lecture slides.

## Additional Files
- `index.html`: Standalone interactive web prototype (implemented UI slice + simulated AI placeholders).
- `01_SPEC.md`: System use case, inputs, fallback strategy, and design revisions.
- `02_PROMPT_LOG.md`: Simulated LLM JSON intent-parsing tests (Test A and Test B).
- `system_path.png`: System architecture and Human-AI control boundary diagram.
- `normal_storyboard.png`, `failure_storyboard.png`, `secondary_user_storyboard.png`: Early interaction walkthrough storyboards.