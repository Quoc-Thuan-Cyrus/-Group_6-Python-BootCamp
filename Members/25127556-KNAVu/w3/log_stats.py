from collections import Counter, defaultdict
import math

def analyse(pairs: list[tuple[str, float]]) -> dict:
    if not pairs:
        return {"counts": {}, "p95": {}, "slowest": None}
    counts = Counter()
    route_latencies = defaultdict(list)
    for route, latency in pairs:
        counts[route] += 1
        route_latencies[route].append(latency)
    p95_dict = {}
    for route, latencies in route_latencies.items():
        sorted_lat = sorted(latencies)
        k = math.ceil(0.95 * len(sorted_lat)) - 1
        p95_dict[route] = sorted_lat[max(0, k)]
    slowest_route = max(p95_dict, key=p95_dict.get) if p95_dict else None
    return {"counts": dict(counts), "p95": p95_dict, "slowest": slowest_route}
