Title: Python Concurrency (and much more !)
Date: 2025-07-09
Modified: 2025-07-09
Category: Articles
Tags: software development, software engineering, python, concurrency, parallelism
Slug: python-concurrency
Authors: Juan José Farina
Summary: Distilled version of the talk given on friday 4 of July at PwC.
Keywords: software, development, engineering, python, concurrency, parallelism, gil, threads, processes, locks

---

We're going to see somewhat superficially many topics, which many of them are really low-level, but personally I think it's very important and useful to understand what goes under the hood.

Some of the topics are not python exclusive, but more on the operating system level, which also means it may work differently in Windows vs Unix-based systems, and that is reflected in some code snippets.

The first thing we'll do is go through some of the concepts we'll be focusing on, the terms we'll be using:

- Concurrency

- Parallelism

Both things kinda mean many tasks ocurring "simultaneously", but not exactly the same way.

As you can see, we have four different situations:
1. No concurrency nor parallelism
2. Concurrency without parallelism
3. Parallelism without concurrency
4. Concurrency and parallelism

The fist example is a sequential execution of tasks: task 1 starts and finishes before task 2 can start.

The second example is about concurrency, for which you can think of a cheff:

- 1 Cheff needs to execute many tasks when cooking, but don't usually go over them sequentially; the cheff may start one task and while waiting for it to finish it will go do something else, and thus have many tasks in progress at the same time. But the cheff can only focus on only ONE task at a single time.

- Parallelism is much more easier to understand, because it basically means having 2 cheffs; so two tasks can be executed at the same time (one for each cheff).

None of these task executions are specifically tied to only one CPU core, which is something that may confuse further in the talk.

Now, let's talk about CPU-bound and I/O-bound operations. These are two completely different operations. Let's take a look:

```python
import requests

# I/O-bound operation, requesting content through the network
response = requests.get("https://www.example.com")

# CPU-bound operation, processing data from a dictionary
items = response.headers.items()
headers = [f"{key}: {value}" for key, value in items]
formatted_headers = "\n".join(headers)

# I/O-bound operation, writing data to a file
with open("headers.txt", "w") as file:
    file.write(formatted_headers)
```

Basically, CPU-bound operations are exclusively made by the microprocessor (executing Python lines of code), while the I/O-bound operations will depend on peripherals, and potentially in external agents to our system.

For example, the HTTP request shown above will eventually reach the network card, and even keep awaiting for a response from somewhere else.

Now, how can we achieve concurrency or parallelism with these operations ? To find the answer we'll have to talk about processes and threads.

These are logical concepts very different to the CPU and its cores, which are physical concepts.

A process is a resource-boundary for executing tasks, and it will use one CPU-core, but is not necessarily binded exclusively to one specific core.

A process may have one or more threads of execution.

Threads all share the same resources, for e.g. memory space, inside one parent process.

We can achieve parallelism both using processes or threads. In both cases, we can execute different tasks simultaneously; at process-level we multiplicate all resources, and at thread-level we share the parent process' resources.

We can execute in parallel both CPU-bound and I/O-bound operations, but it's important to understand that at process-level we can't share in-memory objects, so attempting to process the same memory object may end in a duplication