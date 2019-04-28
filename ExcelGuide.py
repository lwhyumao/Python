import xlrd


class excelGuide:
    # 获取表格数据
    def __init__(self, excel_Name=input()):
        print("请输入需要导出表格的名字")
        try:
            self.excel_data = xlrd.open_workbook(excel_Name)
        except:
            print("表格名字不正确")
    # 获取工作薄数据
    def sheet_Data(self,sheet_name = input()):
        print("请输入需要导出的表格工作薄名字")
        try:
            self.sheet_Data = self.excel_data.sheet_names(sheet_name)
        except:
            print("工作薄名字不正确")


d = excelGuide()
d.sheet_Data()

