class Variables:
    
    HOST = "127.0.0.1"
    HTTP_PORT=8080 
    HTTPS_PORT=8443
    
    ACCEPT_HTTPS_TRAFFIC = True
    ACCEPT_HTTP_TRAFFIC = True
    
    ROOT = "./data"
    
    PATH_TO_SSL_CERTIFICATE = "./ssl/certificate.pem"
    PATH_TO_SSL_PRIVATE_KEY = "./ssl/private_key.pem"
    
    FORM_SAFE = True

    COMPATIBLE_FILES = {
        "html": "text/html",
        "css": "text/css",
        "js": "application/javascript",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "gif": "image/gif",
        "ico": "image/x-icon",
        "svg": "image/svg+xml",
        "csv": "text/plain",
        "txt": "text/plain",
        "json": "application/json",
        "xml": "application/xml",
        "webmanifest": "application/manifest+json"
    }

