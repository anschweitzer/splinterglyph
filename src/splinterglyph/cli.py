import os
from typing import Annotated
from typing import Optional

import typer
from splinterglyph import splinterglyph_tools

app = typer.Typer(
    no_args_is_help=True,
    pretty_exceptions_enable=False,
    rich_markup_mode="rich",
    help="splinterglyph command-Line debug tools.",
)

@app.command()
def encrypt(
    plain: Annotated[
        str,
        typer.Argument(
            help="Path to (input) plaintext file."
        )
    ],
    crypt: Annotated[
        Optional[str],
        typer.Argument(
            help="Path to (output) encrypted file; default is <inpath>.splinterglyph",
        ),
    ] = None,
    N: Annotated[
        int,
        typer.Option(help="Number of distributed key shares.")
    ] = 5,
    M: Annotated[
        int,
        typer.Option(help="Minimum required key shares for recovery.")
    ] = 2,
    key_bit_length: Annotated[
        int,
        typer.Option(
            help="Length of AES key in bits (e.g., 128 or 256)"
        )
    ] = 128
) -> None:
    """Encrypt file and produce multiple crypto key shares."""
    splinterglyph_tools.encrypt(
        plain_path=plain,
        crypt_path=crypt,
        distributed_shares=N,
        required_shares=M,
        key_bit_length=key_bit_length,
    )

@app.command()
def decrypt(
    plain: Annotated[str, typer.Argument(help="Path to (output) plaintext file.")],
    crypt: Annotated[Optional[str], typer.Argument(help="Path to (input) encrypted file; default is STDOUT")] = None,
    shares: Annotated[
        Optional[str],
        typer.Argument(
            help=(
                f"Key shares for recovery.  These can be specified either "
                f"as a path to a file containing the samples, or as a list of the "
                f"samples themselves, e.g., --shares '1-even,thermostat,hinted,easel 3-odd,them,harv,wut'"
            )
        )
    ] = None,
) -> None:
    """"""

    if os.path.exists(shares):
        with open(shares) as fp:
            key_shares = fp.read().split()
    else:
        key_shares = shares.split()
    splinterglyph_tools.decrypt(
        plain_path=plain, crypt_path=crypt, key_shares=key_shares
    )

# For sphinx:
typer_click_object = typer.main.get_command(app)



if __name__ == "__main__":
    app()
