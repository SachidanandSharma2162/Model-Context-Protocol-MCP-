# 🧮 FastMCP Calculator Server

A simple **Calculator MCP (Model Context Protocol) Server** built using **FastMCP**. This server exposes common mathematical operations as MCP tools that can be used by AI assistants like **Claude Desktop**, **Cursor**, or any MCP-compatible client.

---

## 🚀 Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🔢 Power
- √ Square Root

---

## 🛠️ Tech Stack

- Python 3.14+
- FastMCP 3.x
- MCP SDK
- UV (Python Package Manager)

---

## 📂 Project Structure

```
fastmcp-demo-server/
│
├── .venv/
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
└── .python-version
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/fastmcp-demo-server.git

cd fastmcp-demo-server
```

---

### 2. Create Virtual Environment

Using UV

```bash
uv venv
```

Activate

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

### 3. Install FastMCP

```bash
uv add fastmcp
```

or

```bash
pip install fastmcp
```

---

## ▶️ Running the Server

Run using FastMCP

```bash
fastmcp run main.py
```

or

```bash
uv run fastmcp run main.py
```

Expected output:

```
FastMCP 3.x

Starting MCP server...
Transport: stdio
```

---

## 🔍 Inspect the Server

Launch the MCP Inspector

```bash
uv run fastmcp dev main.py
```

or

```bash
fastmcp dev main.py
```

Open the Inspector in your browser and connect to the server.

---

# 🔧 Available Tools

## Add

```python
add(a, b)
```

Example

```
add(10, 5)

Output:
15
```

---

## Subtract

```python
subtract(a, b)
```

Example

```
subtract(10,5)

Output:
5
```

---

## Multiply

```python
multiply(a,b)
```

Example

```
multiply(8,4)

Output:
32
```

---

## Divide

```python
divide(a,b)
```

Example

```
divide(20,4)

Output:
5
```

Throws an exception if the divisor is zero.

---

## Power

```python
power(a,b)
```

Example

```
power(2,5)

Output:
32
```

---

## Square Root

```python
sqrt(x)
```

Example

```
sqrt(25)

Output:
5
```

Throws an exception for negative numbers.

---

# 📄 main.py

```python
from fastmcp import FastMCP

mcp = FastMCP("Calculator Server")
```

Each function is registered using

```python
@mcp.tool()
```

making it available to any MCP-compatible client.

---

# 🤖 Claude Desktop Integration

If automatic installation works:

```bash
uv run fastmcp install claude-desktop main.py
```

If not, manually add the server to your Claude Desktop configuration.

Example:

```json
{
  "mcpServers": {
    "calculator": {
      "command": "C:\\Users\\YOUR_USERNAME\\Desktop\\fastmcp-demo-server\\.venv\\Scripts\\fastmcp.exe",
      "args": [
        "run",
        "C:\\Users\\YOUR_USERNAME\\Desktop\\fastmcp-demo-server\\main.py"
      ]
    }
  }
}
```

Restart Claude Desktop after saving the configuration.

---

# ⚠️ Common Windows Issues

## 1. `uv` not recognized

Install UV

```bash
pip install uv
```

If necessary

```bash
python -m uv
```

---

## 2. `npx not found`

Install Node.js

https://nodejs.org

Verify

```bash
node -v
npm -v
npx -v
```

---

## 3. PowerShell Execution Policy

Run PowerShell as Administrator

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 4. Claude Desktop Config Not Found

Create

```
%APPDATA%\Claude
```

and place

```
claude_desktop_config.json
```

inside it if it does not already exist.

---

# 🧪 Example Usage

```
User:
What is 12 + 30?

Claude

↓

Calls

↓

add(12,30)

↓

Returns

42
```

---

# 📚 Learnings

Through this project, I learned:

- Model Context Protocol (MCP)
- FastMCP Framework
- MCP Tools
- STDIO Transport
- MCP Inspector
- Claude Desktop Integration
- Virtual Environments
- UV Package Manager
- Debugging Windows Environment Issues
- Manual MCP Configuration

---

# 📖 References

- https://gofastmcp.com
- https://modelcontextprotocol.io

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

## 👨‍💻 Author

**Sachidanand Sharma**

- 💼 Full Stack Developer
- 🤖 AI & MCP Enthusiast
- 🌐 Exploring AI Agents, LangGraph, MCP, and LLM Applications
