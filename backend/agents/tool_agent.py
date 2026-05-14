from tools.calculator import calculator
from tools.file_tool import read_file


def execute_tool(tool_name, tool_input):

    if tool_name == "calculator":
        return calculator(tool_input)

    if tool_name == "file_reader":
        return read_file(tool_input)

    return "Unknown tool"