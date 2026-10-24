from typing import List
from shared.contract import Block


def render(blocks: List[Block]) -> str:
    """
    Renders a list of study blocks into a readable text plan.
    """
    if not blocks:
        return "No study blocks scheduled."

    lines = ["=== Study Plan ==="]
    total_hours = 0.0

    for idx, block in enumerate(blocks, start=1):
        lines.append(
            f"{idx}. Task: {block.task.title} | Allocated: {block.hours}h"
        )
        total_hours += block.hours

    lines.append(f"Total planned time: {total_hours}h")
    return "\n".join(lines)