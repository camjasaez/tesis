from config.db_config import db_client
from utils.responses import success_response


async def status() -> dict:
    """
    Check API status

    """
    try:
        async with db_client() as mongodb:
            await mongodb.command("ping")
            return success_response(status=200, message="Happy Coding! 📚💻")
    except Exception as e:
        print({"message": f"Database connection error: {str(e)}"})
        return {"Status": "Offline", "Message": "Database connection error ❌💻"}
