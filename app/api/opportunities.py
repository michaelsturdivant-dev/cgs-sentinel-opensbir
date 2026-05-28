from fastapi import APIRouter

from app.models import Opportunity

router = APIRouter(prefix="/opportunities", tags=["opportunities"])

OPPORTUNITIES: list[Opportunity] = []


@router.get("")
def list_opportunities():
    return OPPORTUNITIES


@router.post("")
def create_opportunity(opportunity: Opportunity):
    OPPORTUNITIES.append(opportunity)
    return {"opportunity": opportunity, "note": "Use this public endpoint for non-sensitive reference-model opportunity tracking."}
