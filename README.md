# Hybrid Interaction for Precise AI Image Editing

**Author:** Jiamu Rao | **Student ID:** 3204917

## 1. Project Overview
This project explores a hybrid human-AI interaction system designed to bridge the "gulf of execution" in generative AI image editing. It allows users to combine natural language text prompts with a direct-manipulation brush mask, ensuring precise spatial control over AI-generated localized edits without unpredictable global pixel drift.

## 2. Technology Stack
* **Front-end (Simulated):** HTML5 Canvas API (for drawing the spatial mask) and JavaScript (for UI state management, including the glowing mask boundary during generation).
* **Back-end Logic:** Python (Flask routing).
* **AI Component:** LLM acts strictly as a structured intent parser via System Prompts (simulated JSON generation), rather than a conversational agent.

## 3. Architecture and Data Flow
1. **User Input:** The user paints a spatial mask and enters a text prompt (e.g., "Add a red hat").
2. **Intent Parsing:** The backend LLM parses the text into a JSON object containing `{operation, target_object, attributes}`.
3. **Validation Harness:** Python logic intercepts the JSON. If the text requests a global change but a small local mask is drawn, the system rejects the operation.
4. **Execution & Feedback:** The rendering engine applies the edit inside the mask coordinates. The UI displays "Generating inside mask..." to bridge the evaluation gulf before showing the final image.

## 4. Development Diary
* **Week 1-2:** Identified the spatial control problem in text-to-image models. Drew normal and failure recovery storyboards focusing on visual feedback.
* **Week 3-4:** Built the backend intent parser. Implemented strict JSON schema constraints and a fallback repair turn to prevent AI hallucination and ensure the system respects the mixed-initiative boundary.
* **Week 7-8:** Evaluated the system against Amershi et al.'s Guidelines, ensuring reversibility (Undo mechanism/G12) and clear error explanations (G11).

## 5. AI Assistance
* **Tools used:** Gemini (Large Language Model)
* **What I asked for help with:** I used the AI to help structure the academic formatting of the A2 Project Report, refine the English phrasing for the design rationale (connecting my Week 2-4 labs to Norman's execution/evaluation gulfs and Amershi's guidelines), and draft the README template based on my project notes.
* **How I used and changed suggestions:** I provided the AI with my specific project context ("Brush mask with text prompt hybrid system"), my storyboard ideas, and my Lab 3 prompt logs. I used its suggested report structure but reviewed and modified the theoretical justifications to ensure they accurately reflected the actual JSON intent parser logic and fallback strategies I designed in my labs.
* **How I checked the result:** I cross-referenced the AI-generated theoretical connections (e.g., Amershi's G11 and G12 guidelines) with the Week 7 course lecture slides to ensure absolute academic accuracy before finalizing the text.