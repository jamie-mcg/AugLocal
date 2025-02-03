import re
import matplotlib.pyplot as plt


# Function to parse the log file and extract accuracies
def parse_log_file(log_file_path):
    with open(log_file_path, "r") as file:
        log_data = file.read()

    # Regular expression to match the accuracy pattern
    accuracy_pattern = r"layer \[(\d+)\], Prec@1 \d+\.?\d* \((\d+\.?\d*)\)"

    # Split the log data into classes
    class_data = log_data.split("\n\n")

    # Dictionary to hold accuracies for each class
    class_accuracies = {}

    for class_section in class_data:
        # Find the class number
        class_number_match = re.search(r"Class (\d+):", class_section)
        if class_number_match:
            class_number = int(class_number_match.group(1))
            # Find all accuracies for this class
            accuracies = re.findall(accuracy_pattern, class_section)
            # Convert accuracies to float and store them
            class_accuracies[class_number] = [float(acc) for _, acc in accuracies]

    return class_accuracies


# Function to plot the accuracies for each class
def plot_accuracies(class_accuracies):
    for class_number, accuracies in class_accuracies.items():
        plt.figure()
        plt.plot(range(len(accuracies)), accuracies, marker="o")
        if class_number == 10:
            plt.title(f"Total Accuracy")
        else:
            plt.title(f"Class {class_number} Accuracy")
        plt.xlabel("Layer Index")
        plt.ylabel("Accuracy (%)")
        plt.xticks(range(len(accuracies)))
        plt.ylim(75, 100)  # Adjust y-axis limits if necessary
        plt.grid(True)
        plt.savefig(f"class_{class_number}_accuracy.png")  # Save the plot
        plt.show()


# Path to your log file
log_file_path = "/proj/gpu_mtk53548/AugLocal/2024-04-13_00-13-36_1234/log_final.txt"

# Parse the log file and get accuracies
class_accuracies = parse_log_file(log_file_path)

# Plot the accuracies for each class
plot_accuracies(class_accuracies)
