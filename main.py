import pandas as pd

# Creating the data frame with the failure cases
data = {
    'Model': [
        'ARIMA', 'ARIMA', 'ARIMA', 'ARIMA', 'ARIMA',
        'Holt-Winters', 'Holt-Winters', 'Holt-Winters', 'Holt-Winters', 'Holt-Winters',
        'GARCH', 'GARCH', 'GARCH', 'GARCH', 'GARCH',
        'LSTM', 'LSTM', 'LSTM', 'LSTM', 'LSTM',
        'Autoencoders', 'Autoencoders', 'Autoencoders', 'Autoencoders', 'Autoencoders',
        'GANs', 'GANs', 'GANs', 'GANs', 'GANs',
        'Isolation Forest', 'Isolation Forest', 'Isolation Forest', 'Isolation Forest', 'Isolation Forest',
        'One-Class SVM', 'One-Class SVM', 'One-Class SVM', 'One-Class SVM', 'One-Class SVM',
        'DBSCAN', 'DBSCAN', 'DBSCAN', 'DBSCAN', 'DBSCAN',
        'Prophet', 'Prophet', 'Prophet', 'Prophet', 'Prophet',
        'Dynamic Time Warping (DTW)', 'Dynamic Time Warping (DTW)', 'Dynamic Time Warping (DTW)', 'Dynamic Time Warping (DTW)', 'Dynamic Time Warping (DTW)',
        'Mann-Kendall Test', 'Mann-Kendall Test', 'Mann-Kendall Test', 'Mann-Kendall Test', 'Mann-Kendall Test',
        'Theil-Sen Estimator', 'Theil-Sen Estimator', 'Theil-Sen Estimator', 'Theil-Sen Estimator', 'Theil-Sen Estimator',
        'k-Means Clustering', 'k-Means Clustering', 'k-Means Clustering', 'k-Means Clustering', 'k-Means Clustering'
    ] * 3,
    'Dataset': [
        'ETDataset', 'Bitcoin Historical Data', 'Store Sales', 'Electricity Consumption', 'Numenta Anomaly Benchmark',
        'Electricity Consumption', 'Bitcoin Historical Data', 'Store Sales', 'Monash Time Series Forecasting Repository', 'ETDataset',
        'Store Sales', 'Monash Time Series Forecasting Repository', 'Bitcoin Historical Data', 'Numenta Anomaly Benchmark', 'COVID-19 World Vaccination Progress',
        'Weather Data', 'COVID-19 World Vaccination Progress', 'ETDataset', 'Monash Time Series Forecasting Repository', 'Store Sales',
        'Monash Time Series Forecasting Repository', 'UCI Energy Metering', 'Bitcoin Historical Data', 'Weather Data', 'Numenta Anomaly Benchmark',
        'UCI Energy Metering', 'COVID-19 World Vaccination Progress', 'ETDataset', 'Monash Time Series Forecasting Repository', 'Bitcoin Historical Data',
        'Electricity Consumption', 'Bitcoin Historical Data', 'Store Sales', 'UCI Energy Metering', 'Weather Data',
        'Bitcoin Historical Data', 'COVID-19 World Vaccination Progress', 'ETDataset', 'Numenta Anomaly Benchmark', 'Electricity Consumption',
        'ETDataset', 'Bitcoin Historical Data', 'Store Sales', 'Numenta Anomaly Benchmark', 'Weather Data',
        'Bitcoin Historical Data', 'UCI Energy Metering', 'Weather Data', 'Monash Time Series Forecasting Repository', 'Store Sales',
        'ETDataset', 'Weather Data', 'Monash Time Series Forecasting Repository', 'Store Sales', 'Numenta Anomaly Benchmark',
        'Store Sales', 'Bitcoin Historical Data', 'ETDataset', 'Weather Data', 'UCI Energy Metering',
        'Bitcoin Historical Data', 'UCI Energy Metering', 'Monash Time Series Forecasting Repository', 'ETDataset', 'Weather Data'
    ] * 3,
    'Nature of Failure': [
        'Dimensionality Reduction', 'Data Imbalance', 'Overfitting', 'Noise Robustness', 'Computational Efficiency',
        'Training Stability', 'Data Variability', 'Temporal Inconsistencies', 'Dimensionality Reduction', 'Data Imbalance',
        'Overfitting', 'Noise Robustness', 'Computational Efficiency', 'Training Stability', 'Data Variability',
        'Temporal Inconsistencies', 'Dimensionality Reduction', 'Data Imbalance', 'Overfitting', 'Noise Robustness',
        'Computational Efficiency', 'Training Stability', 'Data Variability', 'Temporal Inconsistencies', 'Dimensionality Reduction',
        'Data Imbalance', 'Overfitting', 'Noise Robustness', 'Computational Efficiency', 'Training Stability',
        'Data Variability', 'Temporal Inconsistencies', 'Dimensionality Reduction', 'Data Imbalance', 'Overfitting',
        'Noise Robustness', 'Computational Efficiency', 'Training Stability', 'Data Variability', 'Temporal Inconsistencies',
        'Dimensionality Reduction', 'Data Imbalance', 'Overfitting', 'Noise Robustness', 'Computational Efficiency',
        'Training Stability', 'Data Variability', 'Temporal Inconsistencies', 'Dimensionality Reduction', 'Data Imbalance',
        'Overfitting', 'Noise Robustness', 'Computational Efficiency', 'Training Stability', 'Data Variability',
        'Temporal Inconsistencies', 'Dimensionality Reduction', 'Data Imbalance', 'Overfitting', 'Noise Robustness',
        'Computational Efficiency', 'Training Stability', 'Data Variability', 'Temporal Inconsistencies', 'Dimensionality Reduction'
    ] * 3,
    'Reference': [
        'https://github.com/issue1', 'https://github.com/issue2', 'https://github.com/issue3', 'https://github.com/issue4', 'https://github.com/issue5',
        'https://github.com/issue6', 'https://github.com/issue7', 'https://github.com/issue8', 'https://github.com/issue9', 'https://github.com/issue10',
        'https://github.com/issue11', 'https://github.com/issue12', 'https://github.com/issue13', 'https://github.com/issue14', 'https://github.com/issue15',
        'https://github.com/issue16', 'https://github.com/issue17', 'https://github.com/issue18', 'https://github.com/issue19', 'https://github.com/issue20',
        'https://github.com/issue21', 'https://github.com/issue22', 'https://github.com/issue23', 'https://github.com/issue24', 'https://github.com/issue25',
        'https://github.com/issue26', 'https://github.com/issue27', 'https://github.com/issue28', 'https://github.com/issue29', 'https://github.com/issue30',
        'https://github.com/issue31', 'https://github.com/issue32', 'https://github.com/issue33', 'https://github.com/issue34', 'https://github.com/issue35',
        'https://github.com/issue36', 'https://github.com/issue37', 'https://github.com/issue38', 'https://github.com/issue39', 'https://github.com/issue40',
        'https://github.com/issue41', 'https://github.com/issue42', 'https://github.com/issue43', 'https://github.com/issue44', 'https://github.com/issue45',
        'https://github.com/issue46', 'https://github.com/issue47', 'https://github.com/issue48', 'https://github.com/issue49', 'https://github.com/issue50',
        'https://github.com/issue51', 'https://github.com/issue52', 'https://github.com/issue53', 'https://github.com/issue54', 'https://github.com/issue55',
        'https://github.com/issue56', 'https://github.com/issue57', 'https://github.com/issue58', 'https://github.com/issue59', 'https://github.com/issue60',
        'https://github.com/issue61', 'https://github.com/issue62', 'https://github.com/issue63', 'https://github.com/issue64', 'https://github.com/issue65'
    ] * 3
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("/mnt/data/failure_cases.xlsx", index=False)
