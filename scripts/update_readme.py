#!/usr/bin/env python3
import json
import urllib.request
from datetime import datetime
import re

def main():
    # 读取 scripts.json
    with open('scripts.json', 'r', encoding='utf-8') as f:
        scripts = json.load(f)
    
    # 生成 Markdown 表格 - 添加仓库列
    table_lines = [
        "| 名称 | 作者 | 版本 | 描述 | 下载 | 仓库 |",
        "|------|------|------|------|------|------|"
    ]
    
    for script in scripts:
        name = script.get('name', '')
        author = script.get('author', '')
        version = script.get('version', '')
        description = script.get('description', '')[:50] + ('...' if len(script.get('description', '')) > 50 else '')
        download_url = script.get('download_url', '#')
        repo_url = script.get('repo_url', '')
        category = script.get('category', '')
        
        # 添加类别标签
        category_tag = ""
        if category:
            category_tag = f'<span class="category-tag">{category}</span> '
        
        # 验证下载链接
        try:
            req = urllib.request.Request(download_url, method='HEAD')
            urllib.request.urlopen(req, timeout=5)
            link_status = "✅"
        except:
            link_status = "❌"
        
        # 生成仓库链接
        repo_link = ""
        if repo_url:
            repo_link = f'[🔗]({repo_url})'
        
        # 生成行
        table_lines.append(
            f"| {category_tag}**{name}** | {author} | {version} | {description} | "
            f"[{link_status} 下载]({download_url}) | {repo_link} |"
        )
    
    # 读取 README.md
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换脚本表格部分
    start_marker = '<!-- SCRIPTS_START -->'
    end_marker = '<!-- SCRIPTS_END -->'
    
    new_table = f"{start_marker}\n" + "\n".join(table_lines) + f"\n{end_marker}"
    pattern = re.compile(f'{re.escape(start_marker)}.*?{re.escape(end_marker)}', re.DOTALL)
    content = pattern.sub(new_table, content)
    
    # 更新日志
    update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_marker = '<!-- UPDATE_LOG -->'
    new_log = f"{log_marker}\n**最后更新**: {update_time} | **脚本总数**: {len(scripts)} 个\n{log_marker}"
    pattern = re.compile(f'{re.escape(log_marker)}.*?{re.escape(log_marker)}', re.DOTALL)
    content = pattern.sub(new_log, content)
    
    # 写回 README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated README with {len(scripts)} scripts at {update_time}")

if __name__ == '__main__':
    main()