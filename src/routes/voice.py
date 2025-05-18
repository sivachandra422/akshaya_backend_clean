from fastapi import APIRouter

router = APIRouter()

@router.get('/voice')
def example():
    return {'message': 'voice route active'}
