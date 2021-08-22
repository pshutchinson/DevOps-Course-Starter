PORT=$1
exec gunicorn 'todo_app.app:create_app()' \
    --bind '0.0.0.0:${PORT}'