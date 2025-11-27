## Simple Prompt

- Task Description (what to do, may include a role/persona and output format)
- Examples (can be positive and negative examples)
- Task

Prompt example:

_Given a text, extract all entities. Output only the list of extracted_ 
_entities, separated by commas, and nothing else._

_Text: "Brave New World is a dystopian novel written by Aldous Huxley, first_ 
_published in 1932."_
_Entities: Brave New World, Aldous Huxley_

_Text: ${THE TEXT THAT YOU WANT TO EXTRACT ENTITIES FROM}_
_Entities:_

## In-Context Learning

- **Zero-shot learning**: means the prompt doesn't contain examples.
- **One-shot learning**: means the prompt has 1 example.
- **Few-shot learning**: means the prompt has n > 1 examples.

_Context_ is used differently by different authors, but considering the amount 
of new techniques on _Context Engineering_, the standard meaning is becoming 
that of "information provided to the model so that it can perform a given task".

## System Prompt vs User Prompt

Most LLM APIs allow the possibility of sending two types of prompts: system and 
user. These are then merged into a single prompt following a template; for 
instance, this is Llama 2's template:

_< s >[INST] << sys >>_

*{{ system_prompt }}*

_<< /SYS >>_

*{{ user_message }} [/INT]*

There is no standard for the templates the model's API follow. Llama 3 changed 
its template to:

_<|begin_of_text|><|start_header_id|>system<|end_header_id|>_

*{{ system_prompt }}<|eot_id|><|start_header_id|>user<|end_header_id|>*

