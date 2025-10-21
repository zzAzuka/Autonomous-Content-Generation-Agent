# Autonomous-Content-Generation-Agent
This project implements an **agentic workflow for automated content creation**, capable of researching, outlining, drafting, reviewing, and evaluating articles — all orchestrated through a **multi-step LangGraph pipeline**.

The system integrates **human-in-the-loop checkpoints** for quality assurance and uses an **LLM-as-a-Judge** evaluator to assess the final output, ensuring both creativity and factual integrity.

---

## 🚀 Overview

Given a topic, the Content-Creation Agent performs the following sequence:

1. **Research** – Gathers relevant information using external search tools.  
2. **Outline Generation** – Produces a structured content outline.  
3. **Human Review (1)** – Allows manual refinement of the outline.  
4. **Drafting** – Expands the approved outline into a detailed article draft.  
5. **Human Review (2)** – Invites feedback on the draft before finalization.  
6. **Final Article Generation** – Produces the polished final article.  
7. **Evaluation** – Uses an LLM-as-a-Judge to rate the article’s quality.

Each stage of the workflow is managed by a **distinct node** in the LangGraph framework, promoting modularity and clear separation of responsibilities.

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Framework** | [LangGraph](https://langchain-ai.github.io/langgraph/) |
| **Model Provider** | [Google Gemini](https://deepmind.google/technologies/gemini/) |
| **Model Used** | Gemini 2.5 Flash |
| **Search Tool** | [Tavily Search](https://tavily.com/) |

---

## 🧩 Workflow Architecture

The workflow is designed as a **multi-node LangGraph pipeline**:
Topic Input → Research Node → Outline Node → Human Review → Draft Node → Human Review → Final Article Node → LLM Evaluation


- Each **node** represents a distinct stage in the process.
- **Conditional edges** ensure that the workflow proceeds only after human validation or successful model execution.
- The design allows flexibility to **re-run specific stages** without restarting the entire workflow.

---

## 👥 Human-in-the-Loop Implementation

To ensure quality and human oversight, the system embeds **two checkpoints** for human intervention:

1. **Outline Review Checkpoint**  
   - After the outline is generated, the human user can review, edit, or approve it.  
   - The workflow halts here until feedback is provided.

2. **Draft Review Checkpoint**  
   - After the draft is created, it’s presented for another round of human feedback.  
   - The user can suggest refinements before the final article is generated.

This two-step feedback mechanism ensures that the final content aligns with user intent, tone, and factual accuracy.

---

## ⚖️ LLM-as-a-Judge Evaluation

The **LLM Evaluation Module** functions as a standalone evaluation agent:

- It reads input text files containing the **research**, **outline**, and **draft** content.  
- The evaluator then passes these inputs to a **Judge LLM** (Gemini 2.5 Flash).  
- The Judge LLM scores the output on parameters such as:
  - Content coherence  
  - Factual consistency  
  - Depth of research  
  - Writing style and tone  
  - Overall quality  

This creates a self-assessment feedback loop that helps quantify the performance of each generated article.

---

