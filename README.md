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

## Setting Up Your Project Directory

Before cloning the repository, it's a good practice to create a dedicated directory for your projects. This helps keep your work organized and makes it easier to find your projects later.

**On macOS/Linux:**
```bash
mkdir -p ~/Projects
cd ~/Projects
```

**On Windows:**
```bash
mkdir C:\Projects
cd C:\Projects
```

Or you can create a directory anywhere on your system that makes sense for you (e.g., `~/Desktop/Projects` on macOS, or `C:\Users\YourName\Documents\Projects` on Windows).

**Why this matters:** Having a dedicated projects folder helps you:
- Keep all your coding projects in one place
- Easily navigate between different projects
- Maintain a clean and organized workspace

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

## Contributing Your Changes (Git Workflow)

**IMPORTANT: Always create your own branch before making changes!** This is a critical best practice that protects the main branch and allows others to review your work before it's merged. Never commit directly to the `main` branch.

### Why Create a Branch?

Creating a branch is like creating your own copy of the project to experiment with. It allows you to:
- Make changes without affecting the main codebase
- Work on multiple features simultaneously
- Collaborate safely with others
- Keep the main branch stable and clean

### Step-by-Step Guide to Pushing Your Changes

#### Step 1: Check Your Current Status

Before making any changes, check what branch you're on and what files have been modified:

```bash
# Check current branch
git branch

# Check status of your repository
git status
```

You should see that you're on the `main` branch initially. The `*` indicates your current branch.

#### Step 2: Create and Switch to Your Own Branch

**Always create a new branch before making changes!** Use a descriptive name that indicates what you're working on.

```bash
# Create and switch to a new branch
git checkout -b your-name
```


**Tip:** Use a naming convention like `your-name` to make it clear who created the branch

#### Step 3: Make Your Changes

Now you can safely make your changes. Here are some common types of changes you might make:

**Adding a new model file:**
- Create a new `.txt` file in the `models/` directory (like `Aldea_Model.txt`)
- Add your Antimony model definition to the file

**Adding a new script:**
- Create a new Python script (like `Run_Aldea_Antimony.py`)
- Write code to load and simulate your model

**Adding figures:**
- Run your simulation and save plots to the `figures/` directory
- Generated plots will be saved as image files (e.g., `.png` files)

**Modifying existing files:**
- Edit existing Python scripts
- Update model parameters
- Modify documentation

#### Step 4: Check What Changed

After making your changes, check what files have been modified:

```bash
git status
```

This shows:
- **Untracked files**: New files you've created (shown in red)
- **Modified files**: Files you've changed (shown in red)

You can also see the specific changes:

```bash
# See detailed changes in modified files
git diff

# See what new files would be added
git status
```

#### Step 5: Stage Your Changes

Before committing, you need to "stage" your changes. This tells Git which files you want to include in your commit.

**For new files:**
```bash
# Add a specific new file
git add models/Aldea_Model.txt
git add Run_Aldea_Antimony.py
git add figures/your_plot.png
```

**For modified files:**
```bash
# Add a specific modified file
git add example1.py
```

**To add all changes at once:**
```bash
# Add all changes (new and modified files)
git add .
```

**Warning:** Be careful with `git add .` - it adds everything. Make sure you only want to commit the files you've actually changed.

#### Step 6: Commit Your Changes

A commit is like saving a snapshot of your changes with a message describing what you did.

```bash
git commit -m "Descriptive message about your changes"
```

**Good commit messages:**
```bash
git commit -m "Add Aldea model and simulation script"
git commit -m "Add new pharmacokinetic model example"
git commit -m "Update example1.py with new parameters"
git commit -m "Add simulation results figure"
```

**Bad commit messages (avoid these):**
```bash
git commit -m "changes"
git commit -m "stuff"
git commit -m "asdf"
```

Your commit message should clearly describe what you added or changed.

#### Step 7: Push Your Branch to GitHub

Now push your branch (with all your commits) to GitHub:

```bash
git push origin your-name
```

The first time you push a new branch, Git might ask you to set the upstream:

```bash
git push -u origin your-name
```

The `-u` flag sets up tracking so future pushes are simpler.

#### Step 8: Create a Pull Request (Optional but Recommended)

After pushing, go to the GitHub repository page. You'll likely see a banner suggesting you create a pull request. A pull request allows others to:
- Review your changes
- Discuss improvements
- Merge your changes into the main branch

Click "Compare & pull request" and fill out the description of what you changed.

### Complete Workflow Example

Here's a complete example of the workflow:

```bash
# 1. Check current status
git status
git branch

# 2. Create your branch
git checkout -b student/my-new-model

# 3. Make your changes (create files, edit files, etc.)
# ... work on your files ...

# 4. Check what changed
git status
git diff

# 5. Stage your changes
git add models/My_Model.txt
git add Run_My_Model.py
git add figures/my_plot.png

# 6. Commit with a message
git commit -m "Add my new model with simulation script and results"

# 7. Push to GitHub
git push -u origin student/my-new-model
```

### Common Scenarios

**Scenario 1: Adding a new model and script**
```bash
git checkout -b student/pharmacokinetic-model
# Create models/PK_Model.txt
# Create Run_PK_Model.py
git add models/PK_Model.txt Run_PK_Model.py
git commit -m "Add pharmacokinetic model and simulation script"
git push -u origin student/pharmacokinetic-model
```

**Scenario 2: Adding a figure from a simulation**
```bash
git checkout -b student/add-simulation-results
# Run your simulation, save figure to figures/
git add figures/simulation_results.png
git commit -m "Add simulation results figure"
git push -u origin student/add-simulation-results
```

**Scenario 3: Modifying an existing file**
```bash
git checkout -b student/update-example-parameters
# Edit example1.py
git add example1.py
git commit -m "Update example1.py with new rate constants"
git push -u origin student/update-example-parameters
```

### Important Reminders

1. **Always create a branch before making changes** - Never commit directly to `main`
2. **Use descriptive branch names** - Help others understand what you're working on
3. **Write clear commit messages** - Describe what you changed and why
4. **Check your status frequently** - Use `git status` to see what's changed
5. **Push regularly** - Don't wait until you're completely done; push your work periodically

### Troubleshooting Git Issues

**If you accidentally committed to main:**
```bash
# Create a branch from your current position (saves your work)
git checkout -b your-name

# Switch back to main and reset it
git checkout main
git reset --hard origin/main
```

**If you want to undo changes before committing:**
```bash
# Discard changes to a specific file
git checkout -- filename.py

# Discard all uncommitted changes (be careful!)
git reset --hard
```

**If you need to update your branch with latest changes from main:**
```bash
# Switch to main and pull latest changes
git checkout main
git pull origin main

# Switch back to your branch and merge main into it
git checkout your-name
git merge main
```

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
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── example1.py                 # First example script
├── Run_Aldea_Antimony.py       # Second example: Aldea model simulation
├── models/                     # Directory containing Antimony model files
│   └── Aldea_Model.txt         # Aldea pharmacokinetic/pharmacodynamic model
├── figures/                    # Directory for saving simulation plots
│   └── aldea_antimony_simulation_case_1.png  # Example simulation results
└── .gitignore                  # Git ignore file
```

## License

This example is provided for educational purposes. Please refer to the Tellurium license for usage terms.
