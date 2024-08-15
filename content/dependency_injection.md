Title: Dependency Injection
Date: 2024-08-14
Modified: 2024-08-14
Category: Design Patterns
Tags: dependency injection, design patterns, programming, python
Slug: dependency-injection
Authors: Juan José Farina
Summary: Ready to learn about DI ? This article is for you ! Let's find out how to use dependency injection to make your code more flexible and easy to maintain.
Keywords: dependency injection, design patterns, programming, python

---

Dependency Injection is a very simple and easy to implement concept that is very useful and can be used to understand more complex patterns.

In simple words, it means `passing an object (A) to another object (B)`, so B can make use of A's behaviors. The core idea is that a client (B) needs to use a service (A) through an interface (public methods), this is called a `dependency`, and instead of making B have all of the functionalities, or instantiating A in B's code, simply stating that it expects to receive the dependency allows B to use A, C, D or any service as long as the interface (API, or the expected methods) is the same.

In the example below, the Sender class instantiates the required Service as needed, but in the revised version we'll inject the dependency in the constructor of the Sender class, so the Sender class will be able to use whatever service is given to send a message to a given user.

**Instead of:**

```python
from enum import Enum, auto


class Services(Enum):
    SERVICE_A = auto()
    SERVICE_B = auto()


class Service:
    def send(self, sender: str, to: str) -> None:
        print(f"{sender} is sending a message to {to}")


class ServiceA(Service):
    def send(self, sender: str, to: str) -> None:
        super().send(sender, to)
        print("Using Service A")


class ServiceB(Service):
    def send(self, sender: str, to: str) -> None:
        super().send(sender, to)
        print("Using Service B")


class Sender:
    def send(self, sender: str, to: str, use_x_service: Services):
        if use_x_service == Services.SERVICE_A:
            service: Service = ServiceA()
            service.send(sender, to)

        elif use_x_service == Services.SERVICE_B:
            service = ServiceB()
            service.send(sender, to)


if __name__ == "__main__":
    sender = Sender()
    sender.send("Juan", "Jose", Services.SERVICE_A)
    sender.send("Juan", "Jose", Services.SERVICE_B)
```

**Do:**

```python
class Service:
    def __init__(self) -> None: ...

    def send(self, sender: str, to: str) -> None:
        print(f"{sender} is sending a message to {to}")


class ServiceA(Service):
    def send(self, sender: str, to: str) -> None:
        super().send(sender, to)
        print("Using Service A")


class ServiceB(Service):
    def send(self, sender: str, to: str) -> None:
        super().send(sender, to)
        print("Using Service B")


class Sender:
    def __init__(self, service: Service) -> None:
        self.service = service

    def send(self, sender: str, to: str) -> None:
        self.service.send(sender, to)


if __name__ == "__main__":
    sender = Sender(ServiceA())
    sender.send("Juan", "Jose")
    sender.service = ServiceB()
    sender.send("Juan", "Jose")
```

It's possible to inject a dependency inside a constructor, by using a setter or a property, decorating the class with the service, or using frameworks. Dependency Injection offers several advantages:

- **Decoupling:** By injecting dependencies rather than instantiating objects or copying code, the classes become more modular and easier to maintain. This decoupling allows each class to focus on its core responsibilities without worrying about how its dependencies are created or managed.

- **Testability:** Classes that rely on Dependency Injection are easier to test because you can easily substitute real dependencies with mocks or stubs. This allows for more effective unit testing.

- **Flexibility:** With Dependency Injection, you can change the behavior of your application by swapping out implementations of dependencies without altering the dependent class. This is especially useful in scenarios where you need to support different environments (e.g., development, testing, production).
