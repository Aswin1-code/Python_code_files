import time
start_time=time.time()

def handle_exceptions():
    print("\t**List of some common errors**\n".title())
    try:
        # ArithmeticError
        result = 1 / 0
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError: {e}")
    print("----")
    
    try:
        # BufferError
        raise BufferError("Buffer error occurred")
    except BufferError as e:
        print(f"BufferError: {e}")
    print("----")
    
    try:
        # EOFError
        raise EOFError("EOF error occurred")
    except EOFError as e:
        print(f"EOFError: {e}")
    print("----")
    
    try:
        # ImportError
        import math  # Example of a valid module
    except ImportError as e:
        print(f"ImportError: {e}")
    print("----")
    
    try:
        # IndexError
        lst = [1, 2, 3]
        print(lst[10])
    except IndexError as e:
        print(f"IndexError: {e}")
    print("----")
    
    try:
        # KeyError
        d = {'key': 'value'}
        print(d['non_existent_key'])
    except KeyError as e:
        print(f"KeyError: {e}")
    print("----")
    
    try:
        # MemoryError
        raise MemoryError("Memory error occurred")
    except MemoryError as e:
        print(f"MemoryError: {e}")
    print("----")
    
    try:
        # NameError
        non_existent_variable = "This variable is now defined"
        print(non_existent_variable)
    except NameError as e:
        print(f"NameError: {e}")
    print("----")
    
    try:
        # OSError
        raise OSError("OS error occurred")
    except OSError as e:
        print(f"OSError: {e}")
    print("----")
    
    try:
        # ReferenceError
        import weakref
        class A:
            pass
        a = A()
        r = weakref.ref(a)
        del a
        print(r())
    except ReferenceError as e:
        print(f"ReferenceError: {e}")
    print("----")
    
    try:
        # RuntimeError
        raise RuntimeError("Runtime error occurred")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
    print("----")
    
    try:
        # StopIteration
        it = iter([1, 2, 3])
        while True:
            print(next(it))
    except StopIteration as e:
        print(f"StopIteration: {e}")
    print("----")
    
    try:
        # SyntaxError
        exec('x === x')
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
    print("----")
    
    try:
        # SystemError
        raise SystemError("System error occurred")
    except SystemError as e:
        print(f"SystemError: {e}")
    print("----")
    
    try:
        # TypeError
        print(str(1) + '1')
    except TypeError as e:
        print(f"TypeError: {e}")
    print("----")
    
    try:
        # ValueError
        int('car')
    except ValueError as e:
        print(f"ValueError: {e}")
    print("----")
    
    try:
        # UnicodeError
        'ascii'.encode('utf-8').decode('ascii')
    except UnicodeError as e:
        print(f"UnicodeError: {e}")

# Call the function to handle exceptions

handle_exceptions()
end_time=time.time()
print(f"Execution time :{end_time-start_time}")