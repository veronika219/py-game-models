import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as file:
        content = json.load(file)

    for nickname, info in content.items():
        race, _ = Race.objects.get_or_create(
            name=info["race"]["name"], description=info["race"]["description"]
        )

        guild = info.get("guild")
        if guild:
            guild, _ = Guild.objects.get_or_create(
                name=guild["name"], description=guild["description"]
            )

        Player.objects.create(
            nickname=nickname,
            email=info.get("email"),
            bio=info["bio"],
            race=race,
            guild=guild,
        )

        for skill in info["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"], bonus=skill["bonus"], race=race
            )


if __name__ == "__main__":
    main()
