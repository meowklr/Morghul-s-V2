from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich import box
from rich.table import Table
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from db_init import *

console = Console()

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