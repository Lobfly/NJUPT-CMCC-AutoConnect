// os模块 request模块
const os = require("os");
const request = require("request");
///获取本机ip///
function getIPAdress() {
  var interfaces = os.networkInterfaces();
  for (var devName in interfaces) {
    var iface = interfaces[devName];
    for (var i = 0; i < iface.length; i++) {
      var alias = iface[i];
      if (
        alias.family === "IPv4" &&
        alias.address !== "127.0.0.1" &&
        !alias.internal
      ) {
        return alias.address;
      }
    }
  }
}
const ip = getIPAdress();
console.log(ip)
const url = `http://p.njupt.edu.cn:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=p.njupt.edu.cn&iTermType=1&
            wlanuserip=${ip}&wlanacip=10.255.252.150&wlanacname=XL-BRAS-SR8806-X&mac=00-00-00-00-00-00&
            ip=${ip}&enAdvert=0&queryACIP=0&loginMethod=1`;


request.post(
  {
    url: url,
    form: {
      "DDDDD": ",0,B19070135@cmcc",
      "upass": "040017",
      "0MKKey": "123456",
    },
  },
  function (error, response) {
    // if (!error && response.statusCode == 200) {
    //   console.log("success");
    // }
    console.log(response)
  }
);