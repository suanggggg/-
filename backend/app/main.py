from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import yaml

from app.api.routers import users, questions, assessments
from app.db import base as db_base

from contextlib import asynccontextmanager
from sqlalchemy.exc import SQLAlchemyError
app = FastAPI(title="Exam & Interview System")

# 开发模式允许本地前端访问 API（根据需要调整 origin 列表）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174", "http://127.0.0.1:5174", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# lifespan handler替换startup事件
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 创建数据库表（dev 环境用），生产请使用迁移工具
    try:
        db_base.Base.metadata.create_all(bind=db_base.engine)
    except SQLAlchemyError:
        pass
    # 尝试加载外部 OpenAPI YAML 作为应用的 schema（如果存在）
    repo_root = Path(__file__).resolve().parents[2]
    swagger_path = repo_root / "docs" / "api" / "swagger.yaml"
    if swagger_path.exists():
        try:
            with open(swagger_path, "r", encoding="utf-8") as f:
                spec = yaml.safe_load(f)
                app.openapi_schema = spec
        except Exception:
            pass
    yield

app.router.lifespan_context = lifespan

# 注册路由
app.include_router(users.router, prefix="/auth", tags=["auth"])
app.include_router(questions.router, prefix="/questions", tags=["questions"])
app.include_router(assessments.router, prefix="/assessments", tags=["assessments"])


@app.get("/")
async def root():
    return {"message": "Exam & Interview System API - skeleton"}
