import xlrd


class excelGuide:
    def __init__(self, excel_Name=input()):
        print("请输入需要导出表格的名字")
        try:
            self.excel_data = xlrd.open_workbook(excel_Name)
            return self.excel_data
        except:
            print("")

    def sheet_Data(self):
        self.sheet_Data = self.excel_data.sheet_names()


d = excelGuide()
d.sheet_Data()
