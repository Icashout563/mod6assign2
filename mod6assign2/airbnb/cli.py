import typer

app = typer.Typer()

@app.command()
def run():
    print("Airbnb CLI running")

if __name__ == "__main__":
    app()
