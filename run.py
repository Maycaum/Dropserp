from app import app

if __name__ == "__main__": 
    app.run()
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 300