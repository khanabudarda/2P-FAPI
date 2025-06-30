from typing import Dict, Annotated, Any
from fastapi import Body, FastAPI, APIRouter

app = FastAPI()

v1_router = APIRouter(prefix="/v1/api")

@v1_router.get("/")
async def welcome():
    print("Welcome to 2P Quiz Game...")

@v1_router.post("/user/register")
async def register_user(data):
    print(data)
    pass

@v1_router.post("/user/login")
async def login(data):
    print(data)
    pass

@v1_router.get("/subjects")
async def get_subjects():
    print("Showing all Subjects")
    return "SUB"

@v1_router.post("/matchmaking/join")
async def join_match():
    print("Will join a game if available or create a new game with new id and wait for another player")
    pass

@v1_router.post("/matchmaking/join")
async def join_match():
    print("API to leave lobby. This will lead to other player joining the wait list for next player")
    pass

@v1_router.get("/match/status")
async def get_game_status():
    print("This will return time for game to start predictive based on number of current active players")
    pass

v1_router.get("/quiz/start")
async def start_quiz(match_id):
    print("Both players are ready to recive questions... and recieve all the questions")
    pass

v1_router.post("/quiz/answer")
async def get_all_answer(game_data):
    print("This API is responsible for saving answer for the question and posting the next question for player and game")
    pass

v1_router.get("/quiz/progress")
async def get_match_status(match_id):
    print("Gives information such as time remaining, questions remaning etc...")
    pass

v1_router.get("/match/result")
async def check_match_result():
    print("Check any match result...")
    pass

v1_router.get("/leaderboard/global")
async def check_leaderboard(subject="All"):
    print("Gives leaderboard for each subject or for overall wins by player")
    pass

v1_router.get("/leaderboard/location")
async def get_my_leaderboard(player_id):
    print("Shows users current position on the leader board.")


app.include_router(v1_router)