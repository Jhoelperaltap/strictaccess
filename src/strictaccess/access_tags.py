def private(func):
    func._access_level = 'private'
    return func

def protected(func):
    func._access_level = 'protected'
    return func

def public(func):
    func._access_level = 'public'
    return func
