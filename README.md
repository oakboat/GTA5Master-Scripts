# GTA5Master 脚本中心

## 📦 可用脚本列表

<!-- SCRIPTS_START -->
| 名称 | 作者 | 版本 | 描述 | 下载 |
|------|------|------|------|------|
| *脚本列表将通过CI自动更新* | | | | |
<!-- SCRIPTS_END -->

## 📥 手动安装方法
1. 下载脚本文件（`.lua` 格式）
2. 放到 `GTA5Master/scripts/` 文件夹
3. 重启 GTA5Master

## 🚀 提交你的脚本

### 开发规范
```
你的脚本名/
├── main.lua      # 主文件（必须）
└── info.json     # 插件信息（必须）
```

**info.json 格式：**
```json
{
  "name": "脚本名称",
  "author": "你的名字",
  "version": "1.0",
  "description": "脚本功能描述",
  "gta5_version": "1.68",
  "download_url": "https://github.com/你的名字/仓库名/raw/main/main.lua"
}
```

### 提交步骤
1. **开发脚本**
   - 创建 `main.lua` 和 `info.json`
   - 测试功能正常

2. **上传到GitHub**
   - 创建公开仓库
   - 上传你的文件
   - **确保 `main.lua` 有直接下载链接**

3. **添加到官方列表**
   - Fork 本仓库
   - 编辑 `scripts.json` 文件
   - 添加你的脚本信息：
     ```json
     {
       "name": "你的脚本名",
       "author": "你的名字",
       "version": "1.0",
       "description": "脚本描述",
       "download_url": "https://github.com/你的名字/仓库名/raw/main/main.lua",
       "source_url": "https://github.com/你的名字/仓库名",
       "last_updated": "2024-01-20"
     }
     ```
   - 提交 Pull Request

## ⚙️ 自动更新系统
本仓库使用 GitHub Actions 自动：
- ✅ 验证 scripts.json 格式
- ✅ 检查下载链接有效性
- ✅ 自动更新 README 中的脚本表格
- ✅ 每周自动检查链接状态

## 📁 仓库文件结构
```
GTA5Master-Scripts/
├── README.md          # 本文件（自动更新）
├── scripts.json       # 脚本索引数据库
├── .github/workflows/ # CI/CD 配置
│   └── update-readme.yml
└── scripts/           # （可选）官方示例脚本
```

## ⚠️ 注意事项
1. 脚本必须安全，无恶意代码
2. 确保下载链接长期有效
3. 注明兼容的GTA5版本
4. 定期更新维护你的脚本

## 📚 开发资源
- API文档：查看 GTA5Master 内置文档
- 示例代码：[示例仓库](https://github.com/GTA5Master/Examples)
- 问题反馈：创建 Issue

---

## 🔄 自动更新日志
<!-- UPDATE_LOG -->
最后更新: 等待第一次运行...
<!-- UPDATE_LOG -->

---

**只需两个文件即可提交脚本！欢迎贡献！**
