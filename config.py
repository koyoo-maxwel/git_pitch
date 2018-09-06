import os

class Config:
    '''
    Describes the general configurations
    '''
   
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
    
    DEBUG = True

class TestConfig(Config):
    '''
    Test configuration child class
    
    Args:
        Config: The parent configuration class with general configuration settings
    '''
   

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}