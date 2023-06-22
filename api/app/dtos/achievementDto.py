from pydantic import BaseModel

class achievementPostDto(BaseModel):
    xp: int
    name: str
    description: str
    metas: str
    
    