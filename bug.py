def function_with_uncommon_error(data):
    try:
        result = data[0] / data[1]
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except IndexError:
        return "Index out of range"
    except TypeError:
        return "Type error"

# Uncommon Error: The function silently handles errors without providing specific information about the failure. This makes debugging difficult as it doesn't clearly indicate which specific exception occurred or at what point in the data.  
data = [10, 0] # will cause ZeroDivisionError
data2 = [10] # will cause IndexError
data3 = [10, 'a'] # will cause TypeError

print(function_with_uncommon_error(data))
print(function_with_uncommon_error(data2))
print(function_with_uncommon_error(data3))