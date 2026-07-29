from app.handlers import (
    start,
    earnings,
    design,
    courses,
    profile
)


dp.include_router(start.router)
dp.include_router(earnings.router)
dp.include_router(design.router)
dp.include_router(courses.router)
dp.include_router(profile.router)