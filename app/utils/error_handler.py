def console_error_handler(error: Exception, file: str, funtion: str):
    print(f"! Error in {file} -> {funtion}:\n")
    print(error)
    return None
