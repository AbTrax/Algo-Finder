"""Tool for getting the best Time Space Complexity of a Algorithm"""

import ast
import io
import joblib
import click
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Helper function to count the number of occurrences of a given token in the AST
def count_tokens(ast_node, token):
    token_count = 0
    for node in ast.walk(ast_node):
        if isinstance(node, ast.AST):
            token_count += 1
    return token_count


# Helper function to compute the time complexity of an algorithm from its AST
def compute_time_complexity(ast_node):
    # Count the number of loop and conditional statements
    loop_count = count_tokens(ast_node, ast.For) + count_tokens(ast_node, ast.While)
    conditional_count = count_tokens(ast_node, ast.If)
    # The time complexity is O(loop_count * conditional_count)
    return loop_count + conditional_count, (loop_count, conditional_count)


# Helper function to compute the space complexity of an algorithm from its AST
def compute_space_complexity(ast_node):
    # Count the number of variables and arrays
    variable_count = count_tokens(ast_node, ast.Name)
    array_count = count_tokens(ast_node, ast.Subscript)
    # The space complexity is O(variable_count + array_count)
    return variable_count + array_count, (variable_count, array_count)


# Function to train a machine learning model for complexity prediction
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model Mean Squared Error: {mse}")
    return model


# Function to predict time and space complexity using the trained model
def predict_complexity(model, features):
    return model.predict([features])[0]


# Main function that analyzes the time and space complexity of the algorithms
# in a Python file and recommends better algorithms
def analyze_complexity(filepath):
    # Parse the Python file into an AST
    with open(filepath, "r") as f:
        code = f.read()
    ast_node = ast.parse(code)

    # Compute the time and space complexity of each algorithm
    algorithms = {}
    for node in ast.walk(ast_node):
        if isinstance(node, ast.FunctionDef):
            time_complexity, time_range = compute_time_complexity(node)
            space_complexity, space_range = compute_space_complexity(node)
            algorithms[node.name] = (time_complexity, space_complexity, time_range, space_range)

    # Print the time and space complexity of each algorithm
    for name, (time_complexity, space_complexity, time_range, space_range) in algorithms.items():
        print(
            f"Algorithm {name} has time complexity O({time_complexity}) (range: {time_range}) and space complexity O({space_complexity}) (range: {space_range})"
        )

    # Recommend better algorithms based on their time and space complexity
    for name, (time_complexity, space_complexity, _, _) in algorithms.items():
        if time_complexity > 1:
            print(f"Consider using a faster algorithm for {name}")
        if space_complexity > 1:
            print(f"Consider using a more memory-efficient algorithm for {name}")


# Main function that uses Click to parse the command line arguments
@click.command()
@click.argument("filepath")
def main(filepath):
    # Analyze the complexity of the algorithms in the given Python file
    analyze_complexity(filepath)


if __name__ == "__main__":
    main()
