import typer 
import subprocess
from typing_extensions import Annotated
import rich 
from rich.console import Console
from pathlib import Path


console = Console()
app = typer.Typer()


def make_ida_cmd(binary: Path, logfile: Path):

    func_list = Path("function_list.py").resolve()

    ida = Path("~/idapro-8.3/idat64").expanduser()

    cmd = f'{ida.resolve()} -c -A -S"{func_list.resolve()}" -L{logfile.resolve()} {binary.resolve()}'

    #TODO: This only works for i64 
    clear_cmd = f"rm {binary.resolve()}.i64"

    return cmd, clear_cmd





@app.command()
def ida_on(binary: Annotated[str, typer.Argument(help="bin to run on")], 
           logfile: Annotated[str, typer.Argument(help="bin to run on")]):



    cmd, clear_cmd = make_ida_cmd(Path(binary), Path(logfile))
    print(cmd)

    res = subprocess.check_output(cmd,shell=True)
    print(res)
    res = subprocess.check_output(clear_cmd, shell=True)

    return


if __name__ == "__main__":
    app()
