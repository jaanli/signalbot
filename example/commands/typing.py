import asyncio
from src.signalbot import Command, Context


class TypingCommand(Command):
    def describe(self) -> str:
        return None

    async def handle(self, c: Context):
        command = c.message.text

        if command == "typing":
            await c.start_typing()
            seconds = 5
            await asyncio.sleep(seconds)
            await c.stop_typing()
            await c.send(f"Typed for {seconds}s")
