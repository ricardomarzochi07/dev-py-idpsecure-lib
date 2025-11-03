import pytest
from buddybet_idpsecure.validation.validator import TokenValidator
from buddybet_idpsecure.core.settings_config import load_config


# EJECUTAR:
# $env:APP_ENV="local"; pytest -v tests_validate_wso2_id_token.py
class TestValidateWSO2IdToken:
    """
    Prueba real de validate_wso2_id_token().
    """

    @pytest.fixture(scope="class")
    def validator(self):
        """Crea el validador con la configuración real del entorno (por ejemplo, DEV)."""
        config = load_config()
        return TokenValidator(config)

    def test_validate_token_valido(self, validator):
        """
        ✅ Caso: token válido emitido por WSO2.
        Sustituye el token por uno real obtenido desde tu flujo de login.
        """
        TOKEN_ID_TOKEN = "eyJ4NXQiOiJjZmNONHdac21NMWxtOXBXX2xFUl9LS3ZwRmMiLCJraWQiOiJPV0ptTnpneU5UTmhNR05pTXpFMU5HUTNaall4WlRVellUSTJNbVpoWlRFeVl6SmtZVGRsTURCallqSTJNRE5sWldJeFltUTJNRGt6WVdZNU9ERm1aUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJpc2siOiJmOWY0MTdhOGI3NDU1YzhmNzcyODgzNjAwNjRiOTcxODc4MDYyZTllYTcyMDRlNzRkMzEyZDQ2YWIxNTg4NmZkIiwiYXRfaGFzaCI6IjlNRi1BTkV2aDl3VldYOUtrXzhIbnciLCJzdWIiOiIxYWRhMGMxZS03MjFkLTQ4YWUtOTFmOS1jOThjYzdjODg2YTIiLCJhbXIiOlsiQmFzaWNBdXRoZW50aWNhdG9yIl0sImlzcyI6Imh0dHBzOlwvXC9sb2NhbGhvc3Q6OTQ0M1wvb2F1dGgyXC90b2tlbiIsIm5vbmNlIjoiVGVzdGUwMTAxIiwic2lkIjoiYjkyNDZhM2QtZjNlZS00NDRhLTlhZWYtNzdhYjIxNDQ3ODQzIiwiYXVkIjpbIklYbXZDeXFkZmlWT1VkTnROY084UVVQelM4Z2EiLCJidWRkeWJldHMtY2xpZW50X2xvZ2luIl0sImNfaGFzaCI6Im9NcGJpRFdKUVVwVGhaRGVZbFZ3NlEiLCJuYmYiOjE3NjIyMDAxNzcsImF6cCI6IklYbXZDeXFkZmlWT1VkTnROY084UVVQelM4Z2EiLCJvcmdfaWQiOiIxMDA4NGE4ZC0xMTNmLTQyMTEtYTBkNS1lZmUzNmIwODIyMTEiLCJleHAiOjE3NjIyMDM3NzcsIm9yZ19uYW1lIjoiU3VwZXIiLCJpYXQiOjE3NjIyMDAxNzcsImp0aSI6IjdkOTUwMTk3LTFiMzYtNGVkMC1hNDliLWE2NTRhYjllMGZlNyIsIm9yZ19oYW5kbGUiOiJjYXJib24uc3VwZXIiLCJ1c2VybmFtZSI6ImFkbWluIn0.kkZ-FeasvQm7E5rk8V34v5_Uei41O1HUg4bQi3xXebyjOgc-F0_s8gwd1gkGoYfiGH7pMCFT1OWdUB7cYQvIesGB3et9DyeFoid3MnfZP28h2YV66xKM0XJ6fH9jNxox0RpaWWuZaDgFYRJ8R6MN_Uppds0S8PSOP2y4gykDhriTwBo_NkmyOJKtT73iKs2MiMu-y_VkPo7N7bqrtFSPLs7BdeyLRFCbDM0j7C977TSDfbOVH9gkz6wsi9CmY5GyBU1lLWrTn2foYhVoskD2NPqsgl-1QB9oRZKtiKm1imvZNcBhhV3LiTth0GDQLpboc2miHhgbXUTTjDfmlvBrtA"
        ACCESS_TOKEN = "eyJ4NXQiOiJjZmNONHdac21NMWxtOXBXX2xFUl9LS3ZwRmMiLCJraWQiOiJPV0ptTnpneU5UTmhNR05pTXpFMU5HUTNaall4WlRVellUSTJNbVpoWlRFeVl6SmtZVGRsTURCallqSTJNRE5sWldJeFltUTJNRGt6WVdZNU9ERm1aUV9SUzI1NiIsInR5cCI6ImF0K2p3dCIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiIxYWRhMGMxZS03MjFkLTQ4YWUtOTFmOS1jOThjYzdjODg2YTIiLCJhdXQiOiJBUFBMSUNBVElPTl9VU0VSIiwiYmluZGluZ190eXBlIjoic3NvLXNlc3Npb24iLCJpc3MiOiJodHRwczpcL1wvbG9jYWxob3N0Ojk0NDNcL29hdXRoMlwvdG9rZW4iLCJjbGllbnRfaWQiOiJJWG12Q3lxZGZpVk9VZE50TmNPOFFVUHpTOGdhIiwiYXVkIjpbIklYbXZDeXFkZmlWT1VkTnROY084UVVQelM4Z2EiLCJidWRkeWJldHMtY2xpZW50X2xvZ2luIl0sIm5iZiI6MTc2MjIwMDE3NywiYXpwIjoiSVhtdkN5cWRmaVZPVWROdE5jTzhRVVB6UzhnYSIsIm9yZ19pZCI6IjEwMDg0YThkLTExM2YtNDIxMS1hMGQ1LWVmZTM2YjA4MjIxMSIsInNjb3BlIjoiZW1haWwgb3BlbmlkIHByb2ZpbGUiLCJleHAiOjE3NjIyMDM3NzcsIm9yZ19uYW1lIjoiU3VwZXIiLCJpYXQiOjE3NjIyMDAxNzcsImJpbmRpbmdfcmVmIjoiZmQ0OWMxY2NhNWQwMDZhNzU2OTdlOTRlODcyN2ZhMDUiLCJqdGkiOiI2Y2NjY2IwYy0xY2Q2LTQ4OGEtYWExMy1iNjY2YTBkNGUxY2UiLCJvcmdfaGFuZGxlIjoiY2FyYm9uLnN1cGVyIn0.fTpzIV7xm45jsEyCIkayN-EOun0A6nf9DlSvhLQ02UnVEgRpy-B45TWipCf4oi-GoBGxZHbN_3cSqKN5txBdiT1Y5hdNUBGh3lO1MIuGOUAbwj48Jtno_PAF5f1qf6J4eN8SdslQnA6vowA6s_cA7e98IeidER1sYq9_c55MmIqQVSVGhZGh6AQ_Xdgwmthu0Ng6HGUsNSiVGU4-yuezdY9K0Cnmit3dcBYFO_ovTvHabI3JFfxX5StnLMhFuNCuKFH54JssNj8559nutnZk5jH5KH8ZBuSI3ZJ0lxBw-2VOqnmXjDK4OS_pIq0qJt1FqvkJEyB-Xux5ASNuGh6g2Q"
        nonce = "Teste0101"
        try:
            claims = validator.validate_wso2_id_token(id_token=TOKEN_ID_TOKEN,
                                                      access_token=ACCESS_TOKEN,
                                                      nonce=nonce)
            assert isinstance(claims, dict)
            assert "iss" in claims
            print("✅ Token válido, claims:", claims)
        except ValueError as e:
            pytest.fail(f"❌ Error de validación: {e}")
        except Exception as e:
            pytest.fail(f"⚠️ Error inesperado: {type(e).__name__} → {e}")
