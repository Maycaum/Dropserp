from app import app

if __name__ == "__main__": 
    app.run(debug=False)
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 300