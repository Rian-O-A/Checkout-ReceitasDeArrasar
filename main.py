from backend.auth import create_app
from waitress import serve

# serve(create_app(), host="0.0.0.0", port=2000)
create_app().run(host="0.0.0.0", port=2000, debug=False)