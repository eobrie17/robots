# Evolutionary Robotics Project

## Quick summary
This project is from the Evolutionary Robotics course (with Josh Bongard). It evolves locomotion strategies for a procedurally generated multi-legged robot using PyBullet physics and pyrosim’s URDF/neural-network tooling. The project highlights applied AI, robotics simulation, and lightweight evolutionary search.

[▶️ Watch final result on YouTube](https://youtu.be/Zl3Lk0_gKPg)

## Highlights
- **Expressive morphology:** Robots are generated entirely in code, with articulated limbs, touch sensors, and coordinated motor neurons.
- **Neuro-evolution core:** Each candidate has a weight matrix mapping sensors to motors; targeted mutations explore the search space without complex frameworks.
- **Parallel hill climbing:** Parents and children evaluate asynchronously, and the champion robot can be replayed in the PyBullet GUI for live demos.
- **Quantitative tracking:** Fitness and speed metrics are logged to disk, and optional plotting utilities turn raw distances into visuals.
- **Modular simulation harness:** Sensing, thinking, and acting stay cleanly separated.

## Quick Start
1. **Install dependencies**
   ```bash
   pip install numpy pybullet pyrosim matplotlib
2. **Run an evolutionary session**

   `python3 search.py`
   
   This launches the parallel hill climber, evaluates the population, and replays the best performer when finished.
3. **Review outcomes**
- Inspect `evolutions/` for per-parent fitness logs.
- Enable plotting helpers (e.g., PARALLEL_HILLCLIMBER.graph_speeds()) to visualize progress.

## Project Structure
- `search.py` – Minimal entry point that instantiates the parallel hill climber, runs the evolutionary loop, and replays the champion controller in the GUI for demos.
- `parallelHillClimber.py` – Handles population lifecycle: clearing old artifacts, spawning and mutating child solutions, evaluating them in batch, selecting the fitter individuals, and offering optional plotting helpers plus a GUI replay method for the current best robot.
- `solution.py` – Seeds each candidate’s neural weights, creates the PyBullet world, and writes URDF/NN definitions for the octopod by default while also providing alternate quadruped builders you can swap in when showcasing adaptability.
- `simulation.py` – Wraps PyBullet setup, stepping, and teardown; instantiates the world and robot, iterates for the configured horizon, and forwards sensing/thinking/acting each frame.
- `robot.py` – Loads the generated body/brain, maps sensors and motors via pyrosim, drives joints from the neural network each tick, and logs per-run fitness artifacts for later analysis.
- `sensor.py` & `motor.py` – Lightweight adapters that cache touch sensor traces, expose a convenience saver, and send joint targets through PyBullet’s position controller.
- `constants.py` – Centralizes hyperparameters—iterations, population size, motor range, and the neuron counts for both octopod and quadruped configurations—so experiments stay tweakable from one file.
- `simulate.py` & `world.py` – Provide the subprocess entry point that drives a single rollout and the minimal world loader that spawns the plane plus the custom obstacle.
- `generate.py` – Legacy sandbox illustrating how to handcraft a simpler body/brain pair, useful for quick explanations before diving into the automated evolution pipeline.
