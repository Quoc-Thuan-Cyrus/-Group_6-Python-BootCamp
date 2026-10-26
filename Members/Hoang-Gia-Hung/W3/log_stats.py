"""W3-2: Chat log analysis module calculating counts, p95 latency, and slowest route."""

import math
from collections import Counter, defaultdict
from typing import Any


def analyse(pairs: list[tuple[str, float]]) -> dict[str, Any]:
    """Analyse request log pairs and compute route frequency and latency metrics.

    Args:
        pairs: A list of (route, latency_ms) tuples.

    Returns:
        A dictionary containing:
            - "counts": Counter of requests per route.
            - "p95": Dictionary mapping each route to its 95th percentile latency (ms).
            - "slowest": Route with the highest p95 latency, or None if pairs is empty.
    """
    counts: Counter[str] = Counter()
    latencies_by_route: defaultdict[str, list[float]] = defaultdict(list)

    for route, latency in pairs:
        counts[route] += 1
        latencies_by_route[route].append(latency)

    p95_by_route: dict[str, float] = {}
    for route, latencies in latencies_by_route.items():
        sorted_lats = sorted(latencies)
        # Nearest-rank method for 95th percentile
        idx = max(0, math.ceil(0.95 * len(sorted_lats)) - 1)
        p95_by_route[route] = sorted_lats[idx]

    slowest_route: str | None = (
        max(p95_by_route, key=lambda k: p95_by_route[k]) if p95_by_route else None
    )

    return {
        "counts": counts,
        "p95": p95_by_route,
        "slowest": slowest_route,
    }