*{{ user_message }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>*

There is usually no significant difference among both types of prompts other 
than the system prompt being first (with most models being better at processing 
instructions that come first); in the end, they are both the same for the 
foundational model, unless it has been post-trained to pay more attention to 
the system prompt.

## Lost In The Middle

While the context window (or maximum context length) for most LLMs is big 
enough for most context needs, researchs have shown that models understand much 
better the instructions given at the beginning and the end of a prompt.

## Best Practices

For specific models reference, you should see the model provider's 
documentation, such as Anthropic, Google, and OpenAI. Some general tips are:

- Explain, without ambiguity, what you want the model to do, in great detail
- Ask the model to adopt a persona at the beginning of your prompt, to obtain 
responses with different perspectives _("You're a first-grade teacher")_
- Provide examples to reduce ambiguity (prefer example formats that use fewer 
tokens if that's a constraint)
- Specify the output format for conciseness and structure (if you're expecting 
a structured output, use markers to indicate the end of the prompt, so the 
model understands that it must append the structured output directly at the 
beginning of its answer)

## Break Complex Yasks into Simpler Subtasks

Complex tasks usually require multiple steps where you break those tasks into 
subtasks. Instead of having one prompt and one call, you create many prompts, 
with chained calls until a final response.

While this approach usually increases costs (not always, the sum of smaller 
tasks may not be as big as the original single-prompt, and you also have the 
possibility of using smaller and different models for different tasks) and 
latency (unless you are able to parallelize calls), you'll gain many benefits 
besides improved correctness:

- You can monitor intermediate steps instead of just the final output
- You can isolate issues in smaller tasks
- You can write simpler prompts

## Chain-Of-Thought

This means to explicitly ask the model to "think step by step" or "explain your 
decision". Another option is to explicitly specify the steps that the model 
should take and/or include examples of what the steps should look like in your 
prompt.

This is an example with specific steps:

_Which animal is faster: cats or dogs? Follow these steps to find an answer:_

_1. Determine the speed of the fastest dog breed._
_2. Determine the speed of the fastest cat breed._
_3. Determine which one is faster._

This is an example of CoT with _one-shot learning_: 

_Which animal is faster: sharks or dolphins?_

_1. The fastest shark breed is the shortfin mako shark, which can reach speeds_ 
_around 74 km/h._
_2. The fastest dolphin breed is the common dolphin, which can reach speeds_ 
_around 60 km/h._

_Which animal is faster: cats or dogs?_

## Advanced Techniques

An important number of more advanced prompting techniques have been developed, 
often involving multiple LLM calls. You can learn more about all of them at 
[Learn Prompting](https://learnprompting.org/docs/introduction).

These are just a select few techniques from a broad range of innovative ideas 
that have been presented in numerous papers. Let's briefly revise some of them:

### Generated Knowledge

Similar to CoT, this can be done both, in single or dual prompt. In the single 
version, you ask the LLM to generate knowledge or facts that help improve the 
outcome. Example:

_Generate 4 facts about the Kermode bear, then use these facts to write a_ 
_short blog post using the information:_

In a dual prompt version, you separate both tasks like this:

_Generate 4 facts about the Kermode bear:_

Then you pass that output into another prompt:

_1. The Kermode bear, also known as the Spirit Bear, is a rare subspecies of_ 
_the American black bear found in British Columbia, Canada._

_2. The Kermode bear has a unique white or cream-colored coat, which is caused_ 
_by a recessive gene._

_3. The Kermode bear is a symbol of hope and renewal for the First Nations_ 
_people of British Columbia._

_4. The Kermode bear is a protected species and is listed as a species of_ 
_special concern by the Committee on the Status of Endangered Wildlife in_ 
_Canada._

_Use the above facts to write a one paragraph blog post about the Kermode bear:_

### Chunking and Iterative Approach for dealing with Long Form Content

You divide the content in smaller chunks or sections, then process them chunk 
by chunk from the first one, and appending processed ones to each prompt, so 
the LLM has context of previous parts of the content.

### Self-Ask

The basis of this technique, is to ask the LLM if it needs follow up questions 
in order to complete the required task. This is a basic template:

_Question: {A complex question}_

_Are follow up questions needed here: Yes._

_Follow up: {Sub-question 1} Intermediate answer: {Correct answer to_ 
_sub-question 1}_

_Follow up: {Sub-question 2} Intermediate answer: {Correct answer to_ 
_sub-question 2}_

_So the final answer is: {Correct answer to the complex question}_

_Question: {Your prompt with a complex question}_

_Are follow up questions needed here:_

### Step-Back Prompting

This method involves two steps: abstraction and reasoning.

During abstraction, the model is asked to answer a high-level concept or 
principle related to the question, which can be useful to answer it. It's a 
generalization step.

During reasoning, the high-level abstraction is appended to help the model more 
effectively reason about the question.

This is a basic example of this method:

_Question: what happens to the pressure of an ideal gas when temperature_ 
_increases by a factor of 8?_

_What are the fundamental concepts or principles involved in this problem ?_

Afterwards, use this output to solve the original problem:

_${abstraction}_

_Use the previous explanation to answer the question: what happens to the_ 
_pressure of an ideal gas when temperature increases by a factor of 2, and_ 
_volume increases by a factor of 8?_

### Mixture of Reasoning Experts (MoRE)

This technique addresses the models' lack of reasoning skills. It consists of 
four different models/prompts:

- Factual Expert: Uses retrieval-augmented prompting to pull information from 
external sources.

- Multihop Expert: Uses Chain-of-Thought (CoT) to break down complex questions.

- Mathematical Expert: Also uses CoT but should be fine-tuned to handle 
numerical and logical computations.

- Commonsense Expert: Uses Generated Knowledge prompting to append relevant 
factoids to answer questions.

MoRE uses an answer selector to choose the best response based on each expert's 
predictions; if the answers are not reliable, it can abstain from answering.

### Prompt Paraphrasing

This technique consists in creating more varied high-quality prompts to 
retrieve more accurate answers.

It takes an initial prompt and creates several semantically similar versions, 
then uses these for answering, by leveraging one of two methods:

- Top-1 Prompt Selection: each prompt is tested and then the best one is chosen 
for the real task.

- Ensemble: all candidate prompts are used simultaneously, and then all 
responses are combined with Majority Voting or Averaging.

### Self-Calibration

- Get the initial answer.
- Ask the model whether the proposed answer is true or false.

### Self-Refine

This is similar to Self-Calibration but instead of classifying an answer as 
true or false, it asks for feedback, improves the answer, and loops until no 
more refinement is needed.

### Plan-and-Solve Prompting

This is an evolution from Zero-Shot CoT prompting: it prompts the LLM to "Let's 
first understand the problem and devise a plan to solve the problem. Then, 
let's carry out the plan and solve the problem step by step".

Example:

_Q: In a dance class of 20 students, 20% enrolled in contemporary dance, 25%_ 
_of the remaining enrolled in jazz dance, and the rest enrolled in hip-hop_ 
_dance. What percentage of the entire students enrolled in hip-hop dance?_

_A: Let's first understand the problem and devise a plan to solve the problem._ 
_Then, let's carry out the plan and solve the problem step by step._

