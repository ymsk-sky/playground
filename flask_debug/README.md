# flask_debug
Flaskでアプリケーション実行時に, 別プロセス(`main.py`では`mc`)を作成すると初期化が2回発生する.

以下が起動時のログ.

```python
> python main.py
initialized
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:8000
Press CTRL+C to quit
 * Restarting with stat
initialized
 * Debugger is active!
 * Debugger PIN: 322-492-692
```

`debug`だとこの症状が発生する.

`use_reloader`引数を記述することで解決できる.

```python
app.run(host="localhost", port=8000, debug=True, use_reloader=False)
```
