# PyBestV8
PyBestV8 is a Python library based on the [BestV8](https://github.com/BestToYou/bestV8_release) project, which is a fast and easy-to-use JS execution library.

### Installation
```bash
$ pip install PyBestV8
```

or

```bash
$ easy_install PyBestV8
```

### Run
Run JavaScript code from Python.

PyBestV8 is a porting of BestV8 from Ruby. PyBestV8 automatically picks the best runtime available to evaluate your JavaScript program.

A short example:

```python
import bestv8

js_string = """a = 1;a"""
result = bestv8.eval(js_string)
print("result:", result, type(result))

```

or

```python
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

```

### 声明
该调试工具仅供技术人员进行内部测试和分析使用。请勿将其用于非法用途或以任何方式窃取第三方数据。使用该工具产生的所有风险均由用户自行承担，作者不对用户因使用该工具而造成的任何损失或损害承担任何责任。作者不保证该工具的完整性、准确性和适用性，并且可以随时更改或终止该工具的使用。任何个人或组织通过使用该工具造成的侵犯他人权益或违反法律法规的行为，作者概不负责。