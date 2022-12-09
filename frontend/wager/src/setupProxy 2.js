const proxy = require('http-proxy-middleware')
module.exports = function(app) {
    const headers  = {
        "Content-Type": "application/json",
        Authorization: process.env.REACT_APP_TWITTER_API_BEARERTOKEN,
    }
    //proxyの第一引数はドメイン以下の部分
    //第二引数のtarget部はドメイン
    app.use(proxy(process.env.REACT_APP_TWITTER_BASE_CONTEXT, { target: process.env.REACT_APP_BASE_URL,changeOrigin: true,secure: false,headers: headers}));
};