from moderation_service import app
from moderation_service import BASIC_APP_AUTH_KEY
from http_constants.status import HttpStatus
from http_constants.headers import HttpHeaders


def test_metrics():
    response = app.test_client().get(
        '/metrics',
        headers={
            HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
            HttpHeaders.AUTHORIZATION: BASIC_APP_AUTH_KEY
        }
    )
    result = response.json

    assert response.status_code == HttpStatus.OK
    assert ['requests', 'elapsed_seconds'].sort() == list(result.keys()).sort()


def test_moderation_ok():
    response = app.test_client().post(
        '/moderation',
        json={'content': 'text'},
        headers={
            HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
            HttpHeaders.AUTHORIZATION: BASIC_APP_AUTH_KEY
        }
    )
    result = response.json

    assert response.status_code == HttpStatus.OK
    assert ['OK', 'H', 'SH', 'V', 'HR', 'V2', 'S', 'S3', 'H2'].sort() == list(result.keys()).sort()
    assert "OK" == max(result, key=result.get)


def test_moderation_nok():
    response = app.test_client().post(
        '/moderation',
        json={
            'content': 'lets build the wall and deport illegals "they walk across the border like this is Central park"'
        },
        headers={
            HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
            HttpHeaders.AUTHORIZATION: BASIC_APP_AUTH_KEY
        }
    )
    result = response.json

    assert response.status_code == HttpStatus.OK
    assert ['OK', 'H', 'SH', 'V', 'HR', 'V2', 'S', 'S3', 'H2'].sort() == list(result.keys()).sort()
    assert "OK" != max(result, key=result.get)


def test_metrics_forbidden():
    # without authorization header
    response = app.test_client().get(
        '/metrics'
    )
    assert response.status_code == HttpStatus.FORBIDDEN

    # with wrong authorization header
    response = app.test_client().get(
        '/metrics',
        headers={
            HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
            HttpHeaders.AUTHORIZATION: 'WRONG'
        }
    )
    assert response.status_code == HttpStatus.FORBIDDEN


def test_moderation_forbidden():
    # without authorization header
    response = app.test_client().post(
        '/moderation',
        json={'content': 'text'}
    )
    assert response.status_code == HttpStatus.FORBIDDEN

    # with wrong authorization header
    response = app.test_client().post(
        '/moderation',
        json={
            'content': 'lets build the wall and deport illegals "they walk across the border like this is Central park"'
        },
        headers={
            HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
            HttpHeaders.AUTHORIZATION: 'WRONG'
        }
    )
    assert response.status_code == HttpStatus.FORBIDDEN


def test_resource_unknown():
    response = app.test_client().get('/unknown')
    assert response.status_code == HttpStatus.NOT_FOUND


def test_bad_request():
    response = app.test_client().post(
        '/moderation',
        json={'unknown': 'text'},
        headers={
            HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
            HttpHeaders.AUTHORIZATION: BASIC_APP_AUTH_KEY
        }
    )
    assert response.status_code == HttpStatus.INTERNAL_SERVER_ERROR


def test_metrics_reset():
    # forcing reset
    app.test_client().get(
        '/metrics',
        headers={
            HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
            HttpHeaders.AUTHORIZATION: BASIC_APP_AUTH_KEY
        }
    )

    # updating stats
    app.test_client().post(
        '/moderation',
        json={'content': 'text'},
        headers={
            HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
            HttpHeaders.AUTHORIZATION: BASIC_APP_AUTH_KEY
        }
    )
    app.test_client().post(
        '/moderation',
        json={'content': 'text'},
        headers={
            HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
            HttpHeaders.AUTHORIZATION: BASIC_APP_AUTH_KEY
        }
    )

    # retrieve latest
    response = app.test_client().get(
        '/metrics',
        headers={
            HttpHeaders.CONTENT_TYPE: HttpHeaders.CONTENT_TYPE_VALUES.json,
            HttpHeaders.AUTHORIZATION: BASIC_APP_AUTH_KEY
        }
    )
    result = response.json

    assert response.status_code == HttpStatus.OK
    assert ['requests', 'elapsed_seconds'].sort() == list(result.keys()).sort()
    assert response.json['requests'] == 2

