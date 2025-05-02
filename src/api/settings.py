from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = {
        "env_file": [".env.local"],
        "extra": "allow",
    }

    aws_region: str
    aws_access_key_id: str
    aws_secret_access_key: str

    system_api_key: str

    rekognition_collection_id: str


settings = Settings()
