#!/usr/bin/env python3
"""
Tellurium Example 1

This script demonstrates how to:
1. Load a basic biochemical model using Antimony syntax
2. Simulate the model using RoadRunner
3. Visualize the simulation results

The model represents a basic first-order reaction: S1 -> S2
"""

import tellurium as te

def main():
    """
    Main function that runs the Tellurium example.
    """
    print("Tellurium Example 1")
    print("=" * 30)
    
    # Define the model using Antimony syntax
    # This creates a basic reaction: S1 -> S2 with first-order kinetics
    antimony_model = 'S1 -> S2; k1*S1; k1 = 0.1; S1 = 10'
    
    print(f"Model definition: {antimony_model}")
    print()
    
    # Load the model into RoadRunner
    print("Loading model into RoadRunner...")
    r = te.loada(antimony_model)
    
    # Print model information
    print("Model loaded successfully!")
    print(f"Species: {r.getFloatingSpeciesIds()}")
    print(f"Parameters: {r.getGlobalParameterIds()}")
    print()
    
    # Run simulation
    print("Running simulation from t=0 to t=50 with 100 points...")
    r.simulate(0, 50, 100)
    
    # Display simulation results
    print("Simulation completed!")
    print("Final concentrations:")
    print(f"  S1: {r.S1:.4f}")
    print(f"  S2: {r.S2:.4f}")
    print()
    
    # Create and display the plot
    print("Generating plot...")
    r.plot()
    
    print("Example completed successfully!")

if __name__ == "__main__":
    main()
