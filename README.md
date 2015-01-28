
Usage
=====

Arduino
-------

接线参照:
![接线图](http://www.fibidi.com/wp-content/uploads/2013/05/Arduino+IR-Receiver2.jpg)


上传 Arduino 程序:
```sh
git clone https://github.com/sudar/Arduino-Makefile
mv Arduino-Makefile ~/work/github/Arduino-Makefile
git clone https://github.com/shirriff/Arduino-IRremote
mv Arduino-IRremote /usr/share/arduino/libraries/IRremote
git clone https://github.com/jaypei/Arduino-PPT-Remote-Control
mv Arduino-PPT-Remote-Control ~/work/Arduino-PPT-Remote-Control

cd ~/work/Arduino-PPT-Remote-Control
make
sudo make upload
```


PC
--

```sh
apt-get install python-serial
apt-get install xdotool
sudo ./ppt-ir-remote-control.py
```

可自行修改 `ppt-ir-remote-control.py` 的头部变量.


参考
====

* http://www.fibidi.com/arduino-ir-receiver-module/
