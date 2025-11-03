from buddybet_idpsecure.authorization.transaction_auth import TransactionAuthorization
from buddybet_idpsecure.core.environment_config import AppConfigEnvironment, AppConfig
from buddybet_idpsecure.model.user_claims import UserClaims
import pytest

# ==========================
# Configuración de prueba
# ==========================
env_config = AppConfigEnvironment(
    idp_jwks_uri= "https://localhost:9443/oauth2/jwks",
    idp_openid_uri= "https://localhost:9443/oauth2/token/.well-known/openid-configuration",
    ttl= 3600,
    expected_audience= "signup-service",
    audience_signin= "IXmvCyqdfiVOUdNtNcO8QUPzS8ga",
    issuer= "https://localhost:9443/oauth2/token",
    algorithm= "RS256",
)

app_config = AppConfig(
    idp_lib_env=env_config
)



# ==========================
# Tokens de prueba
# ==========================
ACCESS_TOKEN = "eyJ4NXQiOiJjZmNONHdac21NMWxtOXBXX2xFUl9LS3ZwRmMiLCJraWQiOiJPV0ptTnpneU5UTmhNR05pTXpFMU5HUTNaall4WlRVellUSTJNbVpoWlRFeVl6SmtZVGRsTURCallqSTJNRE5sWldJeFltUTJNRGt6WVdZNU9ERm1aUV9SUzI1NiIsInR5cCI6ImF0K2p3dCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxYWRhMGMxZS03MjFkLTQ4YWUtOTFmOS1jOThjYzdjODg2YTIiLCJhdXQiOiJBUFBMSUNBVElPTl9VU0VSIiwiYmluZGluZ190eXBlIjoic3NvLXNlc3Npb24iLCJpc3MiOiJodHRwczpcL1wvbG9jYWxob3N0Ojk0NDNcL29hdXRoMlwvdG9rZW4iLCJjbGllbnRfaWQiOiJJWG12Q3lxZGZpVk9VZE50TmNPOFFVUHpTOGdhIiwiYXVkIjpbIklYbXZDeXFkZmlWT1VkTnROY084UVVQelM4Z2EiLCJidWRkeWJldHMtY2xpZW50X2xvZ2luIl0sIm5iZiI6MTc2MjIwMDE3NywiYXpwIjoiSVhtdkN5cWRmaVZPVWROdE5jTzhRVVB6UzhnYSIsIm9yZ19pZCI6IjEwMDg0YThkLTExM2YtNDIxMS1hMGQ1LWVmZTM2YjA4MjIxMSIsInNjb3BlIjoiZW1haWwgb3BlbmlkIHByb2ZpbGUiLCJleHAiOjE3NjIyMDM3NzcsIm9yZ19uYW1lIjoiU3VwZXIiLCJpYXQiOjE3NjIyMDAxNzcsImJpbmRpbmdfcmVmIjoiZmQ0OWMxY2NhNWQwMDZhNzU2OTdlOTRlODcyN2ZhMDUiLCJqdGkiOiI2Y2NjY2IwYy0xY2Q2LTQ4OGEtYWExMy1iNjY2YTBkNGUxY2UiLCJvcmdfaGFuZGxlIjoiY2FyYm9uLnN1cGVyIn0.fTpzIV7xm45jsEyCIkayN-EOun0A6nf9DlSvhLQ02UnVEgRpy-B45TWipCf4oi-GoBGxZHbN_3cSqKN5txBdiT1Y5hdNUBGh3lO1MIuGOUAbwj48Jtno_PAF5f1qf6J4eN8SdslQnA6vowA6s_cA7e98IeidER1sYq9_c55MmIqQVSVGhZGh6AQ_Xdgwmthu0Ng6HGUsNSiVGU4-yuezdY9K0Cnmit3dcBYFO_ovTvHabI3JFfxX5StnLMhFuNCuKFH54JssNj8559nutnZk5jH5KH8ZBuSI3ZJ0lxBw-2VOqnmXjDK4OS_pIq0qJt1FqvkJEyB-Xux5ASNuGh6g2Q"


# ==========================
# Tests unitarios
# ==========================

@pytest.fixture(autouse=True)
def set_env(monkeypatch):
    monkeypatch.setenv("APP_ENV", "local")

@pytest.mark.asyncio
async def test_id_token():
    auth = TransactionAuthorization(ACCESS_TOKEN)
    user: UserClaims = await auth.transaction_valid(None)
    print(" ROLE ", user.scope)
    assert isinstance(user, UserClaims)

