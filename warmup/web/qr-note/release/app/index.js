const express = require("express");
const multer = require("multer");
const qrreader = require("./utils/qrreader.js");
const {
  sanitize,
  parseLinks,
  validateXSSContent,
} = require("./utils/sanitize.js");

const app = express();
const uploader = multer({
  dest: "/tmp",
  limits: { fileSize: 1000000 /* limit 1mb */ },
});

app.set("view engine", "ejs");
app.set("views", "pages");

app.get("/", (_, res) => {
  res.render("index");
});

app.get("/quote", async (_, res) => {
  res.setHeader("Content-Type", "text/plain");
  const quote = "awali pagimu dengan semangat! anjayy!!!!";
  res.send(quote.content);
});

app.post("/process", uploader.single("qrnote"), async (req, res) => {
  if (!req.file) {
    return res.status(400).send("No file uploaded.");
  }

  try {
    const raw = await qrreader(req.file.path);
    const note = sanitize(raw);

    // idk why need this, but maybe it's will enhance the security
    const links = parseLinks(note);
    if (links) {
      const isSafe = await validateXSSContent(...links);
      if (!isSafe) {
        return res.status(400).send("Note maybe not safe");
      }
    }

    res.render("note", { note });
  } catch (e) {
    console.log(e);
    return res.status(500).send("Ooops something went wrong.");
  }
});

app.use((req, res, err) => {
  console.log(err);
  res.status(500).send("Ooops something went wrong.");
});

app.listen(80, () => console.log(`Server is running on port 80`));
