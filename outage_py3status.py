import subprocess

# a py3status module that runs the outage script
# and pipes the output to my status bar
class Py3status:
    
    def outage_py3status(self):
        return {
            'full_text': subprocess.run(['python','/home/flash/Programming/Sideline/Android/Outages/script/outage.py'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip(),
            'cached_until': self.py3.CACHE_FOREVER
        }
