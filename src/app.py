from shiny import App, ui, render, reactive
import redis
import sys
import socket

def find_free_port(start_port=8000, max_port=8999):
    """Find a free port in the given range."""
    for port in range(start_port, max_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind(('127.0.0.1', port))
                return port
            except OSError:
                continue
    raise RuntimeError("No free ports found in range")

# Initialize Redis connection
try:
    redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    # Test the connection
    redis_client.ping()
except redis.ConnectionError as e:
    print("Error connecting to Redis. Make sure Redis server is running.")
    print(f"Error details: {e}")
    sys.exit(1)

app_ui = ui.page_fluid(
    ui.h1("Redis-Powered Shiny App"),
    ui.input_text("name", "What's your name?", ""),
    ui.input_text("message", "Leave a message:", ""),
    ui.input_action_button("submit", "Submit!", class_="btn-primary"),
    ui.output_text("visitor_count"),
    ui.output_ui("messages")
)

def server(input, output, session):
    # Create reactive values
    count = reactive.Value(0)
    
    @reactive.Effect
    def _():
        # Update count when app starts and after each submit
        count.set(redis_client.incr('visitor_count'))
    
    @reactive.Effect
    @reactive.event(input.submit)
    def _():
        name = input.name()
        message = input.message()
        if name and message:
            # Store message in Redis
            full_message = f"{name}: {message}"
            redis_client.lpush('messages', full_message)
    
    @output
    @render.text
    def visitor_count():
        return f"Visitor count: {count()}"
    
    @output
    @render.ui
    def messages():
        # Get last 5 messages
        messages = redis_client.lrange('messages', 0, 4)
        if not messages:
            return ui.p("No messages yet!")
        
        return ui.tags.div(
            ui.h3("Recent Messages:"),
            ui.tags.ul([
                ui.tags.li(msg) for msg in messages
            ])
        )

# Create the app instance
app = App(app_ui, server)

if __name__ == "__main__":
    try:
        free_port = find_free_port()
        print(f"Starting app on port {free_port}")
        app.run(
            port=free_port,
            host="127.0.0.1",
            reload=True
        )
    except Exception as e:
        print(f"Error starting the app: {e}")
        sys.exit(1)
