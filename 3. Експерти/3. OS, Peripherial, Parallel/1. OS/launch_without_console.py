import subprocess


def launch_without_console(command, args):
   """Launches 'command' windowless"""
   startupinfo = subprocess.STARTUPINFO()
   startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

   return subprocess.Popen([command] + args, startupinfo=startupinfo,
                    stderr=subprocess.PIPE, stdout=subprocess.PIPE)


if __name__ == "__main__":
   # process = launch_without_console("d:\bin\gzip.exe", ["-d", "myfile.gz"])
   process = launch_without_console("arp", ["-a", "192.168.1.1"])
   stdout, stderr  = process.communicate()
   print(stdout)