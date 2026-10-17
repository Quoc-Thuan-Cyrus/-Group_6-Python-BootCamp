from shared.contract import Task, Block

def allocate(tasks: list[Task], hours: float) -> list[Block]:
    blocks = []
    for task in tasks:
        if hours <= 0:
            break
        
        # Determine how much time we can allocate to the task
        allocated_hours = min(task.effort_h, hours)
        
        # Add the block
        blocks.append(Block(task=task, hours=allocated_hours))
        
        # Subtract the allocated time from our available hours
        hours -= allocated_hours
        
    return blocks