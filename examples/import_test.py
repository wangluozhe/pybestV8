import bestv8

js_string = """
function get_location(){
    return location;
}
"""

ctx = bestv8.compile(js_string)
ctx.bestv8_import("import_test.js")
result = ctx.call("get_location")
print("import->result:", result, type(result))
