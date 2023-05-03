import bestv8

js_string = """a = 1;a"""
result = bestv8.eval(js_string, recv_size=200)
print("result:", result, type(result))
