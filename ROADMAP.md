# 🛣️ Roadmap
---

### ✅ Phase 1: Core CLI (Complete)
- [x] Detect `.c`, `.cpp`, `.h` files
- [x] Auto-generate a `Makefile`
- [x] Support custom `--target`, `--lang`, `--compiler`
- [x] Default compiler inference based on language
- [x] Success messages and safe feedback

---

### 🚧 Phase 2: CLI Enhancements (Next Up)
- [ ] `--force`: Overwrite existing `Makefile`
- [ ] `--output`: Allow custom file path/name for output
- [ ] `--build`: `debug` or `release` mode (`-g` or `-O2`)
- [ ] `--include-subdirs`: Search subdirectories
- [ ] `--dry-run`: Print instead of writing

---

### 🌱 Phase 3: Project Bootstrap & Quality of Life
- [ ] `--init`: Generate starter `main.c` or `main.cpp`
- [ ] `--run`: Automatically build after Makefile generation
- [ ] Interactive mode: prompt user if no args given
- [ ] `--preset`: Templates for common project types (cli-app, lib, test)

---

### 🚀 Phase 4: Packaging & Distribution
- [ ] Package with `setuptools` for `pip install makegen`
- [ ] Add unit tests (e.g., using `pytest`)
- [ ] Homebrew or AUR packaging (optional)
- [ ] Publish GitHub release with example projects
