#!/usr/bin/env python3

import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Generate a Makefile.")
    parser.add_argument("--target", type=str, default="myapp", help="Output binary name")
    parser.add_argument("--lang", choices=["c", "cpp"], default="c", help="Language")
    parser.add_argument("--compiler", type=str, help="Compiler to use")
    parser.add_argument("--force", action="store_true", help="Overwrite existing Makefile")
    args = parser.parse_args()

    project_dir = Path.cwd()
    makefile_path = project_dir / "Makefile"

    if makefile_path.exists() and not args.force:
        print("❌ Makefile already exists. Use --force to overwrite.")
        return

    c_files = list(project_dir.glob("*.c"))
    cpp_files = list(project_dir.glob("*.cpp"))
    h_files = list(project_dir.glob("*.h"))

    build_rules = ""
    if c_files:
        build_rules += """%.o: %.c\n\t$(CC) $(CFLAGS) -c $< -o $@\n\n"""
    if cpp_files:
        build_rules += """%.o: %.cpp\n\t$(CC) $(CFLAGS) -c $< -o $@\n"""

    source_files = c_files + cpp_files
    src_files = [f.name for f in source_files]
    obj_files = [f.with_suffix(".o").name for f in source_files]

    lang = args.lang
    compiler = args.compiler or ("g++" if lang == "cpp" else "gcc")
    target = args.target

    MAKEFILE_TEMPLATE = """
CC = {compiler}
CFLAGS = -Wall -Wextra -g
TARGET = {target}

SRCS = {srcs}
OBJS = {objs}

$(TARGET): $(OBJS)
\t$(CC) $(CFLAGS) $(OBJS) -o $(TARGET)

{build_rules}

clean:
\trm -f $(TARGET) $(OBJS)
"""

    rendered = MAKEFILE_TEMPLATE.format(
        compiler=compiler,
        target=target,
        srcs=" ".join(src_files),
        objs=" ".join(obj_files),
        build_rules=build_rules.strip()
    )

    makefile_path.write_text(rendered)
    print(f"✅ Makefile written for '{target}' using {lang.upper()} in {project_dir}")

if __name__ == "__main__":
    main()