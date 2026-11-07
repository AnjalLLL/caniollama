"""Vercel entry point: serves the FastAPI app as a Python serverless function."""

from compat_registry.main import app

__all__ = ["app"]
