from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {
        "env_file": [".env.local"],
        "extra": "allow",
    }

    rekognition_collection_id: str
    aws_region: str
    aws_access_key_id: str
    aws_secret_access_key: str


settings = Settings()
