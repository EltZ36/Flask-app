from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from project import app,db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
   manager.run()

data = {
  'key':'value',
  'key2':'value',
}