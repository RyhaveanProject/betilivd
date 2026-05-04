# app.py - Railway/Render için entry point
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

# Direkt exploit.py'yi import et ve web modunda çalıştır
exec(open("exploit.py").read())

if __name__ == "__main__":
    # Web modu için environment variable
    os.environ.setdefault("MODE", "web")
    sys.argv = ["exploit.py", "web"]
    main()
