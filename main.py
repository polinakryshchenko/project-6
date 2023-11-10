result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError("a should be greater than or equal to b")
        if b == 0:
            raise ZeroDivisionError("b should not be zero")
        if b > 100:
            raise IndexError("b should not exceed 100")

        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None


#data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
data = {10: 2, 2: 5, "123": 4, 18: 0, tuple(): 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    if res is not None:
        result.append(res)

print(result)