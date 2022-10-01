from app import app

if __name__ == "__main__": 
    app.run(debug=True)
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = 300