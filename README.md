---

# Loan Approval Prediction

## Project Overview

This project focuses on predicting loan approvals using machine learning. A Random Forest Classifier is used to achieve a prediction accuracy of 75%. The model has been fine-tuned using hyperparameter tuning techniques to enhance its performance. The dataset used for training was pre-existing, and the model has been saved for deployment.

For deployment, FastAPI has been utilized, and Uvicorn is used to serve the application. This project demonstrates how machine learning models can be seamlessly integrated into a web service using FastAPI.

## Features

- Loan approval prediction with 75% accuracy
- Random Forest Classifier with hyperparameter tuning
- Model deployment using FastAPI and Uvicorn
- Saved model for inference
- REST API for making loan predictions

## Getting Started

### Prerequisites

Before running the project, make sure you have Python 3.x installed on your machine.

### Installation

1. Clone the repository
   
2. Install the required dependencies:
   requirements.txt

3. Run the FastAPI app:
   ```bash
   uvicorn main:app --reload
   ```

### How to Use

Once the FastAPI server is running, you can make predictions by sending POST requests to the API.

Example request:
```bash
POST /predict
{
   "feature1": value1,
   "feature2": value2,
   ...
}
```

The model will respond with whether the loan is approved or not.

## Model Training

The model was trained using a dataset containing various features related to loan applications. A Random Forest Classifier was selected due to its robustness in handling complex datasets. Hyperparameter tuning was applied to optimize the model, and the final accuracy achieved was 75%.

The trained model is saved for inference and can be loaded during API requests to make predictions.

## Requirements

The project requires the following libraries and tools:

```txt
fastapi==0.95.0
uvicorn==0.22.0
scikit-learn==1.2.2
numpy==1.23.4
pandas==1.5.2
```

Make sure to install these dependencies by running `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The dataset was pre-existing and used for training the model.
- FastAPI for providing a lightweight framework for deployment.
- Uvicorn for serving the FastAPI application.

---
