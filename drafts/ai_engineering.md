# All About AI Engineering

AI engineering is basically the craft of building real applications on top of foundation models: how we prompt them, shape their outputs, inject context, evaluate performance, and so on. This is not about GPU clusters or training giant models from scratch — it’s about using existing models to build real functionality.

---

## Foundation Models

Large Language Models and multimodal models are the backbone. These are pretrained on huge amounts of text (and often other modalities) and come in different architectural flavors.

### Masked language models

These models fill in missing tokens in a sentence. They’re mainly used for understanding tasks, rather than generating creative text.
Examples:

* **BERT**

### Autoregressive language models (generative)

Given previous tokens, they predict the next one — over and over — which allows them to generate open-ended text.
Examples:

* GPT
* LLaMA
* Mistral
* Gemini
* Claude

Tokenization matters here. These models operate in tokens, not words. A useful rule of thumb:

> ~100 tokens ≈ ~75 words (for GPT-style models)

A model’s vocabulary is fixed and finite, but the possible combinations are infinite — that’s why they’re generative.

### Model as a Service (APIs)

You don’t need to host the model — just call it:

* OpenAI GPT
* Google Gemini
* Anthropic Claude

### Pre-training (completion model)

This is the initial large-scale training stage that shapes the general “world knowledge” of the model.

### Fine-tuning

This happens *after* pre-training. We adapt models to specific tasks, styles, or domains.

#### Supervised Fine-Tuning (SFT)

Train the model on annotated input→output examples.

#### Preference Finetuning

Instead of telling the model the “correct answer”, we train it on *preferred answers*:

* RL
* RLHF (human feedback)
* Direct Preference Optimization
* RL from AI feedback

#### PEFT — Parameter Efficient Fine-Tuning

We don’t retrain the entire model — we modify a small subset or add adapters.

Adapter-based methods:

* LoRA
* BitFit
* IA3
* LongLoRA
* QLoRA

Soft-prompt methods:

* Prefix-tuning
* P-Tuning
* Prompt tuning

Tools that make this practical:

* Finetuning APIs
* LLaMA-Factory
* Unsloth
* Axolotl
* LitGPT
* TRL

### Model merging

Instead of fine-tuning, sometimes we just *blend* existing models:

Summing approaches:

* Linear combination
* SLERP

Layer strategies:

* Passthrough
* Depthwise scaling

Or direct concatenation of layers.

### Model registry

Where models and versions live, get tracked, and get published:

* HuggingFace
* ZenML
* CometML
* SageMaker
* W&B
* MLFlow
* Neptune

### Sampling (token generation controls)

How we influence output style and randomness:

* Temperature
* Top-k
* Top-p
* Logit-bias
* Seed
* Constrained sampling
* Prompt caching

### Model Gateway

These tools let apps switch between multiple models or vendors seamlessly:

* LiteLLM
* Portkey
* MLFlow AI Gateway
* Wealthsimple Gateway
* TrueFoundry
* Kong
* Cloudflare

### Inconsistency & Hallucination

Models don’t “know” truth — they know probability. Anything that has ever appeared in text has a non-zero chance of being generated.
Examples:

* Snowballing (the model builds fiction on top of fiction)
* The “unknown labeler knowledge” problem

---

## In-Context Learning / Prompt Engineering

This is how we talk to models.

### Roles

* System prompt — sets dominant behavior
* User prompt — the instruction or query

### Techniques

* Zero-shot
* Few-shot
* Persona / role-playing
* Chain-of-Thought
* Self-critique

### Prompt Attacks

Because prompts are inputs — they can be exploited:

* Prompt extraction
* Jailbreaking / prompt injection
* Information extraction
* Remote code or tool execution
* Data leaks
* Social harm
* Misinformation
* Service interruption
* Brand risk

### Tools

* LangChain
* LlamaIndex
* Promptflow
* Promptlayer
* AgentOps

---

## Context Engineering

How to supplement a model’s private knowledge with additional external information.

### Retrieval-Augmented Generation (RAG)

We search a document corpus and feed relevant chunks into the model.

#### Indexing

Sparse (term-based):

* Elasticsearch
* BM25

Dense (embedding-based):

* LSH
* HNSW
* PQ
* IVF
* Annoy

Searching algorithms:

* Cosine similarity
* Euclidean distance
* Dot product

#### Chunking strategies

* By characters
* By words
* By sentences
* By paragraphs
* Recursive splitting
* Overlapping windows

#### Query rewriting

Transforming user queries into queries the retriever system can handle better.

#### Reranking

Reordering retrieved candidates for relevance.

#### Retriever Tools

* LlamaIndex
* LangChain
* Haystack
* Elasticsearch Hybrid
* Vespa.ai
* Azure AI Search

#### Embedding models

* Sentence Transformers
* Word2Vec
* GloVe
* BERT
* OpenAI text embeddings
* Google Gecko
* VoyageAI
* Cohere
* E5
* Jina
* BAAI bge
* Instructor XL

#### Vector Databases

* Pinecone
* Weaviate
* Milvus
* FAISS
* Chroma
* LanceDB
* Qdrant
* Pgvector
* AI Search

#### Metrics

* Context Precision
* Context Recall
* NDCG
* MAP
* MRR

---

## Workflows

These are structured task pipelines with a defined completion point.

Tools:

* LangChain
* LlamaIndex
* Flowise
* LangFlow
* Haystack
* LangGraph
* DUST
* CrewAI

---

## Agents

Agents don’t have a defined completion — they persist, monitor, and interact with an environment.

### Tools / Function calling

* Read / queries
* Write / commands

### Reasoning & Control

* Tool-selection logic
* Reflection loops
* Multi-agent agreement
* Task decomposition

### Communication protocols

* MCP (Model Context Protocol)
* Agent-to-Agent (A2A)

---

## Memory Systems

Models need memory beyond their prompt window.

### Types

* Internal knowledge (from pretraining)
* Short-term conversation memory
* Long-term persistent memory (RAG-style)

### Techniques

* FIFO
* Summarization

---

## Evaluation

How we measure usefulness and correctness.

### Exact (objective) evaluation

* Functional correctness
* Answer similarity

  * Exact match
  * Lexical similarity

    * fuzzy matching, n-gram, BLEU, ROUGE
  * Semantic similarity
* Multiple-choice scoring

### Subjective evaluation

* AI as a judge

  * factual correctness
  * toxicity
* Human evaluation

### Slice-based evaluation

We evaluate performance on specific subsets — languages, user types, topics, etc.

### Tools

* DeepEval
* RAGAS
* ARES
* ChatEval

---

## Monitoring & Observability

Once an application is running, things can drift, degrade, or fail silently.

Tools:

* DataDog
* LangSmith
* LangFuse
* Opik
* Galileo