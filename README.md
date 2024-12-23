# Fraud Detection Model

This repository contains a fraud detection system designed to identify and adapt to suspicious activities in financial transactions effectively. The project leverages synthetic transaction data, advanced feature engineering, and machine learning models. The solution includes a feedback loop for continuous improvement, ensuring adaptability to evolving fraud patterns.

## Features

1. **Synthetic Data Generation**:
   - Created realistic transaction data using Python libraries like `Faker` and `NumPy`.
   - Simulated real-world behaviors, including high-frequency transactions and time-based anomalies.

2. **Feature Engineering**:
   - Derived features such as account age, transaction frequency, and daily totals.
   - Designed custom rules for identifying suspicious activities (e.g., high-value late-night transactions).

3. **Machine Learning Models**:
   - Developed and evaluated Logistic Regression and XGBoost models.
   - Addressed class imbalance using SMOTE (Synthetic Minority Oversampling Technique).
   - Achieved an AUC of 0.99 and recall of 94% with the XGBoost model.

4. **Feedback Loop Integration**:
   - Incorporated human feedback to update training data and retrain models periodically.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Ccinaza/fraud_detection_model.git
   cd fraud_detection_model
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the notebook to generate synthetic data, engineer features, and train models.
2. Evaluate model performance using provided metrics and visualizations.
3. Save the best-performing model for deployment.

## Dependencies
The project relies on the following Python libraries:
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- imbalanced-learn
- xgboost
- faker

Refer to `requirements.txt` for the complete list of dependencies.

## Results
- Logistic Regression Model: AUC = 0.97, Recall = 92%
- XGBoost Model: AUC = 0.99, Recall = 94%

## Project Structure
- `fraud_detection.ipynb`: Main notebook with code and detailed explanations.
- `requirements.txt`: File listing the required dependencies.
- `synthetic_data.csv`: Generated synthetic transaction data (not included due to size constraints).

## Future Improvements
- Integration with a real-time fraud detection pipeline.
- Expansion of synthetic data to include additional transaction types and patterns.
- Deployment of the model as a web service.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- Open-source contributors for the tools and libraries used.

Feel free to reach out for collaboration or suggestions!

