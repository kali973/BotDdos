import logging
import os
import pathlib as pathlib
import platform
import shutil
import sys
import threading
import time


def a():
    os.system("wireshark")


def b():
    os.system("xterm -e \"sudo python slowloris.py\"")


def c():
    os.system("xterm -e \"sudo python synFlooding.py\"")


def d():
    os.system("xterm -e \"sudo wget https://inmon.com/products/sFlow-RT/sflow-rt.tar.gz\"")
    os.system("xterm -e \"sudo tar -xvzf sflow-rt.tar.gz\"")
    os.system("xterm -e \"sudo " + path + "/sflow-rt/get-app.sh sflow-rt browse-metrics\"")
    os.system("xterm -e \"sudo " + path + "/sflow-rt/get-app.sh sflow-rt browse-flows\"")
    os.system("xterm -e \"sudo " + path + "/sflow-rt/get-app.sh sflow-rt ddos-protect\"")
    file = pathlib.Path("sflow-rt.tar.gz")
    if file.exists():
        os.remove(file)


def e():
    os.system("xterm -e \"sudo " + path + "/sflow-rt/start.sh\"")
    os.system("xterm -e \"sudo systemctl restart sflow-rt\"")


def f():
    os.system("google-chrome --no-sandbox http://localhost:8008")


def g():
    os.system("xterm -e \"sudo python ifConfigPython.py\"")


def h():
    os.system("xterm -e \"sudo python icmpFlooding.py\"")


def i():
    os.system("xterm -e \"sudo systemctl status grafana-server\"")


def k():
    os.system("xterm -e \"sudo systemctl status apache_exporter\"")


def l():
    os.system("xterm -e \"sudo systemctl status prometheus\"")


def m():
    os.system("xterm -e \"sudo systemctl status alertmanager.service\"")


def n():
    os.system("xterm -e \"systemctl status influxdb\"")


def o():
    os.system("xterm -e \"systemctl status elasticsearch\"")


def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


logging.disable(sys.maxsize)
number = 1
data = ""
os.system("sudo apt-get install -y xterm")
os.environ['TERM'] = 'xterm'
path = os.getcwd()

