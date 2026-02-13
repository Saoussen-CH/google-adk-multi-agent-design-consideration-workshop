# Google ADK Workshop Quiz

Test your understanding of the concepts covered in this workshop!

---

### Question 1: What is the role of the **Runner** in ADK?

- A) It defines the agent's personality and behavior through a prompt
- B) It orchestrates agent execution, manages the event loop, and coordinates with the SessionService
- C) It stores conversation history and state between interactions

<details>
<summary>Answer</summary>

**B)** The Runner is the central orchestrator that receives the user's query, invokes the agent's execution logic, processes events, and updates session state.

*Covered in: Part 1*
</details>

---

### Question 2: Why can't you mix `google_search` (built-in tool) with custom Python function tools in the same agent?

- A) Built-in tools use a different API protocol than custom function tools
- B) It's an ADK limitation — each agent must use either built-in or custom tools, not both
- C) Custom tools override built-in tools and cause naming conflicts

<details>
<summary>Answer</summary>

**B)** This is a current ADK limitation. The solution is to create separate specialist agents, each with their own tool type.

*Covered in: Part 2*
</details>

---

### Question 3: What is the difference between `AgentTool` and `sub_agents`?

- A) `AgentTool` runs in an isolated session (black box), while `sub_agents` share the same execution context with full event visibility
- B) `AgentTool` is for LLM agents only, while `sub_agents` is for workflow agents only
- C) They are identical — just two names for the same feature

<details>
<summary>Answer</summary>

**A)** `AgentTool` wraps an agent as a discrete, self-contained tool call (the caller only sees the final result). `sub_agents` share the invocation context, enabling event visibility, shared state, and structured execution order.

*Covered in: Part 3*
</details>

---

### Question 4: How does a `SequentialAgent` pass data between its sub-agents?

- A) Each sub-agent directly calls the next sub-agent using AgentTool
- B) Through the `output_key` parameter, which stores results in session state, and `{{variable}}` interpolation to read them
- C) The Runner serializes each agent's output to a shared file on disk

<details>
<summary>Answer</summary>

**B)** The `output_key` parameter saves an agent's output to session state under a given key. The next agent in the sequence reads it using `{{key_name}}` variable interpolation in its instructions.

*Covered in: Part 4*
</details>

---

### Question 5: How does a `LoopAgent` know when to stop iterating?

- A) It stops after exactly 3 iterations by default
- B) A tool sets `tool_context.actions.escalate = True`, or the `max_iterations` safety limit is reached
- C) The Runner monitors output quality and automatically terminates the loop

<details>
<summary>Answer</summary>

**B)** A tool within the loop can set `tool_context.actions.escalate = True` to signal termination. The `max_iterations` parameter acts as a safety limit to prevent infinite loops.

*Covered in: Part 5*
</details>

---

### Question 6: What execution pattern does the `ParallelAgent` implement?

- A) Round-robin — each sub-agent takes turns processing the query
- B) Pipeline — each sub-agent processes the output of the previous one
- C) Fan-out/Fan-in — all sub-agents execute concurrently, then results are collected

<details>
<summary>Answer</summary>

**C)** The ParallelAgent distributes work to all sub-agents simultaneously (fan-out), then collects their individual results (fan-in). Each agent stores output via its `output_key`.

*Covered in: Part 6*
</details>

---

### Question 7: What are the three data persistence layers in ADK, and how do they differ in scope?

- A) Cache (request-only), Database (permanent), Logs (append-only)
- B) State (within a session), Artifacts (persistent files beyond a session), Memory (cross-session recall)
- C) Local storage (agent-only), Shared storage (team-only), Global storage (all agents)

<details>
<summary>Answer</summary>

**B)** **State** is key-value data that lives within a single session. **Artifacts** are files (text or binary) that persist beyond the session. **Memory** enables agents to recall information from past sessions automatically.

*Covered in: Part 7*
</details>

---

### Question 8: In the capstone architecture, what pattern connects the master orchestrator to the specialist agents?

- A) All specialists are direct sub-agents of the master orchestrator
- B) A hierarchical design where the master delegates to workflow agents (Sequential, Loop, Parallel), which in turn coordinate specialist agents
- C) Each specialist runs as an independent microservice with REST API calls

<details>
<summary>Answer</summary>

**B)** The capstone uses hierarchical orchestration: a Master agent delegates to mid-level workflow agents (SequentialAgent, LoopAgent, ParallelAgent), which coordinate the specialist agents and their tools.

