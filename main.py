#!/usr/bin/env python3

import argparse
from pathlib import Path

def main():

    parser = argparse.ArgumentParser(description="Generate a Makefile.")
    parser.add_argument("--target", type=str, default="myapp", help="Output binary name")
    parser.add_argument("--lang", choices=["c", "cpp"], default="c", help="Language")
    parser.add_argument("--compiler", type=str, help="Compiler to use")
    args = parser.parse_args()

    project_dir = Path.cwd()

    c_files = list(project_dir.glob("*.c"))
    cpp_files = list(project_dir.glob("*.cpp"))
    h_files = list(project_dir.glob("*.h"))

    print("C files:", [f.name for f in c_files])
    print("C++ files:", [f.name for f in cpp_files])
    print("Header files:", [f.name for f in h_files])

    source_files = c_files + cpp_files
    src_files = [f.name for f in source_files]
    obj_files = [f.with_suffix(".o").name for f in source_files]
    compiler = args.compiler or ("g++" if lang == "cpp" else "gcc")
    lang = args.lang
    target = args.target

    MAKEFILE_TEMPLATE = """
    CC = {compiler}
    CFLAGS = -Wall -Wextra -g
    TARGET = {target}

    SRCS = {srcs}
    OBJS = {objs}

    $(TARGET): $(OBJS)
    \t$(CC) $(CFLAGS) $(OBJS) -o $(TARGET)

    %.o: %.{ext}
    \t$(CC) $(CFLAGS) -c $< -o $@

    clean:
    \trm -f $(TARGET) $(OBJS)
    """

    ext = "cpp" if lang == "cpp" else "c"

    rendered = MAKEFILE_TEMPLATE.format(
        compiler=compiler,
        target=target,
        srcs=" ".join(src_files),
        objs=" ".join(obj_files),
        ext=ext
    )

    with open("Makefile", "w") as f:
        f.write(rendered)

    print(f"✅ Makefile generated for '{target}' using {lang.upper()} in {project_dir}")

if __name__ == "__main__":
    main()