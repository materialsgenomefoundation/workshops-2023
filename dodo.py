from pathlib import Path

DOIT_CONFIG = dict(backend="json", verbosity=2)
PDF = Path("workshops-2023.pdf")
README = Path("README.md")


def task_pdf():
    """build a pdf from the markdown using pandoc and tectonic in mamba.

    you gotta install that business yourself."""
    return dict(
        targets=[PDF],
        file_dep=[README],
        actions=[f"pandoc --from=gfm --to=pdf --pdf-engine=tectonic -o {PDF} {README}"],
        clean=True,
    )
