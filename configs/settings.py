from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Settings class for application configuration.
    This class uses Pydantic to manage application settings.
    It includes settings for the Socket.IO server and API keys.
    The settings are loaded from a .env file.
    """
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # Socket.IO server settings
    SERVER_HOST: str = "localhost"
    SERVER_PORT: int = 5000

    # Logging settings
    # The log level can be set to DEBUG, INFO, WARNING, ERROR, or CRITICAL
    # Default is INFO if not specified in the environment
    LOG_LEVEL: str = "INFO"

    # LLM API Keys

    # More settings can be added here as needed

# Create an instance of the Settings class
settings = Settings()