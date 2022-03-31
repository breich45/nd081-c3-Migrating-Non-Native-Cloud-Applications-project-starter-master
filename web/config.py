import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="121migrationdb.postgres.database.azure.com"
    POSTGRES_USER="azureuser"
    POSTGRES_PW="storage55!"
    POSTGRES_DB="121migration-db"
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING =''Endpoint=sb://servicebus121.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=t3OUYwCQ2gz+4U6LjrXMsQ6quIdQrt595ys3rjbNY64=""
    SERVICE_BUS_QUEUE_NAME ='121notificationqueue'
    ADMIN_EMAIL_ADDRESS: 'brent.reich@gmail.com'
    SENDGRID_API_KEY = ''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"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False