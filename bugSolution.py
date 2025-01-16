import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def function_with_improved_error_handling(data):
    try:
        result = data[0] / data[1]
        return result
    except ZeroDivisionError as e:
        logging.error(f"ZeroDivisionError occurred: {e}")
        return f"Division by zero: {e}"
    except IndexError as e:
        logging.error(f"IndexError occurred: {e}")
        return f"Index out of range: {e}"
    except TypeError as e:
        logging.error(f"TypeError occurred: {e}")
        return f"Type error: {e}"
    except Exception as e:
        logging.exception(f"An unexpected error occurred: {e}")
        return f"An unexpected error occurred: {e}"

# Example Usage
data = [10, 0]
data2 = [10]
data3 = [10, 'a']

print(function_with_improved_error_handling(data))
print(function_with_improved_error_handling(data2))
print(function_with_improved_error_handling(data3))