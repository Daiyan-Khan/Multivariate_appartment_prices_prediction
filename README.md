# Multivariate Linear Regression with Feature Scaling

This repository contains an implementation of multivariate linear regression with feature scaling in Python. The code demonstrates how to perform gradient descent optimization to find the best-fit hyperplane for predicting house prices based on multiple features. It also includes feature scaling using z-score normalization to ensure that the features are on a similar scale.

## Requirements

- pandas
- numpy
- matplotlib
- scikit-learn

You can install the required packages by running the following command:
pip install pandas numpy matplotlib scikit-learn


## Usage

1. Clone the repository or download the `linear_regression.py` file.

2. Make sure you have a CSV file (`Daegu_Real_Estate_data.csv`) containing the dataset you want to use for regression. Adjust the file path in the code if necessary.

3. Run the script using a Python interpreter:
python linear_regression.py

4. The script will output the calculated weights and intercept for the linear regression model, as well as the mean absolute error (MAE), mean squared error (MSE), root mean squared error (RMSE), and explained variance score (VarScore) for the predictions on the test data.

5. Additionally, a scatter plot will be displayed showing the predicted prices versus the actual prices for the test data.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


