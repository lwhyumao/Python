import xlrd


class excelGuide:
    # 获取表格数据
    def __init__(self, excel_Name=input()):
        print("请输入需要导出表格的名字")
        try:
            self.excel_data = xlrd.open_workbook(excel_Name)
        except FileNotFoundError:
            print("表格名字不正确")
    # 获取工作薄数据
    def sheet_Data(self,sheet_name = input()):
        print("请输入需要导出的表格工作薄名字")
        try:
            self.sheet_Data = self.excel_data.sheet_names(sheet_name)
        except FileNotFoundError:
            print("工作薄名字不正确")

    # 获取工作薄表头，获取第一行数据
    def sheet_Header(self):
        self.sheet_Data


d = excelGuide()
d.sheet_Data()

