import matplotlib
matplotlib.use('Agg')  # Important for Flask server
import matplotlib.pyplot as plt
import os
import uuid

def create_soil_nutrient_graph(N, P, K, upload_folder='static'):
    """
    Create and save a soil nutrient distribution graph.
    
    Parameters:
    - N: Nitrogen value
    - P: Phosphorus value
    - K: Potassium value
    - upload_folder: where to save the image

    Returns:
    - filename of the saved graph image
    """

    # Nutrient names and values
    nutrients = ['Nitrogen', 'Phosphorus', 'Potassium']
    values = [float(N), float(P), float(K)]

    # Create the plot
    plt.figure(figsize=(6,4))
    plt.bar(nutrients, values, color=['green', 'blue', 'orange'])
    plt.title('Soil Nutrient Distribution')
    plt.ylabel('Amount')
    plt.ylim(0, max(values) + 20)

    # Save the plot
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join(upload_folder, filename)
    plt.savefig(filepath)
    plt.close()

    return filename
