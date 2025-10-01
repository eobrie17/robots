import matplotlib.pyplot as plt
import os
import numpy as np

def read_fitness_file(filename):
    """Reads a single fitness file and returns a list of float values representing fitness per generation."""
    with open(filename, 'r') as file:
        fitness_data = [float(line.strip()) for line in file.readlines()]
    return np.array(fitness_data)

def average_in_groups(data, group_size):
    """Averages data points in groups of a specified size."""
    num_groups = len(data) // group_size
    grouped_data = [
        np.mean(data[i * group_size:(i + 1) * group_size])
        for i in range(num_groups)
    ]
    return np.array(grouped_data)

def average_groups(files, directory, group_size):
    """Average fitness data from groups of files and reduce data points by averaging in groups."""
    group_data = []
    for file_group in files:
        aggregated_data = []
        for idx, file in enumerate(file_group):
            filepath = os.path.join(directory, file)
            data = read_fitness_file(filepath)
            if idx == 0:
                aggregated_data = data.copy()  # Initialize with the first file's data
            else:
                # Ensure that all files have the same length of data
                if len(data) != len(aggregated_data):
                    raise ValueError(f"Data length mismatch in file {file}")
                aggregated_data += data
        aggregated_data /= len(file_group)  # Average the sum

        # Average in specified groups (e.g., groups of 10)
        grouped_data = average_in_groups(aggregated_data, group_size)
        group_data.append(grouped_data)
    return group_data

def plot_fitness_curves():
    directory = os.getcwd() + '/evolutions'
    all_files = os.listdir(directory)
    octo_files = [f for f in all_files if f.startswith('octocurve')]
    quad_files = [f for f in all_files if f.startswith('quadcurve')]

    # Check if there are files in each category
    if not octo_files or not quad_files:
        raise FileNotFoundError("No appropriate files found in the directory.")

    # Change group size here (e.g., 10 for averaging 10 generations)
    group_size = 10
    averaged_data = average_groups([octo_files, quad_files], directory, group_size)

    plt.figure(figsize=(10, 5))

    # Plot octocurve data
    plt.plot(averaged_data[0], marker='o', linestyle='-', color='blue', label='Octopod Average Fitness')
    # Plot quadcurve data
    plt.plot(averaged_data[1], marker='o', linestyle='-', color='green', label='Quadruped Average Fitness')

    plt.title('Average Fitness per Generation for Octopod and Quadruped')
    plt.xlabel(f'Generation')
    plt.ylabel('Average Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()

# Usage
plot_fitness_curves()
