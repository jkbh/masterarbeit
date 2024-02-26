# Master Notes

## Di Feb 20

### Meeting

This was the worst meeting yet. Can only do better from now on :)

### Do Feb 22

Where: Hamburg
Wakeup: 7:30
Start: 8:30
End:
Focus Points: 5/10

**Made continous user inputs possible**

Before the user could only input the task in the first chat, then it was fixed.

Now the user can change the current step input. If the user continous without any input the first input (task) is used for the step prompt.

**Chose to output vector DB retrieved data in an own file**

As the output can get large it is better to save it into a file and return the filename as the ability output.

**Added best practices to task-step prompt**

Contents:
- Respect errors
- No ability twice (might cause problems)
- Prefer querying vector DB before answering
- Say what the LLM is doing instead of saying an early answer to the task

Need to evaluate what helps and what not.

**Added vector DB to task-step prompt as a resource**

This could help the language model to access the vector DB

**Switched from GPT-3-Turbo to GPT-4-Turbo**

GPT 4 seems to be alot better at planning than version 3. Need to test the differences more. Remember that in the end i likely need to use an open source language model. Nonetheless this is an important observation to write down.

## Fr Feb 23

Where: HH
Start: 9:30
focus points: 3/10

- Wrote paragraphs about methods to improve LLM knowledge on-demand
- Refactored agent class
- Organized references

## Mo Feb 26 

**Reasons I split up the RAG steps into single steps**

A fixed rag pipeline works for single question and answer conversation flows
But what if the query are more complex and require a retrieving two different topics and then connecting the results in an answer.
So we might need retrieval and generation once, or retrieval twice and generation once or any other combination. 
Also iterating generation steps could be on option.

**Implemeting backlinging sentences to retrieved source** 

Either use similarity again or ask the model to inlucde source tokens into the answer.

## Loose Ideas

- Environment
  - Data Sources
    - Ingested documents
      - Summary index: index over documents
      - Index for each doucument with its chunks

- Web search
      -

- Actions
  - Websearch
  - Database search
  - Question answering
  - Summarization of documents
  - Ask for more specific query?
  - Answer question

- Add websearch findings to database

- **How can a research data repository be combined with open-world web-search for information retrieval?**
- **How to employ strict knowledge boundaries for LLM Agents doing IR?**

- Problem of proprietary solutions
  - Guiding/moderation might be unknown
  - Most of the time general agents, not information retrieval focused

- Prompt rewriting
  - User input -> LLM input
  - LLM output -> User expected output
  - LLM output -> Better LLM input

- Benchmarking existing solutions
  - AutoGPT
  - OpenAI RAG <https://platform.openai.com/docs/assistants/tools/knowledge-retrieval>
  - Perplexity

- Create benchmark question/answer pairs with GPT-4
  - Go through literature to find benchmarking methods

- What is the environment?
  - Research PC?

## Paper List

[The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/pdf/2309.07864.pdf)

> What is an agent?

AI agents as artificial entities that are capable of perceiving their surroundings using sensors, making decisions, and then taking actions in response using actuators

Agent modules:

1. Perception
2. Brain: Memory, Knowledge, Decision Making

3. Action

