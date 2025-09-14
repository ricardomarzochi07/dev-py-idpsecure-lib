from fastapi import FastAPI, Depends
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from buddybet_idpsecure.fastapi_authorization import FastAPIAuthorization
from buddybet_idpsecure.core.environment_config import AppConfigEnvironment, AppConfig
from buddybet_idpsecure.user_claims import UserClaims

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
# FastAPI App
# ==========================
app = FastAPI()

# ==========================
# Sobrescribimos la dependencia para tests
# ==========================
bearer = HTTPBearer(auto_error=False)


async def get_test_user(credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    auth = FastAPIAuthorization(config=app_config)
    return await auth(credentials)


app.dependency_overrides[FastAPIAuthorization] = get_test_user


@app.get("/me")
async def me(user: UserClaims = Depends(FastAPIAuthorization)):
    print("Sub del usuario:", user.sub)  # imprime el sub

    return user


client = TestClient(app)

# ==========================
# Tokens de prueba
# ==========================
TOKEN_VALID = "eyJ4NXQiOiJjZmNONHdac21NMWxtOXBXX2xFUl9LS3ZwRmMiLCJraWQiOiJPV0ptTnpneU5UTmhNR05pTXpFMU5HUTNaall4WlRVellUSTJNbVpoWlRFeVl6SmtZVGRsTURCallqSTJNRE5sWldJeFltUTJNRGt6WVdZNU9ERm1aUV9SUzI1NiIsInR5cCI6ImF0K2p3dCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJXWVlmaWoxTVFnQ0wyS1JNeUVWaWJvT2ZqRXNhIiwiYXV0IjoiQVBQTElDQVRJT04iLCJpc3MiOiJodHRwczpcL1wvbG9jYWxob3N0Ojk0NDNcL29hdXRoMlwvdG9rZW4iLCJjbGllbnRfaWQiOiJXWVlmaWoxTVFnQ0wyS1JNeUVWaWJvT2ZqRXNhIiwiYXVkIjpbIldZWWZpajFNUWdDTDJLUk15RVZpYm9PZmpFc2EiLCJzaWdudXAtc2VydmljZSJdLCJuYmYiOjE3NTc4ODA3OTgsImF6cCI6IldZWWZpajFNUWdDTDJLUk15RVZpYm9PZmpFc2EiLCJvcmdfaWQiOiIxMDA4NGE4ZC0xMTNmLTQyMTEtYTBkNS1lZmUzNmIwODIyMTEiLCJleHAiOjE3NTc4ODQzOTgsIm9yZ19uYW1lIjoiU3VwZXIiLCJpYXQiOjE3NTc4ODA3OTgsImp0aSI6IjFiZWE3NjhiLTUyYzAtNDVmZC1iMzdkLTcwMmVhZjM3YjY2MiIsIm9yZ19oYW5kbGUiOiJjYXJib24uc3VwZXIifQ.jrBLQ7uOAnNmA2gsJ5bpdIvpDN6ObZ_SbNm-8TI87iMQ_Vi5bEtlG5eE3KUcAKgKS3tKdWR04vvm_KixG37fbUrygHper9WGotTGoxAednP_zRbfqjOiJlg0vJvc2lpAOHIP1yJM9VAEPgQBZV9_qs3ohPxwZMHBb9pPVpeDlXWb_OmMoprHJViXaC7dDxrzZA397hsBy4Z8JhprcDLkkACMDiB3on2TBRCH0k35HkcQSCgQj8rY7wSWaXQ9OFuEOaZTszEbAfDNpOrSywUV2uhWcIgzZCOimlTellx-H1HteZqToTtOSIA61ZmD-7TmOxuHawp5ZDsNd2ij1NrVVQ"
TOKEN_INVALID = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0LXVzZXIiLCJhdWQiOiJzaWdudXAiLCJpc3MiOiJodHRwczovL2xvY2FsaG9zdDo5NDQzL29hdXRoMi90b2tlbiIsImV4cCI6MTc1Nzg3NDE3NiwibmJmIjoxNzU3ODczODc2fQ.RV1HyHy0PHA-6otu1VSJOP_IsDTnTWS1rQni1f0GYSWJntoWYcwXluiZwu39LAK2RjXKJS1S3JQJ2IeXihWFl0HKG_wj-NW1Jv_neRzyaQiHPzQibUx4R-MtRdrtDkjqB-d7gDv4hgjRANCzDvhGFxM-R_oZMDHDmG-3l_Y-c175zYJbOxfLUXLGbL7uyiOaGtUTsLncrQo6Ad98a7zX4aEGTFTelSi4kBC0IMuucFEYwZdaGoG_qDd7ICot9N8_wwBn5QPwItNuPwMFprVCbg1TaM36C__YXI7G8Md4eI8JuKDWR4r34ATU9qf3sbctrvTw614UhwGrynbUbkWjuA"


# ==========================
# Tests
# ==========================
def test_token_invalido():
    response = client.get("/me", headers={"Authorization": f"Bearer {TOKEN_INVALID}"})
    assert response.status_code == 401
    assert "Invalid" in response.json()["detail"] or "expired" in response.json()["detail"]


def test_token_valido():
    response = client.get("/me", headers={"Authorization": f"Bearer {TOKEN_VALID}"})
    assert response.status_code == 200
    data = response.json()
    print("Sub del usuario:", data.get("sub"))  # imprime el sub

    # Validamos que el payload tenga campos específicos
    assert "sub" in data
    assert data["sub"] == "WYYfij1MQgCL2KRMyEViboOfjEsa"  # o el valor esperado