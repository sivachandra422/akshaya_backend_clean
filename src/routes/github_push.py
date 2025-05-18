from fastapi import APIRouter

router = APIRouter()

@router.get('/github_push')
def example():
    return {'message': 'github_push route active'}
