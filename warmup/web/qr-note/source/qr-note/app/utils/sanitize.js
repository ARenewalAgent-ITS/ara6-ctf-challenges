const DOMPurify = require("isomorphic-dompurify");
const axios = require("axios");

const blacklists = ["'", '"', "`", ",", ".", ":"];

function sanitize(raw) {
  return DOMPurify.sanitize(raw, {
    ALLOWED_TAGS: ["div", "span", "p", "h1", "h2", "h3", "b", "i"],
  });
}

function parseLinks(content) {
  return content.match(/(?:https?:)?\/\/[^\s"'<>]+/g);
}

async function validateXSSContent(...links) {
  if (links.some((l) => l.startsWith("//"))) {
    return false;
  }
  let allcontent = "";
  for (const link of links) {
    const res = await axios.get(link);
    if (res.data.length > 350) {
      return false;
    }
    allcontent += res.data;
  }

  for (const blacklist of blacklists) {
    if (allcontent.includes(blacklist)) {
      console.log(blacklist);
      return false;
    }
  }
  return true;
}

module.exports = {
  sanitize,
  parseLinks,
  validateXSSContent,
};
