import bestv8

js_string = """
a = 1;
b = 2;
function abc(){
    a += 1;
    b += 2;
    return {
        name: "lisa",
        age: 18
    }
}
function bcd(){
    return [a, b];
}
"""
ctx = bestv8.compile(js_string)
result = ctx.call("bcd")
print("bcd->result:", result, type(result))
result = ctx.call("abc")
print("abc->result:", result, type(result))
result = ctx.call("bcd")
print("bcd->result:", result, type(result))
