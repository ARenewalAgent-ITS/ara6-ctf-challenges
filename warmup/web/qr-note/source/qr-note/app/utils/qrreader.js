const qr = require("qrnode");

function qrreader(path) {
  return new Promise((resolve) => {
    qr.detect(path, (data) => {
      resolve(data);
    });
  });
}

module.exports = qrreader;
