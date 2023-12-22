## Documentation Problems

Documentation can provide a wrong view of the source code. There are two cases:

- Undocumented features
- Idealized presentation

A feature may not be documented because it may be:

- Not officially supported
- Provided only as a support mechanism for suitably trained engineers
- Experimental or intended for a future release
- Used by the product's vendor to gain an advantage over the competition
- Badly implemented
- A security threat
- Intended only for a subset of the users or product versions
- A Trojan horse, time bomb, or back door

Features are sometimes not documented due to oversight. When reading code you should be wary of undocumented features. Classify each instance as justified, careless, or malicious, and accordingly decide whether the code or the documentation should be fixed.

Idealized presentation could be due writing end-user documentation based on a functional specification and the hope that the system will be implemented as specified. It could also be due to not updating the documentation when structural change are implemented. Inconsistency could be due to inability to be verified by tools.

If unknown used words hinder your understanding of the code, look it up in the documentation glossary.

## Exercise

Create documentation glossary for Rails codebase.

Create an annotated list of documentation sources for Rails framework. Categorize the sources based on the type of information they provide. Strive for wide coverage of areas (for example, specifications, design, user documentation) rather than completeness.

Use the Git repository to see the detailed history of the source code's evolution and any comments justifying each change.
