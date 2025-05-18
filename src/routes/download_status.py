from fastapi import APIRouter

router = APIRouter()

@router.get('/download_status')
def example():
    return {'message': 'download_status route active'}
