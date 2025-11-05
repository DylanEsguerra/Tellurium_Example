#!/usr/bin/env python3
"""
Tellurium Example 2: Aldea Antimony Model

This script demonstrates how to:
1. Load a complex biochemical model from an Antimony file
2. Run a timecourse simulation with specific parameters
3. Create custom visualizations with multiple subplots
4. Save results to files

The model represents an ARIA-E case study with pharmacokinetics and pharmacodynamics.
Source:
1. Aldea R, Grimm HP, Gieschke R, et al. In silico exploration of amyloid‐related imaging abnormalities in the gantenerumab open‐label extension trials using a semi‐mechanistic model. A&D Transl Res & Clin Interv. 2022;8(1):e12306. doi:10.1002/trc2.12306

"""

import tellurium as te
import matplotlib.pyplot as plt
from pathlib import Path


def load_model(model_file_path):
    """
    Load an Antimony model from a file.
    
    Args:
        model_file_path (Path): Path to the Antimony model file
        
    Returns:
        RoadRunner: Loaded model ready for simulation
    """
    print(f"Loading model from: {model_file_path}")
    
    # Read the model file content
    with open(model_file_path, 'r') as f:
        model_data = f.read()
    
    # Load the model into RoadRunner
    r = te.loada(model_data)
    print("Model loaded successfully!")
    
    return r


def run_simulation(r, start_time=0, end_time=840, time_step=0.1):
    """
    Run a timecourse simulation on the loaded model.
    
    Args:
        r (RoadRunner): The loaded model
        start_time (float): Simulation start time
        end_time (float): Simulation end time For this model we use 840 days or 120 weeks
        time_step (float): Time step size
        
    Returns:
        numpy.ndarray: Simulation results
    """
    print(f"Running simulation from t={start_time} to t={end_time}...")
    
    # Calculate number of steps
    n_steps = int((end_time - start_time) / time_step)
    
    # Reset model to initial state
    r.reset()
    
    # Run simulation and select specific species to track
    result = r.simulate(start_time, end_time, n_steps, 
                       selections=['time', '[C]', '[A_beta]', '[VWD]', 'BGTS'])
    
    print("Simulation completed!")
    return result


def create_plots(result, output_dir):
    """
    Create and save custom plots of the simulation results.
    
    Args:
        result (numpy.ndarray): Simulation results
        output_dir (Path): Directory to save the plot
    """
    print("Creating plots...")
    
    # Extract time and data
    times = result[:, 0]
    
    # Create figure with 4 subplots
    plt.figure(figsize=(10, 8))
    plt.subplots_adjust(hspace=0.3)
    
    # Define dose administration times and amounts
    dose_times = [0, 32, 56, 84, 102, 140, 280, 309, 336, 365, 420, 455, 483, 504, 529, 560, 588, 616, 644, 675, 703]
    dose_amounts = [450, 450, 900, 900, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200, 1200]
    
    # Plot 1: Central Concentration (Pharmacokinetics)
    ax1 = plt.subplot(4, 1, 1)
    central_conc = result['[C]']
    plt.plot(times/7, central_conc, 
             label='Central Concentration (C)', 
             color='magenta', 
             linewidth=2)
    
    # Add dose administration markers
    plt.scatter([t/7 for t in dose_times], [d/10 for d in dose_amounts], 
               marker='+', color='orange', s=100, linewidth=2,
               label='Dose administrations')
    
    ax1.set_ylabel('PK [mcg/ml]', fontsize=12)
    ax1.set_title('ARIA-E case 1 (Antimony)', fontsize=14, pad=10)
    ax1.set_ylim(0, 150)
    ax1.set_yticks([0, 75, 150])
    ax1.grid(True, alpha=0.2)
    ax1.legend()
    
    # Plot 2: Local Amyloid
    plt.subplot(4, 1, 2)
    plt.plot(times/7, result['[A_beta]'], 
             color='limegreen', linewidth=2)
    plt.ylabel('Local Amyloid [-]', fontsize=12)
    plt.ylim(0, 5)
    plt.yticks([0, 2.5, 5])
    plt.grid(True, alpha=0.2)
    
    # Plot 3: VWD (Vessel Wall Damage)
    plt.subplot(4, 1, 3)
    plt.plot(times/7, result['[VWD]'], 
             color='red', linewidth=2)
    plt.ylabel('VWD [-]', fontsize=12)
    plt.ylim(0, 1)
    plt.yticks([0, 0.5, 1])
    plt.grid(True, alpha=0.2)
    
    # Plot 4: BGTS (ARIA-E biomarker)
    plt.subplot(4, 1, 4)
    plt.plot(times/7, result['BGTS'], 
             color='cyan', linewidth=2)
    plt.xlabel('Weeks since first dose', fontsize=12)
    plt.ylabel('ARIA-E [BGTS]', fontsize=12)
    plt.ylim(0, 30)
    plt.yticks([0, 15, 30])
    plt.grid(True, alpha=0.2)
    
    # Set consistent x-axis for all subplots
    for i in range(1, 5):
        plt.subplot(4, 1, i)
        plt.xticks(range(0, 121, 12))
        if i < 4:
            plt.xlabel('')
    
    # Save the plot
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / 'aldea_antimony_simulation_case_1.png'
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    print(f"Plot saved to: {output_file}")
    
    # Display the plot
    plt.show()
    plt.close()


def print_results(result):
    """
    Print the final simulation results in a readable format.
    
    Args:
        result (numpy.ndarray): Simulation results
    """
    print("\n" + "="*50)
    print("SIMULATION RESULTS")
    print("="*50)
    print("Final values:")
    print(f"  Central concentration: {result['[C]'][-1]:.2f} mcg/ml")
    print(f"  Local Amyloid: {result['[A_beta]'][-1]:.2f}")
    print(f"  VWD: {result['[VWD]'][-1]:.2f}")
    print(f"  BGTS: {result['BGTS'][-1]:.2f}")
    print("="*50)


def main():
    """
    Main function that runs the Aldea Antimony model simulation.
    """
    print("Tellurium Example 2: Aldea Antimony Model")
    print("=" * 50)
    
    # Set up file paths
    model_file = Path(__file__).parent / "models" / "Aldea_Model.txt"
    output_dir = Path(__file__).parent / "figures"
    
    # Load the model
    r = load_model(model_file)
    
    # Print model information (similar to example1.py)
    print(f"Species: {r.getFloatingSpeciesIds()}")
    print(f"Parameters: {r.getGlobalParameterIds()}")
    print()
    
    # Run simulation
    result = run_simulation(r)
    
    # Create and save plots
    create_plots(result, output_dir)
    
    # Print final results
    print_results(result)
    
    print("\nExample completed successfully!")


if __name__ == "__main__":
    main()