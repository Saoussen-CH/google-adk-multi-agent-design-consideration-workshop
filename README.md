# Google ADK Multi-Agent on Vertex AI

**Multi-Agent Content Creation design consideration Workshop**

An intelligent, multi-agent content creation system and comprehensive workshop powered by Google's Gemini models. This project demonstrates how to build AI agents with custom tools using Google's Agent Development Kit (ADK). Throughout the workshop, you will explore various design patterns (Sequential, Parallel, Iterative architectures), navigate agent architecture trade-offs (Sub-agents vs. Agent as a Tool), and master memory & context for reliable agent teams. It also covers implementing callbacks & observability, managing sessions, state, and artifacts, and achieving scalable deployment of a full-stack system (React frontend, FastAPI backend) to Vertex AI Agent Engine and Cloud Run on Google Cloud Platform.

## Workshop Notebooks - Start Here!

**New to AI agents?** Start with our interactive notebooks - no setup required, just click and learn!

Interactive Jupyter notebooks to learn how to build multi-agent systems step by step. Click the badge to open directly in Google Colab:

| Part | Topic | Description | Colab Link |
|------|-------|-------------|------------|
| 1 | First Agent | Create your first AI agent with Google ADK | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saoussen-CH/google-adk-multi-agent-design-consideration-workshop/blob/main/notebooks/part1_first_agent.ipynb) |
| 2 | Custom Tools | Build custom tools for your agents | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saoussen-CH/google-adk-multi-agent-design-consideration-workshop/blob/main/notebooks/part2_custom_tools.ipynb) |
| 3 | Agent Teams | Coordinate multiple agents working together | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saoussen-CH/google-adk-multi-agent-design-consideration-workshop/blob/main/notebooks/part3_agent_teams.ipynb) |
| 4 | Sequential Workflows & Design Patterns | Sequential pipelines + when to use LLM vs workflow agents | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saoussen-CH/google-adk-multi-agent-design-consideration-workshop/blob/main/notebooks/part4_sequential_workflows_and_design_patterns.ipynb) |
| 5 | Iterative Workflows | Create quality improvement loops | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saoussen-CH/google-adk-multi-agent-design-consideration-workshop/blob/main/notebooks/part5_iterative_workflows.ipynb) |
| 6 | Parallel Workflows | Execute agents in parallel for efficiency | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saoussen-CH/google-adk-multi-agent-design-consideration-workshop/blob/main/notebooks/part6_parallel_workflows.ipynb) |
| 7 | Callbacks, Context & Memory | Callbacks, sessions/state, artifacts, and memory, including ADK's LoggingPlugin for local observability | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saoussen-CH/google-adk-multi-agent-design-consideration-workshop/blob/main/notebooks/part7_callbacks_context_memory.ipynb) |
| 8 | Capstone Project | Build the complete Content Creation Studio | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saoussen-CH/google-adk-multi-agent-design-consideration-workshop/blob/main/notebooks/part8_capstone_project.ipynb) |
| 9 | Deployment | Deploy agents to Agent Engine on GCP | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saoussen-CH/google-adk-multi-agent-design-consideration-workshop/blob/main/notebooks/part9_deployment_agent_engine.ipynb) |
| 10 | Full-Stack Cloud Run | Deploy full-stack app (React + FastAPI) to Cloud Run | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Saoussen-CH/google-adk-multi-agent-design-consideration-workshop/blob/main/notebooks/part10_fullstack_cloud_run.ipynb) |

### Workshop Learning Path

1. **Part 1-2**: Foundations - Learn basic agent creation and custom tools
2. **Part 3-6**: Advanced Patterns - Master agent coordination, workflows, and design patterns
3. **Part 7**: Callbacks, Context & Memory - Callbacks, sessions/state, artifacts, and long-term memory
4. **Part 8**: Capstone Project - Build the complete Content Creation Studio
5. **Part 9**: Deployment - Deploy to Vertex AI Agent Engine on GCP
6. **Part 10**: Full-Stack Cloud Run - Deploy the full-stack app (React + FastAPI + Agent Engine) to Cloud Run

**Tip**: Each notebook is self-contained and can be run independently in Google Colab. No local setup required!

---

