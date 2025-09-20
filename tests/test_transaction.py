from buddybet_idpsecure.authorization.transaction_auth import TransactionAuthorization
from buddybet_idpsecure.core.environment_config import AppConfigEnvironment, AppConfig
from buddybet_idpsecure.model.user_claims import UserClaims
import pytest

# ==========================
# Configuración de prueba
# ==========================
env_config = AppConfigEnvironment(
    idp_certificates_url="https://localhost:9443/oauth2/jwks",
    ttl=3600,
    expected_audience="signup-service",
    issuer="https://localhost:9443/oauth2/token"
)

app_config = AppConfig(
    idp_lib_env=env_config
)

# ==========================
# Tokens de prueba
# ==========================
TOKEN_VALID = "eyJ4NXQiOiJjZmNONHdac21NMWxtOXBXX2xFUl9LS3ZwRmMiLCJraWQiOiJPV0ptTnpneU5UTmhNR05pTXpFMU5HUTNaall4WlRVellUSTJNbVpoWlRFeVl6SmtZVGRsTURCallqSTJNRE5sWldJeFltUTJNRGt6WVdZNU9ERm1aUV9SUzI1NiIsInR5cCI6ImF0K2p3dCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJXWVlmaWoxTVFnQ0wyS1JNeUVWaWJvT2ZqRXNhIiwiYXV0IjoiQVBQTElDQVRJT04iLCJpc3MiOiJodHRwczpcL1wvbG9jYWxob3N0Ojk0NDNcL29hdXRoMlwvdG9rZW4iLCJjbGllbnRfaWQiOiJXWVlmaWoxTVFnQ0wyS1JNeUVWaWJvT2ZqRXNhIiwiYXVkIjpbIldZWWZpajFNUWdDTDJLUk15RVZpYm9PZmpFc2EiLCJzaWdudXAtc2VydmljZSJdLCJuYmYiOjE3NTgzNjU3NjcsImF6cCI6IldZWWZpajFNUWdDTDJLUk15RVZpYm9PZmpFc2EiLCJvcmdfaWQiOiIxMDA4NGE4ZC0xMTNmLTQyMTEtYTBkNS1lZmUzNmIwODIyMTEiLCJzY29wZSI6ImludGVybmFsX3VzZXJfbWd0X2NyZWF0ZSIsImV4cCI6MTc1ODM2OTM2Nywib3JnX25hbWUiOiJTdXBlciIsImlhdCI6MTc1ODM2NTc2NywianRpIjoiY2ZmOGJhMjQtNDIwMy00Yjk5LTgyYjYtN2JlMTMyMDMzNjEwIiwib3JnX2hhbmRsZSI6ImNhcmJvbi5zdXBlciJ9.VyjrZ8kBiepESnGk8R5dHtP05BlQ9UPFEokQ9h-g8f9SOQxQIFFYFxJTe1ZrQ2kwavDNPziNXNKP-N_nRcMrXqX6o_vHdPzH8LssROOEZWLss2ZnTORxP-DMAzkTEtNm1H16PawxWk104NRePFrSAt5mpViHRsp0B6ZM63R7p0JP7RXQXoyy5ppKNAUi64gp4NAW0i03vQ39UToClmcyB4LXsSibeC5_QOCMk7n13iZVyhF8ALwV9ooYm8b6r3avXEFicMSr-fs-tgMNh-f9padl53xCsBlOUmCEIfU98qJ9AfJCsRE3r0ZLekujzBQ_6g8JlwmwJJwsXDD8CfaOZQ"
TOKEN_INVALID = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0LXVzZXIiLCJhdWQiOiJzaWdudXAiLCJpc3MiOiJodHRwczovL2xvY2FsaG9zdDo5NDQzL29hdXRoMi90b2tlbiIsImV4cCI6MTc1Nzg3NDE3NiwibmJmIjoxNzU3ODczODc2fQ.RV1HyHy0PHA-6otu1VSJOP_IsDTnTWS1rQni1f0GYSWJntoWYcwXluiZwu39LAK2RjXKJS1S3JQJ2IeXihWFl0HKG_wj-NW1Jv_neRzyaQiHPzQibUx4R-MtRdrtDkjqB-d7gDv4hgjRANCzDvhGFxM-R_oZMDHDmG-3l_Y-c175zYJbOxfLUXLGbL7uyiOaGtUTsLncrQo6Ad98a7zX4aEGTFTelSi4kBC0IMuucFEYwZdaGoG_qDd7ICot9N8_wwBn5QPwItNuPwMFprVCbg1TaM36C__YXI7G8Md4eI8JuKDWR4r34ATU9qf3sbctrvTw614UhwGrynbUbkWjuA"


# ==========================
# Tests unitarios
# ==========================
@pytest.mark.asyncio
async def test_token_valido():
    auth = TransactionAuthorization(TOKEN_VALID)
    user: UserClaims = await auth.transaction_valid(app_config)
    print(" ROLE ", user.scope)
    assert isinstance(user, UserClaims)


@pytest.mark.asyncio
async def test_token_invalido():
    auth = TransactionAuthorization(TOKEN_INVALID)
    user: UserClaims = await auth.transaction_valid(app_config)
    assert isinstance(user, UserClaims)

