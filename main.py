import base64, json, logging
from google.cloud import aiplatform, bigquery

PROJECT_ID = "cyber-threat-intel-platform"
REGION = "us-central1"
ENDPOINT_ID = "<your-endpoint-id>"

def predict_threat(instance):
    aiplatform.init(project=PROJECT_ID, location=REGION)
    endpoint = aiplatform.Endpoint(endpoint_name=ENDPOINT_ID)
    return endpoint.predict(instances=[instance])

def log_to_bigquery(data):
    client = bigquery.Client()
    table_id = f"{PROJECT_ID}.threat_logs.threat_predictions"
    client.insert_rows_json(table_id, [data])

def pubsub_trigger(event, context):
    try:
        message = base64.b64decode(event["data"]).decode("utf-8")
        log_entry = json.loads(message)
        instance = {
            "src_ip": log_entry.get("src_ip"),
            "dest_ip": log_entry.get("dest_ip"),
            "bytes_sent": log_entry.get("bytes_sent", 0),
            "bytes_received": log_entry.get("bytes_received", 0)
        }
        result = predict_threat(instance)
        score = result.predictions[0] if result.predictions else 0.0
        log_entry["threat_score"] = score
        if score > 0.7:
            log_to_bigquery(log_entry)
    except Exception as e:
        logging.error(f"Error: {e}")