# makegen

A minimal, no-frills Makefile generator for C and C++ projects.

---

## 🚀 Features

- Auto-detects `.c` and `.cpp` source files in your current directory
- Generates a clean and working `Makefile`
- Supports C or C++ with customizable compiler
- Fast, offline, and dependency-free (just Python 3)

---

## 🧱 Installation

Make sure the script is executable:

```bash
chmod +x makegen
```

Move it into your `PATH` for global access:

```bash
sudo mv makegen /usr/local/bin/
```

---

## ⚙️ Usage

```bash
makegen [--target name] [--lang c|cpp] [--compiler gcc|clang|g++] [--force]
```

### Examples

```bash
makegen --target myapp --lang cpp
makegen --target hello_c --compiler clang
```

---

## 🛡️ Options

| Flag            | Description                                      | Default   |
|-----------------|--------------------------------------------------|-----------|
| `--target`      | Output binary name                               | `myapp`   |
| `--lang`        | Language: `c` or `cpp`                           | `c`       |
| `--compiler`    | Compiler to use (e.g., `gcc`, `clang`, `g++`)   | inferred  |
| `--force`       | Overwrite existing `Makefile`                    | `False`   |

---

## 📦 Output

A simple `Makefile` with:

- Automatic object file compilation
- Debug flags (`-Wall -Wextra -g`)
- `clean` rule

---

## 🗺️ Roadmap

See below ↓
