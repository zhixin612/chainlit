import os

from chainlit.logger import logger

# Default chainlit.md file created if none exists
DEFAULT_MARKDOWN_STR = """# Welcome to Chainlit! 🚀🤖

Hi there, Developer! 👋 We're excited to have you on board. Chainlit is a powerful tool designed to help you prototype, debug and share applications built on top of LLMs.

## Useful Links 🔗

- **Documentation:** Get started with our comprehensive [Chainlit Documentation](https://docs.chainlit.io) 📚
- **Discord Community:** Join our friendly [Chainlit Discord](https://discord.gg/k73SQ3FyUh) to ask questions, share your projects, and connect with other developers! 💬

We can't wait to see what you create with Chainlit! Happy coding! 💻😊

## Welcome screen

To modify the welcome screen, edit the `chainlit.md` file at the root of your project. If you do not want a welcome screen, just leave this file empty.
"""


def init_markdown(root: str):
    """Initialize the chainlit.md file if it doesn't exist."""
    chainlit_md_file = os.path.join(root, "welcome.md")

    if not os.path.exists(chainlit_md_file):
        with open(chainlit_md_file, "w", encoding="utf-8") as f:
            f.write(DEFAULT_MARKDOWN_STR)
            logger.info(f"Created default chainlit markdown file at {chainlit_md_file}")


def get_markdown_str(root: str, language: str):
    """Get the chainlit.md file as a string."""
    translated_chainlit_md_path = os.path.join(root, "welcome.md")
    default_chainlit_md_path = os.path.join(root, "welcome.md")

    if os.path.exists(translated_chainlit_md_path):
        chainlit_md_path = translated_chainlit_md_path
    else:
        chainlit_md_path = default_chainlit_md_path
        logger.warning(
            f"Translated markdown file for {language} not found. Defaulting to welcome.md."
        )

    if os.path.exists(chainlit_md_path):
        with open(chainlit_md_path, "r", encoding="utf-8") as f:
            chainlit_md = f.read()
            return chainlit_md
    else:
        return None


def init_version(root: str):
    """Initialize the chainlit.md file if it doesn't exist."""
    chainlit_md_file = os.path.join(root, "version.md")

    if not os.path.exists(chainlit_md_file):
        with open(chainlit_md_file, "w", encoding="utf-8") as f:
            f.write(DEFAULT_MARKDOWN_STR)
            logger.info(f"Created default chainlit markdown file at {chainlit_md_file}")


def get_version_str(root: str, language: str):
    """Get the chainlit.md file as a string."""
    translated_chainlit_md_path = os.path.join(root, "version.md")
    default_chainlit_md_path = os.path.join(root, "version.md")

    if os.path.exists(translated_chainlit_md_path):
        chainlit_md_path = translated_chainlit_md_path
    else:
        chainlit_md_path = default_chainlit_md_path
        logger.warning(
            f"Translated markdown file for {language} not found. Defaulting to version.md."
        )

    if os.path.exists(chainlit_md_path):
        with open(chainlit_md_path, "r", encoding="utf-8") as f:
            chainlit_md = f.read()
            return chainlit_md
    else:
        return None
