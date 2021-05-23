import os
from management import create_app
from management import db
from management.models import *
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

app = create_app(os.getenv("FLASK_CONFIG") or "development")
manager = Manager(app)

migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(app=current_app, db=db, S1Data=S1Data,S4Data=S4Data, )


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000")
