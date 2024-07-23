Title: Understanding REST APIs
Date: 2024-07-22
Modified: 2024-07-22
Category: Articles
Tags: software engineering, api
Slug: understanding-rest-apis
Authors: Juan José Farina
Summary: Are you a master of REST APIs? Check this article where I delve into the origins of REST APIs, their structure, and how they work.

---

## What is an API?

First things first: API means `Application Programming Interface`. It's a set of rules and protocols for building and interacting with software applications. It's essentially an exposed communication protocol so external systems can make an application return either data or execute some functionality.

That was very formal, let's break it down: suppose you have a data structure of an `array` and you don't know its contents. Something like: `[?, ?, ?, ?, ?...]`, where you don't even know how many elements are in the array, nor can community in any way.

An API would be a `means for you to communicate with the array`, for instance, retrieving the length of the array, retrieving an item at certain index, or sorting the array. And yes, all those methods and properties that you use in your every day programming language, are APIs of the data structures that you are using.

But, when we are talking about REST APIs, we are not talking about any kind of API, but specifically Web APIs, or HTTP APIs.

## But, what is HTTP?

`Hypertext Transfer Protocol (HTTP)` is the foundation of any data exchange on the Web and a protocol used for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but it can also be used for other purposes.

HTTP is an `application layer protocol` that most commonly make use of `TCP/IP`, a four layers model for network communication between devices. We won't delve into the latter because of the more complex technicalities of such a low-level communication protocol, but just do know that HTTP relies on other lower-level layers of communication. Let's keep talking about HTTP, a typical request or response consists vaguely of two things:

- **Headers**: additional information about the request or response.
- **Body**: the actual data being transferred.

Requests also have a method, which is the action that the client wants to perform on the server. The most common methods are:

- **GET**: Retrieve an existing resource using a URI. This could be anything, and it's what is commonly done when browsing the web: retrieving HTML, CSS, etc. GET has no body.

*(this method exists since the first public version of HTTP 0.9 of 1991)*
- **POST**: Send data to a server. This was the method to create a resource or ask the server to perform an action. Basically, anything that wasn't a "retrieve operation" (a GET operation), used to be a POST operation.
- **PUT**: Put a resource in a specific URI. This is usually used for updating an existing resource, though it can be used to create a new resource too.
- **DELETE**: Delete an existing resource at a specific URI.

*(these methods, among others, were introduced in HTTP 1.0 of 1996)*
- **PATCH**: This updates an existing resource partially.

*(this method was introduced with HTTP 1.1 of 1997)*

You can learn more about the changes of the HTTP protocol in [this page](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Evolution_of_HTTP).

GET, PUT and DELETE are `idempotent` operations, which means that they can be performed multiple times without changing the result beyond the initial application of the operation.

POST and PATCH are not naturally idempotent, meaning successive calls to the same endpoint with the same payload may result in multiple resources being created or consecutive modifications being made.

## Are HTTP APIs or REST APIs the same as CRUD then ?

A typical misconception of HTTP methods and REST APIs is that they map to one of the `CRUD operations`. CRUD stands for `Create, Read, Update, and Delete`. It's a set of operations that are commonly used to manage data:

- **Create**: Create a new resource. Mistakenly mapped to POST.
- **Read**: Retrieve an existing resource. Similar to GET.
- **Update**: Update an existing resource. Somewhat similar, but not equal, to PUT and PATCH.
- **Delete**: Delete an existing resource. Similar to DELETE.



<!-- <p align="center">
  <img src="image.png" alt="Example Image">
</p> -->
