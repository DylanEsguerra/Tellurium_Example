# Tellurium Example Repository

This repository provides an intro example of how to use Tellurium, a Python library for modeling and simulating biological systems.

## What is Tellurium?

Tellurium is a Python package that knits together a variety of important packages for carrying out simulation studies in systems biology and other disciplines. 

- Loading and simulating SBML models
- Creating models using the Antimony language
- Visualizing simulation results
- Parameter estimation and optimization

## Prerequisites

Before you begin, make sure you have Python 3.7 or higher installed on your system. You can check your Python version by running:

```bash
python --version
```

**Note**: On some systems, you may need to use `python3` instead of `python`.

## Getting Started

### Step 1: Clone this Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/DylanEsguerra/Tellurium_Example.git
cd Tellurium_Example
```

### Step 2: Create a Virtual Environment

It's a best practice to use a virtual environment for Python projects. This keeps your project dependencies separate from your system Python installation.

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` at the beginning of your command prompt, indicating that the virtual environment is active.

### Step 3: Install Dependencies

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

This will install Tellurium and its dependencies.

### Step 4: Run the Example

Now you can run the first example:

```bash
python example1.py
```

This will:
1. Load a simple biochemical model using Antimony syntax
2. Simulate the model for 50 time units
3. Display a plot of the simulation results

## Understanding the Example

The example in `example1.py` demonstrates:

1. **Model Definition**: A basic reaction `S1 -> S2` with first-order kinetics
2. **Parameter Setting**: Rate constant `k1 = 0.1` and initial condition `S1 = 10`
3. **Simulation**: Running a timecourse simulation from 0 to 50 time units
4. **Visualization**: Plotting the results

### The Antimony Syntax

The model is defined using Antimony, a human-readable representation of SBML models:

```python
'S1 -> S2; k1*S1; k1 = 0.1; S1 = 10'
```

This means:
- `S1 -> S2`: A reaction converting S1 to S2
- `k1*S1`: The reaction rate is proportional to S1 concentration
- `k1 = 0.1`: The rate constant is 0.1
- `S1 = 10`: The initial concentration of S1 is 10

## Next Steps

Once you've successfully run the example, you can:

1. Modify the model parameters and see how they affect the simulation
2. Add more species and reactions to create more complex models
3. Explore Tellurium's documentation for more advanced features
4. Try the additional examples on the Tellurium documentation

## Troubleshooting

### Common Issues

1. **Python not found**: Make sure Python is installed and in your PATH
2. **Permission errors**: On some systems, you may need to use `python3` instead of `python`

### Getting Help

- [Tellurium Documentation](http://tellurium.readthedocs.io/)
- [Tellurium GitHub Repository](https://github.com/sys-bio/tellurium)

We encorage the use of LLM to help with programming work. They are great at helping clone repositories, set up virtual environments and all aspects of this tutorial. (I made it today using one)

## Deactivating the Virtual Environment

When you're done working on the project, you can deactivate the virtual environment:

```bash
deactivate
```

## File Structure

```
Tellurium_Example/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── example1.py           # First example script
└── .gitignore            # Git ignore file
```

## License

This example is provided for educational purposes. Please refer to the Tellurium license for usage terms.
