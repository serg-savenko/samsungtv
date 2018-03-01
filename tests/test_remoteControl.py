import json

import mock
from unittest import TestCase
from samsungtv.services.remote_control import RemoteControl


def mock_conn(data=None):
    j = json.dumps(data)

    websocket_conn = mock.MagicMock()
    websocket_conn.close.return_value = True
    websocket_conn.connected = True
    websocket_conn.recv.return_value = j

    return websocket_conn


class TestRemoteControl(TestCase):
    def setUp(self):
        self.rc = RemoteControl("192.168.0.100")

    @mock.patch('samsungtv.services.remote_control.websocket')
    def test_connect(self, mock_ws):
        mock_ws.create_connection.return_value = mock_conn({'data': {'id': 'ID_OK'}})

        id = self.rc.connect()
        self.rc.close()

        self.assertIsNotNone(id)
        self.assertEquals(id, u'ID_OK')

    @mock.patch('samsungtv.services.remote_control.websocket')
    def test_command(self, mock_ws):
        mock_ws.create_connection.return_value = mock_conn({'data': {'id': 'ID_OK'}})

        id = self.rc.connect()
        r = self.rc.command("KEY_2")

        self.rc.close()

        self.assertIsNotNone(id)

    @mock.patch('samsungtv.services.remote_control.websocket')
    def test_launch(self, mock_ws):
        mock_ws.create_connection.return_value = mock_conn({'data': {'id': 'ID_OK'}})
        id = self.rc.connect()
        r = self.rc.launch("org.tizen.browser")

        self.rc.close()


    # def test_real(self):
    #     rc = RemoteControl("192.168.0.100")
    #
    #     rc.connect()
    #     rc.command("KEY_0")
    #     rc.launch("org.tizen.browser")
    #     rc.close()

