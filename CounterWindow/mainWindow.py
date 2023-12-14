import os
import datetime
import time
import numpy as np

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow

from CounterWindow.CounterWindow import Ui_MainWindow
from SaveDialog.childSaveDialog import SaveDialog
from utils import *

INF = int(1e4)

import sys

isDebug = True if sys.gettrace() else False
if isDebug:
    print("debug mode is on")
else:
    print("debug mode is off")


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        # PyQT渲染页面控件
        self.setupUi(self)  # 渲染页面控件
        # 初始化一些变量
        self.languageStats = {}
        self.model = None
        self.loggingCursor = None
        self.exportUtil = ExportUtils()
        self.functionUtil = FunctionUtil()
        self.saveDialog = SaveDialog()
        # 初始化页面和程序
        self.setWindowTitle("✨Code Counter✨")
        self.setCentralWidget(self.verticalLayoutWidget)
        self.connectSignals()  # 设置信号槽
        self.createTable()
        self.initDateEdit()

    def connectSignals(self):
        """
        连接信号与槽函数
        :return:
        """
        self.startButton.clicked.connect(self.onPushStartButton)
        self.SelectDirButton.clicked.connect(self.onPushSelectDirButton)
        self.saveResultButton.clicked.connect(self.onSaveResultButton)
        self.actionInfo.triggered.connect(self.onTriggerInfoAction)

    def createTable(self):
        """
        初始化数据表（用于显示统计结果）
        :return:
        """
        self.model = QStandardItemModel(0, 7)
        self.model.setHorizontalHeaderLabels(
            ['Language', 'Files', 'Lines', 'Functions',
             'Function Max', 'Function Min', 'Functions Avg.', 'Functions Med.'])
        self.resultTable.setModel(self.model)
        self.resultTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.resultTable.resizeColumnsToContents()
        self.resultTable.resizeRowsToContents()
        self.resultTable.setShowGrid(True)

    def initDateEdit(self):
        """
        初始化日期选择组件
        :return:
        """
        self.startDateEdit.setCalendarPopup(True)
        self.endDateEdit.setCalendarPopup(True)
        self.endDateEdit.setDate(datetime.datetime.now())

    def onTriggerInfoAction(self):
        """
        Info消息
        :return:
        """
        QtWidgets.QMessageBox.information(self, "About Us", "这是一个用于统计代码量的小工具",
                                          QtWidgets.QMessageBox.StandardButton.Ok)

    def onPushSelectDirButton(self):
        """
        打开File Dialog选择目录
        :return:
        """
        selectedDir = QtWidgets.QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.SelectDirText.setText(selectedDir)

    def onPushStartButton(self):
        """
        开始统计的按钮，点击后开始统计过程
        :return:
        """
        print("Start Button")
        checkBoxes = self.findChildren(QtWidgets.QCheckBox)
        languages = []
        for checkbox in checkBoxes:
            if checkbox.isChecked():
                languages.append(checkbox.text())
        code_dir = self.SelectDirText.text()
        if not code_dir:
            QtWidgets.QMessageBox.warning(self, "警告", "请选择要统计的文件夹",
                                          QtWidgets.QMessageBox.StandardButton.Ok)
        elif not languages:
            QtWidgets.QMessageBox.warning(self, "警告", "请选择要统计的语言",
                                          QtWidgets.QMessageBox.StandardButton.Ok)
        else:
            QtWidgets.QMessageBox.information(self, "提示", "开始统计！",
                                              QtWidgets.QMessageBox.StandardButton.Ok)
            languageDict = {lang: languageExtensionsMap[lang] for lang in languages}
            languageExtensionsInverseMap = {}
            for lang, extensions in languageDict.items():
                for extension in extensions:
                    languageExtensionsInverseMap[extension] = lang
            self.languageStats = {}
            for lang in languageDict.keys():
                # 文件个数、代码行数、函数个数、函数行数最大值、函数行数最小值、函数行数平均值、函数行数中位数
                self.languageStats[lang] = ([0, 0, 0, -INF, INF, 0, 0])
            self.updateTable(self.languageStats)
            print("start counting")
            start = time.time()
            self.startCounting(self.languageStats, languageExtensionsInverseMap)
            end = time.time()
            QtWidgets.QMessageBox.information(self,
                                              "提示",
                                              "此次统计总用时:\n" + time.strftime("%H:%M:%S", time.gmtime(end - start)),
                                              QtWidgets.QMessageBox.StandardButton.Ok)

    def startCounting(self, languageStats, langExtsInvMap):
        """
        代码统计函数
        :param languageStats: 各语言代码统计结果，初始化全为0
        :param langExtsInvMap: 语言与文件后缀的映射
        :return:
        """
        self.loggingBrowser.clear()
        startTime = self.startDateEdit.date().toPyDate()
        endTime = self.endDateEdit.date().toPyDate()
        self.loggingBrowser.clearHistory()
        code_dir = self.SelectDirText.text()
        languageFunctionsLists = {}
        for key in languageStats.keys():
            languageFunctionsLists[key] = np.asarray([])
        for root, dirs, files in os.walk(code_dir):
            for file in files:
                filename = os.path.join(root, file)
                mtime = os.path.getmtime(filename)
                timeList = datetime.datetime.fromtimestamp(int(mtime)).strftime("%Y-%m-%d").split('-')
                mtimeDate = datetime.date(int(timeList[0]), int(timeList[1]), int(timeList[2]))
                if mtimeDate < startTime or mtimeDate > endTime:
                    continue
                message = filename
                extension = os.path.splitext(filename)[-1].lower()
                if extension in extensions:
                    try:
                        # 获取文件对应语言
                        language = langExtsInvMap[extension]
                        # 文件数
                        languageStats[language][0] += 1
                        # 代码行数
                        languageStats[language][1] += countLines(filename)
                        # 返回的是 filename 文件中所有函数的行数
                        # lineList = countFunc(filename)
                        lineList = getattr(self.functionUtil, f"count{language.title()}Function")(filename)
                        languageFunctionsLists[language] = np.concatenate([languageFunctionsLists[language], lineList])
                    except Exception as e:
                        message = str(e)
                    self.log(message)
        with open("../err.txt", 'w') as err_f:
            err_f.writelines(errorFiles)
        # 计算最值、平均数和中位数
        self.updateFunctionStats(languageStats, languageFunctionsLists)
        self.updateTable(languageStats)

    def updateFunctionStats(self, languageStats, languageFunctionsList):
        """
        更新函数统计数据
        :param languageStats: 各语言代码统计结果
        :param languageFunctionsList: 各语言所有代码文件中所有函数的行数数据
        :return:
        """
        for key in languageStats.keys():
            if not languageFunctionsList[key].size:
                continue
            # 函数个数
            languageStats[key][2] = languageFunctionsList[key].size
            # 函数最大值
            languageStats[key][3] = np.max(languageFunctionsList[key]).astype(int)
            # 函数最小值
            languageStats[key][4] = np.min(languageFunctionsList[key]).astype(int)
            # 函数平均值
            languageStats[key][5] = np.round(np.mean(languageFunctionsList[key]), 2)
            # 函数中位数
            functionList = languageFunctionsList[key]
            functionList.sort()
            size = len(functionList)
            median = functionList[size // 2] if size % 2 == 0 else (functionList[size // 2] +
                                                                    functionList[size // 2 + 1]) / 2
            languageStats[key][6] = np.round(median, 2)

    def updateTable(self, languageStats):
        """
        更新统计结果并显示到数据表上
        :param languageStats: 各语言统计结果
        :return:
        """
        print("update table")
        for idx, item in enumerate(languageStats.items()):
            tableItems = [QStandardItem(item[0])]
            for j in range(len(item[1])):
                tableItems.append(QStandardItem(str(item[1][j])))
            for i in range(len(tableItems)):
                tableItems[i].setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                self.model.setItem(idx, i, tableItems[i])

    def log(self, message):
        """
        打印信息到TextEdit中
        :param message:
        :return:
        """
        self.loggingBrowser.append(message)
        self.loggingCursor = self.loggingBrowser.textCursor()
        self.loggingBrowser.moveCursor(self.loggingCursor.End)
        QtWidgets.QApplication.processEvents()

    def getDataFromTableModel(self):
        """
        从数据表中获取统计数据
        :return:
        """
        headerCount = self.model.columnCount()
        labels = [self.model.headerData(i, QtCore.Qt.Orientation.Horizontal) for i in range(headerCount)]
        print(labels)
        data = {}
        for label in labels:
            data[label] = []
        for key, value in self.languageStats.items():
            data["Language"].append(key)
            print(value)
            for idx, dataKey in enumerate(labels[1:]):
                data[dataKey].append(value[idx])
        return data

    def onSaveResultButton(self):
        """
        保存结果的按钮，点击后打开新的对话框，选择保存的文件类型
        :return:
        """
        if self.model.rowCount() == 0:
            QtWidgets.QMessageBox.warning(self, "警告", "请先进行统计再保存结果！",
                                          QtWidgets.QMessageBox.StandardButton.Ok)
        else:
            self.saveDialog.exec_()
            checkboxes = self.saveDialog.findChildren(QtWidgets.QCheckBox)
            fileType = []
            for checkbox in checkboxes:
                if checkbox.isChecked():
                    fileType.append(checkbox.text())
            try:
                data = self.getDataFromTableModel()
                savedir = self.saveDialog.saveDirEdit.text()
                if not savedir:
                    raise ValueError(f"'{savedir}' 路径不存在")
                for type in fileType:
                    savepath = os.path.join(savedir, "result." + type)
                    getattr(self.exportUtil, f"export{type.title()}File")(data, savepath)
            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "警告", str(e),
                                              QtWidgets.QMessageBox.StandardButton.Ok)
                print(str(e))
            QtWidgets.QMessageBox.information(self, "提示", "结果导出成功！",
                                              QtWidgets.QMessageBox.StandardButton.Ok)
