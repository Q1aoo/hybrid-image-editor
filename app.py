import json, os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import model  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
SCHEMA = {"reply": str, "options": list, "action": (dict, type(None)), "unsupported_claims": list}

def fallback_turn():
    """A malformed reply is a caught error, never a blank page."""
    return {"reply": "I could not read the reply, so I have not changed anything. Try again or ask the module lead.",
            "options": [], "action": None, "unsupported_claims": []}

def turn(message):
    # 这是你上周写的核心系统指令
    system_instruction = """You are an intent parser for an image editing tool. 
    You will receive a user's text prompt. 
    You must output ONLY a valid JSON object with the following keys:
    - "operation" (e.g., add, remove, modify)
    - "target_object" (what the user wants to affect)
    - "attributes" (any specific details like color, size, etc.)
    If the prompt is ambiguous or asks for global changes (like changing the whole style), output a JSON with a single key "error" explaining the issue.
    
    Format your response to fit this schema:
    Put your conversational response or error message in 'reply'.
    Put the extracted JSON parsing result in 'action'.
    Keep 'options' and 'unsupported_claims' as empty lists.
    
    User Prompt: """
    
    full_message = system_instruction + (message or "")
    
    data = model.call_json([{"role": "user", "content": full_message}], SCHEMA)
    
    if isinstance(data, dict) and all(k in data and isinstance(data[k], t) for k, t in SCHEMA.items()):
        return data
    else:
        return fallback_turn()

class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        self.send_response(code); self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)

    def do_GET(self):
        with open(os.path.join(HERE, "index.html"), "rb") as f:
            self._send(200, f.read(), "text/html; charset=utf-8")

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        msg = json.loads(self.rfile.read(n).decode("utf-8")).get("message", "")
        self._send(200, json.dumps(turn(msg)).encode("utf-8"))

    def log_message(self, *a):
        pass

if __name__ == "__main__":
    print("serving on http://localhost:8000")
    HTTPServer(("localhost", 8000), Handler).serve_forever()