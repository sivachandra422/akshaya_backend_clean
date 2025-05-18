from fastapi import APIRouter

router = APIRouter()

@router.get('/build_trigger')
def example():
    return {'message': 'build_trigger route active'}
