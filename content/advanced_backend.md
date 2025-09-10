Title: Advanced Backend Development
Date: 2025-09-10
Modified: 2025-09-10
Category: Articles
Tags: software, development, engineering, backend, 
Slug: unit-testing-and-tdd-schools
Authors: Juan José Farina
Summary: Unit Testing is the most important part of software development. This article will cover the basics of unit testing, test driven development, and the two main schools of thought behind it.
Keywords: testing, unit testing, test driven development, tdd, software development, software engineering, chicago school, london school

---

## Introduction

Brief overview of backend development and why advanced concepts are essential for scalable, maintainable, and secure systems.

Backend Architecture and Design Patterns

Layered Architecture: Separation of presentation, business logic, and data access layers. Example: MVC. [1][2]
Microservices Architecture: Independent services for scalability. Example: Netflix. [1][2]
Authentication and Security

JWT for Stateless Authentication. Example: Auth0. [3][4]
OAuth and OpenID Connect for Delegated Authorization. Example: Google Login. [3][4]
Data Transfer Objects (DTOs)

Use in decoupling service and data layers. Example: Transform database entities for client use. [1]
Structuring/Organizing the Backend

Modular Architecture: Encapsulation via modules/packages. Example: Node.js npm packages. [5]
Service Layer: Handles business logic. [5]
API Versioning

URI and Header-Based Strategies. Example: GitHub API. [6]
Best Practices

Logging and Monitoring. Example: ELK Stack. [7][8]
Error Handling and Caching. Example: Redis. [7][8]
Object-Relational Mapping (ORM)

Tools for interacting with databases using objects. Example: Django ORM. [9]
DTOs vs. Models/Entities

Differences between transferring data and internal representation. [1]
Onion Architecture

Separation of concerns with core business logic at the center. Example: Financial applications. [2][5]
Vertical Slice Architecture

Feature-focused encapsulation of UI, logic, and data. Example: E-commerce order processing. [10]
CQRS (Command Query Responsibility Segregation)

Separate read and write models for optimization. Example: Banking systems. [2]
Orthogonality

Independent modules for maintainability and reusability. Example: Separation of UI and business logic. [11]
Hexagonal Architecture (Ports and Adapters)

Core logic with flexible adapters for external systems. Example: Payment gateways. [2][12]
Additional Concepts and Patterns

Event-Driven Architecture. Example: Kafka. [12]
Domain-Driven Design (DDD). Example: Bounded contexts in billing systems. [2]
Serverless Architecture. Example: AWS Lambda. [13]
Twelve-Factor App Methodology. [14]
Load Balancing and Failover Strategies. Example: AWS Elastic Load Balancing. [13]
API Gateways. Example: Kong. [13]

## Conclusion

Wrap up key points and emphasize the importance of continued learning in backend development.

## References

CHATGPT 10 MÁS IMPORTANTES:

"Learning Domain-Driven Design" - CONFIRMADO
"Patterns of Enterprise Application Architecture"
Richardson, C. (2019). Microservice Patterns: With Examples in Java. New York: Manning
Publications.
"Microsoft Application Architecture Guide, 2nd Edition". https://learn.microsoft.com/en-us/previous-versions/msp-n-p/ff650706(v=pandp.10)


"Designing Data-Intensive Applications" - DESESTIMADO
"Clean Architecture" - DESESTIMADO (revisar nuevamente por onion architecture y structure/organization of backend)
"Node.js Design Patterns" - CONFIRMADO
"Flask Web Development" - CONFIRMADO
"The Art of Scalability"
"Building Microservices"
"Django for Professionals"
"Python Asyncio Jump-Start"
"Professional Node.js: Building JavaScript Based Scalable Software"
"Security Engineering"

"Domain-Driven Design: Tackling Complexity in the Heart of Software" by Eric Evans
"Distributed Systems: Principles and Paradigms"
"High Performance Browser Networking"
"Site Reliability Engineering: How Google Runs Production Systems" by Niall Richard Murphy et al.
"Pro Hibernate and MongoDB" by Anghel Leonard
"The Pragmatic Programmer: Your Journey to Mastery" by Andrew Hunt and David Thomas
"Implementing Domain-Driven Design" by Vaughn Vernon

Articles and blog posts by Jimmy Bogard

"API Security in Action" by Neil Madden
"OAuth 2 in Action" by Justin Richer and Antonio Sanso
"RESTful Web APIs" by Leonard Richardson and Mike Amundsen
"The Art of Monitoring" by James Turnbull

BUSCAR:

Arquitectura Hexagonal (https://www.youtube.com/live/k0ykTxw7s0Y?si=tdGHuTLEU6MrvPqv)
https://github.com/donnemartin/system-design-primer

