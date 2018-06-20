DEBUG = True
SECRET_KEY = 'appleservicechallengesecretkey'

MYSQL_DATABASE_USER='root'
MYSQL_DATABASE_PASSWORD='MyNewPass'
MYSQL_DATABASE_DB = 'appleservicechallenge'
MYSQL_DATABASE_HOST = 'localhost'
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 1800
JWT_OPTIONS = {
        'verify_signature': True,
        'verify_exp': True,
        'verify_nbf': False,
        'verify_iat': False,
        'verify_aud': True,
        'verify_iss': True,
        'require_exp': True,
        'require_iat': False,
        'require_nbf': False
    }

