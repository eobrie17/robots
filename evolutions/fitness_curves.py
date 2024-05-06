import matplotlib.pyplot as plt
import os
import numpy as np  # Ensure to import numpy for color mapping
import constants as c

def read_fitness_file(filename):
    """Reads a single fitness file and returns a list of float values representing average fitness per generation."""
    with open(filename, 'r') as file:
        # Read and convert lines to float
        fitness_data = [float(line.strip()) for line in file.readlines()]
        # Calculate average fitness every 10 entries
        generation_avg = []
        for i in range(0, len(fitness_data), 15):
            # Compute average for this generation
            average = np.mean(fitness_data[i:i+15])
            generation_avg.append(average)
    return generation_avg

def plot_fitness_curves():
    # Get the directory where the script is running
    directory = os.getcwd() + '/evolutions'  # Gets the current working directory
    files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    colors = plt.cm.viridis(np.linspace(0, 1, len(files)))  # Generate colors

    plt.figure(figsize=(10, 5))

    for file, color in zip(files, colors):
        filepath = os.path.join(directory, file)
        average_fitness_data = read_fitness_file(filepath)
        plt.plot(average_fitness_data, marker='o', linestyle='-', color=color, label=f'{os.path.basename(file)}')

    plt.title('Average Fitness per Generation Across Different Experiments')
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.legend(title="File")
    plt.grid(True)
    plt.show()

# Usage
plot_fitness_curves()
