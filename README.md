# Oral Cancer Detection API

This repository contains the code for a server API developed using Django REST framework and TensorFlow. The API accepts an image of a person's mouth, processes it through a machine learning model, and predicts whether the person has oral cancer. The model uses binary classification and employs a combination of ViT, VGG16, VGG19, ResNet50, and EfficientNetB0 for feature extraction.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Model Details](#model-details)
- [License](#license)

## Features

- Accepts images of a person's mouth for analysis.
- Predicts the presence of oral cancer using a binary classification model.
- Utilizes multiple state-of-the-art models for feature extraction.
- Provides a RESTful API for easy integration with other applications.

## Technologies Used

- **Backend:** Django, Django REST framework
- **Machine Learning:** TensorFlow, Keras
- **Feature Extraction Models:** ViT, VGG16, VGG19, ResNet50, EfficientNetB0

## Installation

To set up the API locally, follow these steps:

1. **Clone the repository:**

   sh
   `git clone https://github.com/abhiramrpk/Cancer_API.git
   cd Cancer_API`
   

2. **Create and activate a virtual environment:**

   sh
   `python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate`
   

3. **Install the dependencies:**

   sh
   `pip install -r requirements.txt`
   

4. **Apply database migrations:**

   sh
   `python manage.py migrate`
   

5. **Start the development server:**

   sh
   `python manage.py runserver`
   

6. **Open your web browser and navigate to `http://127.0.0.1:8000`.**

## Usage

To use the API, send a POST request to the `/predict/` endpoint with an image file. The API will return a prediction indicating whether the person has oral cancer.

## API Endpoints

### `/list/`

- **Method:** GET
- **Description:** The endpoint will display all the other available endpints.
  

## Model Details

The machine learning model uses a combination of ViT, VGG16, VGG19, ResNet50, and EfficientNetB0 for feature extraction. These features are then fed into a binary classification model to predict the presence of oral cancer.

- **ViT (Vision Transformer):** Transformer-based model for image classification.
- **VGG16 and VGG19:** Convolutional neural networks known for their depth and simplicity.
- **ResNet50:** Deep residual network that addresses the vanishing gradient problem.
- **EfficientNetB0:** Model that balances performance and efficiency by scaling depth, width, and resolution.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---

Developed with ❤️ to assist in the early detection of oral cancer.
