from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box
from rich.table import Table
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from db_init import *

console = Console()


#?==================================== MENU PRINCIPAL ====================================


def display_menu_banner():
    console.clear()
    banner = Panel(Align.center("[bold cyan] MORGHUL'S CHRONICLES [/bold cyan]"),
        subtitle = "[dim]Version 2.0[/dim]",
        border_style = "blue",
        box=box.ROUNDED,
        width = 100,
        padding = (1, 1)
    )
    console.print(Align.center(banner))

def display_menu_choices():
    choice = inquirer.select(
        message="Menu Principal :",
        choices=[
            Choice(value=1, name="Démarrer le jeu"),
            Choice(value=2, name="Voir le classement"),
            Choice(value=3, name="Quitter"),
        ],
        pointer="> ",
    ).execute()
    return choice


#?==================================== CHOIX EQUIPE ====================================


def select_heroes(team_lenght = 3):
    heroes = get_all_heroes()

    choices = []
    for i, hero in enumerate(heroes):
        choices.append(Choice(
            value=i,
            name=f"{hero.name} - ATK: {hero.attack}, DEF: {hero.defense}, HP: {hero.hp}"
        ))
    selected_indexes = inquirer.checkbox(
        message="Voici la liste des héros :",
        choices=choices,
        pointer="> ",
        validate=lambda result: len(result) == team_lenght,
        invalid_message=f"Tu dois sélectionner exactement {team_lenght} héros.",
    ).execute()
    return [heroes[i] for i in selected_indexes]


def print_team(team):
    table = Table(
        title="[bold cyan] VOTRE ÉQUIPE ACTUELLE [/bold cyan]",
        box=box.ROUNDED,
        border_style="bright_blue"
    )
    table.add_column("#", justify="center", style="bold", width=3)
    table.add_column("Nom", style="white")
    table.add_column("ATK", justify="center", style="red")
    table.add_column("DEF", justify="center", style="blue")
    table.add_column("HP", justify="center", style="green")

    for i, hero in enumerate(team, 1):
        table.add_row(
            str(i),
            hero.name,
            str(hero.attack),
            str(hero.defense),
            f"{hero.hp}/{getattr(hero, 'max_hp', hero.hp)}",
        )
    console.print()
    console.print(table)
    console.print()


#?==================================== CLASSEMENT ====================================


def show_leaderboard():
    leaderboard = get_leaderboard()

    if not leaderboard:
        console.print("\n[italic yellow]Aucun score enregistré pour le moment.[/italic yellow]\n")
        input("Appuie sur Entrée pour revenir au menu...")
        return

    # 1. Création de la table
    table = Table(
        title="[bold yellow] TOP 10 [/bold yellow]",
        box=box.ROUNDED,          # Bords arrondis modernes
        border_style="bright_blue",
        header_style="bold cyan",
        title_style="bold",
        padding=(0, 1)
    )

    # 2. Définition des colonnes
    table.add_column("Rang", justify="center", style="bold", width=6)
    table.add_column("Joueur", style="white", min_width=12)
    table.add_column("Vagues", justify="right", style="green", width=10)
    table.add_column("Équipe engagée", style="magenta")

    for rank, score in enumerate(leaderboard, start=1):
        rank_str = f"#{rank}"
        waves_str = f"{score['count']}"
        team_str = ", ".join(score["team"])

        table.add_row(
            rank_str,
            score["name"],
            waves_str,
            team_str
        )

    # 4. Affichage centré dans le terminal
    console.print()
    console.print(Align.center(table))
    console.print()