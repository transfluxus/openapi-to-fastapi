"""
This module extends some of FastAPI models, to include extra data into them
"""

from typing import Dict, Optional

from fastapi.openapi import models as oas
from pydantic import BaseModel, ConfigDict, Field

# do we have these somewhere in fastapi or starlette?
GET_METHOD = "get"
POST_METHOD = "post"
PUT_METHOD = "put"
DELETE_METHOD = "delete"
PATCH_METHOD = "patch"
OPTIONS_METHOD = "options"
HEAD_METHOD = "head"

METHODS = [GET_METHOD, POST_METHOD, PUT_METHOD, DELETE_METHOD, PATCH_METHOD, OPTIONS_METHOD, HEAD_METHOD]
BODY_METHODS = [POST_METHOD, PUT_METHOD, PATCH_METHOD]

class Header(oas.Header):
    model_config = ConfigDict(extra="ignore")


class ParsedResponse(BaseModel):
    description: Optional[str] = None
    name: Optional[str] = None


class Operation(oas.Operation):
    requestBodyModel: Optional[str] = ""
    parsedResponses: Dict[int, ParsedResponse] = Field(default_factory=dict)
    headers: Optional[Dict[str, Header]] = None
    deprecated: Optional[bool] = None


class PathItem(oas.PathItem):
    get: Optional[Operation] = None
    put: Optional[Operation] = None
    post: Optional[Operation] = None
    delete: Optional[Operation] = None
    options: Optional[Operation] = None
    head: Optional[Operation] = None
    patch: Optional[Operation] = None
