from collections import Counter, defaultdict
import math

def analyse(pairs: list[tuple[str, float]]) -> dict:
    counts = Counter()
    latencies_by_route = defaultdict(list)
    
    for route, latency in pairs:
        counts[route] += 1
        latencies_by_route[route].append(latency)
        
    p95_by_route = {}
    for route, latencies in latencies_by_route.items():
        sorted_lats = sorted(latencies)
        # Calculate 95th percentile using the nearest rank method
        idx = max(0, math.ceil(0.95 * len(sorted_lats)) - 1)
        p95_by_route[route] = sorted_lats[idx]
        
    slowest_route = max(p95_by_route, key=p95_by_route.get) if p95_by_route else None
    
    return {
        "counts": counts,
        "p95": p95_by_route,
        "slowest": slowest_route
    }