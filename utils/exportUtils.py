import pandas as pd
import json
import xml.etree.ElementTree as ET
import yaml


class ExportUtils:
    def __init__(self):
        pass

    def exportCsvFile(self, data, savepath):
        resultDF = pd.DataFrame(data)
        resultDF.to_csv(savepath, index=False)

    def exportXlsxFile(self, data, savepath):
        resultDF = pd.DataFrame(data)
        resultDF.to_excel(savepath, index=False)

    def exportJsonFile(self, data, savepath):
        jsonData = {}
        strKeys = list(map(str, data.keys()))
        for idx, language in enumerate(data["Language"]):
            jsonData[language] = {}
            for key in strKeys[1:]:
                jsonData[language][key] = str(data[key][idx])
        with open(savepath, "w", encoding="utf-8") as f:
            json.dump(jsonData, f, ensure_ascii=False, indent=4)

    def exportXmlFile(self, data, savepath):
        root = ET.Element("Results")
        strKeys = list(map(str, data.keys()))
        for idx, language in enumerate(data["Language"]):
            record = ET.SubElement(root, "Record")
            languageNode = ET.SubElement(record, "Language")
            languageNode.text = language
            for key in strKeys[1:]:
                node = ET.SubElement(record, key.replace(" ", "_"))
                node.text = str(data[key][idx])
        tree = ET.ElementTree(root)
        tree.write(savepath)

    def exportYamlFile(self, data, savepath):
        yamlData = {}
        strKeys = list(map(str, data.keys()))
        for idx, language in enumerate(data["Language"]):
            yamlData[language] = {}
            for key in strKeys[1:]:
                yamlData[language][key] = str(data[key][idx])
        with open(savepath, "w", encoding="utf-8") as f:
            yaml.dump(yamlData, f)
