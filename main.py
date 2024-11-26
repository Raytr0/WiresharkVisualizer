#pandas for csv file processing
import pandas as pd
#matplotlib for plotting functionality
import matplotlib.pyplot as plt
#re for regular expressions to allow for extraction of window size from Info field
import re

def extract_window_size(info):
    #Extracts the window size (Win=XXXXX) from the Info field.
    match = re.search(r"Win=(\d+)", info)
    print(match)
    #extracts the window number from Win=XXXXX
    return int(match.group(1))

def process_and_plot(csv_file, title, ax):
    #Processes a CSV file to extract frame time and window size and plots them.
    try:
        # Load data from CSV file
        data = pd.read_csv(csv_file)

        # Extract window size
        data["Window Size"] = data["Info"].apply(extract_window_size)
        data.dropna(subset=["Window Size"], inplace=True)

        # Plot data
        ax.plot(data["Time"], data["Window Size"], label=title, color="blue", linewidth=1)
        ax.set_title(title)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Congestion Window Size (bytes)")
        ax.legend()
    except Exception as e:
        print(f"Error processing {csv_file}: {e}")

# File paths for the CSV files
h1_csv = "h1info.csv"
h3_csv = "h3info.csv"

# Create subplots
fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Process and plot the data for h1 and h3 traffic
process_and_plot(h1_csv, "Congestion Window vs Time (h1 Traffic)", axes[0])
process_and_plot(h3_csv, "Congestion Window vs Time (h3 Traffic)", axes[1])

# Adjust layout
plt.tight_layout()
plt.show()
