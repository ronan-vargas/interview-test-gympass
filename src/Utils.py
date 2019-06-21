from datetime import datetime, timedelta
class Utils:
    def converter_string_para_hora_volta(self, hora_string):
        return datetime.strptime(hora_string, '%H:%M:%S.%f')

    def converter_string_para_tempo_volta(self, tempo_string):
        d = datetime.strptime(tempo_string, '%M:%S.%f')
        return timedelta(minutes=d.minute, seconds=d.second, microseconds=d.microsecond)