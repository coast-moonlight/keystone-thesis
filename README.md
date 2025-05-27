# Thesis: Evaluating RISC-V Enclaves: Performance Benchmarks and Configuration Best Practices

This repository contains the LaTeX source code for my master's thesis titled **"Evaluating RISC-V Enclaves: Performance Benchmarks and Configuration Best Practices"**. The goal of this thesis is to evaluate the performance of Keystone enclaves, a Trusted Execution Environment (TEE) framework for RISC-V platforms. The evaluation focuses on identifying performance bottlenecks and providing configuration best practices to optimize enclave execution.

---

## Table of Contents
1. [Overview](#overview)
2. [Structure](#structure)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Compiling the Thesis](#compiling-the-thesis)
4. [Directory Structure](#directory-structure)
5. [Contributing](#contributing)

---

## Overview

This thesis investigates the performance of Keystone enclaves by conducting a benchmarking study across various system configurations. The research evaluates system parameters like CPU core count, cache size, and memory allocation, and presents configuration recommendations to optimize enclave execution.

---

## Structure

The repository is organized as follows:

- **`main.tex`**: The main LaTeX file that contains the thesis content. It loads the `preamble.tex` for LaTeX setup and configurations.
- **`preamble.tex`**: Contains all the LaTeX configurations, settings, and package inclusions that are shared across the document. This helps keep `main.tex` clean and focused on the content.
- **`figures/`**: Stores any figures, charts, or images referenced in the thesis.
- **`bibliography/`**: Contains the `.bib` file for references used in the thesis.

---

## Getting Started

### Prerequisites

To compile the thesis, you'll need a LaTeX distribution. I recommend using [TeX Live](https://www.tug.org/texlive/) or [MiKTeX](https://miktex.org/) for this purpose.

If you are using Ubuntu (or a similar Linux distribution), you can install the required LaTeX packages using the following command:

```bash
sudo apt-get install texlive-full
```

If you use **VS Code** or another LaTeX editor, make sure to install the appropriate extensions, such as `LaTeX Workshop`.

## Directory Structure

Here’s a breakdown of the main directories and files in the repository:


- **`main.tex`**: The main LaTeX file that ties everything together. It includes the document content and loads the `preamble.tex` file for LaTeX configurations.
    
- **`preamble.tex`**: The file containing all LaTeX package configurations, document class settings, and thesis-specific setups.

**`chapters/`**: Contains LaTeX files for each chapter.

- `introduction.tex`: Introduction chapter.
    
- `background.tex`: Background and system architecture.
    
- `methodology.tex`: Methodology for experimental setup.
    
- `results.tex`: Results from performance evaluation.
    
- `conclusion.tex`: Conclusion and future work.

- **`figures/`**: Store figures, diagrams, and images.
- **`bibliography/`**: Contains the `.bib` file with the references used in the thesis.
    - `references.bib`: Bibliography file for citations.

## Contributing

This repository is primarily for the thesis project, but if you'd like to contribute or collaborate, feel free to fork the repository and create a pull request. Contributions could include:
- Improving the LaTeX structure.
- Adding additional benchmarks or experiments.
- Reviewing and suggesting improvements to the content.

If you're working on a specific chapter or section, please follow the modular structure and ensure that your contributions are compatible with the rest of the thesis.
