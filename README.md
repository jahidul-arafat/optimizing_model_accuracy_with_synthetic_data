# Optimizing Model Accuracy with Synthetic Data for Time Series Anomaly Detection

This project provides a comprehensive framework for leveraging synthetic data to enhance the performance of time series anomaly detection models. The core of this research lies in the strategic generation and integration of synthetic data to address the challenge of data imbalance, where anomalies are rare and difficult to detect. By creating realistic synthetic examples of anomalies, we can train more robust and accurate models that are better equipped to identify real-world anomalies.

## Project Overview

This repository is the official implementation of the research paper, "Optimizing Model Convergence and Accuracy in Time Series Anomaly Detection using Synthetic Data Integration and Rolling Window Stratified Cross." The project delves into the application of deep learning techniques for synthetic data generation and proposes a novel methodology for their integration into the model training pipeline.

The primary objectives of this research are:

*   **To explore the efficacy of various synthetic data generation models**, with a focus on Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs), for creating high-fidelity time series data.
*   **To introduce a novel rolling window stratified cross-validation strategy** that effectively integrates synthetic data into the training process, ensuring that the model learns from a balanced and representative dataset.
*   **To conduct a rigorous evaluation of the proposed approach** on a diverse set of real-world time series datasets, demonstrating its superiority over traditional methods.
*   **To provide an open-source and reproducible implementation** of the proposed methods, enabling other researchers and practitioners to build upon this work.

## Getting Started

### Prerequisites

*   Python 3.6 or higher
*   Jupyter Notebook or JupyterLab

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/optimizing_model_accuracy_with_synthetic_data.git
    cd optimizing_model_accuracy_with_synthetic_data
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    The project's dependencies are listed in the `requirements.txt` file. You can install them using pip:

    ```bash
    pip install -r requirements.txt
    ```

    If the `requirements.txt` file is not available, you can create it from the project's dependencies:

    ```bash
    pip freeze > requirements.txt
    ```

    The key dependencies are:

    *   `pandas`
    *   `numpy`
    *   `tensorflow`
    *   `scikit-learn`
    *   `matplotlib`
    *   `seaborn`
    *   `jupyter`

## Usage

The project's workflow is primarily managed through a series of Jupyter notebooks. To get started, launch the Jupyter Notebook or JupyterLab server:

```bash
jupyter notebook
```

Here is a breakdown of the key notebooks and their roles:

*   **`synthetic_data_qa.ipynb`**: This is the central notebook of the project. It guides you through the entire process of loading and preprocessing the data, training the synthetic data generation models, creating synthetic data, and finally, training and evaluating the anomaly detection models. It is recommended to run the cells in this notebook sequentially to understand the complete workflow.

*   **`loss_analysis.ipynb` and `loss-analysis.ipynb`**: These notebooks are dedicated to the analysis of the model's loss functions. They provide insights into the training dynamics and convergence of the models. The outputs of these notebooks are the loss plots saved in the `data/` and `data_test/` directories.

*   **`confusion_matrix.ipynb`**: This notebook focuses on the evaluation of the anomaly detection models. It contains the code to generate confusion matrices, which are essential for understanding the model's performance in terms of true positives, true negatives, false positives, and false negatives.

*   **`failure-taxonomy-pic.ipynb`**: This notebook is used to generate a visual representation of the failure taxonomy of different anomaly detection models. This helps in understanding the common pitfalls and limitations of various models.

## Project Structure

```
.
├── data
│   └── ... (Loss plots and other generated images)
├── data_test
│   └── ... (Loss plots and other generated images for testing)
├── loss
│   └── ... (Saved loss values from model training)
├── paper
│   └── ... (Research paper and related documents)
├── simulation results
│   └── ... (Confusion matrices, performance metrics, and loss plots)
├── .gitignore
├── confusion_matrix.ipynb
├── failure-taxonomy-pic.ipynb
├── loss_analysis.ipynb
├── loss-analysis.ipynb
├── main.py
├── README.md
└── synthetic_data_qa.ipynb
```

## Results and Findings

The comprehensive results of this research are detailed in the paper located in the `paper/` directory. The `simulation results/` directory provides a wealth of supplementary materials, including:

*   **Confusion matrices** for various models, offering a granular view of their classification performance.
*   **Performance metrics** such as precision, recall, and F1-score, which provide a quantitative measure of the models' accuracy.
*   **Training and validation loss curves**, which illustrate the learning process and help diagnose potential issues like overfitting.

The key takeaway from this research is that the strategic use of synthetic data, combined with the proposed rolling window stratified cross-validation technique, can significantly improve the accuracy and robustness of time series anomaly detection models.

## Contributing

We welcome contributions from the community. If you would like to contribute to the project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with a clear and descriptive commit message.
4.  Push your changes to your fork.
5.  Create a pull request to the main repository.

Before submitting a pull request, please ensure that your code adheres to the existing code style and that all tests pass.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
