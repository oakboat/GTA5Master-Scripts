<style>
.category-tag {
    display: inline-block;
    background-color: #3498db;
    color: white;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.8em;
    margin-right: 5px;
}
</style>

# GTA5Master 脚本中心

## 📦 可用脚本列表

<!-- SCRIPTS_START -->
| 名称 | 作者 | 版本 | 描述 | 下载 | 仓库 |
|------|------|------|------|------|------|
| *脚本列表将通过CI自动更新* | | | | | |
<!-- SCRIPTS_END -->

## 📥 安装方法
1. 点击"下载"链接获取脚本文件（`.lua`格式）
2. 将文件放入 `GTA5Master/scripts/` 文件夹
3. 重启 GTA5Master 即可使用

## 🚀 提交你的脚本

### 开发规范
```
脚本文件夹/
├── main.lua      # 主文件（必须）
├── info.json     # 插件信息（必须）
└── README.md     # 说明文档（可选）
```

**info.json 格式：**
```json
{
  "name": "脚本名称",
  "author": "你的名字",
  "version": "1.0",
  "description": "脚本功能描述",
  "download_url": "https://github.com/你的名字/仓库名/raw/main/main.lua",
  "repo_url": "https://github.com/你的名字/仓库名",
  "category": "脚本分类"
}
```

### 提交步骤
1. **开发并测试**你的脚本
2. **上传到GitHub**仓库
3. **编辑本仓库的 `scripts.json`** 文件，添加你的脚本信息
4. **提交 Pull Request**

### 提交示例
编辑 `scripts.json`，添加：
```json
{
  "name": "你的脚本名",
  "author": "你的名字",
  "version": "1.0",
  "description": "脚本描述",
  "download_url": "https://github.com/你的名字/仓库名/raw/main/main.lua",
  "repo_url": "https://github.com/你的名字/仓库名",
  "category": "工具"
}
```

## ⚙️ 自动更新
本仓库使用 GitHub Actions 自动：
- ✅ 每周更新脚本列表
- ✅ 检查下载链接有效性
- ✅ 自动更新此 README 文件

## 📚 开发资源
- API文档：查看 GTA5Master 内置文档
- 示例代码：[查看示例](https://github.com/GTA5Master/Examples)
- 问题反馈：创建 Issue

## 🔄 更新日志
<!-- UPDATE_LOG -->
**最后更新**: 等待第一次运行... | **脚本总数**: 0 个
<!-- UPDATE_LOG -->

---

**只需两个文件即可提交脚本！欢迎贡献！**