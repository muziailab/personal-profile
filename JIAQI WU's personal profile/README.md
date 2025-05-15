# 个人主页项目

## 项目结构

```
project/
├── streamlit_app.py        # 主应用入口点
├── .streamlit/             # Streamlit配置
│   └── config.toml         # Streamlit配置文件
├── components/             # 可重用UI组件
│   ├── footer.py           # 页脚组件
│   ├── interactive.py      # 交互式可视化
│   └── styles.py           # CSS和样式工具
├── page_content/           # 网站页面
│   ├── home.py             # 主页
│   ├── experience.py       # 工作经验页面
│   ├── education.py        # 教育经历页面
│   ├── resume.py           # 简历页面
│   └── contact.py          # 联系页面
└── static/                 # 静态资源
    ├── css/                # CSS样式表
    │   └── style.css       # 主样式表
    ├── images/             # 图片文件
    │   └── profile.png     # 个人照片
    └── docs/               # 文档
        ├── resume.md       # Markdown格式简历
        └── resume.pdf      # PDF格式简历
```

## 功能特点

- 多页面导航（带侧边栏）
- 交互式数据可视化
- 响应式设计与自定义CSS
- 可下载简历
- 联系表单
- 通过config.toml实现Streamlit主题定制

## 安装与运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行应用：
```bash
streamlit run streamlit_app.py
```