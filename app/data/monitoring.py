from prometheus_client import Counter, Histogram, Gauge
import psutil
import time

SPELL_COUNTER = Counter(
    "magic_spells_total", 
    "Total number of spells cast", 
    ["spell_type", "status"]
)

SPELL_LATENCY = Histogram(
    "magic_spell_latency_seconds",
    "Time taken to process magic",
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0] # Time buckets
)

SYSTEM_CPU = Gauge("system_cpu_usage_percent", "Current CPU usage percentage")
SYSTEM_MEMORY = Gauge("system_memory_usage_percent", "Current RAM usage percentage")

metrics_history = []

def record_spell_metric(spell_type: str, status: str, duration: float):
    SPELL_COUNTER.labels(spell_type=spell_type, status=status).inc()
    SPELL_LATENCY.observe(duration)
    
    metrics_history.append({
        "timestamp": time.time(),
        "type": spell_type,
        "duration": duration
    })
    if len(metrics_history) > 100:
        metrics_history.pop(0)

def update_system_metrics():
    SYSTEM_CPU.set(psutil.cpu_percent())
    SYSTEM_MEMORY.set(psutil.virtual_memory().percent)