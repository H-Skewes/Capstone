from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
import logging

app = FastAPI()
