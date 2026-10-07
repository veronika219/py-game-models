import init_django_orm  # noqa: F401
import json
from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json") as file:
        players = json.load(file)

    for name, info in players.items():
        player = Player.objects.create(
            nickname=name,
            email=info["email"],
            bio = info["bio"],
        )

        dict_race = info["race"]

        race, _ = Race.objects.get_or_create(
            name=dict_race["name"],
            description=dict_race["description"]
        )

        skills_list = dict_race["skills"]

        if skills_list:
            for skill in skills_list:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        player.race = race

        if info["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=info["guild"]["name"],
                description=info["guild"]["description"]
            )
            player.guild = guild

        player.save()

if __name__ == "__main__":
    main()