while number != '0':

    data += ' ----------------------------\n'
    if os.name == "nt":
        print(' [!] Please run the script on Linux Machine !')
        quit()
    elif os.name != "nt":
        data = (' ----------------------------\n')
        data += ' Hi ' + platform.uname()[
            1] + ' Ce Bot est de type académique et il ne doit pas etre utilisé en dehors de ce cadre !\n'

    data += ' ----------------------------\n'
    data += ' Select option:\n'
    data += ' [1] Start Apache2\n'
    data += ' [2] Stop Apache2\n'
    data += ' [3] ReStart Apache2\n'
    data += ' [4] Open Localhost\n'
    data += ' [5] Show my local Ip Address & Network Interface\n'
    data += ' [6] Scan Network and find target\n'
    data += ' [7] ICMP flooding\n'
    data += ' [8] Attack Slow Loris\n'
    data += ' [9] Attack Ettercap with analyzing Wireshark\n'
    data += ' [A] Installation Grafana, Prometheus, Apache Exporter\n'
    data += ' [B] Launch service Remotely Triggered Black Hole\n'
    data += ' [C] Stop DDOS Attack by Remotely Triggered Black Hole (RTBH) Routing\n'
    data += ' [0] Exit\n'
    print(data)
    number = input(" Number~# ")
    if number == '1':
        print("\n [***] Please wait ...")
        os.system("sudo service apache2 start")
        print(" [I] Apache2 Service has been Started !\n")
        time.sleep(5)
        clear()
        data = ""
    elif number == '2':
        print('\n [***] Please wait ...')
        os.system("sudo service apache2 stop")
        print(" [O] Apache2 Service has been Stoped !\n")
        time.sleep(5)
        clear()
        data = ""
    elif number == '3':
        print('\n [***] Please wait ...')
        os.system("sudo service apache2 restart")
        print(" [R] Apache2 Service has been ReStarted !\n")
        time.sleep(5)
        clear()
        data = ""
    elif number == '4':
        print("\n [***] Please wait ...\n")
        print(" [O] Opening http://127.0.0.1 ...\n")
        os.system("firefox http://127.0.0.1")
        print(" Successfully !\n")
        time.sleep(5)
        clear()
        data = ""
    elif number == '5':
        print("\n Show my local Ip Address & Network Interface ...\n")
        threading.Thread(target=g).start()
        clear()
        data = ""
    elif number == '6':
        print("\n Scan Network and find target...\n")
        os.system("sudo python nmap.py")
        data = ""
    elif number == '7':
        print("\n [ICMP flooding ...\n")
        threading.Thread(target=a).start()
        t = threading.Timer(20, h)
        t.start()
        print("\033[H\033[J", end="")
        data = ""
    elif number == '8':
        print("\n [SlowLoris Attack ...\n")
        threading.Thread(target=a).start()
        s = threading.Timer(20, b)
        s.start()
        print("\033[H\033[J", end="")
        data = ""
    elif number == '9':
        print("\n [Attarck Ettercap with analyzing Wireshark  ...\n")
        os.system("python ettercapAttack.py")
        time.sleep(5)
        clear()
        data = ""
    elif number == 'A':
        print("\n [Installation monitoring ...\n")
        # update system package
        os.system("xterm -e \"sudo apt update && sudo apt install wget curl\"")
        # install nodejs & npm
        os.system("xterm -e \"sudo apt-get install -y nodejs\"")
        os.system("xterm -e \"sudo apt-get install -y npm\"")
        # install wireshark
        os.system("xterm -e \"sudo apt-get install -y wireshark\"")
        # install prometheus
        os.system("xterm -e \"tar -xvf prometheus-files.tar.gz\"")
        os.system("xterm -e \"sudo cp apache_exporter-*.linux-amd64/apache_exporter /usr/local/bin\"")
        os.system("sudo chmod +x /usr/local/bin/apache_exporter")
        os.system("sudo groupadd --system prometheus")
        os.system("sudo useradd -s /sbin/nologin --system -g prometheus prometheus")
        os.system("xterm -e \"sudo apt-get -y install daemonize\"")
        os.system("sudo systemctl daemon-reload")
        os.system("sudo systemctl enable apache_exporter.service")
        os.system("sudo systemctl start apache_exporter.service")
        os.system("sudo systemctl restart prometheus")
        # install grafana-enterprise
        os.system("xterm -e \"sudo apt-get install -y apt-transport-https software-properties-common\"")
        os.system("xterm -e \"wget -O - https://packages.grafana.com/gpg.key | sudo apt-key add -\"")
        os.system("xterm -e \"sudo add-apt-repository deb https://packages.grafana.com/oss/deb stable main\"")
        os.system("xterm -e \"sudo apt-get update\"")
        os.system("xterm -e \"sudo apt-get install -y grafana\"")
        os.system("xterm -e \"sudo /bin/systemctl start grafana-server\"")
        # install dashboards
        folder = pathlib.Path("/var/lib/grafana")
        if not os.path.exists(folder):
            os.system("sudo mkdir /var/lib/grafana")
        folder = pathlib.Path("/var/lib/grafana/dashboards")
        if not os.path.exists(folder):
            os.system("sudo mkdir /var/lib/grafana/dashboards")
        dashboards = "sudo cp " + path + "/dashboards/apache_rev1.json /var/lib/grafana/dashboards"
        os.system(dashboards)
        sample = "sudo cp " + path + "/monitoring/sample.yaml /usr/share/grafana/conf/provisioning/dashboards/"
        sample = "sudo cp " + path + "/monitoring/sample.yaml /etc/grafana/provisioning/dashboards/"
        # install prometheus
        os.system("sudo useradd --no-create-home --shell /bin/false prometheus")
        folder = pathlib.Path("/etc/prometheus")
        if not os.path.exists(folder):
            os.system("sudo mkdir /etc/prometheus")
        folder = pathlib.Path("/var/lib/prometheus")
        if not os.path.exists(folder):
            os.system("sudo mkdir /var/lib/prometheus")
        os.system("sudo chown prometheus:prometheus /etc/prometheus")
        os.system("sudo chown prometheus:prometheus /var/lib/prometheus")
        prometheusfiles = "sudo cp " + path + "/prometheus-2.41.0.linux-amd64/prometheus /usr/local/bin/"
        os.system(prometheusfiles)
        promtool = "sudo cp " + path + "/prometheus-2.41.0.linux-amd64/promtool /usr/local/bin/"
        os.system(promtool)
        os.system("sudo chown prometheus:prometheus /usr/local/bin/prometheus")
        os.system("sudo chown prometheus:prometheus /usr/local/bin/promtool")
        consoles = "sudo cp -r " + path + "/prometheus-2.41.0.linux-amd64/consoles /etc/prometheus"
        os.system(consoles)
        consolelibraries = "sudo cp -r " + path + "/prometheus-2.41.0.linux-amd64/console_libraries /etc/prometheus"
        os.system(consolelibraries)
        os.system("sudo chown -R prometheus:prometheus /etc/prometheus/consoles")
        os.system("sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries")
        prometheus_yml = "sudo cp -r " + path + "/monitoring/prometheus.yml /etc/prometheus/"
        os.system(prometheus_yml)
        os.system("sudo chown prometheus:prometheus /etc/prometheus/prometheus.yml")
        prometheus_service = "sudo cp -r " + path + "/monitoring/prometheus.service /etc/systemd/system/"
        os.system(prometheus_service)
        os.system("sudo systemctl daemon-reload")
        os.system("sudo systemctl start prometheus")
        # create apache_exporter
        folder = pathlib.Path("/etc/sysconfig")
        if not os.path.exists(folder):
            os.system("sudo mkdir /etc/sysconfig")
        apache_exporter = "sudo cp -r " + path + "/monitoring/apache_exporter /etc/sysconfig/"
        os.system(apache_exporter)
        apache_exporter_service = "sudo cp -r " + path + "/monitoring/apache_exporter.service /etc/systemd/system/"
        os.system(apache_exporter_service)
        # create alertmanager
        directory = "/opt/alertmanager/"
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.system(
            "xterm -e \"wget https://github.com/prometheus/alertmanager/releases/download/v0.22.2/alertmanager-0.22.2.linux-amd64.tar.gz\"")
        os.system("sudo tar xzf alertmanager-0.22.2.linux-amd64.tar.gz")
        src = path + "/alertmanager-0.22.2.linux-amd64"
        dst = "/opt/alertmanager/"
        shutil.copytree(src, dst)
        os.system("sudo chown -Rfv root:root /opt/alertmanager")
        os.system("sudo mkdir -v /opt/alertmanager/data")
        os.system("sudo chown -Rfv prometheus:prometheus /opt/alertmanager/data")
        alertmanager_service = "sudo cp -r " + path + "/monitoring/alertmanager.service /etc/systemd/system/alertmanager.service"
        os.system(alertmanager_service)
        os.system("sudo systemctl daemon-reload")
        os.system("sudo systemctl start alertmanager.service")
        # install influxdb
        os.system("xterm -e \"sudo apt-get update\"")
        os.system("xterm -e \"sudo apt install -y gnupg2 curl wget\"")
        os.system("wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -")
        os.system(
            "echo deb https://repos.influxdata.com/debian $(lsb_release -cs) stable | sudo tee /etc/apt/sources.list.d/influxdb.list")
        os.system("xterm -e \"sudo apt-get update\"")
        os.system("xterm -e \"sudo apt install -y influxdb\"")
        os.system("xterm -e \"sudo systemctl enable --now influxdb\"")
        influxdb_conf = "sudo cp -r " + path + "/monitoring/influxdb.conf /etc/influxdb/"
        os.system(influxdb_conf)
        os.system("xterm -e \"sudo apt -y install ufw\"")
        os.system("xterm -e \"sudo ufw enable\"")
        os.system("xterm -e \"sudo ufw allow 22/tcp\"")
        os.system("xterm -e \"sudo ufw allow 8086/tcp\"")
        # install elasticsearch
        # os.system("xterm -e \"wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -\"")
        # os.system("xterm -e \"sudo sh -c 'echo deb https://artifacts.elastic.co/packages/7.x/apt stable main > /etc/apt/sources.list.d/elastic-7.x.list\"")
        # os.system("xterm -e \"sudo apt update\"")
        # os.system("xterm -e \"sudo apt install elasticsearch\"")
        # os.system("xterm -e \"sudo systemctl enable elasticsearch.service\"")
        # os.system("sudo systemctl start elasticsearch")
        # elasticsearch = "sudo cp -r " + path + "/monitoring/elasticsearch.yml /etc/elasticsearch/"
        # os.system(elasticsearch)
        # install chrome browser
        os.system("xterm -e \"wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb\"")
        os.system("xterm -e \"apt install ./google-chrome-stable_current_amd64.deb\"")
        print("[O] Opening http://localhost:3000 ...\n")
        os.system("google-chrome --no-sandbox http://localhost:3000/d/2K0pTah4k/apache?orgId=1&refresh=5s")
        file = pathlib.Path("google-chrome-stable_current_amd64.deb")
        if file.exists():
            os.remove(file)
        directory = path + '/alertmanager-0.22.2.linux-amd64'
        if os.path.exists(directory):
            shutil.rmtree(directory)
        directory = path + '/prometheus-2.41.0.linux-amd64'
        if os.path.exists(directory):
            shutil.rmtree(directory)
        file = pathlib.Path("alertmanager-0.22.2.linux-amd64.tar.gz")
        if file.exists():
            os.remove(file)
        os.system("sudo systemctl restart prometheus")
        os.system("sudo systemctl restart grafana-server")
        os.system("sudo systemctl restart alertmanager")
        os.system("sudo systemctl restart influxdb")
        # threading.Thread(target=i).start()
        # threading.Thread(target=k).start()
        # threading.Thread(target=l).start()
        # threading.Thread(target=m).start()
        # threading.Thread(target=n).start()
        # threading.Thread(target=o).start()
        clear()
        data = ""
    elif number == 'B':
        print("\n Launch service Remotely Triggered Black Hole  ...\n")
        threading.Thread(target=d).start()
        threading.Thread(target=e).start()
        clear()
        data = ""
    elif number == 'C':
        print("\n Stop DDOS Attack by Remotely Triggered Black Hole (RTBH) Routing  ...\n")
        threading.Thread(target=f).start()
        clear()
        data = ""
    elif number == 'D':
        print("\n Remove Promeutheus, Apache Exporter, Grafana, AlertManager  ...\n")
        os.system("sudo apt-get remove -y prometheus")
        os.system("sudo apt-get remove -y influxdb")
        os.system("sudo apt-get remove -y grafana-enterprise")
        # os.system("sudo apt-get remove -y elasticsearch")
        clear()
        data = ""
    elif number == '0':
        print('\n [+] Good Bye ' + platform.uname()[1] + ' !\n')
        quit()
    else:
        print("\n [X] Error !\n [!] Select this number: 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C or 0\n")
