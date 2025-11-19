# 考试系统（骨架代码）

此仓库包含需求文档与后端 FastAPI 项目骨架（示例），用于演示系统结构与接口草案。具体实现留白，便于按故事逐步实现。

快速开始（针对后端骨架，Windows + PowerShell）:

```powershell
cd d:/code/软件体系结构/backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

下一步建议：根据用户故事按优先级实现 API 与数据库迁移。
