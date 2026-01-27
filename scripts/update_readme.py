#!/usr/bin/env python3
import json
import urllib.request
from datetime import datetime
import re

def main():
    # 读取 scripts.json
    with open('scripts.json', 'r', encoding='utf-8') as f:
        scripts = json.load(f)
    
    # 生成 Markdown 表格
    table_lines = [
        "| 名称 | 作者 | 版本 | 描述 | 下载 |",
        "|------|------|------|------|------|"
    ]
    
    for script in scripts:
        name = script.get('name', '')
        author = script.get('author', '')
        version = script.get('version', '')
        description = script.get('description', '')[:50] + ('...' if len(script.get('description', '')) > 50 else '')
        download_url = script.get('download_url', '#')
        
        # 验证链接（可选）
        try:
            req = urllib.request.Request(download_url, method='HEAD')
            urllib.request.urlopen(req, timeout=5)
            link_status = "✅"
        except:
            link_status = "❌"
        
        table_lines.append(f"| {name} | {author} | {version} | {description} | [{link_status} 下载]({download_url}) |")
    
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
    new_log = f"{log_marker}\n最后更新: {update_time} (共 {len(scripts)} 个脚本)\n{log_marker}"
    pattern = re.compile(f'{re.escape(log_marker)}.*?{re.escape(log_marker)}', re.DOTALL)
    content = pattern.sub(new_log, content)
    
    # 写回 README.md
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated README with {len(scripts)} scripts at {update_time}")

if __name__ == '__main__':
    main()
