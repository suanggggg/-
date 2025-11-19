import os


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "ExamInterview")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me")


settings = Settings()
