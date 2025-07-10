from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Profile(BaseModel):
    id: int
    name: str
    address: str
    mobile: str
    password: str
    email: str
    amount: int


class ReadProfile(BaseModel):
    id: int
    name: str
    address: str
    mobile: str
    password: str
    email: str
    amount: int
    class Config:
        from_attributes = True


class Records(BaseModel):
    id: int
    username: str
    address: str
    pincode: str
    user_amount: int


class ReadRecords(BaseModel):
    id: int
    username: str
    address: str
    pincode: str
    user_amount: int
    class Config:
        from_attributes = True


class Class(BaseModel):
    id: int
    subject: str


class ReadClass(BaseModel):
    id: int
    subject: str
    class Config:
        from_attributes = True


class Students(BaseModel):
    id: int
    name: str
    age: str


class ReadStudents(BaseModel):
    id: int
    name: str
    age: str
    class Config:
        from_attributes = True


