"""Simple Python practice script.

This file can be used for local practice and as a target for a workflow.
"""

import argparse


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def greeting(name: str) -> str:
    """Return a simple greeting message."""
    return f"Hello, {name}! Welcome to Python practice."


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple Python practice tool.")
    parser.add_argument("--name", type=str, default="Developer", help="Name to greet")
    parser.add_argument("--a", type=int, default=2, help="First number")
    parser.add_argument("--b", type=int, default=3, help="Second number")
    parser.add_argument("--action", choices=["greet", "add", "multiply"], default="greet",
                        help="Action to perform")

    args = parser.parse_args()

    if args.action == "greet":
        print(greeting(args.name))
    elif args.action == "add":
        print(f"{args.a} + {args.b} = {add(args.a, args.b)}")
    elif args.action == "multiply":
        print(f"{args.a} * {args.b} = {multiply(args.a, args.b)}")


if __name__ == "__main__":
    main()
