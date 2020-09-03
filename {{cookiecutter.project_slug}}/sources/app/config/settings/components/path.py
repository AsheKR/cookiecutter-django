from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
TEMPLATE_DIR = BASE_DIR.joinpath('templates')
