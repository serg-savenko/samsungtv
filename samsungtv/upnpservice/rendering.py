#!/usr/bin/env python
from base import UPnPServiceBase


class UPnPServiceRendering(UPnPServiceBase):

    def __init__(self, ip, port="9197", config=None):
        super(UPnPServiceRendering, self).__init__(ip, port)

        self.id = '0'
        self.endpoint = '/dmr/upnp/control/RenderingControl1'
        self.stype = 'RenderingControl'

        if config is not None :
           self.endpoint = config['controlURL']


    def mute(self, mute):
        mute_value = '1' if mute is True else '0'

        action = 'SetMute'
        args = [('InstanceID', self.id), ('Channel', 'Master'), ('DesiredMute', mute_value)]

        response = self._send_cmd(action, args)

        return self._get_result(response)

    def tv_slide_show(self):

        action = 'X_GetTVSlideShow'
        args = [('InstanceID', self.id)]

        response = self._send_cmd(action, args)

        return self._get_result(response)

    def set_tv_slide_show(self, state, theme):

        action = 'X_SetTVSlideShow'
        args = [('InstanceID', self.id), ('CurrentShowState', state), ('CurrentShowTheme', theme)]

        response = self._send_cmd(action, args)

        return self._get_result(response)

    def zoom(self, x, y, w=0, h=0):

        action = 'X_SetZoom'
        args = [('InstanceID', self.id), ('x', x), ('y', y), ('w', w), ('h', h)]

        response = self._send_cmd(action, args)
        print response
        return self._get_result(response)

    def audio_selection(self):

        action = 'X_GetAudioSelection'
        args = [('InstanceID', self.id)]

        response = self._send_cmd(action, args)

        return self._get_result(response)

    def video_selection(self):

        action = 'X_GetVideoSelection'
        args = [('InstanceID', self.id)]

        response = self._send_cmd(action, args)

        return self._get_result(response)

    def presets(self):

        action = 'ListPresets'
        args = [('InstanceID', self.id)]

        response = self._send_cmd(action, args)

        return self._get_result(response)

    def select_preset(self, name=""):

        action = 'SelectPreset'
        args = [('InstanceID', self.id), ("PresetName", name)]

        response = self._send_cmd(action, args)

        return self._get_result(response)

    def volume(self, volume=False):
        if volume:

            action = 'SetVolume'
            args = [('InstanceID', self.id), ('Channel', 'Master'), ('DesiredVolume', volume)]

            response = self._send_cmd(action, args)

            return self._get_result(response)

        else:

            action = 'GetVolume'
            args = [('InstanceID', self.id), ('Channel', 'Master')]

            response = self._send_cmd(action, args)

            result = self._get_result(response)

            return int(result['CurrentVolume'])