## Workshop: Google ADK & Vertex AI: Multi-Agent System Design

What we will cover:

- **Build AI Agents**: Create agents with custom tools.                                                                                           
- **Design Patterns**: Choosing between LLM-Driven and Workflow-Driven architectures (Sequential, Parallel, Iterative).                           
- **Agent Architecture**: Navigating the trade-offs between Sub-agents and Agent as a Tool.                                                           
- **Callbacks & Observability**: Implementing custom logging, guardrails, and metrics with callbacks, and utilizing ADK's built-in LoggingPlugin for comprehensive local debugging.                                                                                                                  
- **Management**: How to handle sessions, state, and artifacts within an integrated AI orchestration layer.                                       
- **Memory & Context**: Mastering Short-Term vs. Long-Term memory for reliable agent teams.                                                       
- **Scalable Deployment**: Deploying your full-stack Multi-Agent System to GCP environments.    

---

## Quick Start & Deployment

**New to this project?** Check out [**GETTING_STARTED.md**](GETTING_STARTED.md) for complete step-by-step instructions with 4 test prompts!


---

## Prerequisites

### Required Software
1. **Python 3.11.13** - For backend (via [pyenv](#python-version-management) recommended)
2. **Node.js 18+** - For frontend ([Download](https://nodejs.org/))
3. **Google API Key** - Get from [Google AI Studio](https://aistudio.google.com/app/apikey)
4. **pyenv** (optional) - Python version manager

### For Cloud Deployment
5. **Google Cloud Project** with billing enabled
6. **gcloud CLI** - [Install guide](https://cloud.google.com/sdk/docs/install)


### Python Version Management

This project requires Python 3.11.13. We recommend [pyenv](https://github.com/pyenv/pyenv) for version management.

```bash
# Install pyenv
curl https://pyenv.run | bash

# Add to your shell profile (~/.bashrc or ~/.zshrc)
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"

# Install and activate Python 3.11.13
pyenv install 3.11.13
pyenv local 3.11.13
python --version  # Should show: Python 3.11.13
```

The project includes a `.python-version` file that automatically activates the correct version.

---

## Features

### Two Main Capabilities:

1. **Create Content** - Full multi-agent content package generation
   - Blog posts (800-1200 words)
   - Social media content (LinkedIn, Twitter, Instagram)
   - Email newsletters
   - SEO metadata

2. **Analyze Text** - Text analysis using AI
   - Word count
   - Readability score
   - Hashtag generation

## Architecture

> **Mermaid Diagrams**:
> - [Architecture Diagram](diagrams/architecture.mmd) - Complete system architecture
> - [Multi-Agent System Diagram](diagrams/multi-agent-system.mmd) - Agent workflow and interactions

### System Overview

```mermaid
graph TB
    subgraph "User Interface"
        Browser[Web Browser]
    end

    subgraph "Google Cloud Run"
        subgraph "Combined Service (Port 8080)"
            Frontend[React Frontend<br/>Static Files<br/>Vite + React 18]
            Backend[FastAPI Backend<br/>API Server<br/>Python 3.11 + Uvicorn]
            Frontend -.served by.-> Backend
        end
    end

    subgraph "Google Cloud Platform"
        subgraph "Vertex AI Agent Engine"
            Orchestrator[Master Orchestrator<br/>Agent<br/>gemini-2.5-flash]
            Coordinator[Content Creation<br/>Coordinator<br/>gemini-2.5-flash]
            Analyzer[Content Analyzer<br/>Agent<br/>gemini-2.5-flash]

            Orchestrator --> Coordinator
            Orchestrator --> Analyzer
        end

        subgraph "Infrastructure"
            AR[Artifact Registry<br/>Docker Images]
            Storage[Cloud Storage<br/>Staging Bucket]
            Logging[Cloud Logging<br/>& Monitoring]
        end
    end

    subgraph "AI Models"
        Gemini[Google Gemini 2.5 Flash<br/>via Vertex AI]
    end

    Browser -->|HTTPS| Frontend
    Frontend -->|/api/*| Backend
    Backend -->|RemoteRunner| Orchestrator
    Coordinator -->|API Calls| Gemini
    Analyzer -->|API Calls| Gemini

    Backend -.logs.-> Logging
    AR -.deploys.-> Backend
    Coordinator -.stores.-> Storage

    classDef frontend fill:#61dafb,stroke:#333,color:#000
    classDef backend fill:#009688,stroke:#333,color:#fff
    classDef agent fill:#ff6f00,stroke:#333,color:#fff
    classDef infra fill:#4285f4,stroke:#333,color:#fff
    classDef ai fill:#ea4335,stroke:#333,color:#fff

    class Browser,Frontend frontend
    class Backend backend
    class Orchestrator,Coordinator,Analyzer agent
    class AR,Storage,Logging infra
    class Gemini ai
```

### Multi-Agent System

```mermaid
graph TB
    Start([User Request]) --> Orchestrator[Master Orchestrator<br/>gemini-2.5-flash<br/>+ Callbacks + Memory]

    Orchestrator -->|"content creation"| FullWorkflow[Full Content Workflow<br/>SequentialAgent]
    Orchestrator -->|"text analysis"| Analyzer[Content Analyzer<br/>gemini-2.5-flash]

    subgraph "Phase 1: Research & Draft (Sequential)"
        FullWorkflow --> Research[Topic Research Agent<br/>google_search<br/>output_key: blog_topic]
        Research --> Drafter[Content Drafter Agent<br/>reads: blog_topic<br/>output_key: current_content]
    end

    subgraph "Phase 2: Quality Loop (max 2 iterations)"
        Drafter --> Quality{Quality Checker<br/>Score >= 70?}
        Quality -->|No| Improver[Content Improver<br/>Refine Content]
        Improver --> Quality
        Quality -->|Yes, exit_loop| Approved[Approved Content]
    end

    subgraph "Phase 3: Multi-Channel Generation (Parallel)"
        Approved --> Blog[Blog Post Writer<br/>800-1200 words<br/>output_key: final_blog_post]
        Approved --> Social[Social Media Creator<br/>LinkedIn, Twitter, Instagram<br/>output_key: social_media_posts]
        Approved --> Email[Email Newsletter Writer<br/>Subject + Body + CTA<br/>output_key: email_newsletter]
        Approved --> SEO[SEO Metadata Agent<br/>Meta tags & keywords<br/>output_key: seo_metadata]
    end

    Blog --> Result([Complete Content Package<br/>All outputs in session state])
    Social --> Result
    Email --> Result
    SEO --> Result

    Analyzer --> AnalysisResult([Analysis Report<br/>Word count + Readability + Hashtags])

    classDef orchestrator fill:#9c27b0,stroke:#333,stroke-width:3px,color:#fff
    classDef workflow fill:#ff6f00,stroke:#333,stroke-width:2px,color:#fff
    classDef phase1 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    classDef phase2 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef phase3 fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    classDef analyzer fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef endpoint fill:#ffd700,stroke:#333,stroke-width:3px,color:#000

    class Orchestrator orchestrator
    class FullWorkflow workflow
    class Research,Drafter phase1
    class Quality,Improver,Approved phase2
    class Blog,Social,Email,SEO phase3
    class Analyzer analyzer
    class Start,Result,AnalysisResult endpoint
```

### Agent Responsibilities

| Agent | Type | Responsibility |
|-------|------|----------------|
| **Master Orchestrator** | LLM Agent | Routes requests to content workflow or analyzer |
| **Full Content Workflow** | SequentialAgent | Orchestrates the 3-phase content pipeline |
| **Research & Draft** | SequentialAgent | Runs topic research then content drafting in order |
| **Quality Improvement Loop** | LoopAgent | Checks quality and improves until score >= 70 (max 2 iterations) |
| **Parallel Content Creation** | ParallelAgent | Runs blog, social, email, and SEO agents concurrently |
| **Topic Research Agent** | LLM Agent | Identifies trending topics via google_search |
| **Content Drafter Agent** | LLM Agent | Creates initial content drafts |
| **Quality Checker Agent** | LLM Agent | Evaluates content quality (score 0-100) |
| **Content Improver Agent** | LLM Agent | Refines content based on feedback |
| **Blog Post Writer** | LLM Agent | Generates SEO-optimized blog posts (800-1200 words) |
| **Social Media Creator** | LLM Agent | Creates platform-specific social content |
| **Email Newsletter Writer** | LLM Agent | Writes engaging email newsletters |
| **SEO Metadata Agent** | LLM Agent | Generates meta descriptions and keywords |
| **Content Analyzer Agent** | LLM Agent | Analyzes text (readability, word count, hashtags) |


## Local Development Guide

### Prerequisites for Local Development

Before running locally, ensure you have:
1. Python 3.11.13 installed (via pyenv recommended)
2. Node.js 18+ installed
3. Google API Key from [Google AI Studio](https://aistudio.google.com/app/apikey)
4. Agent deployed to Agent Engine (see [Deploy Agent](#deploy-agent-to-agent-engine))

### Option 1: Local Agent (No Agent Engine Required)

Run the agent entirely on your local machine without deploying to Agent Engine.

**Step 1: Install Dependencies**
```bash
# Ensure Python 3.11.13 is active
python --version  # Should show 3.11.13

# Install Python dependencies
pip install -r requirements.txt

# Install frontend dependencies (optional)
cd frontend
npm install
cd ..
```

**Step 2: Configure Environment**
```bash
# Create .env file
cat > .env << 'EOF'
# Google API Configuration
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=0

# Agent Configuration
WORKER_MODEL=gemini-2.0-flash-exp
COORDINATOR_MODEL=gemini-2.0-flash-exp
QUALITY_SCORE_THRESHOLD=70
MAX_IMPROVEMENT_ITERATIONS=3
EOF
```

---

### Option 2: Local Backend + Agent Engine

Connect your local backend to a deployed Agent Engine instance.

**Step 1: Deploy Agent to Agent Engine**
```bash
# Deploy agent (one time)
python deployment/deploy.py --action deploy

# Copy the AGENT_ENGINE_RESOURCE_NAME from output
```

**Step 2: Configure Environment**
```bash
# Create .env file with Agent Engine resource
cat > .env << 'EOF'
# Google Cloud Configuration
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=1

# Agent Engine Resource
AGENT_ENGINE_RESOURCE_NAME=projects/.../locations/.../reasoningEngines/...

# Agent Configuration
WORKER_MODEL=gemini-2.0-flash-exp
COORDINATOR_MODEL=gemini-2.0-flash-exp
EOF
```

**Step 3: Run Backend Server**
```bash
# Start FastAPI backend
cd backend
python api_server.py
```

**Step 4: Run Frontend (Optional)**

Open a new terminal:
```bash
cd frontend
npm run dev
```

**Step 5: Access Application**
- Frontend UI: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

### Option 3: Full Local Stack (Backend + Frontend + Local Agent)

**Step 1: Install All Dependencies**
```bash
# Python dependencies
pip install -r requirements.txt

# Frontend dependencies
cd frontend && npm install && cd ..
```

**Step 2: Configure for Local Development**
```bash
# .env file (no Agent Engine required)
cat > .env << 'EOF'
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_GENAI_USE_VERTEXAI=0
WORKER_MODEL=gemini-2.0-flash-exp
COORDINATOR_MODEL=gemini-2.0-flash-exp
EOF
```

**Step 3: Start Backend (Terminal 1)**
```bash
cd backend
python api_server.py
```

**Step 4: Start Frontend (Terminal 2)**
```bash
cd frontend
npm run dev
```

**Step 5: Open Browser**
Navigate to http://localhost:5173

---

### Local Development Tips

#### Hot Reload
- **Backend:** Uvicorn auto-reloads on Python file changes
- **Frontend:** Vite hot-reloads on React file changes

#### Common Local Issues

**Issue: "AGENT_ENGINE_RESOURCE_NAME not set"**
```bash
# Option 1: Deploy agent to Agent Engine
python deployment/deploy.py --action deploy

# Option 2: Run locally without Agent Engine
# Set GOOGLE_GENAI_USE_VERTEXAI=0 in .env
```

**Issue: "Module not found"**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# For frontend
cd frontend && npm install
```

**Issue: Port already in use**
```bash
lsof -ti:8000 | xargs kill -9  # Backend
lsof -ti:5173 | xargs kill -9  # Frontend
```

---

## Project Structure

```
content_creation_mas/
├── notebooks/                 # Workshop notebooks (Parts 1-10)
│   ├── part1_first_agent.ipynb
│   ├── part2_custom_tools.ipynb
│   ├── part3_agent_teams.ipynb
│   ├── part4_sequential_workflows_and_design_patterns.ipynb
│   ├── part5_iterative_workflows.ipynb
│   ├── part6_parallel_workflows.ipynb
│   ├── part7_callbacks_context_memory.ipynb
│   ├── part8_capstone_project.ipynb
│   ├── part9_deployment_agent_engine.ipynb
│   └── part10_fullstack_cloud_run.ipynb
├── backend/                   # FastAPI backend (Cloud Run)
│   ├── api_server.py         # API server that connects to Agent Engine
│   └── requirements.txt
├── frontend/                  # React UI (Cloud Run)
│   ├── src/
│   │   ├── components/
│   │   │   ├── ContentForm.jsx
│   │   │   ├── ContentDisplay.jsx
│   │   │   ├── ProgressIndicator.jsx
│   │   │   └── TextAnalyzer.jsx
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
├── content_creation_studio/   # Multi-agent system (Agent Engine)
│   ├── agent.py              # Root agent orchestrator
│   ├── tools.py              # Agent tools
│   └── sub_agents/           # Specialized agents
│       ├── topic_research_agent/
│       ├── content_drafter_agent/
│       ├── quality_checker_agent/
│       ├── content_improver_agent/
│       ├── blog_post_writer_agent/
│       ├── social_media_creator_agent/
│       ├── email_newsletter_writer_agent/
│       ├── seo_metadata_agent/
│       └── content_analyzer_agent/
├── deployment/                # Deployment scripts
│   ├── deploy.py             # Deploy agent to Agent Engine
│   ├── deploy-cloudrun.sh    # Deploy frontend/backend to Cloud Run
│   └── cleanup.py            # Cleanup deployed resources
├── api_server.py             # Legacy local server
└── .env                      # Environment configuration
```

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GOOGLE_API_KEY` | Yes | - | Your Google AI API key |
| `GOOGLE_CLOUD_PROJECT` | Yes | - | Google Cloud Project ID |
| `GOOGLE_CLOUD_LOCATION` | No | `us-central1` | GCP region for deployment |
| `GOOGLE_GENAI_USE_VERTEXAI` | No | `1` | Use Vertex AI (1) or AI Studio (0) |
| `AGENT_ENGINE_RESOURCE_NAME` | Yes* | - | Agent Engine resource name (*required for backend) |
| `WORKER_MODEL` | No | `gemini-2.5-flash` | Model for worker agents |
| `COORDINATOR_MODEL` | No | `gemini-2.5-flash` | Model for coordinator |
| `QUALITY_SCORE_THRESHOLD` | No | `70` | Min quality score |
| `MAX_IMPROVEMENT_ITERATIONS` | No | `3` | Max improvement loops |


## Documentation & Resources

### Architecture & Diagrams
- **[Architecture Diagram](diagrams/architecture.mmd)** - Complete system architecture (Mermaid format)
- **[Multi-Agent System Diagram](diagrams/multi-agent-system.mmd)** - Agent workflow and interactions (Mermaid format)
- **[Diagrams Guide](diagrams/README_DIAGRAMS.md)** - Complete guide to all diagrams

### Deployment Guides
- **[Deployment Overview](deployment/README.md)** - General deployment instructions
- **[Combined Deployment Guide](deployment/COMBINED_DEPLOYMENT.md)** - Deploy frontend + backend as single service
- **[Setup Guide](deployment/SETUP_GUIDE.md)** - Detailed GCP setup instructions

### Application Documentation
- **[Frontend README](frontend/README.md)** - React app documentation
- **[API Docs](http://localhost:8000/docs)** - Interactive API reference (when server running)

### External Resources
- **[Google Agent SDK Documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-builder/overview)** - Official ADK docs
## Contributing

This is a workshop project. Feel free to:
- Fork and experiment with the code
- Submit issues for bugs or improvements
- Share your enhanced versions

## License

This workshop is provided as-is for educational purposes.