*Covered in: Part 8*
</details>

---

### Question 9: What is a **Session** in ADK?

- A) A configuration file that defines agent parameters and tool bindings
- B) A single ongoing interaction that stores the chronological sequence of messages, events, and temporary state
- C) A background process that keeps the agent running between user requests

<details>
<summary>Answer</summary>

**B)** A Session represents one conversation thread. It holds the message history, actions taken by the agent (Events), and temporary key-value data (State) relevant to that interaction.

*Covered in: Part 1*
</details>

---

### Question 10: Why are **docstrings** critical for custom function tools in ADK?

- A) ADK requires docstrings to compile Python functions into executable tools
- B) The LLM reads the docstring to understand what the tool does and when to call it
- C) Docstrings are displayed to the end user as help text in the chat interface

<details>
<summary>Answer</summary>

**B)** ADK uses the function's docstring as the tool description sent to the LLM. Without a clear docstring, the agent won't know when or how to use the tool.

*Covered in: Part 2*
</details>

---

### Question 11: What is the key characteristic of the **Orchestrator Pattern**?

- A) The orchestrator performs all tasks itself using its own tools and capabilities
- B) The orchestrator understands user intent and delegates work to specialist agents without executing tasks itself
- C) The orchestrator runs all specialist agents in parallel and merges their outputs

<details>
<summary>Answer</summary>

**B)** An orchestrator is a coordinator agent. It analyzes the user's request, determines which specialist is best suited, and delegates via AgentTool calls. It does not perform the actual work.

*Covered in: Part 3*
</details>

---

### Question 12: What is the difference between **LLM-driven** and **workflow-driven** agent architecture?

- A) LLM-driven uses GPT models while workflow-driven uses Gemini models
- B) LLM-driven lets the model decide which agent to call at runtime, while workflow-driven follows a predetermined execution order
- C) LLM-driven is for single agents while workflow-driven is for multiple agents

<details>
<summary>Answer</summary>

**B)** In LLM-driven architecture (e.g., Orchestrator + AgentTool), the LLM decides routing dynamically. In workflow-driven architecture (e.g., SequentialAgent, ParallelAgent), execution order is fixed at design time.

*Covered in: Part 4*
</details>

---

### Question 13: What is the **Critique-Refine** pattern used with `LoopAgent`?

- A) One agent generates content, a second agent evaluates quality, and the loop repeats until a threshold is met
- B) Two agents compete to produce the best output, and the winner is selected
- C) A single agent rewrites its own output in a loop until the user approves

<details>
<summary>Answer</summary>

**A)** The Critique-Refine pattern pairs a content-producing agent with an evaluator agent inside a LoopAgent. The evaluator checks quality against a threshold and either approves (escalate) or sends feedback for another iteration.

*Covered in: Part 5*
</details>

---

### Question 14: What is the purpose of the **Intake Agent** pattern used with `ParallelAgent`?

- A) It validates user credentials before allowing access to the agent system
- B) It parses a natural language request into structured session state so parallel agents can each read the fields they need
- C) It queues incoming requests and rate-limits them before distribution

<details>
<summary>Answer</summary>

**B)** The Intake Agent runs first (in a SequentialAgent before the ParallelAgent) to extract structured data (topic, audience, tone, keywords) from the user's free-text query into session state, enabling each parallel agent to access the relevant fields.

*Covered in: Part 6*
</details>

---

### Question 15: What can a `before_model_callback` be used for?

- A) Caching model responses to reduce API costs
- B) Implementing content safety guardrails that block prohibited topics before they reach the LLM
- C) Automatically selecting the best model based on query complexity

<details>
<summary>Answer</summary>

**B)** A `before_model_callback` fires just before the LLM call. It can inspect the request and return an early `LlmResponse` to block the call entirely — for example, rejecting queries about prohibited topics.

*Covered in: Part 7*
</details>

---

### Question 16: What does **Vertex AI Agent Engine** provide for deploying ADK agents?

- A) A code editor for building agents directly in the cloud console
- B) A fully managed, serverless platform that auto-scales agent deployments with zero infrastructure management
- C) A marketplace for buying and selling pre-built agent templates

<details>
<summary>Answer</summary>

**B)** Vertex AI Agent Engine is Google Cloud's managed platform for deploying ADK agents. It handles infrastructure, auto-scaling (from 0 to N instances), and provides a gRPC endpoint for accessing your agents in production.

*Covered in: Part 9*
</details>
