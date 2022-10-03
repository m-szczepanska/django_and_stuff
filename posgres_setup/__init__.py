from __future__ import absolute_import
from .celery_application import app as celery_app


__all__ = ("celery_app",)