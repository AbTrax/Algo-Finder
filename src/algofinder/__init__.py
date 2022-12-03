"""Tool for getting the best Time Space Complexity of a Algorithm
#TODO : add ranges to the complexity calculation 
#TODO : Add Click to the project or better arg parse 
#TODO : use names to format the changes
#TODO : add a better way to get the complexity of the algorithm or train ML to get the complexity
"""

import argparse
import ast
import io

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
    return loop_count + conditional_count


# Helper function to compute the space complexity of an algorithm from its AST
def compute_space_complexity(ast_node):
    # Count the number of variables and arrays
    variable_count = count_tokens(ast_node, ast.Name)
    array_count = count_tokens(ast_node, ast.Subscript)
    # The space complexity is O(variable_count + array_count)
    return variable_count + array_count


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
            time_complexity = compute_time_complexity(node)
            space_complexity = compute_space_complexity(node)
            algorithms[node.name] = (time_complexity, space_complexity)

    # Print the time and space complexity of each algorithm
    for name, (time_complexity, space_complexity) in algorithms.items():
        print(
            f"Algorithm {name} has time complexity O({time_complexity}) and space complexity O({space_complexity})"
        )

    # Recommend better algorithms based on their time and space complexity
    for name, (time_complexity, space_complexity) in algorithms.items():
        if time_complexity > 1:
            print(f"Consider using a faster algorithm for {name}")
        if space_complexity > 1:
            print(f"Consider using a more memory-efficient algorithm for {name}")


# Main function that uses argparse to parse the command line arguments
def main():
    # Define the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="the path to the Python file to Check")

    # Parse the command line arguments
    args = parser.parse_args()
    filepath = args.filepath

    # Analyze the complexity of the algorithms in the given Python file
    analyze_complexity(filepath)


if __name__ == "__main__":
    main()
