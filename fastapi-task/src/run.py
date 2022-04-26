from imp import reload
import uvicorn
from code_const_task.settings import settings


if __name__ == '__main__':
    uvicorn.run(
        "code_const_task.app:app",
        host = settings.host,
        port = settings.port,
        reload = settings.reload,
    )