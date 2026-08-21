from fastapi import APIRouter, Depends

from app.core.config import Settings, get_settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check(settings: Settings = Depends(get_settings)) -> dict[str, str]:
    """Return basic service health information."""

    return {"status": "ok", "app": settings.app_name, "env": settings.app_env}