[Investigating the Factual Knowledge Boundary of Large Language Models with Retrieval Augmentation](https://arxiv.org/pdf/2307.11019.pdf)

Findings:

- LLM's perception of knowledge boundaries is often wrong and overconfident
- Retrieval augmentation can provide benficial knowledge supplement
- Retrieval augmentation enhances capbilities to perceive knowledge boundaries
- LLM relies on retrieved knowledge even if documents are weakly correlated to query

Propsals:

- Use retrieval augmented a priori judgement e.g. "Can i answer this question with the given knowledge". If so, answer with documents else without.
- 5-10 documents seem to be a good number.

[Augmented Language Models: A Survey](https://arxiv.org/pdf/2302.07842.pdf)

[Critic: Large Language Models can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/pdf/2305.11738.pdf)

Use external tools to evaluate certain aspects of a text and revise it based on obtained feedback

[Large Language Models for Information Retrieval: A Survey](https://arxiv.org/pdf/2308.07107.pdf)

[Deep Learning for Sentiment Analysis: A Survey](https://arxiv.org/pdf/1801.07883.pdf)

[Information Retrieval: Recent Advances and Beyond](https://arxiv.org/pdf/2301.08801.pdf)

Describes models used in the retrieval and reranking stages of IR.

[AgentBench](https://arxiv.org/pdf/2308.03688.pdf)

[HuggingGPT](https://arxiv.org/abs/2303.17580)

[Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/pdf/2310.11511.pdf)

## LLMs

Prompting strategies

- Zero-shot
- Few-shot
- Chain-of-thought

## Benchmarking

- [AgentBench](https://arxiv.org/pdf/2308.03688.pdf)
  - Typical reasons of agent failiures
    - Poor long-term reasoning
    - Poor decision-making (?)
    - Poor instruction following (?)
  - To improve agent performance, train on
    - Code
    - High quality mulit-turn alignment data

## Language Agents

- Specific
  - Generative Agents: Mimic social behaviour
  - WebAgent: Complete tasks on websites
  - Meta-GPT: Multi-agent software development
- General
  - AutoGPT
  - BabyAGI
  - SuperAGI

## Agent Frameworks

- Transformers Agents: API to interpret natural language and use tools
- LangChain
- AutoGPT
- Gentopia
- XLang
- Camel
- Meta-GPT
- Agents

## Agents

### [HuggingGPT](https://arxiv.org/abs/2303.17580)

## In-Context Learning

### Language Models are Few Shot Learners

- GPT-3 with 175B can perform unseen NLP tasks after a few examples

## RAG

### [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/pdf/2310.11511.pdf)

## AutoGPT Arch

### AutoGPT

- agent_factory: Module to create agents
  - `configurators.py`: Create agent from config and with handmade profile
  - `generators.py`: Create agent with generated profile
  - `profile_generator.py`: Create the acutal agent profile for a given task
- agent_manager: Defines `AgentManager` for managing different agents.
- agents
  - features
    - `context.py`: Defines a mixin that adds a context section to a prompt
    - `file_workspace.py`: Defines mixin that adds workspace support to a class
    - `watchdog.py`: Mixin that switches LLM when the agent start looping
  - prompt_strategies
    - `one_shot.py`: Methods to build prompts. Defines the prompt template
  - utils
    - `agent_file_manager.py`: Class that represents a workspace for an agent
    - `exceptions.py`: Defines exceptions in the agent execution
    - `prompt_scratchpad.py`: Some extra info for prompts
  - `agent.py`: Defines default AutoGPT `Agent` with one-shot prompting. Extends `BaseAgent`
  - `base.py`:  Defines the base `BaseAgent`

### Forge

bechmark_config

- forge
  - actions: This folder contains all possible actions the agent can perform
    - file_system
      - `files.py`: Operations in the workspace, **list** files in dir, **read/write** file
    - web
      - `web_search.py`: Actions to **search** duckduckgo
      - `web_selenium.py`: **Read webpage** and extract information for a question
    - `finish.py`: Defines the **finish action** to end an autogpt run
    - `registry.py`: Defines the **ActionRegister** and the **action** decorator that are used to keep track of possible actions
  - memory: Contains different Memory defintions **Not used by default**
    - `chroma_memstore.py`: ChromaDB Memorystore with capabilites to add, query, get, update, delete documents. For some reason **does not subclass** `MemStore`.
    - `memstore.py`: Abstract defintion `MemStore` of a memory store
  - prompts: Contains jinja templates to generate llm prompts
    - gpt-3.5-turbo: Contains the gpt specific prompt templates
      - `role-selection.j2`: Template to generate an expert profile to help with a task. Not used by default. Uses the the `expert.j2` technique
      - `system-format.j2`: Defines the json format the model should answer in
      - `task-step.j2`: Template for the prompt that is sent to the LLM. Uses the `expert.j2` template as a Planner. Main content is the given taks but can contain constraints, resources, abilities, best_practices if present
    - techniques: Containts prompt templates for different techniques
      - `chain-of-thought.j2`: Chain of though template
      - `expert.j2`: Template for expert answering
      - `few-shot.j2`: Few-Shot template
  - sdk: The core of the forge agent
    - routes
      - `agent_protocol.py`: Defines the API routes for the agent service
    - `agent.py`: The base `Agent`. Has a database and a workspace.
    - `db.py`: Defines `AgentDB`. Defines tables for tasks, steps, artifacts. Methods to create/get/list tasks/steps/artifaces and to update a step.
    - `prompting.py`: Defines `PromptEnginge`. Has a load_prompt method to populate a prompt template
    - `workspace.py`: Defines abstract `Workspace` and implementions `LocalWorkspace` and `GCSWorkspace` for google cloud. `LocalWorkspace` provides methods to operate on files in a certain folder.
  - `__main__.py`:  Here the app is started
  - `agent.py`: The `ForgeAgent` is defined here. It subclasses `Agent`
  - `app.py`: Agent, Workspace, Database are initialised
  - `db.py`: `ForgeDatabase` that subclasses `AgentDB`. Additional methods to add chat messages and create actions and list chat/action history
  - `llm.py`: Definition of methods to call LLMs

agent.db

run
