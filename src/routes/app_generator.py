from fastapi import APIRouter

router = APIRouter()

@router.get('/app_generator')
def example():
    return {'message': 'app_generator route active'}
