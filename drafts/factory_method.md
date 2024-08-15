Title: Factory Method
Date: 2024-08-09
Modified: 2024-08-09
Category: Design Patterns
Tags: factory method, design patterns, programming, python
Slug: factory method
Authors: Juan José Farina
Summary: 
Keywords: factory method, design patterns, programming, python

---



**Instead of:**

```python
from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result


class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.some_operation()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
```

**Do:**

```python
from typing import Callable


def concrete_creator_1() -> str:
    return f"Creator: The same creator's code has just worked with ""{Result of the ConcreteProduct1}"


def concrete_creator_2() -> str:
    return f"Creator: The same creator's code has just worked with ""{Result of the ConcreteProduct2}"


def client_code(some_operation: Callable[..., str]) -> None:
    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{some_operation()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(concrete_creator_1)
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(concrete_creator_2)
```
