import typer

app = typer.Typer()

@app.command()
def run():
    print("COVID CLI running")

if __name__ == "__main__":
    app()
