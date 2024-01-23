# Master Document for Notes

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
