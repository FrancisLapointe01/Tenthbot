import random
import json
from twitchAPI.chat import ChatCommand
from Persona_Data import RARITY_WEIGHTS, PERSONA_POOL, PROTAG_PERSONAS, POINT_VALUES
DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# !draw with some sauce
async def summon_command(cmd: ChatCommand):
    username = cmd.user.name.lower()
    data = load_data()

    # FIRST TIME USER — AWAKENING
    if username not in data:
        persona = random.choice(PROTAG_PERSONAS)

        data[username] = {
            "points": 10,
            "summons": 1,
            "starter": persona,
            "inventory": []
        }

        save_data(data)

        await cmd.reply(
            f"{cmd.user.name} hears a voice from the Sea of Souls... "
            f"{persona} awakens! You are now a Wild Card. "
            f"+10 Velvet Points."
        )
        return

    # Normal summon
    arcana = random.choice(list(PERSONA_POOL.keys()))

    rarity = random.choices(
        list(RARITY_WEIGHTS.keys()),
        weights=list(RARITY_WEIGHTS.values()),
        k=1
    )[0]

    persona = random.choice(PERSONA_POOL[arcana][rarity])
    points = POINT_VALUES[rarity]

    data[username]["points"] += points
    data[username]["summons"] += 1
    data[username]["inventory"].append({
        "name": persona,
        "rarity": rarity,
        "arcana": arcana
    })

    save_data(data)

    await cmd.reply(
        f"The Arcana is {arcana}... {persona} answers the call. "
        f"({rarity}) +{points} Velvet Points | "
        f"Total: {data[username]['points']}"
    )