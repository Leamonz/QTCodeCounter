import re
import numpy as np


class FunctionUtil:
    def __init__(self):
        pass

    def countCFunction(self, filepath):
        regexBegin = r'(\w+\s+)*\w*\([^)]*\)\s*\{'
        pattern = re.compile(regexBegin)
        codeContent = ""
        beginIndices = []
        with open(filepath, "r") as f:
            codeContent = "".join(f.readlines())
        # for match in re.finditer(regexBegin, codeContent):
        for match in pattern.finditer(codeContent):
            beginIndices.append(match.end())
        lineList = []
        for idx in beginIndices:
            cnt = 0
            stack = ['{']
            while stack:
                cnt += 1 if codeContent[idx] == '\n' else 0
                if codeContent[idx] == '{':
                    stack.append('{')
                elif codeContent[idx] == '}':
                    stack.pop(-1)
                idx += 1
            lineList.append(cnt)
        return np.asarray(lineList)

    def countCppFunction(self, filepath):
        regexBegin = r'(\w+\s+)*\w*\([^)]*\)\s*\{'
        pattern = re.compile(regexBegin)
        codeContent = ""
        beginIndices = []
        with open(filepath, "r") as f:
            codeContent = "".join(f.readlines())
        # for match in re.finditer(regexBegin, codeContent):
        for match in pattern.finditer(codeContent):
            beginIndices.append(match.end())
        lineList = []
        for idx in beginIndices:
            cnt = 0
            stack = ['{']
            while stack:
                cnt += 1 if codeContent[idx] == '\n' else 0
                if codeContent[idx] == '{':
                    stack.append('{')
                elif codeContent[idx] == '}':
                    stack.pop(-1)
                idx += 1
            lineList.append(cnt)
        return np.asarray(lineList)

    def countJavaFunction(self, filepath):
        regexBegin = r'(public|private)(\s+\w+)*\s+(\w+)*\s*\w+\([^)]*\)\s*(throws\s+([\w,])+)*\s*\{'
        pattern = re.compile(regexBegin)
        codeContent = ""
        beginIndices = []
        with open(filepath, "r") as f:
            codeContent = "".join(f.readlines())
        # for match in re.finditer(regexBegin, codeContent):
        for match in pattern.finditer(codeContent):
            beginIndices.append(match.end())
        lineList = []
        for idx in beginIndices:
            cnt = 0
            stack = ['{']
            while stack:
                cnt += 1 if codeContent[idx] == '\n' else 0
                if codeContent[idx] == '{':
                    stack.append('{')
                elif codeContent[idx] == '}':
                    stack.pop(-1)
                idx += 1
            lineList.append(cnt)
        return np.asarray(lineList)

    def countPythonFunction(self, filepath):
        regexBegin = r'def\s+\w+\([^)]*\)\s*:'
        pattern = re.compile(regexBegin)
        codeContent = ""
        beginIndices = []
        endIndices = []
        with open(filepath, "r", encoding='utf-8') as f:
            codeContent = "".join(f.readlines())
        # for match in re.finditer(regexBegin, codeContent):
        for match in pattern.finditer(codeContent):
            beginIndices.append(match.start())
            endIndices.append(match.end())
        lineList = []
        for i in range(len(beginIndices)):
            min_indent = 0
            ind = beginIndices[i]
            # 计算函数起始位置的缩进数量
            while ind > 0 and codeContent[ind] != '\n':
                min_indent += 1 if codeContent[ind] == ' ' and (
                        codeContent[ind - 1] == ' ' or codeContent[ind - 1] == '\n') else 0
                ind -= 1
            # 开始统计行数
            indent = 0
            cnt = 1
            idx = endIndices[i] + 1
            while idx < len(codeContent):
                indent += 1 if codeContent[idx] == ' ' and (
                        codeContent[idx - 1] == ' ' or codeContent[idx - 1] == '\n') else 0
                if codeContent[idx] == '\n':
                    cnt += 1
                    # 缩进数量≤起始位置的缩进数量，那么就退出
                    if indent <= min_indent:
                        break
                    indent = 0
                idx += 1
            lineList.append(cnt)
        return np.asarray(lineList)

    def countHeaderFunction(self, filepath):
        raise NotImplementedError

    def countJavascriptFunction(self, filepath):
        raise NotImplementedError
