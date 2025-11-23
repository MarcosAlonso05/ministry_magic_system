from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse
import matplotlib
import matplotlib.pyplot as plt
import io
import base64

from app.data.monitoring import metrics_history, update_system_metrics, SPELL_COUNTER
from prometheus_client import generate_latest

matplotlib.use('Agg')

router = APIRouter(prefix="/dashboard", tags=["monitoring"])

@router.get("/metrics")
def get_prometheus_metrics():
    update_system_metrics()
    return Response(content=generate_latest(), media_type="text/plain")

@router.get("/stats", response_class=HTMLResponse)
def get_dashboard_ui():
    plt.figure(figsize=(10, 5))
    
    if metrics_history:
        times = [x["timestamp"] for x in metrics_history]
        durations = [x["duration"] for x in metrics_history]
        start_t = times[0]
        times = [t - start_t for t in times]
        
        plt.plot(times, durations, marker='o', linestyle='-', color='purple')
        plt.title("Magic Performance (Response Time)")
        plt.xlabel("Time elapsed (seconds)")
        plt.ylabel("Casting Duration (s)")
        plt.grid(True)
    else:
        plt.text(0.5, 0.5, "No magic cast yet.", ha='center')

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()

    stats = {}
    for entry in metrics_history:
        t = entry["type"]
        stats[t] = stats.get(t, 0) + 1

    table_rows = "".join([f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in stats.items()])

    html_content = f"""
    <html>
        <head>
            <title>Ministry of Magic - Overwatch</title>
            <style>
                body {{ font-family: Arial, sans-serif; padding: 20px; background-color: #f0f0f0; }}
                .container {{ max-width: 1000px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
                h1 {{ color: #4a148c; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
                th, td {{ padding: 10px; border: 1px solid #ddd; text-align: left; }}
                th {{ background-color: #4a148c; color: white; }}
                img {{ max-width: 100%; height: auto; margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Ministry of Magic - Real Time Dashboard</h1>
                
                <h2>System Performance</h2>
                <img src="data:image/png;base64,{img_base64}" />
                
                <h2>Magic Events by Type</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Magic Type</th>
                            <th>Count</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_rows}
                    </tbody>
                </table>
                
                <p><em>Check <a href="/dashboard/metrics">/dashboard/metrics</a> for Prometheus raw data.</em></p>
            </div>
        </body>
    </html>
    """
    return html_content