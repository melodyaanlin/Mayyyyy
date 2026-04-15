# 五一出逃计划 | 拼贴志

复古拼贴风格的互动网页，包含旅行目的地投票与灵魂鉴定功能。

## 目录结构

```
traveltarget/
├── index.html              # 主页面（单文件 HTML 应用）
├── pic/
│   ├── source/             # 原始图片（从 HTML 内嵌 base64 提取而来）
│   │   ├── img_001.jpg
│   │   └── ...             # 共 60 张
│   └── thumbnail/          # 缩略图（由 source 压缩生成，页面实际加载此目录）
│       ├── img_001.jpg
│       └── ...             # 共 60 张，最大 800x450，≤200KB
└── README.md
```

## 脚本说明

脚本位于项目根目录的 `script/` 下：

### extract_images.py

从内嵌 base64 图片的原始 HTML 中提取图片文件。

- 输入：`traveltarget/index.html`（含 base64 内嵌图片的版本）
- 输出：
  - `traveltarget/pic/` 目录下的图片文件
  - `traveltarget/index_clean.html`（base64 替换为本地路径后的 HTML）

```bash
python script/extract_images.py
```

### resize_images.py

将 `pic/source/` 中的原图批量压缩为缩略图，输出到 `pic/thumbnail/`。

- 最大尺寸：800 x 450
- 最大体积：200KB
- 压缩策略：从 quality=85 逐步降至 40，直到满足体积限制
- 依赖：`Pillow`

```bash
pip install Pillow
python script/resize_images.py
```

## 环境准备

### macOS

```bash
# 安装 Homebrew（已安装可跳过）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Python
brew install python

# 验证
python3 --version
pip3 --version
```

### Windows

1. 从 [python.org](https://www.python.org/downloads/) 下载安装包
2. 安装时勾选 **"Add Python to PATH"**
3. 打开命令提示符验证：
   ```bash
   python --version
   pip --version
   ```

### 安装项目依赖

```bash
pip install Pillow
```

## 快速开始

```bash
# 1. 生成缩略图
pip install Pillow
python script/resize_images.py

# 2. 启动本地服务
cd traveltarget
python -m http.server 8000
# 浏览器访问 http://localhost:8000
```
