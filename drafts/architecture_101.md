Title: Architecture 101
Date: 2025-08-09
Modified: 2025-08-09
Category: Articles
Tags: software development, software engineering, software architecture, design patterns
Slug: architecture-101
Authors: Juan José Farina
Summary: Software architecture scares you ? Come here, you'll find all the basics and not-so-basics about designing architectures !
Keywords: software, development, engineering, architecture, design, patterns

---

Feeling overwhelmed when trying to learn about software architecture ?

You're not alone. In the last couple of decades, different authors have used different 
terminologies and have come at different conclusions and variants of architectures.

Learning about architecture today is probably more challenging than it was 15 years ago 
because there are many more possibilities and much more information, but not a clear and 
concise guide (at least, that I know of).

Today I'll be sharing what I've learnt so far from my professional experience, from my 
professional education, and my personal research and practice. A few books have greatly 
aided me on this, as well as countless videos, and I'll be listing them at the end of 
the article.

Without any further ado, let's talk about **architecture**

## What does all of this mean ??

Architecture design has plenty of terms that are ambiguous, similar, and sometimes vaguely described.

Starting by the concept of **software architecture** itself: the *architecture* is the 
*high-level blueprint of the system*; it comprises the subsystems or components that 
interact with each other in order to solve a problem. It is analogous to the more common 
use of architecture, if you build a residential building, you would design a blueprint 
that comprises the whole building with each of the apartments, but you won't design each 
apartment. That's a different task.

Well, the same happens in software engineering. Architecting an application means 
thinking the inputs of the system, the components and subsystems, how they communicate 
with each other, and what is the final artifact.

Let's put an example: if you need to design an e-commerce application, you may think of 
the following components: authenticator, checkout, payment, catalog, etc.

Designing how those components (the apartments of the building) work (are designed) is 
what is called **software design**: this is one level directly below the *architecture*, 
it deals with how modules and objects will be implemented and which design patterns to 
use. Basically, a high-level design of the code implementation. Using the previously 
mentioned *checkout* as example, one could come up with a TaxCalculator object, a Cart 
object, maybe use a Strategy pattern for the shipping, etc.

<p align="center">
  <img src="../content/images/architecture_01.png" alt="Architecture vs Design" width="50%">
</p>

*Design patterns* are specific and in general well-documented and known, you can refer 
to Google, Youtube or almost anywhere on internet about them.

*Architecture patterns* on the contrary tend to be confusing and vague; sometimes the 
same pattern is described in different ways and different patterns from different 
authors may have differing terminology for things that are essentially very similar.

Let's address some terms upfront; don't worry if you haven't yet heard about any of 
these:

- **Layers**: you'll get to hear **A LOT** about these, but I feel no one really 
explains what *these are*. Well, we could say they "aren't", because layers are abstract 
concepts, they are *logical boundaries*, they "don't exist". When someone says "layer" 
they basically mean a cohesive group of modules/code that serve some unified purpose. 
You can think of it as basically a "directory" if it helps you. But the main purpose of 
talking about layers is when you understand more about dependency, coupling, and 
stability. Layer is the fuzzy word we use when we want to say something like "a group of 
code should only do *X* and should only depend on *Y* layer".

- **Tiers**: this is much easier; tiers are *pysical boundaries*. Contrary to layers, 
tiers are entirely different resources, like separate web applications, databases, etc. 
For some reason, people sometimes confuse layers with tiers, but hopefully you've now 
easily understood the difference.

- **Services**: this is another ambiguous concept; some people treat services as mere 
facades of the business logic, having the responsibility of orchestrating the logic and 
providing a public API. Other people treat services as the business logic itself, 
essentially merging two layers into one.

- **Controllers**: same as the orchestrator meaning of *services*. The *MVC Architecture* will 
call them controllers, while the *Layered Architecture* will call them services.

- **Entities**: while this may mean different things for different authors, entities 
should mean the modeled data structures that your system persist/store, as in 
*Entity-Relationship Diagrams* for databases.

- **Models**: One of the most ambiguous terms. Models may refer to **many** things, like 
entities, data structures, objects, or even machine learning models if you work in that 
field. I would encourage people to only call "models" to data structures and/or objects 
that belong to the domain layer.

**By the way, data structures should have no behaviour, and objects should have limited 
or no state (and encapsulated), you can learn more about this from Uncle Bob 
(https://blog.cleancoder.com/uncle-bob/2019/06/16/ObjectsAndDataStructures.html).*

- **Schemas**: these are specifications for validating data; similar to models and 
entities, but these should only serve the purpose of defining a specific "filtering 
structure" for-so-say, not to have real value on itself.

This should be a good basis for your understanding of software architecture in general. 
We haven't covered specific terms of the Domain-Driven Design style, which we'll touch 
upon near the end of the article.

## Classic Architecture Patterns

For this section we'll use Ian Sommerville's book *Software Engineering* as reference, 
which was first published in 1982 and has seen numerous re-editions throughout the 
decades.

### MVC Architecture

This is one of the most known and basic architectures, it separates the codebase into 
Model, View, and Controller.

- **Model**: manages data storage and operations
- **View**: handles how the data is presented to the user
- **Controller**: controls user interactions and orchestrates the view and model

In this model, the controllers are orchestrators of the system; they receive each user 
interaction and decides what to do: either call the model layer for retrieving, storing 
or transforming data, and/or call the view layer to change what's presented to the user.

After the birth of internet, this became one of the most common web application 
architectures, in a time when all of this was handled in a *Server-Side-Rendering* way.

Browsers would request for files to the server either through GET or POST methods, and 
would receive HTML


1. Architecture in the small is concerned with the architecture of individual programs. 
At this level, we are concerned with the way that an individual program is decomposed 
into components. This chapter is mostly concerned with program architectures.
2. Architecture in the large is concerned with the architecture of complex enterprise 
systems that include other systems, programs, and program components. These enterprise 
systems may be distributed over different computers, which may be owned and managed by 
different companies. (I cover architecture in the large in Chapters 17 and 18.)


As Bosch
explains, individual components implement the functional system requirements,
but the dominant influence on the non-functional system characteristics is the
system’s architecture


As Bosch
explains, individual components implement the functional system requirements,
but the dominant influence on the non-functional system characteristics is the
system’s architecture





A good rule of thumb for figuring out what goes in the domain model and what goes in 
other parts of the system, is understanding how important the functionality is to the 
solution, and how likely it is to be changing.

Subdomain components like persistence mechanisms tend to not change much, but business 
logic (core domain) tends to change more frequently because of feature development, 
refactor, bug fixes, etc.