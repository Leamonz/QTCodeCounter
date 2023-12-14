extensions = {'.c', '.cpp', '.h', '.hpp', '.java', '.py', '.js'}
# 分类统计
languageExtensionsMap = {
    'C': {'.c'},
    'Header': {'.h', '.hpp'},
    'Cpp': {'.cpp'},
    'Java': {'.java'},
    'Python': {'.py'},
    'Javascript': {'.js'}
}
availableEncodings = ['utf-8', 'gbk', 'GB2312', 'ISO-8859-1']
errorFiles = []
INF = 1e4


def countLines(filename):
    count = 0
    for i, encoding in enumerate(availableEncodings):
        try:
            with open(filename, 'r', encoding=encoding) as f:
                lines = f.readlines()
                count += len(lines)
        except Exception as e:
            continue
        if count != 0:
            break
    return count
