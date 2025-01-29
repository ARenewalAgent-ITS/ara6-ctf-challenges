const express = require('express');
const routes = require('./routes');
const path = require("path");
const db = require('./database');
const cookieParser = require('cookie-parser');
const nunjucks = require("nunjucks");
const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));
app.use(cookieParser());

nunjucks.configure("views", {
    autoescape: true,
    express: app,
});
app.set("view engine", "html");
app.use(routes);

(async () => {
    await db.connect();
    await db.dropall();
    await db.migrate();
})();

app.listen(6969, async () => {
    console.log(`[*] Webapp Listening on port 6969`)
})


