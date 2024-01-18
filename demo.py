import uiautomation as auto

# 设置等待时间为20秒
auto.SetGlobalSearchTimeout(20)

# 获取桌面窗口
desktop = auto.WindowControl(searchDepth=1, ClassName='WorkerW')

# 获取桌面上的所有控件
children = desktop.GetChildren()

# 遍历并操作这些控件
for child in children:
    # 在这里处理每个控件
    print(child.Name)
