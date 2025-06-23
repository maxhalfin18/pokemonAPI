# Max and Tom Pokémon Project

A data science and image processing project analyzing Pokémon data through statistical exploration and basic machine learning techniques.

## Project Overview

This project includes:

- Processing a dataset of Pokémon with various attributes (type, height, weight, etc.)
- Generating an average image from a folder of Pokémon-related photos
- Visualizing and analyzing data using Pandas and Matplotlib
- Applying clustering (K-Means) to identify patterns in Pokémon features

## Folder Structure

maxandtomPokemonProject/
├── pokemonCSV.csv          # Pokémon dataset (CSV format)
├── images/                 # Folder containing Pokémon-related images
├── average_image.png       # Output: average of all images
├── main.ipynb              # Jupyter Notebook with full analysis
└── main.py                 # Python script version (optional)

## Setup Instructions

1. Clone the repository or download the files.
2. Make sure you have Python 3.7+ installed.
3. Install the required libraries:

pip install numpy pandas matplotlib pillow scikit-learn

4. Run the notebook:

jupyter notebook main.ipynb

Or, run the Python script if you prefer:

python main.py

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Pillow (PIL)
- Scikit-Learn (KMeans)
- Jupyter Notebook

## Example Output

The script produces an average image from all photos and performs clustering on numerical features in the dataset.

## Authors

- Maximus Prime
- Tom

## Notes

- Ensure that the image files are properly formatted (e.g., `.jpg`, `.png`) and located in the correct folder.
- The dataset was provided as part of a course exercise and may require preprocessing for certain analyses.
- Clustering results (e.g., KMeans SSE) may vary depending on initialization and number of iterations.
