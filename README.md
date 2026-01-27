# GTA5Master 脚本中心

## 使用方法
1. 在GTA5Master中点击"脚本市场"
2. 选择脚本点击"安装"
3. 脚本会自动下载到 scripts 文件夹

## 提交你的脚本
1. 把你的脚本上传到GitHub
2. 编辑这个仓库的 scripts.json 文件
3. 添加你的脚本信息
4. 提交Pull Request

# GTA5Master 插件开发规范

## 📁 文件结构（最简单）
```
插件文件夹/
├── main.lua      # 必须：主文件
└── info.json     # 必须：插件信息
```

## 📄 info.json 格式（必须）
```json
{
  "name": "插件名称",
  "author": "你的名字",
  "version": "1.0",
  "description": "插件功能描述"
}
```

## 📝 main.lua 基础模板
```lua
-- 插件加载时显示通知
notify("插件已加载")

-- 创建GUI界面
gui_text("=== 我的插件 ===")
gui_button("按钮", function()
    notify("按钮被点击")
end)
```

## 🚀 如何提交插件

### 1. 开发你的插件
- 创建 `main.lua` 和 `info.json`
- 测试功能是否正常

### 2. 上传到GitHub
1. 创建新仓库
2. 上传你的两个文件
3. 发布Release（打包成zip）

### 3. 添加到官方列表
1. 访问：https://github.com/GTA5Master/Scripts
2. 编辑 `scripts.json`
3. 添加你的插件信息：
```json
{
  "name": "你的插件名",
  "author": "你的名字",
  "download": "https://github.com/你的名字/仓库名/releases/download/v1.0/插件.zip"
}
```

## ⚠️ 注意事项
- 插件文件名不要有中文
- 不要包含恶意代码
- 确保功能正常可用
- 注明GTA5版本要求

## ❓ 需要帮助？
- API文档：查看GTA5Master内置文档
- 示例代码：参考官方示例仓库
- 问题反馈：在GitHub提Issue

---
**最简单的插件只需要两个文件！现在就开始吧！**
