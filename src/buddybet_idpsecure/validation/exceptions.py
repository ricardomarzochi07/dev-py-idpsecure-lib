class JWTValidationError(Exception):
    """Base class for JWT validation errors"""
    pass


class InvalidSignature(JWTValidationError):
    pass


class ExpiredToken(JWTValidationError):
    pass


class InvalidAudience(JWTValidationError):
    pass


class InvalidIssuer(JWTValidationError):
    pass


class InvalidNotBefore(JWTValidationError):
    pass


class InvalidClaims(JWTValidationError):
    pass


class InvalidToken(JWTValidationError):
    pass

