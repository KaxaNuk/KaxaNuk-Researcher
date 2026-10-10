---
description: Filesystem Boundaries
applyTo: "**"
metadata:
  version: 1.3.0
---
# Filesystem Boundaries
When searching or reading local files outside the project directory, only access well-defined,
discoverable locations relevant to the task — such as the current environment dependencies' folders
and packages — except a KaxaNuk library's: its installed files, a clone or a wheel are never
opened, searched or printed. A KaxaNuk tool is known from its skill, its documentation, its
changelog and from running it, never from its code.
Never speculatively browse the user's home directory, arbitrary system paths, or paths that may or
may not exist.
If you need to find the location of an installed package, use the appropriate tooling for the
language rather than guessing at paths.
