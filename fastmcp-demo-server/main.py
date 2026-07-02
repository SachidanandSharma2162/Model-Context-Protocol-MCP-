from fastmcp import FastMCP
import math

mcp = FastMCP("Calculator Server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

@mcp.tool()
def power(a: float, b: float) -> float:
    """Power"""
    return a ** b

@mcp.tool()
def sqrt(x: float) -> float:
    """Square root"""
    if x < 0:
        raise ValueError("Negative number")
    return math.sqrt(x)

if __name__ == "__main__":
    mcp.run()